---
title: Zotero / BibTeX References
nav_order: 16
redirect_from: /11-references.html
---

# References (Zotero / BibTeX)

[`fm-for-ues.bib`](https://github.com/BartonChenTW/FM4UES/blob/main/references/fm-for-ues.bib)
is the master bibliography for this textbook, in BibTeX format. It is
not served by this site (see the last section below), so download it
from the repository.

## Import into Zotero

1. Open Zotero → File → Import.
2. Choose "A file (BibTeX, RIS, Zotero RDF, etc.)" and select
   `fm-for-ues.bib`.
3. Import into a new collection (recommended) so it's easy to see what
   came from this repo.

## Where the entries come from

Seeded from the categorised reference lists that used to live in
`add/reference.md` and `11-references.md` — both removed in the 2026-09-11
restructure, once their content was folded into per-page footnotes
throughout the book (see [`log.md`](https://github.com/BartonChenTW/FM4UES/blob/main/log.md) for the restructure record).
Limited to entries with a confirmed author list, venue, year, and link (DOI
or arXiv ID); entries that were marked `[to confirm]` in those source files
were not carried over.

## Adding a reference

- Citation keys use the pattern `firstauthorYEARshortname` (e.g.
  `ansari2024chronos`), matching the footnote names used when citing in
  the chapter text (see [`CONTRIBUTING.md`](../CONTRIBUTING.md)).
- If you use Zotero with the Better BibTeX plugin, it can auto-generate
  keys in this pattern and re-export this file for you.
- Don't guess missing fields (author lists, venues, DOIs) — leave them out
  or mark `[to confirm]`, and open an issue if you're not sure.

## Why this file is excluded from the built site

Set in `_config.yml`'s `exclude:` list — it's a machine-readable data file
for reference managers, not a page meant to be browsed. The rendered
bibliography for readers lives entirely in the section pages, as
Markdown footnotes.
