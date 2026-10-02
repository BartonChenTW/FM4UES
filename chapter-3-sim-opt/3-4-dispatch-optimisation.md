---
title: "3.4 Operation / Dispatch Optimisation"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 4
status: draft
last_reviewed: 2026-09-11
---

# 3.4 Operation / Dispatch Optimisation
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## The problem

Given a fixed system configuration — devices, capacities, topology — and boundary conditions (weather, demand, prices, carbon intensity), decide how the system should run: device outputs, storage states, imports/exports, cost, emissions (T4 in [§3.1](3-1-taxonomy-of-tasks.html)). Usually formulated as a linear program (LP) if conversion efficiencies are linear and no on/off decisions are needed, or a mixed-integer linear program ([MILP](../appendices/a-glossary.html#milp)) once unit commitment, minimum part-load, or discrete states enter.

This is the workhorse task of the domain: it is the inner object called repeatedly by design optimisation (T5, [§3.5](3-5-design-sizing-optimisation.html)), control (T7), and scenario analysis (T8).

## What kind of ML problem this is

**Multivariate time series with exogenous covariates.** Precisely:

- **Variate dimension** = carriers and devices
- **Sequence dimension** = time
- **Known-future covariates** = weather, demand, prices (known because you are simulating, not forecasting)
- **Static covariates** = installed capacities, efficiencies, storage sizes
- **Target** = operational trajectory

This is a well-studied shape in machine learning — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html) for the [foundation models](../appendices/a-glossary.html#foundation-model) that already target exactly this shape. Framed this way, dispatch as a learning target means choosing and adapting an architecture, not inventing one.

**Why this matters for the amortisation argument.** Because dispatch is called so many times inside outer loops (design search, scenario evaluation, uncertainty quantification), even a modest per-call speedup compounds. This is where the amortisation argument first becomes concrete: paying a one-off training cost to replace a repeatedly-called solver call with a learned approximation. The full arithmetic, and its caveats, is developed in [§3.5](3-5-design-sizing-optimisation.html) and revisited for the case study in [Chapter 5](../chapter-5-case-study/index.html).

**Where this is developed as a build path.** This page frames dispatch as a learning problem; the concrete methods, architecture choices and build path for single-hub dispatch (Tier 1) and multi-hub multi-carrier dispatch (Tier 2) are given in [§4.9.1](../chapter-4-directions/4-9-1-methods-tier1.html) and [§4.9.2](../chapter-4-directions/4-9-2-methods-tier2.html), once [Chapter 4](../chapter-4-directions/index.html) has established which sub-fields pass the FM screen at all.

---
[← Previous: 3.3 Multi-Carrier Energy Hub Formalism](3-3-energy-hub-formalism.html) · [Next: 3.5 Design and Sizing Optimisation →](3-5-design-sizing-optimisation.html)
