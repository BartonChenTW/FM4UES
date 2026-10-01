---
title: "2.4.6 Load & Smart-Meter Forecasting FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 6
status: draft
last_reviewed: 2026-10-01
---

# 2.4.6 Load and Smart-Meter Forecasting Foundation Models (Mature for Aggregated Load)
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Demand forecasting is the other side of [§2.4.3](2-4-3-clean-energy-forecasting-fms.html): predicting how much electricity, heat or gas a building, feeder or region will draw in the next hours to days (T3 in [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)). It is a natural first test for time-series foundation models in energy, because smart-meter and utility data are plentiful and every operator already forecasts load.

Two routes run side by side. One pretrains a model on load data itself: measured meter readings, or a simulated building stock. The other takes a general-purpose model from [§2.4.1](2-4-1-time-series-fms.html), pretrained on time series from every domain, and points it at load zero-shot. Both use the same basic element, a fixed-length patch of the meter series (option (d) in [§2.3.2](2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings)). That choice explains most of what follows. A patch is unambiguous, stable in meaning and scale-independent, and meters sum to feeders and feeders to regions, so it composes too. But it describes the *output*, not the building that produced it.

## Models pretrained on load data

**BuildingsBench** pretrained transformers on Buildings-900K, 900,000 *simulated* buildings representing the U.S. stock, and evaluated them on more than 1,900 real residential and commercial buildings from seven open datasets. The main finding was that synthetically pretrained models generalise surprisingly well, zero-shot, to real commercial buildings. Gains from more and more varied pretraining data followed a power law with diminishing returns, and fine-tuning on a target building improved most of them.[^emami2023buildingsbench] It is direct evidence that simulation can stand in for scarce measured data in this domain, the same lesson [§2.4.3](2-4-3-clean-energy-forecasting-fms.html) draws from synthetic PV histories.

