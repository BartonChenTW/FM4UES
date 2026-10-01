---
title: "4.8 Candidate Sub-Fields for a New FM"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 8
status: draft
last_reviewed: 2026-09-29
---

# 4.8 Candidate Sub-Fields for a New Foundation Model
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## Most promising near-term, limited by data licensing

- **Metadata-conditioned load FM** — cross-attending meter time series with building-register attributes and household survey covariates (on why meter data and household attributes are entangled, see [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html#data-shapes)). Mature tooling (efficient time-series FMs as baselines — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)), EnergyBench as anchor dataset ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)), simulator-paired labels (e.g. from CESAR-P) as differentiator. The method is within reach; the limitation is data. Meter readings paired with building and household attributes are usually held under licences that restrict pooling them into a shared training corpus, and measured data rarely comes paired with building attributes in the first place ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)).

## Novel intersections, in rough order of tractability

1. **Grid-load bridge FM** — cross-attend load-FM embeddings (demand side) with a grid FM's graph representation (topology and physics side). Building and aggregate loads are literally the boundary condition grid-level OPF solves against. Risk: coupling two different basic elements (a time-series patch and a graph node) is an open architectural question — the general form of which is the interface problem in [§4.11](4-11-ecosystem.html).
2. **Simulation-grounded UBEM FM** — formalise simulator-generated building→load pairs (e.g. from CESAR-P, see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)) as a deliberate pretraining corpus for a conditional generative FM, rather than treating simulator output only as fine-tuning or evaluation data.
3. **Weather / microclimate-conditioned building energy FM** — fuse a geospatial FM (see [§2.4.5](../chapter-2-fm-foundations/2-4-5-geospatial-weather-fms.html)) with load or UBEM data, since urban heat islands drive peak cooling load and grid stress simultaneously. No existing paired dataset at FM scale; you would build the corpus, not just the model.
4. **Multi-carrier energy hub FM** — not yet FM-ready in the strict sense. No established basic element, no public data, and discrete decision structure resists replacement by a learned representation. Longer-horizon research question, and the subject of [Chapter 5](../chapter-5-case-study/index.html).
5. **Retrofit and whole-life-carbon FM** — given a building, propose measure combinations scored on cost, operational and embodied emissions ([§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html)). Listed last because it needs both the building representation of [G8](../chapter-6-outlook/6-1-open-gaps.html#g8) and the decision-space representation of [G9](../chapter-6-outlook/6-1-open-gaps.html#g9). Its training data is generable — a stock simulator on one side, LCA impact factors on the other — but the quantity take-off linking the two is archetype-approximated.

---
[← Previous: 4.7 Reading the Screen](4-7-reading-the-screen.html) · [Next: 4.9 A Proposed Development Path →](4-9-methods-landing.html)
