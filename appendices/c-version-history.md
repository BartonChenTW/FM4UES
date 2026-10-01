---
title: Appendix C — Version History
parent: Appendices
nav_order: 3
status: draft
last_reviewed: 2026-10-02
---

# Appendix C — Version History
{: .no_toc }

{% include page-status.html %}

This book is revised continuously, so there are two ways to trace what changed:

- **Every page** has a *Page history* link under its title. It opens the list of every change made to that page on GitHub, with the date, the author and the exact edit.
- **The whole book** is released in numbered versions, listed below. Each one is a tagged [GitHub Release](https://github.com/BartonChenTW/FM4UES/releases), so you can open the book exactly as it stood at that version. Cite a version number when you need a citation to point at fixed text.

**Numbering.** A new major version (2.0, 3.0) means the book was restructured: chapters or section numbers changed. A new minor version (2.1, 2.2) means new sections, substantial rewrites, or new site features, with existing section numbers kept. Corrections and new citations between versions are not numbered separately; the page history records them.

"Last reviewed" on each page is a separate signal. It is set by hand when someone has checked the page's content, so it can be older than the page's most recent edit.

---

## 2.2 — 2 October 2026

55 section pages, 152 references, 39 models in the model index.

**New**
- [§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html) Load and smart-meter forecasting foundation models: models pretrained on load data, ten evaluations of general models sorted by aggregation level, and why aggregated load is close to solved while single buildings are not
- [§2.7](../chapter-2-fm-foundations/2-7-architectures.html#multimodal-models) Multimodal models, with a worked example from this domain
- [Appendix D](d-model-index.html) Model index: every named model with its developer, a one-line description and links to the model and its paper

**Revised**
- §1.4 no longer says time-series models converged on one architecture, and cites a source for every model it names
- §3.1 retitled "Modelling Tasks and Their Mathematical Structure", with a note for task T3
- §4.1's case for testing existing models first, rewritten in plain terms
- §4.8 states the actual status of the metadata-conditioned load model: promising, limited by data licensing
- §4.9 renamed "A Proposed Development Path" and marked as the book's own proposal rather than part of the survey
- §4.11's component table colour-codes each layer's maturity
- Labels defined on one page (R1–R4, G7) are spelled out where other pages use them

**Corrections.** Prithvi-SWIN-L is no longer cited to a paper about a different model (§1.3, §2.4.5).

**Site**
- The book's version under the site title
- Hover cards on section links, glossary terms and model names
- Enlarge and Open in new tab buttons on every diagram

## 2.1 — 1 October 2026

54 section pages, 137 references.

**New sections**
- [§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html) Evaluation criteria for UES foundation models
- [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html) Building retrofit and whole-life carbon (task T10)
- [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html) Social dimensions: behaviour, adoption, energy poverty and justice (task T11)
- [§4.11](../chapter-4-directions/4-11-ecosystem.html) A future ecosystem of UES foundation models
- Appendix C, this page

**Substantially extended**
- §2.4.3 clean-energy forecasting FMs, filled in
- §2.8 now traces the path from surrogate to foundation model
- §3.1 now includes what an energy-system model computes
- §4.1–§4.4 developed from stubs, with citations
- The Chapter 4 landing page has a screening chart of the sub-fields

**Sourcing.** References grew from 54 to 137, with citations added to Chapters 1–4 and §2.5's negative claims sourced. Corrected attributions include the Granite-GFM land-surface-temperature model (§1.3, §2.4.5).

**Site.** Added a light/dark mode toggle, footnote previews on hover, glossary definitions on hover, external links opening in a new tab, and per-page history and edit links.

## 2.0 — 11 September 2026

The book restructured into six chapters, one page per numbered section: background, FM foundations, simulation and optimisation, directions, the energy-hub case study, and outlook, plus appendices. Every claim is cited as a footnote, with a shared BibTeX bibliography (54 references). Old v1.1 page addresses redirect to their new locations.

## 1.1 — 10 September 2026

The first version published as a website: the original textbook in seven parts plus appendices.

---
[← Previous: Appendix B — Pre-Project Checklist](b-checklist.html) · [Next: Appendix D — Model Index →](d-model-index.html) · [Back to Appendices](index.html) · [Back to Home](../index.html)
