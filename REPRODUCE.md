# How this repository was made (Massachusetts)

This file is written by the build on 2026-11-13, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| General Court of Massachusetts | <https://malegislature.gov/Laws/Constitution> | 2026-10-30 | No reuse terms were read. The Constitution is an official legal text of the Commonwealth; statute and constitutional text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| General Court of the Commonwealth of Massachusetts, live General Laws | <https://malegislature.gov/Laws/GeneralLaws> | 2026-11-11 | Official Massachusetts statute text is a government edict; the site's terms restrict photographs and copyrighted site design, not the statutory words. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Commonwealth of Massachusetts | 1 | 2026-10-15 to 2026-10-15 |
| `gl-chapter-0021k` | General Laws, Chapter 21K: Mitigation of hazardous materials | 1 | 2026-11-11 to 2026-11-11 |
| `gl-chapter-0025c` | General Laws, Chapter 25C: Department of telecommunications and cable | 1 | 2026-11-11 to 2026-11-11 |
| `gl-chapter-0040o` | General Laws, Chapter 40O: Business improvement districts | 1 | 2026-11-11 to 2026-11-11 |
| `gl-chapter-0043e` | General Laws, Chapter 43E: Expedited state permitting | 1 | 2026-11-11 to 2026-11-11 |
| `gl-chapter-0068a` | General Laws, Chapter 68A: Limitations upon the conduct of certain trusts and corporations having charitable interests | 1 | 2026-11-11 to 2026-11-11 |
| `gl-chapter-0099` | General Laws, Chapter 99: The metric system of weights and measures | 1 | 2026-11-11 to 2026-11-11 |

The build made 7 commits:

| Commits | Kind |
| ---: | --- |
| 7 | baseline texts where the record starts |
| 0 | named laws, court decisions and treaties |
| 0 | changes no amendment note explains, credited to the publisher |
| 0 | corrections to the existing record |
| 0 | printing or layout changes |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-13.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 7 tags.

## Dates

Each commit is dated at noon (America/New_York) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The page carries no date of its own; the date Common Crawl captured it is used as the date of the single version (oldest version available). https://malegislature.gov/Laws/Constitution

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `08a4f5a43d4c388d3bf90adedbe306dd08c07557a93b7af78b7562da3658bd34` (400506 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `63170edd89e92292ac248dae17d79e486e4e9f19`, `check.py` `e340718c28cd5b0edbe37bdeab1aac31427ada66`, `on.py` `4a8aa1c9a5e6bd8cc831b90a6e68c5a6f448a13c`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Only the Constitution is in this first build: the General Laws were not taken.
- The page states no date of its own, so the capture date is the date of the single version (oldest version available).
- Each unit is one article, one section or one article of amendment, with the Part, Chapter and Section headings above it as its label. Headings that have no text of their own (for example the Part titles) are part of the labels, not units. Units are numbered in document order.
- The General Court's bracketed editorial notes inside the text (for example "[Annulled by Amendments, Art. CVI.]") are part of the printed text and are kept.
- Typographic quotes and dashes were made plain, non-breaking spaces were made ordinary spaces and runs of spaces were collapsed; the text of the page is otherwise unchanged.
- Each included chapter is one current-text baseline. Every listed section was fetched; chapters with unresolved current-text dates or normative images were held for separate review. Source pages for included chapters state no current-text date, so their retrieval day is used explicitly. Reviewed source year references unrelated to the current-text date in chapters 21K, 25C, 40O, 43A, 43E, 68A, 99.

## What AI did and did not do

The source readers and builders were developed under Lexifina's direction with coding assistants, including Claude Code and Codex.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- A model wrote the deterministic collector and parser, but did not author or edit law text.
