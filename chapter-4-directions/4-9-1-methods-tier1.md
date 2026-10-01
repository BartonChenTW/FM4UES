---
title: "4.9.1 Tier 1 — Single Hub Dispatch"
parent: "4.9 A Proposed Development Path"
grand_parent: Chapter 4 — Directions for FMs in UES
nav_order: 1
status: draft
last_reviewed: 2026-09-11
---

# 4.9.1 Tier 1 — Single Hub, Dispatch Only, Simplified Topology
{: .no_toc }

{% include page-status.html %}

{: .note }
Tier 1 of the book's proposed development path toward a multi-carrier foundation model ([§4.9](4-9-methods-landing.html)): a proposal, not a survey of established practice.

1. TOC
{:toc}

---

## The problem

One energy hub. Fixed configuration. Multiple carriers in, multiple demands out, conversion devices and storage in between. Given boundary conditions (weather, demand profiles, prices, possibly carbon intensity), predict the operational trajectory: device outputs, storage states, imports/exports, cost, emissions.

## What kind of ML problem this is

**Multivariate time series with exogenous covariates.** Precisely:

- **Variate dimension** = carriers and devices
- **Sequence dimension** = time
- **Known-future covariates** = weather, demand, prices (known because you are simulating, not forecasting)
- **Static covariates** = installed capacities, efficiencies, storage sizes
- **Target** = operational trajectory

This is a well-studied shape (see [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html)). You are choosing and adapting an architecture, not inventing one.

## The one architectural decision that matters

**How do carriers exchange information?**

**Channel-independent.** Each carrier forecast separately with shared weights. Robust, strong baselines, scales well. **But it discards exactly the coupling that makes a multi-energy system interesting** — CHP ties gas to electricity to heat; a heat pump ties electricity to heat. Discarding this discards the physics.

**Cross-variate (recommended).** Carriers attend to each other (see [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) for what attention does). Two reference implementations:

- **Any-variate attention** ([Moirai](../appendices/d-model-index.html#moirai)) scales to arbitrary numbers of variables — which additionally buys partial transfer across systems with *different carrier sets*.
- **Time and group attention layers** ([Chronos-2](../appendices/d-model-index.html#chronos-2)) exchange information across multiple series.

## The timescale problem

Carrier time constants differ by orders of magnitude:

| Carrier / component | Characteristic time |
| :--- | :--- |
| Electricity balance | seconds – minutes |
| Battery | minutes – hours |
| Building thermal mass | hours |
| Hot water / buffer tank | hours |
| District heating network transport | tens of minutes – hours |
| Seasonal thermal storage | weeks – months |
| Hydrogen storage | days – months |

A single fixed patch size cannot serve all of these. The reference solution is **multi-patch-size projection** (Moirai), handling minute-to-year-scale data in one architecture. This is the direct analogue of the spatial harmonisation problem in Earth-system coupling, where combining incompatible discretisations risks losing physical adjacency and introducing aliasing in attention layers — yours is temporal rather than spatial, and it is arguably the most genuinely novel representation question available in this tier.

## Recommended build path

**Do not train from scratch.** Benchmark pretrained time-series foundation models on your simulator output first, then fine-tune the best.

**Step 1 — Baselines (mandatory).** Omit these and reviewers will dismantle the work:

- seasonal-naive / persistence (the standard covariate-free reference)
- linear model (DLinear-class)
- gradient boosting (LightGBM/XGBoost)
- rule-based dispatch heuristic (domain baseline)

{: .important }
**Why baselines matter more than they appear to.** The usual justification is reviewer defence. The stronger one is epistemic: **a representation-free baseline establishes the floor, and the floor determines whether the foundation-model framing is warranted at all.**
>
> The standard argument runs: the domain is heterogeneous → representation is hard → therefore a foundation model. That chain contains an unexamined step. If gradient boosting on a flat feature vector already predicts the target to within a few percent, the underlying function is not hard, and no amount of representational sophistication earns its keep.
>
> Design the baseline to test exactly the transfer claim: **split along the axis you claim to generalise over** (unseen archetypes, unseen topologies), not randomly. Then three outcomes, all useful:

| Outcome | Interpretation | What the work becomes |
| :--- | :--- | :--- |
| Baseline strong everywhere | The task is easy; FM framing unwarranted | Honest negative result; redirect toward multi-task settings |
| Strong on scalars, weak on profiles | Representation matters at sequence level | Sequence-level emulation |
| Strong in-distribution, collapses out | Representation matters for transfer | The FM claim proper — the most interesting version |

Run this **before** committing to a large data-generation campaign or an architecture. It is roughly a week of work and it either validates the framing or redirects it while redirection is still cheap. Keep it scoped: it is a reference point, not a research programme.

**Step 2 — Zero-shot TSFM evaluation.** Chronos-2, [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0), [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5), [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts). Prioritise the covariate-aware ones — Chronos-2 and TabPFN-TS model target and covariates jointly; TabPFN-TS is the one that also ingests static metadata, which maps onto your installed capacities. (See [§2.4.4](../chapter-2-fm-foundations/2-4-4-tabular-fms.html) — a tabular FM here is also the strongest available version of the attribute-list baseline, one row of attributes per building ([§2.3.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions)), so this step doubles as part of Step 1. See also [§4.1](4-1-off-the-shelf-fms.html) for this same move applied to pure forecasting.)

**Step 3 — Fine-tune.** Chronos-2 ships in five sizes from 9M to 710M parameters, so this fits a modest compute budget comfortably. [Lag-Llama](../appendices/d-model-index.html#lag-llama)[^rasul2023laglama] is architecturally identical to LLMs, so LoRA/PEFT tooling applies directly (see [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html)) and it is the easiest to fine-tune on a large set of proprietary series.

**Step 4 — Custom architecture, only if steps 1–3 leave a gap you can characterise.**

## Where the genuine research contribution sits

Off-the-shelf models will fail on three things. These are the contribution:

**(a) Storage state.** State of charge is a slow, path-dependent variable coupling across long horizons. Autoregressive rollout accumulates error and drifts. Nothing in the TSFM literature handles a *constrained state variable* whose bounds must never be violated. Options: explicit state-carrying architecture, integral constraints in the loss, or a projection step.

**(b) Energy balance.** Predictions must conserve energy per carrier per timestep. See [§4.10.2](4-10-building-it.html#4102-enforcing-physics) for enforcement mechanisms. This is a real methodological contribution because no general TSFM does it.

**(c) Long horizons.** All these models degrade beyond their trained maximum prediction length. Seasonal storage requires exactly the horizons where they are weakest.

**Bonus result available cheaply:** because your covariate–target relationship is *physically determined*, you can rigorously test how well these models actually exploit covariates — an open question the community has flagged as under-verified. That is a clean, publishable side contribution.

[^rasul2023laglama]: Rasul, K., Ashok, A., Williams, A. R. et al. (2023). [Lag-Llama: Towards foundation models for probabilistic time series forecasting](https://arxiv.org/abs/2310.08278). arXiv:2310.08278

---
[← Previous: 4.9 Methods Landing](4-9-methods-landing.html) · [Next: 4.9.2 Tier 2 →](4-9-2-methods-tier2.html)
