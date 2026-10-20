---
title: "3.7 Flexible Loads: EV Charging and Data Centres"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 7
status: draft
last_reviewed: 2026-10-20
---

# 3.7 Flexible Loads: EV Charging and Data Centres
{: .no_toc }

{% include page-status.html %}

Two fast-growing loads that can move in time, move between sites, or shed demand, and what learned models do and do not yet offer for them.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## What flexibility means here

A load is **flexible** when it can change its electricity use in response to a signal, such as a price or a request from the grid operator, without failing the service it exists for. There are three main ways:

- **Shift in time:** run the same work or charge the same energy later or earlier.
- **Shift in space:** move the work to another site, which only some loads can do.
- **Curtail:** reduce demand for a while and accept a cost in lost service.

Electric-vehicle charging and data centres are the two loads where this has grown fastest. To the energy system they are inputs to dispatch and design ([§3.3](3-3-energy-hub-formalism.html)): loads whose size and timing can be chosen within limits. How much a given load can move, when and at what cost is a task of its own, **T12 [flexibility](../appendices/a-glossary.html#flexibility) assessment** in [§3.1](3-1-taxonomy-of-tasks.html).

What flexibility is worth depends on the grid it serves. A capacity-expansion study of data-centre load found the value spatial in the US PJM market, where shifting work between zones cut system cost by 6% in 2028 and 19% in 2038, and temporal in Korea, where shifting load into midday solar hours made extra solar worth building. In both, realistic limits on curtailment events reduced its value.[^khanal2026shiftcurtail]

## Data centres

Research on data-centre flexibility has grown very quickly: a dated search (below) found 117 papers on data-centre flexibility or [demand response](../appendices/a-glossary.html#demand-response) for the grid, almost all from 2026. Most of it is measurement, optimisation and control rather than learned models.

**How much they can move, measured.**
- A deployment on a 130 kW GPU cluster showed rapid load reduction, sustained curtailment and carbon-aware operation while keeping service levels for priority jobs, and moved load between geographically separate clusters.[^williams2026powerflexible]
- Across 131 large-language-model training runs, a study measured how training throughput falls as GPU power is capped, and defined a Power Flexibility Index to price that trade-off.[^colangelo2026powerelasticity]
- A scheduling study found that flexibility has a price ladder. Shifting cooling reliably reduced demand for short periods at about \$30/MWh, and moving backfilled jobs cost \$30–300/MWh. Reordering or delaying jobs started at \$600/MWh, and rose well above \$3,000/MWh. Much more flexibility was available with perfect foresight of the job queue than without it.[^ji2026gpuflexibility]
- A proof-of-concept used flexible language-model inference inside a 150 MW data centre to partly offset the power ramps of AI training, which grid operators such as Alberta's have flagged as a concern.[^liang2026inferenceflex]

**Grid integration.** A review covers what makes data centres unlike other commercial loads: high rack densities, converter-based connections, thermally coupled cooling, uninterruptible power supplies, programmable workloads and on-site generation and storage, with particular attention to effects on distribution feeders.[^dhakal2026dcreview]

**Learned models and tools.**
- Load forecasting: an ensemble that re-weights two machine-learning models as workloads change regime improved short-term forecasts of AI data-centre load on the MIT Supercloud dataset.[^wang2026dcloadensemble]
- Carbon intensity: CarbonX uses general time-series foundation models [zero-shot](../appendices/a-glossary.html#zero-shot) to forecast the carbon intensity that carbon-aware scheduling responds to, with a MAPE of 15.8% across 214 grids.[^maji2026carbonx]
- Simulation: OpenG2G couples a data-centre backend, driven by real measurements of production AI services, with high-fidelity grid simulators, so that classic, optimisation-based and learning-based controllers can be compared on the same scenarios.[^chung2026openg2g]

## EV charging

**Forecasting.** Charging demand is forecast at every level from single charge points to national totals.
- A study of Scottish public charging forecasts the whole hierarchy with valid prediction intervals at every level, while stations are added and removed over time.[^principato2026evhierarchy]
- EV-STLLM adapts a large language model to forecast charging demand and station occupancy across space and time.[^fan2026evstllm]
- A general time-series foundation model, [Chronos-2](../appendices/d-model-index.html#chronos-2), used zero-shot across ten transport datasets including EV charging stations, matched or beat specialised deep-learning models on most of them, especially at longer horizons.[^yanespulido2026tsfmtransport] As for building load ([§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html)), forecasting the load itself is the part that general models already handle.

**Control.** Coordinating many chargers is mainly reinforcement-learning territory.
- HetGPS coordinates 200–3,218 EVs on distribution networks with a graph-based multi-agent policy and a physics-based safety filter. The filter cut voltage violations from 3.9–7.7% of bus-steps to 0.5–3.4%, while 99–100% of vehicles were charged by departure.[^wang2026hetgps]
- Another framework uses a language model inside multi-agent reinforcement learning to choose features and weigh the competing goals of the grid, the stations and the drivers.[^zhang2026llmmarlev]

## What learned models offer so far

These notes read the literature as follows:
- **Forecasting the load is close to solved where it is aggregated.** General time-series models work zero-shot for charging stations, and forecasting tools for data-centre load and carbon intensity exist.
- **Control uses task-specific learning,** usually reinforcement learning with a physics-based safety layer, trained per system rather than pretrained across many.
- **Flexibility itself is measured and optimised, not learned.** No study found here learns how much a fleet or a data centre can move in response to a new signal. That is a counterfactual question: what would the load do under an intervention it has not seen? Current forecasters do well when an intervention repeats one they have seen, and much worse when it is new.[^ashok2026whatifbench] This is logged as [gap G10](../chapter-6-outlook/6-1-open-gaps.html#g10), and the task is screened in [§4.5](../chapter-4-directions/4-5-screening-fields.html#screening-the-tasks).

{: .note }
**Dated search** (arXiv, 20 October 2026). Abstracts with "foundation model" and electric vehicle, EV charging, charging station or charging demand: 4 results, none an EV [foundation model](../appendices/a-glossary.html#foundation-model). "Foundation model" with data centre and energy, power, flexibility or grid: 21 results, none a model of data-centre flexibility. Data centre with flexibility or demand response and grid or power system: 117 results. Learned models of aggregate EV flexibility (EV with flexibility, aggregation and learning, neural or forecasting terms): 0 results.

[^yanespulido2026tsfmtransport]: Yanes-Pulido, J., Rodrigues, F. (2026). [Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis](https://arxiv.org/abs/2602.24238). arXiv:2602.24238.
[^fan2026evstllm]: Fan, H., Chai, Y., Liu, C. et al. (2026). [EV-STLLM: Electric vehicle charging forecasting based on spatio-temporal large language models with multi-frequency and multi-scale information fusion](https://doi.org/10.1016/j.eswa.2026.131620). *Expert Systems with Applications*, 313, 131620. arXiv:2507.09527.
[^zhang2026llmmarlev]: Zhang, Y., Xie, L., Wang, C. et al. (2026). [LLM-Enhanced Multi-Agent Reinforcement Learning for Unified Electric Vehicles-Charging Station-Grid Optimization in Public Charging Systems](https://arxiv.org/abs/2609.13805). arXiv:2609.13805.
[^wang2026hetgps]: Wang, X., Nimalsiri, N., Xia, Y. et al. (2026). [HetGPS: Scalable Graph Multi-Agent Reinforcement Learning with Physics-Anchored Adaptive Safety for EV Charging](https://arxiv.org/abs/2608.00679). arXiv:2608.00679.
[^principato2026evhierarchy]: Principato, G., Amara-Ouali, Y., Goude, Y. et al. (2026). [Probabilistic Forecasting of Electric Vehicle Charging in a Time-varying Hierarchical Infrastructure](https://arxiv.org/abs/2610.13588). arXiv:2610.13588.
[^chung2026openg2g]: Chung, J. W., Liang, Z., Mao, Y. et al. (2026). [OpenG2G: A Simulation Platform for AI Datacenter-Grid Runtime Coordination](https://arxiv.org/abs/2605.05519). arXiv:2605.05519.
[^williams2026powerflexible]: Williams, C., Colangelo, P., Coskun, A. et al. (2026). [Power-Flexible AI Data Centers: A New Paradigm for Grid-Responsive Compute](https://arxiv.org/abs/2606.25098). arXiv:2606.25098.
[^colangelo2026powerelasticity]: Colangelo, P., Dawson, C., Sengupta, S. et al. (2026). [Characterizing Job Power Elasticity for Power-Flexible AI Training](https://arxiv.org/abs/2609.11542). arXiv:2609.11542.
[^ji2026gpuflexibility]: Ji, Y., Crozier, C., Liska, M. (2026). [Quantifying and Attributing Power Flexibility from GPU-Heavy Data Centers](https://arxiv.org/abs/2603.27831). arXiv:2603.27831.
[^liang2026inferenceflex]: Liang, Z. (2026). [Inference as Flexibility: Ramp Management for Transmission-Connected AI Data Centres](https://arxiv.org/abs/2606.21833). arXiv:2606.21833.
[^khanal2026shiftcurtail]: Khanal, S., Roh, G., Yao, B. et al. (2026). [Shift or curtail? How much data-center flexibility is worth depends on the host power grid](https://arxiv.org/abs/2608.19622). arXiv:2608.19622. Submitted to Nature Energy.
[^dhakal2026dcreview]: Dhakal, B., Chamana, M., Gayen, B. et al. (2026). [A Critical Review of Grid Integration Challenges and Flexibility Opportunities for Large-Scale Data Centers](https://arxiv.org/abs/2610.19374). arXiv:2610.19374.
[^wang2026dcloadensemble]: Wang, Z., Zhang, Y., Wang, L. et al. (2026). [Regime-Adaptive Weighted Ensemble Learning for Computing-Driven Dynamic Load Forecasting in AI Data Centers](https://arxiv.org/abs/2604.27207). arXiv:2604.27207.
[^maji2026carbonx]: Maji, D., Yang, K., Shenoy, P. et al. (2026). [CarbonX: An Open-Source Tool for Computational Decarbonization Using Time Series Foundation Models](https://doi.org/10.1145/3744255.3798120). *e-Energy '26*, 569–583. arXiv:2510.01521.
[^ashok2026whatifbench]: Ashok, A., Parmar, M., Goyal, P. et al. (2026). [WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting](https://arxiv.org/abs/2610.26582). arXiv:2610.26582.

---
[← Previous: 3.6 Social Dimensions](3-6-social-dimensions.html) · [Back to Chapter 3](index.html) · [Next: Chapter 4 — Directions for FMs in UES →](../chapter-4-directions/index.html)