**EnergyFM** goes the other way, pretraining on 1.26 billion hourly *measured* smart-meter readings from 76,217 buildings, and is evaluated on forecasting, anomaly detection and appliance classification. That makes it multi-task in the sense of [§2.1](2-1-what-defines-an-fm.html), not only a forecaster.[^arjunan2026energyfm] Its place relative to the grid models is discussed in [§2.4.2](2-4-2-power-grid-fms.html#the-demand-side-has-moved-too--and-shows-the-gap-precisely).

**PowerPM** models electricity time series together with their hierarchy (individual consumers within larger aggregates), using a temporal encoder that takes exogenous variables and a hierarchical encoder for the correlations between levels. It is pretrained self-supervised on a large private dataset, and reported to keep its advantage when transferred to public datasets and other tasks.[^tu2024powerpm] Of the models here, it is the one that builds the composability of meters into the architecture rather than leaving it implicit.

**Beyond electricity**, a contrastively pretrained model for natural gas demand was trained on more than 10,000 industrial, commercial and welfare customers of one utility, with fine-tuning by industry. Its reported gain over the best existing model is modest: 3.68% in MSE.[^zhou2024gasfm]

## General-purpose models tested on load

Most of the literature evaluates the general models of [§2.4.1](2-4-1-time-series-fms.html) (Chronos-2, TimesFM, Moirai, TTM, TimeGPT, TabPFN-TS) on load data. The results look contradictory until they are sorted by how aggregated the load is:

| Level | Study | Finding |
| :--- | :--- | :--- |
| Many energy series, 54 datasets | FETS benchmark[^obermeier2026fets] | Covariate-informed zero-shot models best overall; Chronos-2 median NRMSE 0.472 against 0.611 for task-trained XGBoost. Accuracy **improves with aggregation level** (national load, district heating, grid data) |
| Three grid levels: control area, LV feeders, end consumers | Hertel et al.[^hertel2026gridlevels] | Trained transformers beat established methods by 6.6–10.7%; Chronos-2 zero-shot is competitive on two of the three datasets but **misses special events** in the transmission-operator load |
| 200 low-voltage feeders, net load | Kaas et al.[^kaas2026lvpeak] | Chronos-Bolt, Chronos-2 and TabPFN-TS outperform six baselines, Chronos-2 most clearly; without weather covariates the FMs adapt to the added uncertainty |
| District heating network | Spoek et al.[^spoek2026tabpfndh] | Zero-shot TabPFN-TS and Chronos-2 at CVRMSE of about 13% and 12.5%, with the setup validated on a second network (worked through in [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html)) |
| National markets, Singapore and Australia | Cheong et al.[^cheong2026exogenous] | A simple LSTM baseline often beats every FM in Singapore's stable climate; FMs help mainly where climate is variable, and only some architectures use exogenous features well |
| Households | Meyer et al.[^meyer2025household] | Zero-shot FMs comparable to transformers trained from scratch; with longer input windows, some FMs beat all of them, at much less effort |
| Several load datasets, scarce history | Liao et al.[^liao2025timegpt] | Fine-tuned TimeGPT beats standard benchmarks, especially at short horizons, but not on every dataset; the authors advise checking on a validation set |
| Commercial buildings, synthetic stock | Bose et al.[^bose2024comstock] | Heterogeneity of the training buildings and architecture matter more than parameter count; fine-tuned FMs are competitive, at higher compute cost |
| One net-zero commercial building: occupancy, plug loads, HVAC energy | Park et al.[^park2025buildingtsfm] | Zero-shot accuracy generally suboptimal; full or low-rank (LoRA) fine-tuning fixes it and then beats temporal fusion transformers |
| Building energy management tasks | Mulayim et al.[^mulayim2026bem] | **Limited generalisation**: only marginally better than statistical models on unseen data; adding covariates does not help; results sensitive to the metric |

## Reading the evidence

**Aggregated load is close to solved.** For feeders, district-heating networks and pooled energy series, zero-shot general models are competitive with or better than models trained on the target series.[^obermeier2026fets] [^kaas2026lvpeak] [^spoek2026tabpfndh] National load is the mixed case: trained models still win around special events and in a stable climate.[^hertel2026gridlevels] [^cheong2026exogenous] That pattern is what the patch element predicts. A patch carries nothing about the buildings behind it, and summing many buildings averages out exactly the drivers it cannot see: occupants, equipment, schedules. The aggregate behaves like the weather-driven generation series of [§2.4.3](2-4-3-clean-energy-forecasting-fms.html).

**A single building is not solved.** At the level of one building and its sub-loads, studies more often find zero-shot accuracy no better than simple baselines, or useful only after fine-tuning.[^mulayim2026bem] [^park2025buildingtsfm] Households are the partial exception, where zero-shot models matched transformers trained from scratch.[^meyer2025household] The variation between buildings is the hard part, and it lives in attributes the element leaves out. That fits the finding that the heterogeneity of the training buildings matters more than model size.[^bose2024comstock]

**Covariates are the open technical question.** Weather, calendar and occupancy should help a load forecast. Yet two evaluations find that adding them changes little, or helps only some architectures,[^mulayim2026bem] [^cheong2026exogenous] while a feeder study found weather information important.[^kaas2026lvpeak] Covariate handling is the place where current general models are weakest for this domain, and where a domain model has the most room to add something.

## What this family does not settle

**It forecasts consumption, not the building.** None of the models above can answer a what-if question: what the load becomes after a heat pump is installed or the envelope is insulated. They extrapolate a series rather than represent the object, so they do not replace demand modelling (T1) or retrofit analysis (T10, [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html)). Conditioning a load model on building attributes is the candidate direction in [§4.8](../chapter-4-directions/4-8-candidate-subfields.html), and it is the step that would turn this family into a building model.

**Mostly one carrier.** Nearly all of the work is on electricity. District heat and gas have only one or two studies each here, and none of the models treats several carriers at once, which is the coupling that defines a multi-carrier system ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)).

**The evidence is hard to compare.** Each study picks its own datasets, horizons and metrics, and results shift with the metric.[^mulayim2026bem] FETS is a first attempt at a use-case-differentiated benchmark across energy series.[^obermeier2026fets] Until one is shared, a claim that "FMs beat trained models on load" says as much about the test chosen as about the models.

{: .note }
**Practical consequence.** For aggregated load, a zero-shot general model is a strong default, and running one first is the off-the-shelf path of [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html). For a single building, budget for fine-tuning and test against a simple baseline, which several studies above found hard to beat.

{: .note }
**Dated search** (arXiv, 1 October 2026). Abstracts with "foundation model" and any of "load forecasting", "smart meter" or "demand forecasting": 28 results. Titles with "load forecasting" and abstracts with "foundation model", "zero-shot" or "pretrained": 15. "Foundation model" with heat, cooling, district-heating or gas demand: 6. The table lists the studies in these results that evaluate load forecasting directly; general time-series papers, imputation and appliance-level work were left out.

