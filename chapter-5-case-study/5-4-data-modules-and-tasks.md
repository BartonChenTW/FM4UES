---
title: "5.4 Data, Modules and Training Tasks"
parent: "Chapter 5 — Case Study"
nav_order: 4
status: draft
last_reviewed: 2026-09-11
redirect_from:
  - /chapter-5-case-study/5-3-data-generation.html
  - /chapter-5-case-study/5-7-module-decomposition.html
  - /chapter-5-case-study/5-6-physics-loss.html
---

# 5.4 Data Generation, Modules and Training Tasks
{: .no_toc }

{% include page-status.html %}

The general sampling-design guidance in [§4.8.1](../chapter-4-directions/4-8-building-it.html#481-data-generation-and-sampling-design) applies unchanged to this case study. This page adds what is specific to the multi-carrier hub representation proposed in [§5.3](5-3-concrete-representation.html) and [§5.3](5-3-concrete-representation.html).
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Data generation
{: #data-generation}

### Perturbation axes specific to this representation

Beyond the general axes in [§4.8.1](../chapter-4-directions/4-8-building-it.html#481-data-generation-and-sampling-design) (configurations, boundary conditions, operating regimes), the token schema in [§5.3](5-3-concrete-representation.html) implies specific axes that must be covered for the representation itself to be exercised, not just the physics:

- **Device vocabulary coverage** — every technology class in the fixed vocabulary (§5.3) needs enough instances, at enough different capacities and part-load points, that the model learns the class embedding rather than memorising individual devices.
- **Topology variety** — bipartite graphs with varying numbers of carrier-buses and devices, varying port connectivity, so the model does not overfit to one district's specific graph shape (this is the direct analogue of the topology-generalisation claim in [§4.7.2](../chapter-4-directions/4-7-2-methods-tier2.html)).
- **Carrier-quality boundary cases** — scenarios that exercise the quality-ordering constraint (§5.3, §5.4) at its edges, e.g. heat pumps operating near their COP breakpoints, so the no-upgrade penalty is actually trained against informative examples rather than only the easy interior of the feasible region.
- **Seasonal storage cycles** — full annual cycles for any device with `state_active: true` (§5.3), since the L1/L2 temporal hierarchy exists specifically to let the model learn cross-season coupling; a corpus that only ever samples partial years cannot exercise this.

### Dispatch label generation: not only cost-optimal

Per [Phase 1 of the roadmap](5-1-roadmap.html#phase-1-year-13--simulation-surrogate-deliberately-not-optimisation), the data engine must generate **rule-based and perturbed-optimal dispatch**, not only cost-optimal dispatch. Cost-optimal dispatch is degenerate under the coupling-matrix formalism ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)): many solutions achieve the same objective, so imitating a solver teaches an arbitrary tiebreak that will not generalise (see [risk 1](5-5-risks.html#551-five-risks-most-likely-to-kill-the-programme)). Perturbing away from optimality gives a smooth, learnable manifold instead.

### What survives if the trained model is thrown away

Consistent with the budget realism in [§4.8.4](../chapter-4-directions/4-8-building-it.html#484-realistic-budget-expectations): the honest, durable deliverable of this phase is the data-generation engine and the benchmark set from [Phase 0](5-1-roadmap.html#phase-0-year-01--representation-and-the-data-engine) itself, independent of whether any specific trained model succeeds.

## Module and task decomposition
{: #modules-and-tasks}

Do not build one model. Build an encoder stack, a pretraining task suite, and a downstream benchmark — so the programme is evaluable at each stage rather than a ten-year leap of faith.

### Encoders

| Module | Input | Status |
| :--- | :--- | :--- |
| Demand encoder | Building and district load profiles | Off-the-shelf time-series FM encoders plug in directly (see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html), [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html)) |
| Weather and climate encoder | Irradiance, temperature, climate years | Adapt a geospatial FM (see [§2.4.3](../chapter-2-fm-foundations/2-4-3-clean-energy-forecasting-fms.html#weather-and-geospatial)) |
| Technology encoder | Device class and parameters | Needs building — a device vocabulary (see [§5.3.4](5-3-concrete-representation.html#534-token-schema)) |
| Topology encoder | The bipartite hub graph | Heterogeneous graph [transformer](../appendices/a-glossary.html#transformer), GridFM-adjacent (see [§2.6](../chapter-2-fm-foundations/2-6-architectures.html), [§4.7.2](../chapter-4-directions/4-7-2-methods-tier2.html)) |
| Market and policy encoder | Tariffs, carbon price, regulatory constraints | Needs building |

### Pretraining tasks (self-supervised, no solver labels)

- **P1 — Masked carrier-flow reconstruction.** The direct [GridFM](../appendices/d-model-index.html#gridfm) analogue and workhorse objective. Corresponds to M1 in [§5.3.6](5-3-concrete-representation.html#536-masking-tasks-mapped-onto-the-tokens).
- **P2 — Masked device-attribute inference.** Hide a converter's capacity or efficiency, infer from observed flows. Corresponds to M3.
- **P3 — Rollout / next-window prediction.** Trains inter-temporal structure. Corresponds to M5.
- **P4 — Masked topology completion.** Which device connects these two carrier-buses. Corresponds to M4.

See [§2.5](../chapter-2-fm-foundations/2-5-scaling-laws.html) for what self-supervision means generally, if this framing is new.

### Downstream tasks (the benchmark suite)

| Task | Output | Why well-posed |
| :--- | :--- | :--- |
| D1 Operation emulation | Dispatch trajectory given fixed design | Deterministic under a fixed rule |
| D2 Feasibility classification | Can this design serve this demand | Binary, cheap to label |
| D3 Cost / emissions regression | Objective value from design + boundary conditions | Unique even when the argmin is not |
| D4 Active-set / binary prediction | Which technologies install, which constraints bind | Feeds warm-starting (Family 3, [§4.7.3](../chapter-4-directions/4-7-3-methods-tier3.html)) |
| D5 Flexibility envelope | Aggregate hub flexibility for grid services | The natural grid-FM handshake ([Phase 5](5-1-roadmap.html#phase-5-year-610--multi-scale-coupling)) |
| D6 Retrofit / anomaly | Diagnosis on operating hubs | Where real operating-building data validates |

**D3 is well-posed even where "predict the optimal design" is not.** This is the core reason for the phase sequencing in [§5.1](5-1-roadmap.html), and it directly addresses [risk 1](5-5-risks.html#551-five-risks-most-likely-to-kill-the-programme) (label degeneracy).

Publishing this benchmark suite openly is one of the cheapest, highest-value artefacts this programme can produce — see [gap G4](../chapter-6-outlook/6-1-open-gaps.html#g4).

## Physics loss
{: #physics-loss}

Applying the general physics-enforcement mechanisms from [§4.8.2](../chapter-4-directions/4-8-building-it.html#482-enforcing-physics) to the token schema of [§5.3](5-3-concrete-representation.html), the physics loss for this representation covers:

- Per-carrier nodal balance at every bus and [patch](../appendices/a-glossary.html#patch)
- Conversion relations, `out = η(part-load, boundary conditions) × in`, with temperature-dependent COP
- Storage continuity with self-discharge and cyclic / seasonal boundary conditions
- Capacity, ramp, and minimum-uptime bounds
- Transport losses including thermal time delay
- **No-upgrade penalty** on any flow violating the quality ordering (the `quality_order` edge type in [§5.3.4](5-3-concrete-representation.html#534-token-schema))
- Emissions and primary-energy accounting

Every term references a quantity the token actually exposes — the test a representation has to pass, per [§5.2.1(e)](5-2-representation-problem.html#521-the-causal-chain-representation--data--capability). This is why the schema explicitly carries `exergy_factor`, `quality`, and `eta_params` as static token fields: each physics term above needs one of them, and a term that could not be written this way would be a sign the schema is missing a field, not that the physics should be dropped.


---
[← Previous: 5.3 A Concrete Representation and Token Schema](5-3-concrete-representation.html) · [Back to Chapter 5](index.html) · [Next: 5.5 Risks and Unsettled Design Questions →](5-5-risks.html)
