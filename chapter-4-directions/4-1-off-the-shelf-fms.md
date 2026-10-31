---
title: "4.1 Using Existing FMs Off the Shelf"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 1
status: draft
last_reviewed: 2026-10-30
---

# 4.1 Using Existing Foundation Models Off the Shelf
{: .no_toc }

{% include page-status.html %}

The most useful direction to a practitioner today, and the one requiring the least new work.
{: .fs-6 .fw-300 }

{: .note }
**Partial.** A worked example with reported numbers is below, from a published evaluation rather than a run of these notes' own, together with a table of which inputs each model accepts. What is still missing is these notes' own benchmark run: the numbers below are one group's result on their networks, not a reproduction.

1. TOC
{:toc}

---

## The direction

Before building anything bespoke, the cheapest and most immediately useful thing a UES practitioner can do is evaluate an already-pretrained, general-purpose time-series foundation model **[zero-shot](../appendices/a-glossary.html#zero-shot)** on their own forecasting problem — no training, no [fine-tuning](../appendices/a-glossary.html#fine-tuning), just point the model at the series and read off a forecast. The current generation of these models ([Chronos-2](../appendices/d-model-index.html#chronos-2), [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5), [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0), [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)) is production-grade and free or cheap to run.

This is directly applicable to **load forecasting** — predicting building or district electricity, heat, or cooling demand a few hours to days ahead (T3 in [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)) — where the task screen ([§4.5](4-5-screening-fields.html#screening-the-tasks), [§4.6](4-6-reading-the-screen.html)) finds it close to solved for aggregated load but still open for a single building, on the evidence collected in [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html).

## Why try existing models before building your own

Building and training a model of your own is a large project. Testing an existing one zero-shot needs no training at all, and the result tells you whether the larger project is worth starting. If a pretrained model already forecasts your load well enough, you can stop there.

The notes' proposed development path puts this test second in its first tier, predicting how a single [energy hub](../appendices/a-glossary.html#energy-hub) operates ([§4.7.1](4-7-1-methods-tier1.html), "Step 2"), right after setting up simple baselines. For a hub, the test is only a starting point: a hub model must also keep energy in balance and track how full the storage is, which a forecaster does not do. For load forecasting alone, the zero-shot test is often the whole job.

## A worked example: zero-shot heat-load forecasting in district heating

A published evaluation carries out exactly this exercise for one UES carrier. TabPFN-TS and Chronos-2 were run zero-shot on probabilistic heat-load forecasting for district heating networks, against trained machine-learning baselines.[^spoek2026tabpfndh] The figures below are from the revised version of the preprint (version 2, 6 October 2026), which changed some of the numbers and the title. The reported configuration and numbers are specific enough to be useful rather than merely illustrative:

- **Configuration that mattered:** hourly 24-hour-ahead forecasting with a 12-week rolling context and ambient temperature as the [covariate](../appendices/a-glossary.html#covariate) — a parsimonious setup, and longer context windows did *not* improve accuracy. This is a concrete data point for the "how far back is worth feeding in" question the [Tier 1 build path](4-7-1-methods-tier1.html) leaves open. The main benchmark feeds in measured temperature as if it were the forecast, which the authors call assuming perfect weather forecasts; a separate sensitivity analysis uses retrospective weather predictions instead. In operation only the forecast is available, so the main figures are an upper bound on what the setup achieves.
- **Accuracy:** TabPFN-TS reached [CVRMSE](../appendices/a-glossary.html#cv-rmse) 13.07% against Chronos-2's 12.48% on the main dataset. Chronos-2 also has the lower continuous ranked probability score (CRPS, which scores the whole predicted distribution rather than a single value) on both networks, with TabPFN-TS close behind. Both models beat every trained baseline in point accuracy over the full year. The quality of the predicted distribution matters for the uncertainty-awareness criterion in [§2.8](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) (dimension 6).
- **Transferability actually tested, not assumed:** the configuration was validated on a second, different network — precisely what [§2.8](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) (dimension 2) asks for and what a single-network evaluation cannot show.

One caveat worth carrying forward: TabPFN-TS is pretrained on **synthetic** data rather than real time series, which sidesteps train/test leakage but leaves open whether its learned prior actually captures district-heating dynamics specifically, or transfers on general time-series structure alone — the same synthetic-vs-real question these notes raise for their own corpus in [§4.8.1](4-8-building-it.html#481-data-generation-and-sampling-design).

## Which covariates each model accepts

The worked example uses one covariate, ambient temperature. A building or district forecast usually has three more candidates: calendar features (hour, weekday, holidays), a weather forecast, and fixed facts about the building such as floor area or heating type. Whether a model can use each one depends on the kind of covariate, and the models differ more here than anywhere else ([§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)). A **past-only** covariate is known up to the present but not over the forecast horizon (measured weather). A **known-future** covariate is available over the horizon (a weather forecast, the calendar). A **static** covariate does not change over time (building metadata).

The table is read from each model's paper or official documentation on 20 October 2026. Documentation for these models changes often, so check it again before relying on a row.

| Model | Past-only | Known-future | Categorical | Static | Several target series together | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Chronos-2](../appendices/d-model-index.html#chronos-2) | Yes | Yes | Yes | Not listed | Yes | Paper[^ansari2025chronos2] |
| [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) | No: dropped | Yes, supplied for the horizon | Yes | No: currently dropped | No: split into separate single-series forecasts | Library documentation;[^priorlabs2026tabpfntsreadme] categorical from the Chronos-2 paper[^ansari2025chronos2] |
| [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5) | No: covariates must cover the context and the horizon | Yes, through an added regression model (XReg) | Yes | Yes | No | Repository documentation[^google2026timesfm3] |
| [TimesFM 3.0](../appendices/d-model-index.html#timesfm-3-0) (August 2026) | Yes | Yes | Not stated | Not stated | Yes | Repository documentation only; no paper[^google2026timesfm3] |
| [Timestral](../appendices/d-model-index.html#timestral) (October 2026) | Yes | Yes | Yes | Not stated | Yes | Model card and blog post only; no paper[^mistral2026timestral] |
| [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0) | No | No | No | No | No | Paper: support for covariates and several target series was dropped from version 2.0[^liu2025moirai2] |
| [TiRex](../appendices/d-model-index.html#tirex) | No | No | No | No | No | Chronos-2 paper's comparison table[^ansari2025chronos2] |
| [TiRex-2](../appendices/d-model-index.html#tirex-2) (July 2026) | Yes | Yes | Not stated | Not stated | Yes | Preprint[^podest2026tirex2] |
| [Toto 2.0](../appendices/d-model-index.html#toto-2-0) | No | No | No | No | Yes | Repository: covariate support planned, not yet available[^datadog2026totoreadme] |
| [Toto](../appendices/d-model-index.html#toto) (1.0) | Yes | Yes, since February 2026 | Not stated | Not stated | Yes | Repository[^datadog2026totoreadme] and Chronos-2 paper[^ansari2025chronos2] |

TimesFM 2.5's covariate route works differently from the others. It first fits a regression model on the covariates and then uses the pretrained model to forecast what the regression leaves unexplained, so the pretrained part never sees the covariates directly.[^google2026timesfm3] Chronos-2 and TabPFN-TS model the target and the covariates together.

**What this means in practice.**

- **Weather.** Chronos-2 can take weather either as past measurements or as a forecast. TabPFN-TS and TimesFM 2.5 need it as a known-future covariate, which in operation means a weather forecast. An evaluation that supplies measured weather in its place, as the worked example's main benchmark does, reports a better result than the model would achieve in use.
- **Calendar.** Hour, weekday and holidays are known in advance, so every model that accepts covariates can use them. TabPFN-TS also generates calendar features itself.[^priorlabs2026tabpfntsreadme]
- **Building metadata.** Of the models in the table, only TimesFM 2.5 documents support for static covariates. A static value could be passed to another model as a constant known-future series, but no documentation or evaluation of that was found, so it is untested.

Accepting a covariate is not the same as using it well. On synthetic series with simple, known relationships between target and covariate, TabPFN-TS captured those relationships better than Chronos-2.[^berthelier2026covariate] On national electricity demand, Chronos-2 was the best of the [foundation models](../appendices/a-glossary.html#foundation-model) zero-shot, but a simple baseline often beat all of them in Singapore's stable climate; the foundation models' advantage showed mainly in more variable climates.[^cheong2026exogenous] For a single building, the question to test first is therefore whether adding the weather forecast improves on the model run without it.

## What would still need to be added here

- These notes' own benchmark run, rather than a citation of someone else's — see the caveat in the note above. A useful first version is one single-building electricity series, each model run with and without a weather forecast as covariate.
- The comparison above is for one carrier (heat) on two networks. Published numbers for electricity, from single households to whole grids, are collected in [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html). They show zero-shot models doing well on aggregated load and less reliably for a single building.
- A test of whether building metadata helps when passed as a constant series to a model that does not document static covariates.

[^spoek2026tabpfndh]: Spoek, B., Ben Hicham, K. K., Derzsi, K. et al. (2026). [Systematic evaluation of TabPFN-TS and Chronos-2 for zero-shot heat load forecasting in district heating networks](https://arxiv.org/abs/2608.20024). arXiv:2608.20024, version 2 (6 October 2026).
[^ansari2025chronos2]: Ansari, A. F., Shchur, O., Küken, J. et al. (2025). [Chronos-2: From univariate to universal forecasting](https://arxiv.org/abs/2510.15821). arXiv:2510.15821.
[^priorlabs2026tabpfntsreadme]: Prior Labs (2026). [tabpfn-time-series: GitHub repository README, covariate model table](https://github.com/PriorLabs/tabpfn-time-series). *GitHub*. Read 20 October 2026.
[^google2026timesfm3]: Google Research (2026). [TimesFM: GitHub repository README (TimesFM 2.5 covariates via XReg; TimesFM 3.0 release)](https://github.com/google-research/timesfm). *GitHub*. Read 20 October 2026. TimesFM 3.0 has no paper; released August 2026.
[^liu2025moirai2]: Liu, C., Aksu, T., Liu, J. et al. (2025). [Moirai 2.0: When less is more for time series forecasting](https://arxiv.org/abs/2511.11698). arXiv:2511.11698.
[^podest2026tirex2]: Podest, P., Pichler, M., Bürger, E. et al. (2026). [TiRex-2: Generalizing TiRex to multivariate data and streaming](https://arxiv.org/abs/2607.01204). arXiv:2607.01204.
[^datadog2026totoreadme]: Datadog (2026). [Toto: GitHub repository README](https://github.com/DataDog/toto). *GitHub*. Read 20 October 2026.
[^berthelier2026covariate]: Berthelier, G., Baranova, M., Pantea, A.-T. et al. (2026). [Investigating simple target-covariate relationships for Chronos-2 and TabPFN-TS](https://arxiv.org/abs/2605.12200). arXiv:2605.12200.
[^cheong2026exogenous]: Cheong, W. S., Jiang, L. L., Ling, J. N. S. (2026). [Assessing electricity demand forecasting with exogenous data in time series foundation models](https://arxiv.org/abs/2602.05390). AI4TS Workshop at AAAI 2026. arXiv:2602.05390.
[^mistral2026timestral]: Mistral AI (2026). [Introducing Timestral](https://mistral.ai/news/timestral/). Blog post, 15 October 2026; [model card](https://huggingface.co/mistralai/Timestral-209M) and [code](https://github.com/mistralai/timestral). Technical report not yet released.

---
[← Previous: Chapter 4 — Directions for FMs in UES](index.html) · [Back to Chapter 4](index.html) · [Next: 4.2 FMs for Whole Building Stocks →](4-2-fms-for-building-stocks.html)
