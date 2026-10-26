"""Fetch Big Brother wiki pages (Fandom MediaWiki API) into ../p2-raw.

  uv run python scripts/fetch_bb.py --count            # list the pages in scope, fetch nothing
  uv run python scripts/fetch_bb.py --limit 3          # fetch 3 pages as a trial
  uv run python scripts/fetch_bb.py                    # fetch everything found
"""
import argparse, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

API = "https://bigbrother.fandom.com/api.php"
NAMED = ["Big Brother", "Big Brother House", "Big Brother Rule Book", "Housemates", "Nominations", "Eviction", "Records & Statistics"]
UA = {"User-Agent": "mines-csci498-p2-student-project"}


def get(**params):
    url = API + "?" + urllib.parse.urlencode({**params, "format": "json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 * (attempt + 1))
    raise SystemExit(f"giving up on {url}")


def members(cat):
    """Yield (ns, title) for every member of a category."""
    cont = {}
    while True:
        d = get(action="query", list="categorymembers", cmtitle=cat, cmlimit=500, **cont)
        for m in d["query"]["categorymembers"]:
            yield m["ns"], m["title"]
        if "continue" not in d:
            return
        cont = d["continue"]


def seeds():
    """Titles to fetch: the named pages, the House category, the US hub's pages, and every US season category."""
    pages = {t: "named" for t in NAMED}
    pages.update({f"Big Brother {n} (US)": "season" for n in range(1, 31)})
    for ns, t in members("Category:Big Brother House"):
        if ns == 0:
            pages.setdefault(t, "house")
    for ns, t in members("Category:Big Brother (US)"):
        if ns == 0:
            pages.setdefault(t, "us-hub")
        elif ns == 14 and re.fullmatch(r"Category:Big Brother \d+ \(US\)", t):
            n = 0
            for ns2, t2 in members(t):
                if ns2 == 0:
                    pages.setdefault(t2, t)
                    n += 1
            print(f"{t}: {n} pages", file=sys.stderr)
    return pages


def filename(title):
    return re.sub(r"[^a-z0-9._-]+", "-", title.lower()).strip("-") + ".html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--out", default="../p2-raw")
    a = ap.parse_args()
    pages = seeds()
    print(f"{len(pages)} distinct pages", file=sys.stderr)
    if a.count:
        return
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for i, title in enumerate(sorted(pages)[: a.limit]):
        dest = out / filename(title)
        if dest.exists():
            continue
        d = get(action="parse", page=title, prop="text", redirects=1, disablelimitreport=1)
        html = d.get("parse", {}).get("text", {}).get("*", "")
        dest.write_text(f"<html><head><title>{title}</title></head><body><h1>{title}</h1>{html}</body></html>", encoding="utf-8")
        print(i, title)
        time.sleep(0.3)


main()
