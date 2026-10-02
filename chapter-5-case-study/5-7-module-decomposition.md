---
title: "5.7 Module and Task Decomposition"
parent: Chapter 5 — Case Study
nav_order: 7
status: draft
last_reviewed: 2026-09-11
---

# 5.7 Module and Task Decomposition
{: .no_toc }

{% include page-status.html %}

Do not build one model. Build an encoder stack, a pretraining task suite, and a downstream benchmark — so the programme is evaluable at each stage rather than a ten-year leap of faith.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Encoders

| Module | Input | Status |
| :--- | :--- | :--- |
| Demand encoder | Building and district load profiles | Off-the-shelf time-series FM encoders plug in directly (see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html), [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html)) |
| Weather and climate encoder | Irradiance, temperature, climate years | Adapt a geospatial FM (see [§2.4.5](../chapter-2-fm-foundations/2-4-5-geospatial-weather-fms.html)) |
| Technology encoder | Device class and parameters | Needs building — a device vocabulary (see [§5.5.1](5-5-token-schema.html#551-token-schema)) |
| Topology encoder | The bipartite hub graph | Heterogeneous graph [transformer](../appendices/a-glossary.html#transformer), GridFM-adjacent (see [§2.7](../chapter-2-fm-foundations/2-7-architectures.html), [§4.9.2](../chapter-4-directions/4-9-2-methods-tier2.html)) |
| Market and policy encoder | Tariffs, carbon price, regulatory constraints | Needs building |

## Pretraining tasks (self-supervised, no solver labels)

- **P1 — Masked carrier-flow reconstruction.** The direct [GridFM](../appendices/d-model-index.html#gridfm) analogue and workhorse objective. Corresponds to M1 in [§5.5.3](5-5-token-schema.html#553-masking-tasks-mapped-onto-the-tokens).
- **P2 — Masked device-attribute inference.** Hide a converter's capacity or efficiency, infer from observed flows. Corresponds to M3.
- **P3 — Rollout / next-window prediction.** Trains inter-temporal structure. Corresponds to M5.
- **P4 — Masked topology completion.** Which device connects these two carrier-buses. Corresponds to M4.

See [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html) for what self-supervision means generally, if this framing is new.

## Downstream tasks (the benchmark suite)

| Task | Output | Why well-posed |
| :--- | :--- | :--- |
| D1 Operation emulation | Dispatch trajectory given fixed design | Deterministic under a fixed rule |
| D2 Feasibility classification | Can this design serve this demand | Binary, cheap to label |
| D3 Cost / emissions regression | Objective value from design + boundary conditions | Unique even when the argmin is not |
| D4 Active-set / binary prediction | Which technologies install, which constraints bind | Feeds warm-starting (Family 3, [§4.9.3](../chapter-4-directions/4-9-3-methods-tier3.html)) |
| D5 Flexibility envelope | Aggregate hub flexibility for grid services | The natural grid-FM handshake ([Phase 5](5-1-roadmap.html#phase-5-year-610--multi-scale-coupling)) |
| D6 Retrofit / anomaly | Diagnosis on operating hubs | Where real operating-building data validates |

**D3 is well-posed even where "predict the optimal design" is not.** This is the core reason for the phase sequencing in [§5.1](5-1-roadmap.html), and it directly addresses [risk 1](5-8-risks.html#581-five-risks-most-likely-to-kill-the-programme) (label degeneracy).

Publishing this benchmark suite openly is one of the cheapest, highest-value artefacts this programme can produce — see [gap G4](../chapter-6-outlook/6-1-open-gaps.html#g4).

---
[← Previous: 5.6 Physics Loss](5-6-physics-loss.html) · [Next: 5.8 Risks and Unsettled Design Questions →](5-8-risks.html)
