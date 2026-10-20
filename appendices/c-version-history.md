---
title: Appendix C — Version History
parent: Appendices
nav_order: 3
status: draft
last_reviewed: 2026-10-20
---

# Appendix C — Version History
{: .no_toc }

{% include page-status.html %}

These notes are revised continuously, so there are two ways to trace what changed:

- **Every page** has a *Page history* link under its title. It opens the list of every change made to that page on GitHub, with the date, the author and the exact edit.
- **The notes as a whole** are released in numbered versions, listed below. Each one is a tagged [GitHub Release](https://github.com/BartonChenTW/FM4UES/releases), so you can open the notes exactly as they stood at that version. Cite a version number when you need a citation to point at fixed text.

**Numbering.** A new major version (2.0, 3.0) means the notes were restructured: chapters or section numbers changed. A new minor version (2.1, 2.2) means new sections, substantial rewrites, or new site features, with existing section numbers kept. Corrections and new citations between versions are not numbered separately; the page history records them.

"Last reviewed" on each page is a separate signal. It is set by hand when someone has checked the page's content, so it can be older than the page's most recent edit.

---

## 3.2 — 20 October 2026

43 section pages, 286 references, 52 models in the model index.

**Developed**
- [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html#which-covariates-each-model-accepts) Which covariates (weather, calendar, building metadata) nine time-series models accept, and what that means for a building or district forecast
- [§4.2](../chapter-4-directions/4-2-fms-for-building-stocks.html) Building-stock models: residential and European evidence, three ways of combining a stock-level model with a building-level one, and the four-requirement comparison
- [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html) Agents that build simulation models: tools for envelope and HVAC inputs, how far agent-built models fall from expert ones, a proposed nine-point verification checklist, and tests of language models against real energy surveys
- [§4.4](../chapter-4-directions/4-4-generative-design.html) Generative design: how generated network designs are made feasible, and how a discrete design space can be represented for learning
- [§2.8](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) An eighth evaluation dimension, social and risk properties (representativeness, privacy, explainability, robustness), carried into §5.5
- [§3.5](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html) What learned models have been tried for embodied carbon and retrofit, with a dated search
- [§4.9](../chapter-4-directions/4-9-ecosystem.html) FMI, HELICS and mosaik as templates for coupling models, and a worked example of forecast error carried into a dispatch decision

**Revised**
- G10 ranked between G4 and G5 (§6.1), keeping its label
- §3.3 now cites its dispatch, design and runtime sections; the runtime table is marked as these notes' own estimates
- §4.5 explains how its sub-field table relates to the task screen; §4.6 defines CESAR-P and cites its sources; §4.9's demand row reads "Mature for aggregated load"
- Glossary: covariate, CV(RMSE). Model index: TimesFM 3.0, TiRex-2

**Corrections**
- §4.1 uses the revised version of the district-heating evaluation it is built on: TabPFN-TS's CVRMSE is 13.07%, Chronos-2 has the lower probabilistic error on both networks, and the claim that TabPFN-TS was better calibrated is removed
- §2.4.1 no longer says TabPFN-TS uses static metadata; its documentation says static covariates are dropped
- §4.2 no longer says no stock-pretrained model has been tested on residential or European buildings; BuildingsBench has been, and on residential buildings it does not beat a persistence baseline
- §4.3's earlier finding of no tools for envelope or technology defaults came from an arXiv-only search; journal papers show several
- Two papers listed twice in the bibliography under different keys are merged

## 3.1 — 20 October 2026

43 section pages, 204 references, 50 models in the model index.

**New**
- [§3.7](../chapter-3-sim-opt/3-7-flexible-loads.html) Flexible loads: EV charging and data centres. What flexibility is and what it is worth, how much data centres can move (measured), how EV charging is forecast and controlled, and why flexibility itself is not yet learned.
- Task **T12 Flexibility assessment** in §3.1, screened in §4.5 and read in §4.6 ("Open")
- Gap **G10 Learned flexibility** in §6.1, and a "flexibility model" direction in §4.6
- Glossary: flexibility, demand response

**Revised**
- §2.4.2 now covers the first released pretrained grid models of 2026 (GridSFM, GENCO, LUMINA, heterogeneous graph FMs, edge distillation), with a caution from real operating data; its verdict changes from "emerging" to "first released models", and §4.5 and §4.9 follow
- §2.4.5 adds EV charging stations to its evaluations table
- Model index: GridSFM, GENCO and LUMINA

## 3.0 — 20 October 2026

The notes restructured into fewer, fuller pages: **55 section pages became 42**, and section numbers changed. Every old page address redirects to its new place, and links into the middle of old pages land on the matching part of the new one.

**Merged**
- Chapter 1: the FM landscape and its directions (§1.3); why now and how to use the notes (§1.4)
- Chapter 2: surrogates vs foundation models into what defines an FM (§2.1); what does not exist yet into the §2.4 overview; weather and geospatial models with renewable generation (§2.4.3)
- Chapter 3: the energy hub formalism, dispatch, design and sizing, and where the computational cost is (§3.3); tools and data standards (§3.4)
- Chapter 4: screening sub-fields and tasks (§4.5); reading the screen and candidate sub-fields (§4.6)
- Chapter 5: the concrete representation and token schema (§5.3); data generation, modules and training tasks, and the physics loss (§5.4)

**New**
- [§2.7](../chapter-2-fm-foundations/2-7-multimodal-models.html) Multimodal models, now a section of its own and much extended: how time series are combined with attributes, images and text, what has been tried, what the evidence shows, why it is hard, and a dated search finding no multimodal foundation model yet for buildings, districts, grids or energy hubs

**Renumbered** (old → new): 2.4.5 → 2.4.3, 2.4.6 → 2.4.5, 2.6 → 2.5, 2.7 → 2.6, 2.9 → 2.8; 3.9 → 3.5, 3.10 → 3.6; 4.9 → 4.7 (with 4.9.1–4.9.3 → 4.7.1–4.7.3), 4.10 → 4.8, 4.11 → 4.9; 5.8 → 5.5.

## 2.3 — 2 October 2026

Renamed from a "working textbook" to **Working Notes**, which describes the project more accurately: a record of learning the field, sourced but not peer-reviewed. Section numbers and URLs are unchanged.

- The site description, home page, README, sidebar and contribution guide now call the project working notes. [§1.6](../chapter-1-background/1-4-why-now-and-how-to-use.html#scope-and-how-to-use) opens with "What these notes are", which says where the notes argue for something of their own.
- Every glossary term and every model in the [model index](d-model-index.html) is now linked from its first mention on each page. The model index grew from 39 to 47 entries, with PatchTST, BuildingsBench, LG-HGNN, CLIP and the language models named in §1.3.
- The glossary's "Patch" now covers image patches as well as timesteps.

## 2.2 — 2 October 2026

55 section pages, 152 references, 39 models in the model index.

**New**
- [§2.4.6](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html) Load and smart-meter forecasting foundation models: models pretrained on load data, ten evaluations of general models sorted by aggregation level, and why aggregated load is close to solved while single buildings are not
- [§2.7](../chapter-2-fm-foundations/2-7-multimodal-models.html) Multimodal models, with a worked example from this domain
- [Appendix D](d-model-index.html) Model index: every named model with its developer, a one-line description and links to the model and its paper

**Revised**
- §1.4 no longer says time-series models converged on one architecture, and cites a source for every model it names
- §3.1 retitled "Modelling Tasks and Their Mathematical Structure", with a note for task T3
- §4.1's case for testing existing models first, rewritten in plain terms
- §4.8 states the actual status of the metadata-conditioned load model: promising, limited by data licensing
- §4.9 renamed "A Proposed Development Path" and marked as the notes' own proposal rather than part of the survey
- §4.11's component table colour-codes each layer's maturity
- Labels defined on one page (R1–R4, G7) are spelled out where other pages use them

**Corrections.** Prithvi-SWIN-L is no longer cited to a paper about a different model (§1.3, §2.4.5).

**Site**
- The version number under the site title
- Hover cards on section links, glossary terms and model names
- Enlarge and Open in new tab buttons on every diagram

## 2.1 — 1 October 2026

54 section pages, 137 references.

**New sections**
- [§2.9](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) Evaluation criteria for UES foundation models
- [§3.9](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html) Building retrofit and whole-life carbon (task T10)
- [§3.10](../chapter-3-sim-opt/3-6-social-dimensions.html) Social dimensions: behaviour, adoption, energy poverty and justice (task T11)
- [§4.11](../chapter-4-directions/4-9-ecosystem.html) A future ecosystem of UES foundation models
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
