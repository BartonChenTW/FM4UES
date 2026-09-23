---
title: "6.2 How to Contribute"
parent: Chapter 6 — Outlook
nav_order: 2
status: draft
last_reviewed: 2026-09-11
---

# 6.2 How to Contribute to This Knowledge Base
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

This is a living knowledge base — corrections, references, and new sections are welcome from anyone in the urban energy systems (UES) or foundation model (FM) communities. Full contribution mechanics (issue templates, style notes, the references workflow) live in `CONTRIBUTING.md` in the repository root; this page summarises where a contribution is most likely to land well, given the structure of this book.

## Where a contribution is likely to matter most

- **Filling a stub.** [Chapter 4](../chapter-4-directions/index.html) contains several sections that are still thin, each opening with a note that says what it still lacks ([§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html), [§4.2](../chapter-4-directions/4-2-fms-for-building-stocks.html), [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html), [§4.4](../chapter-4-directions/4-4-generative-design.html)). These are exactly the sections most likely to benefit from someone who knows a specific corner of that direction well.
- **Closing a gap.** Each of the nine gaps in [§6.1](6-1-open-gaps.html) is stated as a research contribution someone could actually make. G8 in particular is explicitly flagged as more a building-simulation problem than a machine-learning one — the community best placed to resolve it may not be the one currently reading this book.
- **Adding a reference.** If you know of published work that bears on a claim in this book and is not yet cited, see [`references/README.md`](../references/README.md) for how the bibliography is organised and how to add an entry.
- **Reporting an error or an outdated claim.** The field this book covers moves fast (see the publication-count warning on the [homepage](../index.html)); anything that reads as a landscape or novelty claim should be re-checked periodically, and corrections are always welcome.

## Ways to contribute

- **Report an error or an outdated claim** — [open an issue](https://github.com/BartonChenTW/FM4UES/issues).
- **Suggest a reference** — [open an issue](https://github.com/BartonChenTW/FM4UES/issues) with the citation (a DOI or URL is enough) and a one-line note on which section it belongs to.
- **Propose a new section or restructuring** — [open an issue](https://github.com/BartonChenTW/FM4UES/issues) first to discuss scope before writing, since this book has an explicit outline (sections are numbered and cross-referenced).
- **Fix a typo or small wording issue** — [open a pull request](https://github.com/BartonChenTW/FM4UES/pulls) directly is fine, no need to open an issue first.
- **Larger additions** (a new section, a reworked argument, filling in a stub) — [open an issue](https://github.com/BartonChenTW/FM4UES/issues) to discuss before investing time in a draft.

## Style notes

- Written for a reader who knows urban energy systems well and machine learning less well (or vice versa) — define jargon on first use, or link to the [Glossary](../appendices/a-glossary.html).
- Cite claims, using Markdown footnotes matching the `.bib` citation keys — see `CONTRIBUTING.md` for the exact convention.
- British English spelling, matching the existing text (e.g. "optimisation", "modelling").
- Match the existing front-matter pattern (`title`, `parent`, `nav_order`, `status`, `last_reviewed`) — see any section page for the format.

---
[← Previous: 6.1 Open Gaps](6-1-open-gaps.html) · [Back to Chapter 6](index.html) · [Back to Home](../index.html)
