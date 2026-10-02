---
title: "4.9.1 Tier 1 — Single Hub Dispatch"
parent: "4.9 A Proposed Development Path"
grand_parent: Chapter 4 — Directions for FMs in UES
nav_order: 1
status: draft
last_reviewed: 2026-10-03
---

# 4.9.1 Tier 1 — Single Hub, Dispatch Only, Simplified Topology
{: .no_toc }

{% include page-status.html %}

{: .note }
Tier 1 of the notes' proposed development path toward a multi-carrier [foundation model](../appendices/a-glossary.html#foundation-model) ([§4.9](4-9-methods-landing.html)): a proposal, not a survey of established practice.

1. TOC
{:toc}

---

## The problem

One [energy hub](../appendices/a-glossary.html#energy-hub). Fixed configuration. Multiple carriers in, multiple demands out, conversion devices and storage in between. Given boundary conditions (weather, demand profiles, prices, possibly carbon intensity), predict the operational trajectory: device outputs, storage states, imports/exports, cost, emissions.

## What kind of ML problem this is

A multivariate time series with covariates: carriers and devices are the variates, time is the sequence, weather, demand and prices are covariates known in advance, and installed capacities are static inputs. [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html) sets out this framing in full. The practical consequence is that the task is to choose and adapt an existing architecture, not to invent one.

## The one architectural decision that matters

**How do carriers exchange information?**

**Channel-independent.** Each carrier forecast separately with shared weights. Robust, strong baselines, scales well. **But it discards exactly the coupling that makes a multi-energy system interesting** — CHP ties gas to electricity to heat; a heat pump ties electricity to heat. Discarding this discards the physics.

**Cross-variate (recommended).** Carriers attend to each other (see [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) for what attention does). Two reference implementations:

- **[Any-variate attention](../appendices/a-glossary.html#any-variate-attention)** ([Moirai](../appendices/d-model-index.html#moirai)) scales to arbitrary numbers of variables — which additionally buys partial transfer across systems with *different carrier sets*.
- **Time and group attention layers** ([Chronos-2](../appendices/d-model-index.html#chronos-2)) exchange information across multiple series.

## The timescale problem

Carrier time constants differ by orders of magnitude. Indicative values, for orientation:

| Carrier / component | Characteristic time |
| :--- | :--- |
| Electricity balance | seconds – minutes |
| Battery | minutes – hours |
| Building thermal mass | hours |
| Hot water / buffer tank | hours |
| District heating network transport | tens of minutes – hours |
| Seasonal thermal storage | weeks – months |
| Hydrogen storage | days – months |

A single fixed [patch](../appendices/a-glossary.html#patch) size cannot serve all of these. The original Moirai addressed this with **multi-patch-size projection**, one input projection per patch size, so that minute-scale and year-scale data share one model.[^woo2024moirai] Its successor Moirai 2.0 dropped the idea in favour of a single patch size,[^liu2025moirai2] so the question is not settled. Representing several timescales at once is, in these notes' view, the most novel representation question in this tier.

## Recommended build path

**Do not train from scratch.** Benchmark pretrained time-series foundation models on your simulator output first, then fine-tune the best.

**Step 1 — Baselines.** Run these before anything else:

- seasonal naive or persistence: repeat the last day or week, the standard reference that uses no covariates
- a simple linear model, such as DLinear: one of a set of one-layer linear models that, in its authors' tests on nine datasets, outperformed the [transformer](../appendices/a-glossary.html#transformer) forecasters of the time[^zeng2023dlinear]
- gradient-boosted trees, such as LightGBM or XGBoost, on a flat feature vector[^ke2017lightgbm] [^chen2016xgboost]
- a rule-based dispatch heuristic, the domain's own baseline

{: .important }
**Why baselines matter more than they appear to.** They are not only a formality. **A baseline that ignores representation sets the floor, and the floor decides whether a foundation model is worth building at all.**
>
> The standard argument runs: the domain is heterogeneous → representation is hard → therefore a foundation model. That chain contains an unexamined step. If gradient boosting on a flat feature vector already predicts the target to within a few percent, the underlying function is not hard, and no amount of representational sophistication earns its keep.
>
> Design the baseline to test exactly the transfer claim: **split along the axis you claim to generalise over** (unseen archetypes, unseen topologies), not randomly. Then three outcomes, all useful:

| Outcome | Interpretation | What the work becomes |
| :--- | :--- | :--- |
| Baseline strong everywhere | The task is easy; FM framing unwarranted | Honest negative result; redirect toward multi-task settings |
| Strong on scalars, weak on profiles | Representation matters at sequence level | Sequence-level emulation |
| Strong in-distribution, collapses out | Representation matters for transfer | The FM claim proper — the most interesting version |

Run this **before** committing to a large data-generation campaign or an architecture. It is a small job by comparison, and it either confirms the framing or changes it while changing course is still cheap. Keep it scoped: it is a reference point, not a research programme.

**Step 2 — [Zero-shot](../appendices/a-glossary.html#zero-shot) [TSFM](../appendices/a-glossary.html#tsfm) evaluation.** Dispatch depends heavily on covariates, so prioritise the models that use them: Chronos-2 and [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) model target and covariates jointly, and TabPFN-TS also takes static metadata, which maps onto installed capacities. [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5) adds covariates only through a separate linear regressor, and [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0) ignores them, so treat both as univariate references ([§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)). Evidence from load forecasting suggests zero-shot results will be weaker for one system than for many pooled together ([§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html)). (See [§2.4.4](../chapter-2-fm-foundations/2-4-4-tabular-fms.html) — a tabular FM here is also the strongest available version of the attribute-list baseline, one row of attributes per building ([§2.3.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions)), so this step doubles as part of Step 1. See also [§4.1](4-1-off-the-shelf-fms.html) for this same move applied to pure forecasting.)

**Step 3 — Fine-tune.** Chronos-2 is a single model of 120M parameters,[^ansari2025chronos2] small enough to fine-tune on a modest compute budget. [Lag-Llama](../appendices/d-model-index.html#lag-llama) is a decoder-only model built on the [LLaMA](../appendices/d-model-index.html#llama) language-model architecture,[^rasul2023laglama] so the standard tools for [fine-tuning](../appendices/a-glossary.html#fine-tuning) language models, such as low-rank adaptation (LoRA), apply to it directly ([§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html)). It is univariate, though, so it suits single carriers better than the coupled problem.

**Step 4 — Custom architecture, only if steps 1–3 leave a gap you can characterise.**

## Where the genuine research contribution sits

Off-the-shelf models are not designed for three things, and these are where new work is needed:

**(a) Storage state.** State of charge changes slowly, depends on everything that happened before, and links distant timesteps. Producing a long trajectory by feeding each forecast back in as the next input (autoregressive rollout) accumulates error, so the state drifts. None of the general models in [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html) has a mechanism to keep a variable within physical bounds; they forecast values, not constrained states. Options: an architecture that carries the state explicitly, constraints on the accumulated quantity in the loss, or a final step that moves each prediction onto the nearest physically valid value.

**(b) Energy balance.** Predictions must conserve energy for each carrier at each timestep. None of the general models in [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html) enforces a conservation law across its outputs, so this has to be added; see [§4.10.2](4-10-building-it.html#4102-enforcing-physics) for the options.

**(c) Long horizons.** Each model is trained up to a maximum forecast length, and beyond it the forecast is built by rollout, with the error growth described in (a) ([§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)). Seasonal storage needs exactly those long horizons.

**A side result that comes cheaply.** Because the relationship between covariates and target is set by physics in a simulator, this setting can test cleanly how well these models use covariates at all. That is an open question: in building energy and electricity demand, adding covariates to general models often changed little.[^mulayim2026bem] [^cheong2026exogenous]

[^woo2024moirai]: Woo, G., Liu, C., Kumar, A. et al. (2024). [Unified training of universal time series forecasting transformers](https://arxiv.org/abs/2402.02592). ICML 2024. arXiv:2402.02592.
[^liu2025moirai2]: Liu, C., Aksu, T., Liu, J. et al. (2025). [Moirai 2.0: When less is more for time series forecasting](https://arxiv.org/abs/2511.11698). arXiv:2511.11698.
[^zeng2023dlinear]: Zeng, A., Chen, M., Zhang, L., Xu, Q. (2023). [Are transformers effective for time series forecasting?](https://doi.org/10.1609/aaai.v37i9.26317) *AAAI 2023*, 37(9), 11121–11128. arXiv:2205.13504.
[^ke2017lightgbm]: Ke, G., Meng, Q., Finley, T. et al. (2017). [LightGBM: A highly efficient gradient boosting decision tree](https://papers.nips.cc/paper_files/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html). *NeurIPS 2017*.
[^chen2016xgboost]: Chen, T., Guestrin, C. (2016). [XGBoost: A scalable tree boosting system](https://doi.org/10.1145/2939672.2939785). *KDD '16*, 785–794.
[^ansari2025chronos2]: Ansari, A. F., Shchur, O., Küken, J. et al. (2025). [Chronos-2: From univariate to universal forecasting](https://arxiv.org/abs/2510.15821). arXiv:2510.15821.
[^mulayim2026bem]: Mulayim, O. B., Quan, P., Han, L. et al. (2026). [Can time-series foundation models perform building energy management tasks?](https://doi.org/10.1017/dce.2026.10040) *Data-Centric Engineering*, 7, e9.
[^cheong2026exogenous]: Cheong, W. S., Jiang, L. L., Ling, J. N. S. (2026). [Assessing electricity demand forecasting with exogenous data in time series foundation models](https://arxiv.org/abs/2602.05390). AI4TS Workshop at AAAI 2026. arXiv:2602.05390.
[^rasul2023laglama]: Rasul, K., Ashok, A., Williams, A. R. et al. (2023). [Lag-Llama: Towards foundation models for probabilistic time series forecasting](https://arxiv.org/abs/2310.08278). arXiv:2310.08278

---
[← Previous: 4.9 A Proposed Development Path](4-9-methods-landing.html) · [Next: 4.9.2 Tier 2 →](4-9-2-methods-tier2.html)
