#!/usr/bin/env python3
"""Merge the raw sources into the canonical Bourgain-pedia dataset.

Reads   data/raw/{zbmath,openalex,arxiv}_raw.json
Writes  data/papers.json          canonical, hand-editable bibliography
        data/collaborators.json   coauthor roster + collaborator scores
        site/data/papers.js       same payload as a JS global (works over file://)
        site/data/collaborators.js
        Papers/<year>.md          one numbered, referenced list per year
        Papers/INDEX.md

zbMATH is the spine: it is the authoritative, disambiguated mathematical
bibliography.  OpenAlex supplies citation counts and open-access PDFs; arXiv
supplies preprint links.  Records are matched on DOI first, then on a
normalised title (accents, LaTeX and punctuation stripped) within a +/-2 year
window.

Editorial fields ("summary", "digestion", "toolkit") are *preserved* across
rebuilds: whatever is already in data/papers.json wins over the generated
blank.  So you can rebuild freely after re-fetching citation counts.
"""
import difflib, json, os, re, sys, unicodedata
from collections import defaultdict, OrderedDict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(HERE, "data", "raw")
DATA = os.path.join(HERE, "data")
SITE_DATA = os.path.join(HERE, "site", "data")
PAPERS_DIR = os.path.join(HERE, "Papers")

EDITORIAL_FIELDS = ("summary", "digestion", "toolkit", "notes")


# ------------------------------------------------------------------ utilities
LATEX_CMD = re.compile(r"\\[a-zA-Z]+")
NON_ALNUM = re.compile(r"[^a-z0-9]+")

# OpenAlex records that are demonstrably not by Jean Bourgain the mathematician.
OPENALEX_EXCLUDE = {
    "W2081111938",   # "L'universite du littoral: une demarche technopolitaine originale"
}

# Extra download links found by hand, keyed by paper id.  Mostly the IHES
# preprint fonds (repo-archives.ihes.fr), which scans Bourgain's IHES preprints
# and so covers exactly the pre-arXiv years where the indices have no full text.
EXTRA_LINKS = {
    "1990-a-remark-on-gradients-of-harmonic-functions-in-dimension-3": [
        ("IHES preprint M/89/31", "pdf",
         "https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/BOURGAIN/"
         "1984-1989/M_89_31/M_89_31.pdf"),
    ],
}

# Individual fields corrected by hand, keyed by OpenAlex id. Used only where a
# source is demonstrably wrong and we can say something true in its place --
# never to fill a gap with a guess.
FIELD_OVERRIDES = {
    # OpenAlex files these 1979 lecture notes under an entomology journal.
    "W653125609": {"reference": "Lecture notes, cours de 3e cycle (1979).",
                   "journal": None, "journal_full": None, "type": "lecture notes"},
}

# Duplicates the automatic matcher cannot see: OCR-mangled titles, translations,
# and OpenAlex records for individual chapters of a Bourgain monograph.  Mapped
# to the zbMATH Zbl number of the item they duplicate, so their citation counts
# are folded into the canonical entry instead of being dropped.
OPENALEX_DUPLICATE_OF = {
    "W2557193132": "0822.35126",  # "Periodic Nonlinear Schrdinger Equation" (CMP 166)
    "W141811253":  "1370.11083",  # arXiv "On A Conjecture of Zaremba's"
    "W2530561127": "1064.35177",  # mangled "On the global Cauchy probl Schrodinger equation"
    "W2312359555": "1113.47021",  # Russian original of "Recent progress in quasi-periodic ..."
    "W172165711":  "0679.46010",  # LNM reprint, "Almost Euclidean sections ..."
    "W2590638291": "0463.46011",  # LNM reprint, "Geometrical implications ..."
    "W2886222405": "0476.46020",  # chapter of the monograph "New classes of L^p-spaces"
    "W2913182145": "0476.46020",  # chapter of the same monograph
    "W2477739861": "0933.35178",  # chapter of AMS Colloq. Publ. 46
    "W2504515834": "0933.35178",  # chapter of AMS Colloq. Publ. 46
    "W2493103935": "0933.35178",  # chapter of AMS Colloq. Publ. 46
    "W2502967621": "0933.35178",  # chapter of AMS Colloq. Publ. 46
    "W4241796606": "1184.01024",  # duplicate record of the GAFA 2000 "Visions" volume
}


