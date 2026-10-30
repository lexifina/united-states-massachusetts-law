# How this repository was made (Massachusetts)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| General Court of Massachusetts | <https://malegislature.gov/Laws/Constitution> | 2026-10-30 | No reuse terms were read. The Constitution is an official legal text of the Commonwealth; statute and constitutional text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartII/TitleI/Chapter183> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartII/TitleI/Chapter186> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartII/TitleIII/Chapter207> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartII/TitleIII/Chapter208> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleII/Chapter231> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartIV/TitleI/Chapter265> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartIV/TitleI/Chapter266> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIII/Chapter30A> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |
| General Court of Massachusetts | <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleX/Chapter66> | 2026-10-30 | Statute text is not copyrightable in the United States (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). No annotations are used. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Commonwealth of Massachusetts | 1 | 2026-10-15 to 2026-10-15 |
| `gl-chapter-0183` | General Laws, Chapter 183: Alienation of land | 1 | 2026-10-21 to 2026-10-21 |
| `gl-chapter-0186` | General Laws, Chapter 186: Estates for years and at will | 1 | 2026-10-19 to 2026-10-19 |
| `gl-chapter-0207` | General Laws, Chapter 207: Marriage | 1 | 2026-10-20 to 2026-10-20 |
| `gl-chapter-0208` | General Laws, Chapter 208: Divorce | 1 | 2026-10-19 to 2026-10-19 |
| `gl-chapter-0231` | General Laws, Chapter 231: Pleading and practice | 1 | 2026-10-19 to 2026-10-19 |
| `gl-chapter-0265` | General Laws, Chapter 265: Crimes against the person | 1 | 2026-10-17 to 2026-10-17 |
| `gl-chapter-0266` | General Laws, Chapter 266: Crimes against property | 1 | 2026-10-18 to 2026-10-18 |
| `gl-chapter-0030a` | General Laws, Chapter 30A: State administrative procedure | 1 | 2026-10-18 to 2026-10-18 |
| `gl-chapter-0066` | General Laws, Chapter 66: Public records | 1 | 2026-10-19 to 2026-10-19 |

The build made 10 commits:

| Commits | Kind |
| ---: | --- |
| 10 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 10 tags.

## Dates

Each commit is dated at noon (America/New_York) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The page carries no date of its own; the date Common Crawl captured it is used as the date of the single version (oldest version available). https://malegislature.gov/Laws/Constitution

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `1cc7ec53e63f6cac1c4b5f08b3336abf693a3d50f6c0fdd2c818555b58fa85c0` (1435656 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a97ff7ea62c3c7595c5668a297d533da0b74373c`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

10 versions of 10 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Only the Constitution is in this first build: the General Laws were not taken.
- The page states no date of its own, so the capture date is the date of the single version (oldest version available).
- Each unit is one article, one section or one article of amendment, with the Part, Chapter and Section headings above it as its label. Headings that have no text of their own (for example the Part titles) are part of the labels, not units. Units are numbered in document order.
- The General Court's bracketed editorial notes inside the text (for example "[Annulled by Amendments, Art. CVI.]") are part of the printed text and are kept.
- Typographic quotes and dashes were made plain, non-breaking spaces were made ordinary spaces and runs of spaces were collapsed; the text of the page is otherwise unchanged.
- General Laws chapter 183: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2025-02-16 to 2026-10-16), so the single version is dated 2026-10-21, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 186: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2025-07-20 to 2026-10-16), so the single version is dated 2026-10-19, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 207: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2026-01-15 to 2026-10-17), so the single version is dated 2026-10-20, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 208: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2025-06-13 to 2026-10-13), so the single version is dated 2026-10-19, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 231: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2024-12-11 to 2026-10-17), so the single version is dated 2026-10-19, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 265: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2024-12-07 to 2026-10-17), so the single version is dated 2026-10-17, the newest capture day (or the Constitution's day, if later, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 266: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2024-12-09 to 2026-10-16), so the single version is dated 2026-10-18, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 30A: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2026-03-14 to 2026-10-17), so the single version is dated 2026-10-18, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.
- General Laws chapter 66: one unit per section listed in the chapter's table of contents, including sections shown as repealed. Sections were read from different web captures (2026-02-10 to 2026-10-17), so the single version is dated 2026-10-19, the newest capture day (or, if later, the day of the newest law already in the repository, or the day after it when the chapter would otherwise sort before it, so the history only grows); a section amended between its capture and that day would show its older text.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
