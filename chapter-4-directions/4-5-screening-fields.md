---
title: "4.5 Screening: Which Sub-Fields Fit the FM Pattern"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 5
status: draft
last_reviewed: 2026-09-29
redirect_from: /05-screening.html
---

# 4.5 Screening: Which Sub-Fields Fit the Foundation-Model Pattern
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## Screening criteria

A task is a plausible foundation-model target if it scores well on all five. These are the questions to ask before committing.

| # | Criterion | Test |
| :--- | :--- | :--- |
| S1 | **Ground-truth generatability** | Can I produce unlimited correct labels? (Usually: is there a simulator?) |
| S2 | **Task homogeneity** | Do instances share enough structure that transfer is plausible? |
| S3 | **Transfer value** | Are there many instances, such that training once and reusing pays back? |
| S4 | **Bottleneck worth solving** | Is the existing method actually too slow or too costly, *in the loop where it is used*? |
| S5 | **Evaluability** | Is there an objective, checkable success criterion? |

{: .important }
These five screen the **task**. They do not screen the **representation**, and a task can pass all five while remaining unviable because no basic element satisfies the criterion in [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion). Run both screens; they are independent.

## Applying the screen at sub-field level

Before applying this screen task-by-task (done in [§4.6](4-6-screening-tasks.html)), it is worth applying it at the level of whole UES sub-fields, since some sub-fields already have a natural basic element and others manifestly do not:

| Sub-field | Basic element | Self-supervision task | Public pretraining data | Maturity |
| :--- | :--- | :--- | :--- | :--- |
| **Load / smart-meter FM** | Windowed patch of a meter time series | Masked / next-value reconstruction | EnergyBench, BuildingsBench (see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)) | Mature — several such models already exist ([§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html)) |
| **Grid FM** (GridFM-v0) | A bus carrying (p, q, v, δ) as a graph node; lines and transformers as edges | Masked node-feature reconstruction + AC power-flow physics loss | PGLIB-OPF, IEEE cases, gridfm-datakit | Emerging but active — see [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html) |
| **UBEM / simulator-grounded FM** | A building (envelope, geometry, HVAC, occupancy) paired with its simulated load | Conditional generation, attribute-to-profile mapping | Privately generable only | Not a found-data FM — simulator-grounded generative model |
| **Urban microclimate / geospatial-energy FM** | Satellite pixel/patch over space-time | Masked spatiotemporal reconstruction | HLS, Sentinel-2, ERA5 | Emerging, adjacent, not yet fused with load or grid data — see [§2.4.5](../chapter-2-fm-foundations/2-4-5-geospatial-weather-fms.html) |
| **District multi-energy hub** | Not yet defined | Not yet defined | Essentially none public | Immature — the subject of [Chapter 5](../chapter-5-case-study/index.html) |
| **Retrofit / whole-life carbon** | Not yet defined — a building *plus* the set of measures feasible on it ([G9](../chapter-6-outlook/6-1-open-gaps.html#g9)) | Not yet defined | Impact factors per material are published (e.g. KBOB); paired building–measure–outcome corpora privately generable only | Immature — domain side in [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html) |
| **Behaviour, adoption and social outcomes** | For people, not settled — a household or owner as an agent; for text sources, the language model's own tokens | For agents, none (no simulator of people); for text, existing LLM pretraining | Surveys (small, periodic), observed adoption (one history), meter data (privacy-constrained), text (abundant, unstructured) | Off-the-shelf LLMs usable as bounded tools; validity unresolved — see [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html), [§4.3](4-3-llm-agents-for-simulation.html) |

**Assessment.** Load FM and grid FM cleanly qualify: each has a natural atomic element, a natural masking-based pretext task, and either real or physically-simulated broad data. UBEM qualifies in spirit but is data-generation-bottlenecked rather than found-data-abundant. **The multi-carrier hub layer currently has no clean basic element** — which is itself the central finding motivating [Chapter 5](../chapter-5-case-study/index.html). **Retrofit fails for a related reason**: its basic element has to carry a decision space as well as a state, which no existing energy FM does. **Behaviour and social outcomes fail differently**: there is no simulator of people to generate ground truth, so the route is using existing language models as checked tools rather than pretraining a new model.

---
[← Previous: 4.4 Generative Design](4-4-generative-design.html) · [Next: 4.6 Screening the Tasks →](4-6-screening-tasks.html)
