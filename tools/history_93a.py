"""Build a Chapter 93A historical correction from saved official page captures.

Reads only the supplied evidence directory and the existing signed-off part.
Run with --evidence <directory> --output <new corpus.d part path>.
"""
import argparse
import copy
import hashlib
import html
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup


def clean(value):
    value = html.unescape(value)
    value = value.replace("\xa0", " ").replace("\xad", "").replace("\u200b", "").replace("\ufeff", "")
    return re.sub(r"[ \t\r\n]+", " ", value).strip()


def make_part(evidence, existing):
    old = json.loads(existing.read_text(encoding="utf-8"))
    assert len(old["acts"]) == 1 and old["acts"][0]["slug"] == "gl-chapter-0093a"
    act = copy.deepcopy(old["acts"][0])
    # Correction trailers use the act URL ahead of the version URL. This act has
    # two source hosts, so let each version's source_url supply Source instead.
    act.pop("url", None)
    assert len(act["versions"]) == 1
    current = act["versions"][0]
    assert current["from"] == "2026-10-21"
    toc = next(evidence.glob("2010-chapter-*.html"))
    raw = toc.read_bytes()
    digest = hashlib.sha256(raw)
    section_dates = []
    units = {}
    for number in range(1, 12):
        page = next(evidence.glob(f"2010-section{number}-*.html"))
        raw = page.read_bytes()
        digest.update(raw)
        section_dates.append(page.stem.rsplit("-", 1)[1][:8])
        soup = BeautifulSoup(raw, "html.parser")
        heading = soup.select_one("li.subHeading4")
        body = soup.select_one("div.Widget.cswhiteBlue div.widgetContent")
        if heading is None or body is None:
            raise ValueError(f"missing heading/body: {page.name}")
        title = clean(heading.get_text(" ", strip=True))
        paragraphs = [clean(p.get_text(" ", strip=True)) for p in body.select("p")]
        paragraphs = [p for p in paragraphs if p]
        if not title.startswith(f"Section {number} ") or not paragraphs or not paragraphs[0].startswith(f"Section {number}."):
            raise ValueError(f"unexpected section: {page.name}: {title}")
        label = f"M.G.L. c. 93A, \u00a7 {number}"
        units[f"sec-{number:04d}"] = {
            "label": label,
            "kind": "section",
            "text": f"# Section {number}: {title.removeprefix(f'Section {number} ')}\n" + "".join(p + "\n" for p in paragraphs),
        }
    if set(units) != set(current["units"]):
        raise ValueError("historic section range differs from signed-off part")
    date = max(section_dates)
    if date != "20100921":
        raise ValueError(f"unexpected capture dates: {section_dates}")
    captured = f"{date[:4]}-{date[4:6]}-{date[6:8]}"
    original = "http://www.malegislature.gov:80/Laws/GeneralLaws/PartI/TitleXV/Chapter93A"
    source = f"https://web.archive.org/web/20100918122547id_/{original}"
    earlier = {
        "from": captured,
        "text_as_of": captured,
        "in_force_basis": "The official section pages give no amendment or commencement date for this assembled text. The latest official-page archive capture (2010-09-21) is used only as the documented as-of baseline; it does not assert that a change took force that day.",
        "source_url": source,
        "sha256": digest.hexdigest(),
        "units": units,
        "credits": {},
        "note": "Internet Archive copies of the General Court's official Chapter 93A table of contents and all 11 section pages, captured 2010-09-18 to 2010-09-21. Source: archive capture 2010-09-18 for the chapter page; individual section capture dates are retained in the evidence list.",
    }
    act["versions"] = [earlier, current]
    return {
        "corrects": existing.name,
        "acts": [act],
        "sources": [{
            "name": "General Court of Massachusetts: Chapter 93A, Internet Archive copies of official pages (2010 captures)",
            "url": source,
            "retrieved": "2026-11-11",
            "requests": 0,
            "licence": "Official Massachusetts statute text is not copyrightable in the United States; no annotations are used.",
            "notes": "Internet Archive capture of the official chapter page on 2010-09-18 and all 11 official section pages on 2010-09-18 to 2010-09-21.",
        }],
        "decisions": ["Chapter 93A: adds a 2010 archival as-of text before the existing 2026 version. The original signed-off act and its current version are copied without change. Later complete 2016 and 2022 archived section sets show the same letters and digits as the 2010 text after excluding a site-internal marker; they add no distinct historical wording. Archive captures are labelled; their timestamps are not claimed as amendment dates."],
        "ai_use": ["An AI worker wrote this deterministic parser and reviewed its checks; no model wrote or corrected legal text."],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, required=True)
    ap.add_argument("--existing", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    part = make_part(args.evidence, args.existing)
    payload = json.dumps(part, ensure_ascii=False, indent=1) + "\n"
    args.output.write_text(payload, encoding="utf-8", newline="\n")
    print(part["acts"][0]["slug"], [v["from"] for v in part["acts"][0]["versions"]], len(payload))


if __name__ == "__main__":
    main()
