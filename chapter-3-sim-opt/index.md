---
title: Chapter 3 — Simulation and Optimisation in UES
nav_order: 4
has_children: true
status: draft
last_reviewed: 2026-09-29
---

# Chapter 3 — Simulation and Optimisation in Urban Energy Systems
{: .no_toc }

{% include page-status.html %}

The domain side, framed for an ML reader: what gets computed, with which tools, what shape the data has, and where the cost is.
{: .fs-6 .fw-300 }

```mermaid
flowchart LR
    A["3.1 Modelling tasks"] --> B["3.2 Building simulation"]
    A --> C["3.3 Multi-carrier hub formalism"]
    B --> D["3.4 Dispatch optimisation"]
    C --> D
    D --> E["3.5 Design and sizing optimisation"]
    A --> F["3.6 Tool landscape"]
    C --> G["3.7 Schemas and data standards"]
    E --> H["3.8 Where the cost is"]
    B --> I["3.9 Retrofit and whole-life carbon"]
    E --> I
    A --> J["3.10 Social dimensions"]
    I --> J
```

## In this chapter

| § | Page | Covers |
| :--- | :--- | :--- |
| 3.1 | [Modelling tasks and their mathematical structure](3-1-taxonomy-of-tasks.html) | Eleven tasks, their mathematical structure, typical runtime |
| 3.2 | [Building energy simulation: loads, datasets, benchmarks](3-2-building-simulation-data.html) | What's learnable, data shapes, benchmarks |
| 3.3 | [Multi-carrier energy hub formalism](3-3-energy-hub-formalism.html) | The formalism a hub FM must subsume or interoperate with |
| 3.4 | [Operation / dispatch optimisation](3-4-dispatch-optimisation.html) | LP/[MILP](../appendices/a-glossary.html#milp) dispatch as an ML problem shape |
| 3.5 | [Design and sizing optimisation](3-5-design-sizing-optimisation.html) | Bilevel structure, MILP/MINLP, the amortisation argument |
| 3.6 | [The tool landscape](3-6-tool-landscape.html) | Simulation, UBEM, optimisation and [co-simulation](../appendices/a-glossary.html#co-simulation) tool families |
| 3.7 | [Schemas and data standards](3-7-schemas-and-standards.html) | ESDL, CIM, and why neither is ML-ready |
| 3.8 | [Where the computational cost actually is](3-8-where-the-cost-is.html) | Runtime brackets and the loops that matter |
| 3.9 | [Building retrofit and whole-life carbon](3-9-retrofit-and-whole-life-carbon.html) | Retrofit as a measure-selection task, embodied carbon of materials, [LCA](../appendices/a-glossary.html#lca) data |
| 3.10 | [Social dimensions](3-10-social-dimensions.html) | Occupant behaviour and technology adoption as inputs; [energy poverty](../appendices/a-glossary.html#energy-poverty) and justice as outcomes; social data |

---
[← Previous: Chapter 2 — Foundation Knowledge of FMs](../chapter-2-fm-foundations/index.html) · [Next: Chapter 4 — Directions for FMs in UES →](../chapter-4-directions/index.html)
