# Massachusetts: law history in git

The Constitution of the Commonwealth of Massachusetts and chapters of the General Laws as a git repository: one file per article, section or article of amendment of the Constitution and one per section of the General Laws, committed with the General Court as its publisher. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/massachusetts/`.

**What is in it now**

| Folder | Act | Units | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the Commonwealth of Massachusetts (1780, as amended): Preamble, Part the First, Part the Second, the Articles of Amendment, and the notes on amendments rejected | 229 | One version: the General Court's online text as captured on 15 October 2026 |
| `gl-chapter-0030a/` | General Laws, Chapter 30A: State administrative procedure | 41 | One version: the General Court's online text, each section from its newest web capture (captured 2026-03-14 to 2026-10-17), dated 2026-10-18 |
| `gl-chapter-0066/` | General Laws, Chapter 66: Public records | 34 | One version: the General Court's online text, each section from its newest web capture (captured 2026-02-10 to 2026-10-17), dated 2026-10-19 |
| `gl-chapter-0183/` | General Laws, Chapter 183: Alienation of land | 85 | One version: the General Court's online text, each section from its newest web capture (captured 2025-02-16 to 2026-10-16), dated 2026-10-21 |
| `gl-chapter-0186/` | General Laws, Chapter 186: Estates for years and at will | 41 | One version: the General Court's online text, each section from its newest web capture (captured 2025-07-20 to 2026-10-16), dated 2026-10-19 |
| `gl-chapter-0207/` | General Laws, Chapter 207: Marriage | 59 | One version: the General Court's online text, each section from its newest web capture (captured 2026-01-15 to 2026-10-17), dated 2026-10-20 |
| `gl-chapter-0208/` | General Laws, Chapter 208: Divorce | 71 | One version: the General Court's online text, each section from its newest web capture (captured 2025-06-13 to 2026-10-13), dated 2026-10-19 |
| `gl-chapter-0231/` | General Laws, Chapter 231: Pleading and practice | 163 | One version: the General Court's online text, each section from its newest web capture (captured 2024-12-11 to 2026-10-17), dated 2026-10-19 |
| `gl-chapter-0265/` | General Laws, Chapter 265: Crimes against the person | 96 | One version: the General Court's online text, each section from its newest web capture (captured 2024-12-07 to 2026-10-17), dated 2026-10-17 |
| `gl-chapter-0266/` | General Laws, Chapter 266: Crimes against property | 218 | One version: the General Court's online text, each section from its newest web capture (captured 2024-12-09 to 2026-10-16), dated 2026-10-18 |

That is all the law this repository holds today. This is a first build: most chapters of the General Laws, the session laws and regulations are not in it, and it has no amendment history yet.

## Where the text comes from

The General Court publishes the whole Constitution as one page at malegislature.gov/Laws/Constitution. The text is the page's text: the General Court's bracketed notes inside it (such as "[Annulled by Amendments, Art. CVI.]") are part of the printed Constitution and are kept.

The General Laws are published one page per section (malegislature.gov/Laws/GeneralLaws/...), with a table of contents page per chapter. The sha256 of the pages read for each chapter is in `data/versions.json`.

## Dates

- The page states no date of its own, so the capture date, **15 October 2026**, dates the single version. It is the oldest version available: the repository holds the Constitution as published online then, with every amendment the General Court had printed by that day (121 articles of amendment), and nothing earlier. The first commit is credited to the publisher as "oldest version available".
- The dates on which the amendments took effect are in the text (the closing notes say when each was ratified), but they are not yet built into dated versions.
- Each General Laws chapter is one version, dated by the newest capture day of its section pages (or, if later, the day of the newest law already in the repository, so the history only grows), and credited to the publisher as "oldest version available". Its sections were captured on different days, which the commit's note gives; a section amended after its capture would show its older text here.

## What it does not show

- Any amendment history: the Constitution as it stood on earlier dates.
- The other chapters of the General Laws: web archives hold only part of their section pages, so a chapter is left out until every one of its sections can be read.
- Nothing here is an official publication.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
