#!/usr/bin/env python3
"""Fill dates and affiliations in data/collaborator_bios.json from Wikidata.

Two lookup passes, then a validity pass:

  1. exact label / alias match via SPARQL      (fast, precise)
  2. the wbsearchentities API for what is left (catches "Haim" -> "Haïm")
  3. every candidate is checked against the collaboration itself

Step 3 is the important one. Wikidata will happily return a different person
with the same surname, so a match is rejected unless the person could actually
have written the joint paper: born at least 18 years before the first joint
paper, not dead before it, and matching the name on whole words. Anything that
fails is left blank, which is what the site displays as a blank.

Hand-written prose in the "bio" field is never touched (see tools/merge_bios.py).

    python3 tools/enrich_collaborators.py             # pass 1
    python3 tools/enrich_collaborators.py --fallback  # pass 2
    python3 tools/enrich_collaborators.py --validate  # pass 3 only, no queries
    python3 tools/enrich_collaborators.py --refresh   # re-query everyone
"""
import json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, "data")
ENDPOINT = "https://query.wikidata.org/sparql"
SEARCH = "https://www.wikidata.org/w/api.php"
UA = "bourgain-pedia/1.0 (mailto:serraj5@math.ethz.ch)"

# occupations that make a match plausible for a Bourgain coauthor
OK_OCCUPATION = {"Q170790",   # mathematician
                 "Q169470",   # physicist
                 "Q82594",    # computer scientist
                 "Q1622272",  # university teacher
                 "Q901"}      # scientist

# Names where the automatic match is known to be the wrong person. The paper
# says which one it is; Wikidata cannot know.
BLOCKED = {
    "Katz, N.",           # Bourgain-Katz-Tao (2004) is Nets Katz, not Nick Katz
    "Wright, James",      # the coauthor is the Edinburgh harmonic analyst
    "Goldstein, Michael", # the coauthor is at Toronto, not the UCLA namesake
    "Burq, Nicolas",      # Wikidata records only a visiting post, not Paris-Saclay
}

MIN_AGE_AT_FIRST_PAPER = 18


# ------------------------------------------------------------------- helpers
def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s or "")
                   if not unicodedata.combining(c))


def words_of(text):
    return [w for w in re.split(r"[^a-z0-9]+", strip_accents(text or "").lower()) if w]


def split_name(name):
    if "," in name:
        last, first = [x.strip() for x in name.split(",", 1)]
    else:
        parts = name.split()
        last, first = parts[-1], " ".join(parts[:-1])
    return last, first


def label_matches(label, surname, given):
    """Whole-word matching: without it, 'Sato' matches 'Satoshi'."""
    lab = " ".join(words_of(label))
    sn = " ".join(words_of(surname))
    if not sn or re.search(r"(?:^| )" + re.escape(sn) + r"(?: |$)", lab) is None:
        return False
    if not given:
        return True
    first = (words_of(given) or [""])[0]
    if not first:
        return True
    if len(first) == 1:                        # only an initial is on record
        return any(w.startswith(first) for w in lab.split())
    return re.search(r"(?:^| )" + re.escape(first) + r"(?: |$)", lab) is not None


def variants(name):
    """'Kenig, Carlos E.' -> ['Carlos E. Kenig', 'Carlos Kenig', 'C. E. Kenig']"""
    last, first = split_name(name)
    out = []
    if first:
        out.append(f"{first} {last}")
        bare = re.sub(r"\b[A-Z]\.\s*", "", first).strip()
        if bare and bare != first:
            out.append(f"{bare} {last}")
        initials = " ".join(w[0] + "." for w in first.split() if w)
        if initials:
            out.append(f"{initials} {last}")
        if len(re.sub(r"[^A-Za-z]", "", first)) <= 2:
            out.append(last)                   # initials only: surname is all we have
    else:
        out.append(last)
    seen, uniq = set(), []
    for v in out:
        k = strip_accents(v).lower()
        if k not in seen:
            seen.add(k)
            uniq.append(v)
    return uniq


def year_of(iso):
    m = re.match(r"(-?\d{1,4})-", iso or "")
    return m.group(1).lstrip("0") if m else ""


