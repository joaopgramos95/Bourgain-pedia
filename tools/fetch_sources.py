#!/usr/bin/env python3
"""Fetch the raw bibliographic sources for the Bourgain-pedia.

Three independent sources are pulled and cached under data/raw/:

  zbmath_raw.json    zbMATH Open  -- the authoritative spine of the bibliography
                     (disambiguated author "Bourgain, Jean"), complete back to
                     1976 and rich in DOIs / NUMDAM / EuDML links.
  openalex_raw.json  OpenAlex     -- citation counts, DOIs, open-access PDFs.
  arxiv_raw.json     arXiv        -- preprint PDF links.

All three APIs are free and need no key.  Run:

    python3 tools/fetch_sources.py            # all sources
    python3 tools/fetch_sources.py openalex   # just one
"""
import json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(HERE, "data", "raw")
MAILTO = "serraj5@math.ethz.ch"
UA = f"bourgain-pedia/1.0 (mailto:{MAILTO})"
OPENALEX_AUTHOR = "A5029411281"   # Jean Bourgain, IAS


def get_json(url, tries=5, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except Exception as exc:                      # noqa: BLE001
            print(f"  retry {attempt + 1}/{tries}: {exc}", file=sys.stderr)
            time.sleep(3 * (attempt + 1))
    raise SystemExit(f"giving up on {url}")


def save(name, obj):
    os.makedirs(RAW, exist_ok=True)
    path = os.path.join(RAW, name)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False)
    print(f"  wrote {path} ({len(obj)} records)")


# --------------------------------------------------------------------- zbMATH
def fetch_zbmath():
    print("zbMATH Open ...")
    query = urllib.parse.quote('au:"Bourgain, Jean"')
    out, page = [], 0
    while True:
        url = (f"https://api.zbmath.org/v1/document/_search?search_string={query}"
               f"&page={page}&results_per_page=100")
        d = get_json(url)
        rows = d.get("result") or []
        if not rows:
            break
        for r in rows:
            out.append({
                "zb_id": r.get("id"),
                "zbl": r.get("identifier"),
                "title": (r.get("title") or {}).get("title"),
                "additional_titles": (r.get("title") or {}).get("additional_titles"),
                "year": r.get("year"),
                "document_type": (r.get("document_type") or {}).get("description"),
                "language": r.get("language"),
                "source": r.get("source"),
                "links": r.get("links"),
                "authors": [a.get("name") for a in
                            ((r.get("contributors") or {}).get("authors") or [])],
                "msc": r.get("msc"),
                "keywords": r.get("keywords"),
                "zbmath_url": r.get("zbmath_url"),
            })
        total = d["status"]["nr_total_results"]
        print(f"  page {page}: {len(out)}/{total}")
        page += 1
        if len(out) >= total:
            break
        time.sleep(0.5)
    save("zbmath_raw.json", out)


# ------------------------------------------------------------------- OpenAlex
def fetch_openalex():
    print("OpenAlex ...")
    out, cursor = [], "*"
    while cursor:
        url = (f"https://api.openalex.org/works?filter=author.id:{OPENALEX_AUTHOR}"
               f"&per-page=200&cursor={urllib.parse.quote(cursor)}&mailto={MAILTO}")
        d = get_json(url)
        out.extend(d["results"])
        cursor = d["meta"].get("next_cursor")
        print(f"  {len(out)}/{d['meta']['count']}")
        if not d["results"]:
            break
    save("openalex_raw.json", out)


# ---------------------------------------------------------------------- arXiv
ARXIV_NS = {"a": "http://www.w3.org/2005/Atom"}
ARXIV_EXT = "{http://arxiv.org/schemas/atom}"


def _arxiv_text(entry, tag):
    node = entry.find(ARXIV_EXT + tag)
    return node.text if node is not None else None


def fetch_arxiv():
    print("arXiv ...")
    # arXiv's author index wants "Surname, Given"; the "Bourgain_J" form
    # returns only a handful of records.
    query = urllib.parse.quote('au:"Bourgain, Jean"')
    out, start = [], 0
    while True:
        url = (f"https://export.arxiv.org/api/query?search_query={query}"
               f"&start={start}&max_results=100")
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        xml = None
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    xml = r.read()
                break
            except Exception as exc:                  # noqa: BLE001
                print(f"  retry {attempt + 1}/5: {exc}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
        if xml is None:
            raise SystemExit("arXiv unreachable")
        entries = ET.fromstring(xml).findall("a:entry", ARXIV_NS)
        if not entries:
            break
        for e in entries:
            aid = e.find("a:id", ARXIV_NS).text
            # keep the "math/" style prefix and drop the version suffix:
            # .../abs/math/0011053v1  ->  math/0011053
            ident = re.sub(r"v\d+$", "", aid.split("/abs/", 1)[-1])
            out.append({
                "arxiv_id": ident,
                "abs_url": aid,
                "title": " ".join(e.find("a:title", ARXIV_NS).text.split()),
                "published": e.find("a:published", ARXIV_NS).text,
                "authors": [a.find("a:name", ARXIV_NS).text
                            for a in e.findall("a:author", ARXIV_NS)],
                "categories": [c.get("term") for c in e.findall("a:category", ARXIV_NS)],
                "doi": _arxiv_text(e, "doi"),
                "journal_ref": _arxiv_text(e, "journal_ref"),
            })
        print(f"  start {start}: {len(out)}")
        start += 100
        time.sleep(3)
    save("arxiv_raw.json", out)


SOURCES = {"zbmath": fetch_zbmath, "openalex": fetch_openalex, "arxiv": fetch_arxiv}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(SOURCES)
    for key in wanted:
        if key not in SOURCES:
            raise SystemExit(f"unknown source {key!r}; pick from {list(SOURCES)}")
        SOURCES[key]()
