---
title: "4.1 Using Existing FMs Off the Shelf"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 1
status: draft
last_reviewed: 2026-11-24
---

# 4.1 Using Existing Foundation Models Off the Shelf
{: .no_toc }

{% include page-status.html %}

The most useful direction to a practitioner today, and the one requiring the least new work.
{: .fs-6 .fw-300 }

{: .note }
**Partial.** Two worked examples with reported numbers are below — a published evaluation on district heating and the companion [FM4UES Playground](https://bartonchentw.github.io/FM4UES-playground/)'s reproducible full-year benchmark on Swiss electricity load and German solar PV — together with a table of which inputs each model accepts. What is still missing is extending the companion playground benchmark to a single-building electricity series.

1. TOC
{:toc}

---

## The direction

Before building anything bespoke, the cheapest and most immediately useful thing a UES practitioner can do is evaluate an already-pretrained, general-purpose time-series foundation model **[zero-shot](../appendices/a-glossary.html#zero-shot)** on their own forecasting problem — no training, no [fine-tuning](../appendices/a-glossary.html#fine-tuning), just point the model at the series and read off a forecast. The current generation of these models ([Chronos-2](../appendices/d-model-index.html#chronos-2), [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5), [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0), [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)) is production-grade and free or cheap to run.

This is directly applicable to **load forecasting** — predicting building or district electricity, heat, or cooling demand a few hours to days ahead (T3 in [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)) — where the task screen ([§4.5](4-5-screening-fields.html#screening-the-tasks), [§4.6](4-6-reading-the-screen.html)) finds it close to solved for aggregated load but still open for a single building, on the evidence collected in [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html).

## Why try existing models before building your own

Building and training a model of your own is a large project. Testing an existing one zero-shot needs no training at all, and the result tells you whether the larger project is worth starting. If a pretrained model already forecasts your load well enough, you can stop there. Mainstream forecasting textbooks now introduce pretrained time-series models in this role: the Python edition of *Forecasting: Principles and Practice* devotes a chapter to zero-shot and covariate-conditioned foundation forecasters, illustrating [TimeGPT](../appendices/d-model-index.html#timegpt) and [Moirai](../appendices/d-model-index.html#moirai) on Nord Pool day-ahead electricity prices with day-ahead load and wind forecasts as known-future covariates, evaluated by rolling cross-validation.[^hyndman2026fpppy]

The notes' proposed development path puts this test second in its first tier, predicting how a single [energy hub](../appendices/a-glossary.html#energy-hub) operates ([§4.7.1](4-7-1-methods-tier1.html), "Step 2"), right after setting up simple baselines. For a hub, the test is only a starting point: a hub model must also keep energy in balance and track how full the storage is, which a forecaster does not do. For load forecasting alone, the zero-shot test is often the whole job.

## A worked example: zero-shot heat-load forecasting in district heating

A published evaluation carries out exactly this exercise for one UES carrier. TabPFN-TS and Chronos-2 were run zero-shot on probabilistic heat-load forecasting for district heating networks, against trained machine-learning baselines.[^spoek2026tabpfndh] The figures below are from the published version, which matches the revised preprint (version 2, 6 October 2026); that revision changed some of the numbers and the title. The reported configuration and numbers are specific enough to be useful rather than merely illustrative:

- **Configuration that mattered:** hourly 24-hour-ahead forecasting with a 12-week rolling context and ambient temperature as the [covariate](../appendices/a-glossary.html#covariate) — a parsimonious setup, and longer context windows did *not* improve accuracy. This is a concrete data point for the "how far back is worth feeding in" question the [Tier 1 build path](4-7-1-methods-tier1.html) leaves open. The main benchmark feeds in measured temperature as if it were the forecast, which the authors call assuming perfect weather forecasts; a separate sensitivity analysis uses retrospective weather predictions instead. In operation only the forecast is available, so the main figures are an upper bound on what the setup achieves.
- **Accuracy:** TabPFN-TS reached [CVRMSE](../appendices/a-glossary.html#cv-rmse) 13.07% against Chronos-2's 12.48% on the main dataset, and both models beat every trained baseline in full-year point accuracy. In daily CVRMSE critical-difference comparisons (α = 0.05), TabPFN-TS sits within the critical difference of Chronos-2 on both networks; on Munich the two foundation models form the leading group ahead of all trained AutoGluon baselines, whereas on Flensburg TFT, DeepAR and AutoGluon Ensemble also sit within the critical difference. Chronos-2 achieves the lower full-year continuous ranked probability score (CRPS, which scores the whole predicted distribution rather than a single value) on both networks (60.49 vs 63.66 kW in Munich; 5.62 vs 5.94 MW in Flensburg), with TabPFN-TS close behind. However, approximate probability integral transform (PIT) histograms show both models deviate from uniformity: TabPFN-TS shifts toward higher PIT values in Munich (underpredicting heat load), while Chronos-2 concentrates excess mass in the highest PIT bin on both networks, meaning its upper predictive tail under-covers peak observed loads. The calibration of the predicted distribution matters for the uncertainty-awareness criterion in [§2.8](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) (dimension 6).
- **Transferability actually tested, not assumed:** the configuration was validated on a second, different network — precisely what [§2.8](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) (dimension 2) asks for and what a single-network evaluation cannot show.

One caveat worth carrying forward: TabPFN-TS is pretrained on **synthetic** data rather than real time series, which sidesteps train/test leakage but leaves open whether its learned prior actually captures district-heating dynamics specifically, or transfers on general time-series structure alone — the same synthetic-vs-real question these notes raise for their own corpus in [§4.8.1](4-8-building-it.html#481-data-generation-and-sampling-design).

## Companion playground benchmark: Swiss electricity load and German solar PV

To ground these notes in a reproducible run of our own, Module 1 of the companion [FM4UES Playground](https://bartonchentw.github.io/FM4UES-playground/) evaluates four zero-shot time-series FMs alongside simple persistence and trained `Ridge` and `LightGBM` baselines (with weather and lag features) across all 365 days of 2019 (day-ahead, 24-hour horizon, 2,048-hour context, run on an NVIDIA Quadro RTX 6000) on two contrasting OPSD series paired with Open-Meteo weather: **Swiss national electricity load** and **German solar PV generation**.

| Model | Load MAE (MW) | Load Peak-5% MAE (MW) | Load CRPS (MW) | Solar MAE (MW) | Solar nMAE (%) | Load GPU energy (J) / time (s) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Last week (persistence) | 401.9 | 328.1 | — | 1,694.0 | 35.4 | — |
| Ridge (+ weather & lags) | 303.4 | 262.7 | — | 781.6 | 16.3 | — |
| LightGBM (+ weather & lags) | 268.0 | 179.3 | 183.8 | 681.1 | 14.2 | — |
| TimesFM 2.5 (200M) | 264.1 | 191.8 | 170.6 | 1,318.6 | 27.6 | 749.9 / 3.5 |
| TiRex (35M xLSTM) | 254.6 | 198.4 | 164.0 | 1,091.5 | 22.8 | 462.7 / 3.4 |
| [Chronos-Bolt](../appendices/d-model-index.html#chronos-bolt) (base) | 254.5 | 171.9 | 165.4 | 1,061.6 | 22.2 | 216.3 / 1.5 |
| Chronos-2 (univariate) | 247.3 | 185.7 | 159.6 | 1,085.0 | 22.7 | 356.6 / 2.1 |
| **Chronos-2 + weather** | **242.0** | **170.5** | **157.2** | **545.5** | **11.4** | 1,150.7 / 5.2 |

Three empirical takeaways follow from the run:

1. **Smooth national load favours zero-shot FMs.** All four univariate FMs (`MAE 247.3–264.1 MW`, `3.9–4.2%` MAPE, `1.5–3.5 s` for 365 days on GPU) beat trained `LightGBM` (`268.0 MW`, `4.3%`) without any training on Swiss load.
2. **Weather covariates sharpen peaks more than averages.** Supplying measured Open-Meteo temperature and shortwave radiation to `Chronos-2` trims overall load MAPE modestly (`3.9% → 3.8%`, `242.0 MW`), but cuts **Peak-5% MAE** during the highest-demand hours from `185.7` to `170.5 MW` (an upper bound, since measured rather than forecast weather is used).
3. **Irradiance-driven PV fails without exogenous weather.** On German solar PV, every univariate zero-shot FM (`MAE 1,061.6–1,318.6 MW`, `nMAE 22.2–27.6%`) loses to trained `LightGBM` (`681.1 MW`, `14.2%`) and `Ridge` (`781.6 MW`, `16.3%`) by 26–48%, and unclipped outputs go negative on 26.0% of hours for `TiRex` and 9.4% for `Chronos-Bolt`. Conditioning **`Chronos-2 + weather`** halves solar MAE to `545.5 MW` (`11.4%` nMAE), beating `LightGBM`. On inference cost, `fp16` precision halves `Chronos-Bolt` peak VRAM (`4.92 → 2.59 GB`) and cuts GPU energy from `197.6` to `80.3 J` at identical `254.5 MW` load MAE on the Turing GPU.

## Which covariates each model accepts

The worked example uses one covariate, ambient temperature. A building or district forecast usually has three more candidates: calendar features (hour, weekday, holidays), a weather forecast, and fixed facts about the building such as floor area or heating type. Whether a model can use each one depends on the kind of covariate, and the models differ more here than anywhere else ([§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)). A **past-only** covariate is known up to the present but not over the forecast horizon (measured weather). A **known-future** covariate is available over the horizon (a weather forecast, the calendar). A **static** covariate does not change over time (building metadata).

The table is read from each model's paper or official documentation on 20 October 2026. Documentation for these models changes often, so check it again before relying on a row.

| Model | Past-only | Known-future | Categorical | Static | Several target series together | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Chronos-2](../appendices/d-model-index.html#chronos-2) | Yes | Yes | Yes | Not listed | Yes | Paper[^ansari2025chronos2] |
| [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) | No: dropped | Yes, supplied for the horizon | Yes | No: currently dropped | No: split into separate single-series forecasts | Library documentation;[^priorlabs2026tabpfntsreadme] categorical from the Chronos-2 paper[^ansari2025chronos2] |
| [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5) | No: covariates must cover the context and the horizon | Yes, through an added regression model (XReg) | Yes | Yes | No | Repository documentation[^google2026timesfm3] |
| [TimesFM 3.0](../appendices/d-model-index.html#timesfm-3-0) (August 2026) | Yes | Yes | Not stated | Not stated | Yes | Repository documentation only; no paper (non-commercial weight licence)[^google2026timesfm3] |
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

- Extending the companion [FM4UES Playground](https://bartonchentw.github.io/FM4UES-playground/) benchmark from national load and solar PV to a single-building electricity series, comparing each model with and without a real (rather than measured) weather forecast as covariate.
- The comparison above is for one carrier (heat) on two networks. Published numbers for electricity, from single households to whole grids, are collected in [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html). They show zero-shot models doing well on aggregated load and less reliably for a single building.
- A test of whether building metadata helps when passed as a constant series to a model that does not document static covariates.

[^spoek2026tabpfndh]: Spoek, B., Ben Hicham, K. K., Derzsi, K. et al. (2026). [Systematic evaluation of TabPFN-TS and Chronos-2 for zero-shot heat load forecasting in district heating networks](https://doi.org/10.1016/j.egyai.2026.100942). *Energy and AI*, 26, 100942. arXiv:2608.20024.
[^ansari2025chronos2]: Ansari, A. F., Shchur, O., Küken, J. et al. (2025). [Chronos-2: From univariate to universal forecasting](https://arxiv.org/abs/2510.15821). arXiv:2510.15821.
[^priorlabs2026tabpfntsreadme]: Prior Labs (2026). [tabpfn-time-series: GitHub repository README, covariate model table](https://github.com/PriorLabs/tabpfn-time-series). *GitHub*. Read 20 October 2026.
[^google2026timesfm3]: Google Research (2026). [TimesFM: GitHub repository README (TimesFM 2.5 covariates via XReg; TimesFM 3.0 release)](https://github.com/google-research/timesfm). *GitHub*. Read 22 November 2026. TimesFM 3.0 has no paper; released August 2026 under a non-commercial weight licence (commercial use via Google Cloud / BigQuery ML).
[^liu2025moirai2]: Liu, C., Aksu, T., Liu, J. et al. (2025). [Moirai 2.0: When less is more for time series forecasting](https://arxiv.org/abs/2511.11698). arXiv:2511.11698.
[^podest2026tirex2]: Podest, P., Pichler, M., Bürger, E. et al. (2026). [TiRex-2: Generalizing TiRex to multivariate data and streaming](https://arxiv.org/abs/2607.01204). arXiv:2607.01204.
[^datadog2026totoreadme]: Datadog (2026). [Toto: GitHub repository README](https://github.com/DataDog/toto). *GitHub*. Read 20 October 2026.
[^berthelier2026covariate]: Berthelier, G., Baranova, M., Pantea, A.-T. et al. (2026). [Investigating simple target-covariate relationships for Chronos-2 and TabPFN-TS](https://arxiv.org/abs/2605.12200). arXiv:2605.12200.
[^cheong2026exogenous]: Cheong, W. S., Jiang, L. L., Ling, J. N. S. (2026). [Assessing electricity demand forecasting with exogenous data in time series foundation models](https://arxiv.org/abs/2602.05390). AI4TS Workshop at AAAI 2026. arXiv:2602.05390.
[^mistral2026timestral]: Mistral AI (2026). [Introducing Timestral](https://mistral.ai/news/timestral/). Blog post, 15 October 2026; [model card](https://huggingface.co/mistralai/Timestral-209M) and [code](https://github.com/mistralai/timestral). Technical report not yet released.
[^hyndman2026fpppy]: Hyndman, R. J., Athanasopoulos, G., Garza, A. et al. (2026). [Foundation forecasting models](https://otexts.com/fpppy/15-foundation-models.html). Chapter 15 in *Forecasting: Principles and Practice, the Pythonic Way*. OTexts.

---
[← Previous: Chapter 4 — Directions for FMs in UES](index.html) · [Back to Chapter 4](index.html) · [Next: 4.2 FMs for Whole Building Stocks →](4-2-fms-for-building-stocks.html)