def get_json(url, tries=4, timeout=90, accept=None):
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except Exception as exc:               # noqa: BLE001
            print(f"    retry {attempt + 1}/{tries}: {exc}", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    return None


# -------------------------------------------------------------------- SPARQL
# P108 is read through its statement node so that the qualifier P580 (start
# time) is available; "latest institution" then means the one that started last.
BODY = """
  OPTIONAL { ?p wdt:P569 ?born }
  OPTIONAL { ?p wdt:P570 ?died }
  OPTIONAL { ?p wdt:P106 ?occ }
  OPTIONAL { ?p p:P108 ?stmt . ?stmt ps:P108 ?empl .
             OPTIONAL { ?stmt pq:P580 ?start } }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
"""

LABEL_QUERY = """
SELECT ?p ?pLabel ?born ?died ?emplLabel ?start ?occ WHERE {
  VALUES ?name { %s }
  ?p rdfs:label|skos:altLabel ?name .
  ?p wdt:P31 wd:Q5 .
""" + BODY + "} LIMIT 120"

QID_QUERY = """
SELECT ?p ?pLabel ?born ?died ?emplLabel ?start ?occ WHERE {
  VALUES ?p { %s }
""" + BODY + "}"


def sparql(query):
    url = ENDPOINT + "?" + urllib.parse.urlencode({"query": query, "format": "json"})
    d = get_json(url, accept="application/sparql-results+json")
    return (d or {}).get("results", {}).get("bindings", [])


def by_label(names):
    values = " ".join('"%s"@en' % n.replace('"', "") for n in names)
    return sparql(LABEL_QUERY % values)


def by_qid(qids):
    if not qids:
        return []
    return sparql(QID_QUERY % " ".join("wd:" + q for q in qids))


def search_qids(term, limit=8):
    url = SEARCH + "?" + urllib.parse.urlencode({
        "action": "wbsearchentities", "search": term, "language": "en",
        "uselang": "en", "type": "item", "limit": limit, "format": "json"})
    d = get_json(url, timeout=45)
    return [x["id"] for x in (d or {}).get("search", [])]


def collect(rows):
    """SPARQL rows -> {qid: {label, born, died, occ, employers[(start, name)]}}"""
    cands = {}
    for r in rows:
        qid = r["p"]["value"].rsplit("/", 1)[-1]
        c = cands.setdefault(qid, {"label": r["pLabel"]["value"], "born": "",
                                   "died": "", "occ": set(), "empl": {}})
        if r.get("born"):
            c["born"] = year_of(r["born"]["value"])
        if r.get("died"):
            c["died"] = year_of(r["died"]["value"])
        if r.get("occ"):
            c["occ"].add(r["occ"]["value"].rsplit("/", 1)[-1])
        if r.get("emplLabel"):
            name = r["emplLabel"]["value"]
            start = year_of(r.get("start", {}).get("value", "")) or ""
            prev = c["empl"].get(name, "")
            c["empl"][name] = max(prev, start)
    return cands


def latest_institutions(empl, keep=2):
    """'Latest institution': the employers whose stated start time is latest."""
    if not empl:
        return ""
    dated = sorted(((int(v), k) for k, v in empl.items() if v), reverse=True)
    if dated:
        return "; ".join(k for _, k in dated[:keep])
    return "; ".join(sorted(empl)[:keep])


def plausible(c, person):
    """Could this person actually have written the joint papers?"""
    first_year = (person.get("years") or [None])[0]
    if not first_year:
        return True, ""
    if c["born"]:
        try:
            if first_year - int(c["born"]) < MIN_AGE_AT_FIRST_PAPER:
                return False, f"born {c['born']}, first joint paper {first_year}"
        except ValueError:
            pass
    if c["died"]:
        try:
            if int(c["died"]) < first_year:
                return False, f"died {c['died']}, first joint paper {first_year}"
        except ValueError:
            pass
    return True, ""


def pick(cands, person):
    surname, given = split_name(person["name"])
    viable, rejected = [], []
    for qid, c in cands.items():
        if not (c["occ"] & OK_OCCUPATION):
            continue
        if not label_matches(c["label"], surname, given):
            continue
        ok, why = plausible(c, person)
        (viable if ok else rejected).append((qid, c, why))
    initials_only = bool(given) and len(re.sub(r"[^A-Za-z]", "", given)) <= 2
    if len(viable) > 1 and initials_only:
        return None, "ambiguous (" + ", ".join(c["label"] for _, c, _ in viable) + ")"
    if not viable:
        if rejected:
            return None, "rejected: " + "; ".join(
                f"{c['label']} ({why})" for _, c, why in rejected[:2])
        return None, "no confident match"
    qid, c, _ = max(viable, key=lambda t: len(t[1]["empl"]))
    c["qid"] = qid
    return c, ""


# --------------------------------------------------------------------- files
def load_all():
    with open(os.path.join(DATA, "collaborators.json"), encoding="utf-8") as fh:
        roster = json.load(fh)["collaborators"]
    bios_path = os.path.join(DATA, "collaborator_bios.json")
    bios = {}
    if os.path.exists(bios_path):
        with open(bios_path, encoding="utf-8") as fh:
            bios = json.load(fh)
    return roster, bios, bios_path


def save(bios, path):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(bios, fh, ensure_ascii=False, indent=1, sort_keys=True)


def apply_match(bios, name, c):
    entry = bios.setdefault(name, {"born": "", "died": "", "institution": "", "bio": ""})
    entry["born"] = c["born"]
    entry["died"] = c["died"]
    entry["institution"] = latest_institutions(c["empl"])
    entry["wikidata"] = c["qid"]
    entry.pop("ambiguous", None)
    return entry


def blank(bios, name, note):
    entry = bios.setdefault(name, {"born": "", "died": "", "institution": "", "bio": ""})
    entry["born"] = entry["died"] = entry["institution"] = ""
    entry.pop("wikidata", None)
    if note.startswith("ambiguous"):
        entry["ambiguous"] = note
    return entry


# --------------------------------------------------------------------- passes
def run(mode="label", refresh=False):
    roster, bios, bios_path = load_all()
    todo = [p for p in roster
            if p["name"] not in BLOCKED
            and (refresh or not bios.get(p["name"], {}).get("wikidata"))]
    print(f"{mode} pass: {len(todo)} of {len(roster)} to look up")

    filled = 0
    for i, person in enumerate(sorted(todo, key=lambda x: -x["score"]), 1):
        name = person["name"]
        if mode == "label":
            rows = by_label(variants(name))
        else:
            qids = []
            for t in variants(name)[:2]:
                qids += [q for q in search_qids(t) if q not in qids]
                time.sleep(0.4)
            rows = by_qid(qids[:12])
        c, note = pick(collect(rows), person)
        if c:
            entry = apply_match(bios, name, c)
            filled += 1
            print(f"  [{i}/{len(todo)}] {name}: {c['label']} "
                  f"{c['born'] or '?'}-{c['died'] or ''} {entry['institution'][:46]}")
        else:
            blank(bios, name, note)
            print(f"  [{i}/{len(todo)}] {name}: {note}")
        if i % 10 == 0:
            save(bios, bios_path)
        time.sleep(1.0 if mode == "label" else 0.6)

    save(bios, bios_path)
    print(f"{mode} pass matched {filled}/{len(todo)}")


def validate():
    """Re-check what is already stored, without querying anything."""
    roster, bios, bios_path = load_all()
    by_name = {p["name"]: p for p in roster}
    dropped = 0
    for name, entry in bios.items():
        person = by_name.get(name)
        if not person or not (entry.get("born") or entry.get("died")):
            continue
        ok, why = plausible({"born": entry.get("born", ""), "died": entry.get("died", "")},
                            person)
        if not ok:
            print(f"  dropping {name}: {why}")
            entry["born"] = entry["died"] = entry["institution"] = ""
            entry.pop("wikidata", None)
            dropped += 1
    save(bios, bios_path)
    print(f"dropped {dropped} implausible match(es)")


if __name__ == "__main__":
    if "--validate" in sys.argv:
        validate()
    elif "--fallback" in sys.argv:
        run("search")
    else:
        run("label", refresh="--refresh" in sys.argv)
    print("now run: python3 tools/merge_bios.py && python3 tools/build_data.py")
