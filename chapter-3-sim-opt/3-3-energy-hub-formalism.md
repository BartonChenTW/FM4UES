---
title: "3.3 Multi-Carrier Energy Hub Formalism"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 3
status: draft
last_reviewed: 2026-09-11
---

# 3.3 Multi-Carrier Energy Hub Formalism
{: .no_toc }

{% include page-status.html %}

The classical, non-learned formalism a multi-carrier hub foundation model would need to either subsume or interoperate with.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## The energy hub

The [energy hub](../appendices/a-glossary.html#energy-hub) concept formalises a node where multiple input energy carriers (electricity, gas, heat, ...) are converted, stored, and dispatched to meet multiple output demands, via a **coupling matrix** that maps inputs to outputs through device efficiencies.[^geidl2007opf][^geidl2007future] Structurally:

```
[P_out] = [C] [P_in]
```

where `C` is the coupling matrix whose entries encode conversion efficiencies (and dispatch factors, where a device can split its input across multiple outputs). This is the formalism underlying most multi-carrier optimisation tools surveyed in [§3.6](3-6-tool-landscape.html) (ehubX, hub formulations in Calliope/oemof), and it is the object [§3.4](3-4-dispatch-optimisation.html) and [§3.5](3-5-design-sizing-optimisation.html) treat as an optimisation problem.

An earlier formulation treats the operational and structural optimisation of multi-carrier energy systems jointly — sizing and dispatch as one combined problem rather than sequential ones.[^geidl2006operational]

## Why this formalism, on its own, is not learning-ready

The coupling-matrix formalism is designed for solvers: it specifies constraints and an objective for a mathematical program, and a human or automated process assembles the matrix from a known set of devices and topology. It was never designed to be read or produced by a learned model, and three properties make the gap explicit:

- **It has no notion of a reusable, learnable token.** The matrix is bespoke to one hub's device set and topology; nothing in it is designed to be shared across hubs the way a grid bus is shared across networks.
- **It does not carry carrier quality as a first-class quantity.** Heat at 80°C and heat at 35°C are both just "heat" in the coupling matrix unless the modeller manually adds separate carriers for each temperature band — see [§5.2](../chapter-5-case-study/5-2-representation-problem.html) for why this matters for a learned representation specifically.
- **It has no standard machine-readable interchange format.** Two tools implementing the hub formalism (ehubX, Calliope, oemof) do not share a common schema; each assembles its own coupling matrix internally. [§3.7](3-7-schemas-and-standards.html) covers the closest existing attempts (ESDL, CIM) and why neither closes this gap.

This is the classical-formalism counterpart to the representation problem developed at length in [§5.2](../chapter-5-case-study/5-2-representation-problem.html) — the energy hub gives humans and solvers a working formalism; it does not by itself give a learned model a [basic element](../appendices/a-glossary.html#basic-element).

[^geidl2007opf]: Geidl, M. and Andersson, G. (2007). [Optimal power flow of multiple energy carriers](https://doi.org/10.1109/TPWRS.2006.888988). *IEEE Transactions on Power Systems*, 22(1), 145–155.
[^geidl2007future]: Geidl, M., Koeppel, G., Favre-Perrod, P. et al. (2007). [Energy hubs for the future](https://doi.org/10.1109/MPAE.2007.264850). *IEEE Power and Energy Magazine*, 5(1), 24–30.
[^geidl2006operational]: Geidl, M. and Andersson, G. (2006). [Operational and structural optimization of multi-carrier energy systems](https://doi.org/10.1002/etep.112). *European Transactions on Electrical Power*, 16(5), 463–477.

---
[← Previous: 3.2 Building Simulation](3-2-building-simulation-data.html) · [Next: 3.4 Operation / Dispatch Optimisation →](3-4-dispatch-optimisation.html)