def title_tokens(text):
    """Word tokens of a title, for fuzzy cross-source matching."""
    if not text:
        return set()
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = LATEX_CMD.sub(" ", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return {w for w in t.split() if len(w) > 2 and w not in TITLE_STOPWORDS}


TITLE_STOPWORDS = {"the", "and", "for", "with", "some", "certain", "its", "into",
                   "sur", "des", "les", "une", "aux", "dans", "que", "qui"}


def token_sim(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    return inter / min(len(a), len(b))          # containment, tolerant of truncation


def norm_title(text):
    """Aggressively normalise a title so the three sources can be matched."""
    if not text:
        return ""
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = LATEX_CMD.sub(" ", t)
    t = NON_ALNUM.sub("", t)
    return t


def slugify(text, maxlen=70):
    t = unicodedata.normalize("NFKD", text or "")
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = LATEX_CMD.sub(" ", t)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:maxlen].strip("-") or "untitled"


def load(name):
    path = os.path.join(RAW, name)
    if not os.path.exists(path):
        print(f"  (missing {name} -- skipping that source)", file=sys.stderr)
        return []
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def clean_doi(doi):
    if not doi:
        return None
    return doi.strip().lower().replace("https://doi.org/", "").replace("http://dx.doi.org/", "")


# ------------------------------------------------------------------- zbMATH IO
def zb_reference(rec):
    """Full bibliographic reference string, zbMATH style."""
    src = rec.get("source") or {}
    if isinstance(src, dict) and src.get("source"):
        return src["source"].strip()
    return ""


def zb_series(rec):
    src = rec.get("source") or {}
    ser = (src.get("series") or [{}])[0] if isinstance(src, dict) else {}
    book = (src.get("book") or [{}])[0] if isinstance(src, dict) else {}
    return {
        "journal": ser.get("short_title"),
        "journal_full": ser.get("title"),
        "volume": ser.get("volume"),
        "issue": ser.get("issue"),
        "pages": src.get("pages") if isinstance(src, dict) else None,
        "publisher": ser.get("publisher") or book.get("publisher"),
        "issn": [i.get("number") for i in (ser.get("issn") or []) if isinstance(i, dict)],
    }


def zb_languages(rec):
    lang = rec.get("language") or {}
    return [l for l in (lang.get("languages") or []) if l]


LINK_LABEL = {
    "doi": "DOI", "arxiv": "arXiv", "numdam": "NUMDAM", "eudml": "EuDML",
    "euclid": "Project Euclid", "emis": "EMIS", "hal": "HAL", "crelle": "Crelle",
    "oeis": "OEIS", "geodesic": "zbMATH full text", "http": "Web", "https": "Web",
}


def zb_links(rec):
    out = []
    for link in rec.get("links") or []:
        if not isinstance(link, dict):
            continue
        kind = (link.get("type") or "").lower()
        url = link.get("url")
        if not url:
            continue
        out.append({"label": LINK_LABEL.get(kind, kind or "Link"),
                    "kind": kind, "url": url,
                    "identifier": link.get("identifier")})
    return out


# ------------------------------------------------------------------- main pass
def build():
    zb = load("zbmath_raw.json")
    oa = load("openalex_raw.json")
    ax = load("arxiv_raw.json")
    print(f"raw: zbMATH {len(zb)}, OpenAlex {len(oa)}, arXiv {len(ax)}")

    # ---- OpenAlex: drop false positives, then collapse preprint/published pairs
    oa = [w for w in oa
          if w["id"].rsplit("/", 1)[-1] not in OPENALEX_EXCLUDE
          and (w.get("publication_year") or 0) >= 1970
          and any(((a.get("author") or {}).get("id") or "").endswith("A5029411281")
                  for a in (w.get("authorships") or []))]
    oa_groups = defaultdict(list)
    for w in oa:
        oa_groups[norm_title(w.get("title") or w.get("display_name"))].append(w)
    print(f"OpenAlex: {len(oa)} Bourgain works in {len(oa_groups)} title groups")

    # ---- arXiv index by normalised title
    ax_by_title = {}
    for a in ax:
        if not any("bourgain" in n.lower() for n in a.get("authors", [])):
            continue
        ax_by_title.setdefault(norm_title(a["title"]), a)

    def oa_pick(group):
        """Merge an OpenAlex title-group into one summary dict."""
        if not group:
            return {}
        published = [w for w in group if w.get("type") != "preprint"] or group
        best = max(published, key=lambda w: (w.get("cited_by_count") or 0))
        doi = clean_doi(best.get("doi")) or next(
            (clean_doi(w.get("doi")) for w in group if w.get("doi")), None)
        pdf = None
        landing = None
        arxiv = None
        for w in group:
            for loc in [w.get("best_oa_location")] + (w.get("locations") or []):
                if not loc:
                    continue
                if loc.get("pdf_url") and not pdf:
                    pdf = loc["pdf_url"]
                if loc.get("is_oa") and loc.get("landing_page_url") and not landing:
                    landing = loc["landing_page_url"]
                for url in (loc.get("landing_page_url"), loc.get("pdf_url")):
                    m = re.search(r"arxiv\.org/(?:abs|pdf)/([^\s/?#]+?)(?:v\d+)?(?:\.pdf)?$",
                                  url or "")
                    if m and not arxiv:
                        arxiv = m.group(1)
        return {
            "cited_by": max((w.get("cited_by_count") or 0) for w in group),
            "doi": doi,
            "oa_pdf": pdf,
            "oa_landing": landing,
            "arxiv": arxiv,
            "openalex_ids": [w["id"].rsplit("/", 1)[-1] for w in group],
            "years": sorted({w.get("publication_year") for w in group if w.get("publication_year")}),
            "title": best.get("title") or best.get("display_name"),
            "type": best.get("type"),
            "biblio": best.get("biblio") or {},
            "authorships": best.get("authorships") or [],
            "venue": (((best.get("primary_location") or {}).get("source") or {}) or {}).get("display_name"),
        }

    oa_by_doi = {}
    for key, grp in oa_groups.items():
        info = oa_pick(grp)
        if info.get("doi"):
            oa_by_doi.setdefault(info["doi"], key)

    oa_tokens = {k: title_tokens(oa_pick(g).get("title")) for k, g in oa_groups.items()}
    oa_years = {k: [w.get("publication_year") for w in g if w.get("publication_year")]
                for k, g in oa_groups.items()}

    used_oa = set()
    entries = []

    # ---- 1. every zbMATH record becomes an entry
    for rec in zb:
        title = (rec.get("title") or "").strip()
        year = int(rec["year"]) if (rec.get("year") or "").isdigit() else None
        links = zb_links(rec)
        doi = next((clean_doi(l["identifier"]) for l in links if l["kind"] == "doi"), None)
        arxiv_id = next((l["identifier"] for l in links if l["kind"] == "arxiv"), None)
        key = norm_title(title)

        oa_key = None
        if doi and doi in oa_by_doi:
            oa_key = oa_by_doi[doi]
        elif key in oa_groups:
            oa_key = key
        else:                              # fuzzy: token containment within +/-3 yr
            oa_key = fuzzy_match(title, year, oa_groups, oa_tokens, oa_years, used_oa)
        info = {}
        if oa_key:
            used_oa.add(oa_key)
            info = oa_pick(oa_groups[oa_key])

        if not arxiv_id:
            hit = ax_by_title.get(key)
            arxiv_id = hit["arxiv_id"] if hit else info.get("arxiv")

        entries.append(make_entry(
            title=title, year=year, authors=rec.get("authors") or [],
            doc_type=rec.get("document_type"), languages=zb_languages(rec),
            reference=zb_reference(rec), series=zb_series(rec),
            doi=doi or info.get("doi"), arxiv_id=arxiv_id,
            zbl=rec.get("zbl"), zbmath_url=rec.get("zbmath_url"),
            msc=rec.get("msc") or [], keywords=rec.get("keywords") or [],
            zb_links=links, oa=info, provenance=["zbMATH"] + (["OpenAlex"] if info else []),
        ))

    # ---- 2a. leftover OpenAlex groups that are really the arXiv preprint (or an
    #          OCR-mangled record) of an entry we already built: fold them in.
    entry_tokens = [(i, title_tokens(e["title"]), norm_title(e["title"]), e["year"])
                    for i, e in enumerate(entries)]
    by_zbl = {e["zbl"]: e for e in entries if e.get("zbl")}
    leftovers = []
    for key, grp in oa_groups.items():
        if key in used_oa or not key:
            continue
        info = oa_pick(grp)
        alias = next((OPENALEX_DUPLICATE_OF[o] for o in (info.get("openalex_ids") or [])
                      if o in OPENALEX_DUPLICATE_OF), None)
        if alias:
            target = by_zbl.get(alias)
            if target is not None:
                merge_openalex_into(target, info, ax_by_title.get(key))
                continue
            print(f"  ! duplicate alias {alias} not found for {info.get('title')!r}",
                  file=sys.stderr)
        toks = title_tokens(info.get("title"))
        yrs = info.get("years") or []
        hit, best = None, 0.80
        if len(toks) >= 3:
            for idx, etoks, enorm, eyear in entry_tokens:
                if eyear and yrs and min(abs(eyear - y) for y in yrs) > 3:
                    continue
                score = max(token_sim(toks, etoks),
                            difflib.SequenceMatcher(None, key, enorm).ratio()
                            if abs(len(key) - len(enorm)) < 20 else 0.0)
                if score > best:
                    hit, best = idx, score
        if hit is None:
            leftovers.append((key, grp, info))
            continue
        merge_openalex_into(entries[hit], info, ax_by_title.get(key))

    # ---- 2b. genuine OpenAlex-only works zbMATH does not carry
    for key, grp, info in leftovers:
        year = info["years"][0] if info["years"] else None
        authors = [a.get("author", {}).get("display_name")
                   for a in info.get("authorships", []) if a.get("author")]
        bib = info.get("biblio") or {}
        pages = None
        if bib.get("first_page"):
            pages = bib["first_page"] + (f"-{bib['last_page']}" if bib.get("last_page") else "")
        ref_bits = [info.get("venue"), bib.get("volume"), pages, f"({year})" if year else None]
        hit = ax_by_title.get(key)
        arxiv_id = hit["arxiv_id"] if hit else info.get("arxiv")
        entries.append(make_entry(
            title=info.get("title") or "", year=year, authors=authors,
            doc_type=info.get("type"), languages=[], provenance=["OpenAlex"],
            reference=", ".join(b for b in ref_bits if b),
            series={"journal": info.get("venue"), "journal_full": info.get("venue"),
                    "volume": bib.get("volume"), "issue": bib.get("issue"),
                    "pages": pages, "publisher": None, "issn": []},
            doi=info.get("doi"), arxiv_id=arxiv_id, zbl=None, zbmath_url=None,
            msc=[], keywords=[], zb_links=[], oa=info,
        ))

    for e in entries:
        for oid in e.get("openalex_ids") or []:
            for field, value in FIELD_OVERRIDES.get(oid, {}).items():
                e[field] = value

    # ---- 3. attach any arXiv preprint still unmatched, by fuzzy title
    attached = {(e["arxiv"] or "").lower() for e in entries if e.get("arxiv")}
    entry_tok2 = [(e, title_tokens(e["title"]), norm_title(e["title"])) for e in entries]
    for a in ax:
        if a["arxiv_id"].lower() in attached:
            continue
        if not any("bourgain" in n.lower() for n in a.get("authors", [])):
            continue
        toks, key = title_tokens(a["title"]), norm_title(a["title"])
        year = int(a["published"][:4]) if a.get("published") else None
        hit, best = None, 0.80
        for e, etoks, enorm in entry_tok2:
            if e.get("arxiv") or (year and e["year"] and abs(e["year"] - year) > 4):
                continue
            score = max(token_sim(toks, etoks),
                        difflib.SequenceMatcher(None, key, enorm).ratio()
                        if abs(len(key) - len(enorm)) < 20 else 0.0)
            if score > best:
                hit, best = e, score
        if hit is not None:
            hit["arxiv"] = a["arxiv_id"]
            _add_link(hit, "arXiv", "arxiv", f"https://arxiv.org/abs/{a['arxiv_id']}")
            _add_link(hit, "arXiv PDF", "pdf", f"https://arxiv.org/pdf/{a['arxiv_id']}")
            if "arXiv" not in hit["provenance"]:
                hit["provenance"].append("arXiv")
            attached.add(a["arxiv_id"].lower())

    # ---- sort, assign stable ids
    entries.sort(key=lambda e: (e["year"] or 9999, norm_title(e["title"])))
    seen = defaultdict(int)
    for e in entries:
        base = f"{e['year'] or 'undated'}-{slugify(e['title'])}"
        seen[base] += 1
        e["id"] = base if seen[base] == 1 else f"{base}-{seen[base]}"

    for e in entries:
        for label, kind, url in EXTRA_LINKS.get(e["id"], []):
            _add_link(e, label, kind, url)
            e["primary_link"] = url
            if "hand-checked" not in e["provenance"]:
                e["provenance"].append("hand-checked")

    entries = assign_areas(entries)
    entries = canonicalise_people(entries)
    entries = carry_editorial(entries)
    write_outputs(entries)
    return entries


def merge_openalex_into(entry, info, arxiv_hit=None):
    """Fold a duplicate OpenAlex record (usually the arXiv preprint) into an entry."""
    if info.get("cited_by") is not None:
        entry["cited_by"] = max(entry["cited_by"] or 0, info["cited_by"])
    for oid in info.get("openalex_ids") or []:
        if oid not in entry["openalex_ids"]:
            entry["openalex_ids"].append(oid)
    if not entry["doi"] and info.get("doi"):
        entry["doi"] = info["doi"]
        _add_link(entry, "DOI", "doi", f"https://doi.org/{info['doi']}")
    if not entry["arxiv"]:
        aid = arxiv_hit["arxiv_id"] if arxiv_hit else info.get("arxiv")
        if aid:
            entry["arxiv"] = aid
            _add_link(entry, "arXiv", "arxiv", f"https://arxiv.org/abs/{aid}")
            _add_link(entry, "arXiv PDF", "pdf", f"https://arxiv.org/pdf/{aid}")
    if info.get("oa_pdf"):
        _add_link(entry, "Open-access PDF", "pdf", info["oa_pdf"])
    if info.get("oa_landing"):
        _add_link(entry, "Open access", "oa", info["oa_landing"])
    if "OpenAlex" not in entry["provenance"]:
        entry["provenance"].append("OpenAlex")


def _link_key(url):
    return re.sub(r"^https?://(?:www\.)?", "", (url or "").strip().rstrip("/")).lower()


def _add_link(entry, label, kind, url):
    if url and all(_link_key(l["url"]) != _link_key(url) for l in entry["links"]):
        entry["links"].append({"label": label, "kind": kind, "url": url})
        if not entry.get("primary_link"):
            entry["primary_link"] = url


def fuzzy_match(title, year, oa_groups, oa_tokens, oa_years, used_oa,
                threshold=0.78, window=3):
    """Best OpenAlex title-group for a zbMATH title, or None.

    OpenAlex titles are frequently truncated, OCR-mangled or upper-cased, so a
    containment score (|A n B| / min(|A|,|B|)) beats plain Jaccard here.  A
    match must also be plausible in time.
    """
    toks = title_tokens(title)
    if len(toks) < 3:
        return None
    nkey = norm_title(title)
    best, best_score = None, threshold
    for key, cand in oa_tokens.items():
        if key in used_oa or len(cand) < 3:
            continue
        score = max(token_sim(toks, cand),
                    difflib.SequenceMatcher(None, nkey, key).ratio()
                    if abs(len(nkey) - len(key)) < 20 else 0.0)
        if score < best_score:
            continue
        yrs = oa_years.get(key) or []
        if year and yrs and min(abs(year - y) for y in yrs) > window:
            continue
        best, best_score = key, score
    return best


# --------------------------------------------------------------- person names
NAME_PARTICLES = {"van", "von", "de", "der", "den", "du", "da", "di", "del",
                  "della", "la", "le", "ten", "ter", "bin", "al", "dos", "das",
                  "st", "mac", "mc"}


def split_person(name):
    """('Bourgain, Jean') and ('Jean Bourgain') both -> ('Bourgain', 'Jean')."""
    n = " ".join((name or "").replace("\u00a0", " ").split())
    if "," in n:
        last, first = [x.strip() for x in n.split(",", 1)]
        return last, first
    parts = n.split()
    if len(parts) < 2:
        return n, ""
    i = len(parts) - 1
    while i > 1 and parts[i - 1].lower().strip(".") in NAME_PARTICLES:
        i -= 1
    return " ".join(parts[i:]), " ".join(parts[:i])


def person_key(name):
    """Surname + first initial, accent- and case-insensitive.

    zbMATH writes 'Bergelson, V.' where OpenAlex writes 'Vitaly Bergelson';
    both must land on one person in the roster.
    """
    last, first = split_person(name)
    last = "".join(c for c in unicodedata.normalize("NFKD", last)
                   if not unicodedata.combining(c)).lower()
    stripped = re.sub(r"[^a-z]+", "", last)
    # a name in a non-Latin script would otherwise key to the empty string, and
    # every such name would merge into one person
    last = stripped or re.sub(r"\s+", "", last)
    initial = ""
    if first:
        f = "".join(c for c in unicodedata.normalize("NFKD", first)
                    if not unicodedata.combining(c))
        f = re.sub(r"[^A-Za-z]+", "", f)
        initial = f[:1].lower()
    return last, initial


def display_name(name):
    last, first = split_person(name)
    return f"{last}, {first}" if first else last


# Bylines no automatic rule can reconcile -- here, a Cyrillic transliteration
# that person_key() cannot fold onto its Latin form.
RAW_NAME_ALIASES = {
    "Э. М. Семенов": "Semenov, E. M.",
    "Семенов, Э. М.": "Semenov, E. M.",
}


def canonicalise_people(entries):
    """Collapse the spelling variants of each coauthor onto one display name."""
    for e in entries:
        e["authors"] = [RAW_NAME_ALIASES.get(a.strip(), a) for a in e["authors"]]

    counts = defaultdict(lambda: defaultdict(int))
    for e in entries:
        for raw in e["authors"]:
            counts[person_key(raw)][display_name(raw)] += 1

    canon = {}
    for key, spellings in counts.items():
        def rank(item):
            name, n = item
            _, first = split_person(name)
            # prefer a spelled-out given name, then a diacritic-bearing form,
            # then the most frequent spelling
            spelled = len(re.sub(r"[^A-Za-z]", "", first)) - 2 * first.count(".")
            accented = any(unicodedata.combining(c)
                           for c in unicodedata.normalize("NFD", name))
            return (spelled, accented, n, -len(name))
        canon[key] = max(spellings.items(), key=rank)[0]

    merged = sum(1 for k, v in counts.items() if len(v) > 1)
    for e in entries:
        e["authors_raw"] = list(e["authors"])
        seen, names = set(), []
        for a in e["authors"]:
            c = canon[person_key(a)]
            if c not in seen:
                seen.add(c)
                names.append(c)
        e["authors"] = names
        e["coauthors"] = [a for a in names if "bourgain" not in a.lower()]
    if merged:
        print(f"  merged spelling variants for {merged} author name(s)")
    return entries

# --------------------------------------------------------------- subject areas
# Papers are grouped by area from their MSC codes (zbMATH supplies these for 536
# of 548 items).  The map is over 2-digit MSC top-level classes; a paper's area
# is decided by its *primary* code, and every area any of its codes touches is
# recorded in "areas" so that cross-field work is findable from either side.
AREAS = [
    ("harmonic-analysis", "Harmonic analysis",
     "Fourier analysis, singular integrals, restriction and Kakeya, maximal operators.",
     ["42", "43"]),
    ("banach-convex", "Banach spaces and convex geometry",
     "Geometry of normed spaces, operator theory, convex bodies in high dimension.",
     ["46", "47", "52"]),
    ("number-theory", "Number theory",
     "Exponential sums, arithmetic combinatorics, the distribution of arithmetic sequences.",
     ["11"]),
    ("pde", "Partial differential equations",
     "Dispersive and nonlinear equations, well-posedness, elliptic problems.",
     ["35"]),
    ("dynamics", "Dynamics and ergodic theory",
     "Pointwise convergence, equidistribution, quasi-periodic and homogeneous dynamics.",
     ["37", "28"]),
    ("probability", "Probability",
     "Random series, concentration, random matrices and random constructions.",
     ["60"]),
    ("math-physics", "Mathematical physics",
     "Schrodinger operators, Anderson localization, statistical mechanics.",
     ["81", "82"]),
    ("complex-analysis", "Complex and real analysis",
     "Hardy spaces, holomorphic function theory, real-variable methods, potential theory.",
     ["30", "31", "32", "26", "40", "41"]),
    ("geometry-topology", "Geometry and topology",
     "Differential geometry, global analysis, general topology.",
     ["53", "54", "55", "57", "58"]),
    ("groups", "Groups and representation theory",
     "Growth and expansion in groups, Lie groups, representation theory.",
     ["20", "22"]),
    ("combinatorics-cs", "Combinatorics and computer science",
     "Extremal and probabilistic combinatorics, Boolean functions, algorithms, coding.",
     ["05", "68", "94"]),
    ("variational", "Calculus of variations",
     "Variational problems, optimisation, control.",
     ["49", "93"]),
    ("logic-foundations", "Logic and foundations",
     "Set theory, descriptive set theory, measure-theoretic foundations.",
     ["03", "04"]),
    ("general", "General and historical",
     "Surveys, collected volumes, obituaries, problem lists.",
     ["00", "01"]),
]
MSC_TO_AREA = {code: key for key, _n, _d, codes in AREAS for code in codes}
UNCLASSIFIED = ("unclassified", "Unclassified",
                "No MSC code on record, so no area could be derived.")


def assign_areas(entries):
    """Give every paper a primary `area` and the set of `areas` it touches."""
    for e in entries:
        keys, primary = [], None
        for i, code in enumerate(e.get("msc") or []):
            key = MSC_TO_AREA.get(str(code)[:2])
            if not key:
                continue
            if primary is None:
                primary = key
            if key not in keys:
                keys.append(key)
        e["area"] = primary or UNCLASSIFIED[0]
        e["areas"] = keys or [UNCLASSIFIED[0]]
    return entries


def area_index(entries):
    counts = defaultdict(int)
    for e in entries:
        counts[e["area"]] += 1
    out = [{"key": k, "name": n, "note": d, "msc": codes, "count": counts.get(k, 0)}
           for k, n, d, codes in AREAS]
    if counts.get(UNCLASSIFIED[0]):
        out.append({"key": UNCLASSIFIED[0], "name": UNCLASSIFIED[1],
                    "note": UNCLASSIFIED[2], "msc": [],
                    "count": counts[UNCLASSIFIED[0]]})
    return [a for a in out if a["count"]]


def make_entry(*, title, year, authors, doc_type, languages, reference, series,
               doi, arxiv_id, zbl, zbmath_url, msc, keywords, zb_links, oa,
               provenance=("zbMATH",)):
    links, seen_urls = [], set()

    def key_of(url):
        return re.sub(r"^https?://(?:www\.)?", "", (url or "").strip().rstrip("/")).lower()

    def add(label, kind, url):
        if url and key_of(url) not in seen_urls:
            seen_urls.add(key_of(url))
            links.append({"label": label, "kind": kind, "url": url})

    if arxiv_id:
        add("arXiv", "arxiv", f"https://arxiv.org/abs/{arxiv_id}")
        add("arXiv PDF", "pdf", f"https://arxiv.org/pdf/{arxiv_id}")
    for l in zb_links:
        if l["kind"] == "arxiv":
            continue
        add(l["label"], l["kind"], l["url"])
    if oa.get("oa_pdf"):
        add("Open-access PDF", "pdf", oa["oa_pdf"])
    if oa.get("oa_landing"):
        add("Open access", "oa", oa["oa_landing"])
    if doi:
        add("DOI", "doi", f"https://doi.org/{doi}")
    if zbmath_url:
        add("zbMATH review", "zbmath", zbmath_url)

    priority = ["arxiv", "pdf", "numdam", "eudml", "euclid", "emis", "oa", "doi",
                "geodesic", "http", "https", "zbmath"]
    primary = None
    for kind in priority:
        primary = next((l["url"] for l in links if l["kind"] == kind), None)
        if primary:
            break

    coauthors = [a for a in authors if a and "bourgain" not in a.lower()]
    return OrderedDict([
        ("id", None),
        ("title", title),
        ("year", year),
        ("authors", authors),
        ("coauthors", coauthors),
        ("type", doc_type),
        ("languages", languages),
        ("reference", reference),
        ("journal", series.get("journal")),
        ("journal_full", series.get("journal_full")),
        ("volume", series.get("volume")),
        ("issue", series.get("issue")),
        ("pages", series.get("pages")),
        ("publisher", series.get("publisher")),
        ("issn", series.get("issn") or []),
        ("doi", doi),
        ("arxiv", arxiv_id),
        ("zbl", zbl),
        ("zbmath_url", zbmath_url),
        ("openalex_ids", oa.get("openalex_ids") or []),
        ("area", None),
        ("areas", []),
        ("msc", [m.get("code") for m in msc if isinstance(m, dict)]),
        ("msc_text", [f"{m.get('code')} {m.get('text')}" for m in msc if isinstance(m, dict)]),
        ("keywords", keywords),
        ("cited_by", oa.get("cited_by")),
        ("links", links),
        ("primary_link", primary),
        ("provenance", list(provenance)),
        # ---- editorial fields, filled in by the project, never by the builder
        ("summary", ""),
        ("digestion", None),
        ("toolkit", []),
        ("notes", ""),
    ])


def carry_editorial(entries):
    """Never clobber hand-written summaries when rebuilding."""
    path = os.path.join(DATA, "papers.json")
    if not os.path.exists(path):
        return entries
    with open(path, encoding="utf-8") as fh:
        old = json.load(fh)
    prev = {}
    for e in old.get("papers", old if isinstance(old, list) else []):
        prev[e.get("id")] = e
        if e.get("zbl"):
            prev.setdefault("zbl:" + e["zbl"], e)
        prev.setdefault("t:" + norm_title(e.get("title")), e)
    kept = 0
    for e in entries:
        old_e = (prev.get(e["id"]) or (prev.get("zbl:" + e["zbl"]) if e.get("zbl") else None)
                 or prev.get("t:" + norm_title(e["title"])))
        if not old_e:
            continue
        for field in EDITORIAL_FIELDS:
            if old_e.get(field):
                e[field] = old_e[field]
                kept += 1
    if kept:
        print(f"  carried over {kept} editorial fields from the previous build")
    return entries


# ------------------------------------------------------------------- outputs
def write_outputs(entries):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # the citation stamp is when OpenAlex was last *fetched*, not when the data
    # was last merged -- a rebuild does not make the counts any fresher
    oa_raw = os.path.join(RAW, "openalex_raw.json")
    cites_stamp = stamp
    if os.path.exists(oa_raw):
        cites_stamp = datetime.fromtimestamp(
            os.path.getmtime(oa_raw), timezone.utc).strftime("%Y-%m-%d")
    years = sorted({e["year"] for e in entries if e["year"]})
    payload = {
        "generated": stamp,
        "citations_updated": cites_stamp,
        "sources": ["zbMATH Open", "OpenAlex", "arXiv"],
        "count": len(entries),
        "year_range": [years[0], years[-1]] if years else [None, None],
        "areas": area_index(entries),
        "papers": entries,
    }
    os.makedirs(DATA, exist_ok=True)
    os.makedirs(SITE_DATA, exist_ok=True)
    with open(os.path.join(DATA, "papers.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(SITE_DATA, "papers.js"), "w", encoding="utf-8") as fh:
        fh.write("// generated by tools/build_data.py -- do not edit by hand\n")
        fh.write("window.BOURGAIN_PAPERS = ")
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")
    print(f"  data/papers.json + site/data/papers.js  ({len(entries)} papers, {years[0]}-{years[-1]})")

    write_collaborators(entries, stamp)
    write_toolkit(entries, stamp)
    write_problems(entries, stamp)
    write_year_files(entries, stamp, cites_stamp)


def write_toolkit(entries, stamp):
    """Publish data/toolkit.json to the site, recomputing every score.

    An idea's score is *derived*: it is the number of catalogued papers whose
    "toolkit" list names it.  Nothing is scored by hand.
    """
    path = os.path.join(DATA, "toolkit.json")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        kit = json.load(fh)

    users = defaultdict(list)
    for e in entries:
        for idea_id in e.get("toolkit") or []:
            users[idea_id].append(e["id"])

    for idea in kit.get("ideas", []):
        idea["papers"] = sorted(set((idea.get("papers") or []) + users.get(idea["id"], [])))
        idea["score"] = len(idea["papers"])
    unknown = sorted(set(users) - {i["id"] for i in kit.get("ideas", [])})
    if unknown:
        print(f"  ! papers reference {len(unknown)} idea(s) missing from data/toolkit.json: "
              f"{', '.join(unknown[:6])}", file=sys.stderr)
    kit["generated"] = stamp
    kit["count"] = len(kit.get("ideas", []))

    with open(path, "w", encoding="utf-8") as fh:
        json.dump(kit, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(SITE_DATA, "toolkit.js"), "w", encoding="utf-8") as fh:
        fh.write("// generated from data/toolkit.json by tools/build_data.py\n")
        fh.write("window.BOURGAIN_TOOLKIT = ")
        json.dump(kit, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")
    print(f"  data/toolkit.json + site/data/toolkit.js  ({kit['count']} ideas)")


def write_problems(entries, stamp):
    """Publish data/problems.json to the site.

    Open problems arrive the same way toolkit entries do: only from a paper the
    project has actually digested.  The builder derives nothing here except a
    check that every `posed_in` really names a paper in the catalogue.
    """
    path = os.path.join(DATA, "problems.json")
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as fh:
        probs = json.load(fh)

    known = {e["id"] for e in entries}
    fields = {f["key"] for f in probs.get("fields", [])}
    for pr in probs.get("problems", []):
        if pr.get("posed_in") and pr["posed_in"] not in known:
            print(f"  ! open problem {pr['id']!r} cites unknown paper "
                  f"{pr['posed_in']!r}", file=sys.stderr)
        if pr.get("field") not in fields:
            print(f"  ! open problem {pr['id']!r} has unknown field "
                  f"{pr.get('field')!r}", file=sys.stderr)

    probs["generated"] = stamp
    probs["count"] = len(probs.get("problems", []))
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(probs, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(SITE_DATA, "problems.js"), "w", encoding="utf-8") as fh:
        fh.write("// generated from data/problems.json by tools/build_data.py\n")
        fh.write("window.BOURGAIN_PROBLEMS = ")
        json.dump(probs, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")
    print(f"  data/problems.json + site/data/problems.js  "
          f"({probs['count']} open problem{'s' if probs['count'] != 1 else ''})")


def canonical_name(name):
    """'Kenig, Carlos E.' -> ('Kenig, Carlos E.', 'K')."""
    n = " ".join((name or "").split())
    letter = unicodedata.normalize("NFKD", n[:1]).encode("ascii", "ignore").decode().upper()
    return n, (letter if letter.isalpha() else "#")


def write_collaborators(entries, stamp):
    """Coauthor roster with collaborator scores; bios live in a hand-edited file."""
    tally = defaultdict(list)
    for e in entries:
        for name in e["coauthors"]:
            tally[" ".join(name.split())].append(e["id"])

    bios_path = os.path.join(DATA, "collaborator_bios.json")
    bios = {}
    if os.path.exists(bios_path):
        with open(bios_path, encoding="utf-8") as fh:
            bios = json.load(fh)

    people = []
    for name, ids in tally.items():
        disp, letter = canonical_name(name)
        bio = bios.get(disp, {})
        years = sorted({p["year"] for p in entries if p["id"] in ids and p["year"]})
        people.append(OrderedDict([
            ("name", disp),
            ("letter", letter),
            ("score", len(ids)),
            ("papers", ids),
            ("years", [years[0], years[-1]] if years else [None, None]),
            ("born", bio.get("born", "")),
            ("died", bio.get("died", "")),
            ("institution", bio.get("institution", "")),
            ("bio", bio.get("bio", "")),
        ]))
    people.sort(key=lambda p: (p["letter"], p["name"]))
    payload = {"generated": stamp, "count": len(people), "collaborators": people}
    with open(os.path.join(DATA, "collaborators.json"), "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(SITE_DATA, "collaborators.js"), "w", encoding="utf-8") as fh:
        fh.write("// generated by tools/build_data.py -- bios come from data/collaborator_bios.json\n")
        fh.write("window.BOURGAIN_COLLABORATORS = ")
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))
        fh.write(";\n")
    print(f"  data/collaborators.json  ({len(people)} coauthors, "
          f"{sum(1 for p in people if p['bio'])} with bios)")

    # a stub bios file so the roster is easy to fill in by hand
    if not os.path.exists(bios_path):
        stub = {p["name"]: {"born": "", "died": "", "institution": "", "bio": ""}
                for p in people}
        with open(bios_path, "w", encoding="utf-8") as fh:
            json.dump(stub, fh, ensure_ascii=False, indent=1, sort_keys=True)
        print(f"  wrote bio stub {bios_path}")


def md_escape(text):
    return (text or "").replace("|", "\\|")


def write_year_files(entries, stamp, cites_stamp=None):
    cites_stamp = cites_stamp or stamp
    os.makedirs(PAPERS_DIR, exist_ok=True)
    by_year = defaultdict(list)
    for e in entries:
        by_year[e["year"]].append(e)

    years = sorted(y for y in by_year if y)
    for year in years:
        rows = sorted(by_year[year], key=lambda e: norm_title(e["title"]))
        lines = [f"# Bourgain {year}",
                 "",
                 f"{len(rows)} item{'s' if len(rows) != 1 else ''}. "
                 f"Generated {stamp} from zbMATH Open, OpenAlex and arXiv "
                 f"by `tools/build_data.py`. Citation counts are OpenAlex counts "
                 f"as of {cites_stamp}.",
                 "",
                 "---",
                 ""]
        for i, e in enumerate(rows, 1):
            authors = "; ".join(e["authors"]) or "Bourgain, Jean"
            if authors.endswith("."):
                authors = authors[:-1]
            lines.append(f"{i}. **{md_escape(e['title'])}**")
            lines.append("")
            lines.append(f"   {md_escape(authors)}.  ")
            if e["reference"]:
                lines.append(f"   *{md_escape(e['reference'])}*  ")
            bits = []
            if e["zbl"]:
                bits.append(f"Zbl {e['zbl']}")
            if e["doi"]:
                bits.append(f"DOI [{e['doi']}](https://doi.org/{e['doi']})")
            if e["arxiv"]:
                bits.append(f"arXiv [{e['arxiv']}](https://arxiv.org/abs/{e['arxiv']})")
            if e["cited_by"] is not None:
                bits.append(f"cited by {e['cited_by']}")
            if e["msc"]:
                bits.append("MSC " + ", ".join(e["msc"][:4]))
            if bits:
                lines.append("   " + " · ".join(bits) + "  ")
            if e["links"]:
                lines.append("   Download: " +
                             " · ".join(f"[{l['label']}]({l['url']})" for l in e["links"]))
            else:
                lines.append("   Download: _no online copy located_")
            lines.append(f"   <!-- id: {e['id']} -->")
            lines.append("")
            lines.append("---")
            lines.append("")
        with open(os.path.join(PAPERS_DIR, f"{year}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))

    undated = by_year.get(None, [])
    index = ["# Papers by year",
             "",
             f"{len(entries)} items, {years[0]}-{years[-1]}. Generated {stamp}.",
             "",
             "| Year | Items | Cited by (total) |",
             "| ---: | ----: | ---------------: |"]
    for year in years:
        rows = by_year[year]
        cites = sum(e["cited_by"] or 0 for e in rows)
        index.append(f"| [{year}]({year}.md) | {len(rows)} | {cites:,} |")
    index += ["", f"**Total** — {len(entries)} items, "
              f"{sum(e['cited_by'] or 0 for e in entries):,} citations."]
    if undated:
        index += ["", f"{len(undated)} undated item(s) are listed in `undated.md`."]
        with open(os.path.join(PAPERS_DIR, "undated.md"), "w", encoding="utf-8") as fh:
            fh.write("# Undated items\n\n" +
                     "\n".join(f"- **{e['title']}** — {e['reference']}" for e in undated) + "\n")
    with open(os.path.join(PAPERS_DIR, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index) + "\n")
    print(f"  Papers/{years[0]}.md ... Papers/{years[-1]}.md + INDEX.md")


if __name__ == "__main__":
    build()