[^emami2023buildingsbench]: Emami, P., Sahu, A., Graf, P. (2023). [BuildingsBench: A large-scale dataset of 900K buildings and benchmark for short-term load forecasting](https://arxiv.org/abs/2307.00142). NeurIPS 2023, Datasets and Benchmarks Track. arXiv:2307.00142.
[^arjunan2026energyfm]: Arjunan, P., Srivastava, N., Kumar, K. et al. (2026). [EnergyFM: Pretrained models for energy meter data analytics](https://doi.org/10.1145/3744255.3798119). *e-Energy '26*, 556–568.
[^tu2024powerpm]: Tu, S., Zhang, Y., Zhang, J. et al. (2024). [PowerPM: Foundation model for power systems](https://arxiv.org/abs/2408.04057). *Advances in Neural Information Processing Systems 37* (NeurIPS 2024), 115233–115260. arXiv:2408.04057.
[^zhou2024gasfm]: Zhou, X., Ye, J., Zhao, S. et al. (2024). [Towards universal large-scale foundational model for natural gas demand forecasting](https://arxiv.org/abs/2409.15794). arXiv:2409.15794.
[^obermeier2026fets]: Obermeier, M., Pruckner, M., Haselbeck, F., Zeiselmair, A. (2026). [FETS Benchmark: Foundation models enable scalable and generalizable energy time series forecasting](https://doi.org/10.1016/j.egyai.2026.100867). *Energy and AI*, 26, 100867. arXiv:2604.22328.
[^hertel2026gridlevels]: Hertel, M., Pütz, S., Kolar, J. et al. (2026). [A benchmark for electrical load forecasting across grid levels: Time-series transformers outperform established methods](https://arxiv.org/abs/2607.15705). arXiv:2607.15705.
[^kaas2026lvpeak]: Kaas, B., Treutlein, M., Gerber, H. B. et al. (2026). [Probabilistic low-voltage peak load forecasting with time series foundation models evaluated on application-oriented metrics](https://arxiv.org/abs/2607.01966). arXiv:2607.01966.
[^spoek2026tabpfndh]: Spoek, B., Ben Hicham, K. K., Derzsi, K. et al. (2026). [Systematic evaluation of TabPFN-TS for zero-shot probabilistic heat load forecasting in district heating networks](https://arxiv.org/abs/2608.20024). arXiv:2608.20024.
[^cheong2026exogenous]: Cheong, W. S., Jiang, L. L., Ling, J. N. S. (2026). [Assessing electricity demand forecasting with exogenous data in time series foundation models](https://arxiv.org/abs/2602.05390). AI4TS Workshop at AAAI 2026. arXiv:2602.05390.
[^meyer2025household]: Meyer, M., Zapata Gonzalez, D., Kaltenpoth, S., Müller, O. (2025). [Benchmarking time series foundation models for short-term household electricity load forecasting](https://doi.org/10.1109/ACCESS.2025.3648056). *IEEE Access*, 13, 218141–218153. arXiv:2410.09487.
[^liao2025timegpt]: Liao, W., Wang, S., Yang, D. et al. (2025). [TimeGPT in load forecasting: A large time series model perspective](https://doi.org/10.1016/j.apenergy.2024.124973). *Applied Energy*, 379, 124973.
[^bose2024comstock]: Bose, S., Li, Y., Van Sant, A. et al. (2024). [From RNNs to foundation models: An empirical study on commercial building energy consumption](https://arxiv.org/abs/2411.14421). NeurIPS 2024 Workshop on Time Series in the Age of Large Models. arXiv:2411.14421.
[^park2025buildingtsfm]: Park, Y.-J., Germain, F., Liu, J. et al. (2025). [Probabilistic forecasting for building energy systems using time-series foundation models](https://doi.org/10.1016/j.enbuild.2025.116446). *Energy and Buildings*, 348, 116446. arXiv:2506.00630.
[^mulayim2026bem]: Mulayim, O. B., Quan, P., Han, L. et al. (2026). [Can time-series foundation models perform building energy management tasks?](https://doi.org/10.1017/dce.2026.10040) *Data-Centric Engineering*, 7, e9. arXiv:2506.11250.

---
[← Previous: 2.4.5 Geospatial & Weather FMs](2-4-5-geospatial-weather-fms.html) · [Next: 2.5 What Does Not Exist Yet →](2-5-what-does-not-exist-yet.html)
