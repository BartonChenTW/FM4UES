---
title: "2.8 Evaluation Criteria for UES Foundation Models"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 8
status: draft
last_reviewed: 2026-09-13
redirect_from:
  - /chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html
---

# 2.8 Evaluation Criteria for UES Foundation Models
{: .no_toc }

{% include page-status.html %}

§2.1 gives the generic three-property test. This section sharpens it into eight questions specific to physical, decision-critical systems — the standard a UES foundation-model proposal should be held to, not just a general-purpose one.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Why the generic definition is not enough here

The three-property definition in [§2.1](2-1-what-defines-an-fm.html) — broad pretraining, transfer, multi-task — is necessary but not sufficient once the model's outputs feed into physical, decision-critical systems. A model can satisfy all three properties and still be useless or dangerous in this domain: it can transfer across buildings while producing physically infeasible predictions, or generalise across tasks while giving no indication of when it is unreliable. The eight dimensions below make that gap concrete.

{: .note }
This framework does not replace the [surrogate](../appendices/a-glossary.html#surrogate)/FM contrast in [§2.1](2-1-what-defines-an-fm.html#surrogates-vs-fms) — it assumes that contrast, then asks a further question: given that something clears the FM bar, how good an FM is it for *this* domain specifically?

## The eight dimensions

**1. Generality.** Does the model support multiple downstream applications — demand forecasting, load disaggregation, anomaly detection, flexibility estimation, retrofit assessment, renewable-generation prediction, dispatch, design — rather than one narrowly defined task? Evaluate at the level of reusable capabilities, not the number of variables a single model happens to output.

**2. Transferability.** Buildings, neighbourhoods, cities, climates, technologies and carriers differ substantially in this domain. Relevant transfer tests: unseen buildings, unseen neighbourhoods or cities, different climates, different archetypes, different technology configurations, different carriers, future time periods. A model that only performs well within its training distribution has not demonstrated this. A building-energy study of time-series foundation models makes the point concretely: [zero-shot](../appendices/a-glossary.html#zero-shot) performance can fall short when the target system differs from the pretraining distribution, while [fine-tuning](../appendices/a-glossary.html#fine-tuning) — including parameter-efficient fine-tuning — recovers much of the gap.[^park2025probforecasting] **Transferability is therefore a property to be measured on held-out systems, not inferred from the fact that a model was pretrained broadly.**

**3. Task generality.** Transfer across *instances* (dimension 2) is not the same as transfer across *task types*. A stronger test is whether the same pretrained representation can be adapted to substantially different downstream tasks — forecasting, classification, simulation, optimisation, control — not just re-run on a new building for the same task it was trained on.

**4. Physical consistency.** Purely data-driven models can produce physically infeasible predictions, and physics-informed machine learning provides established ways to prevent this — as physics-informed inputs, loss functions, architectural design, or ensemble models.[^ma2025piml_bem] (The broader physics-informed ML literature this specific taxonomy sits within is surveyed in [^karniadakis2021piml].) Ask whether a model's outputs satisfy conservation principles, respect technological operating constraints, and remain physically meaningful when transferred to new conditions — not whether the whole model is architecturally a physics-informed neural network. Physics can equally enter through the training data, the loss, the architecture, or coupling with a conventional simulator at inference time. See [§5.4](../chapter-5-case-study/5-4-data-modules-and-tasks.html#physics-loss) for how these notes' own case study handles it.

**5. Data efficiency.** Energy data in this domain is often heterogeneous, incomplete, proprietary, or expensive to collect — see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html). The relevant measurement is how much local data is needed to adapt a pretrained model to a new building, neighbourhood, technology, climate, or task — compared against a task-specific baseline trained from scratch, not assumed from model size alone.

**6. Uncertainty awareness.** Energy-system decisions are made under uncertainty from weather, occupancy, technology performance, prices, and behaviour. A systematic review of uncertainty quantification in ML-based building energy modelling identifies three primary uncertainty sources — building operations, simulation tools, and the ML model itself — and categorises their contributing factors into aleatoric and epistemic uncertainty.[^xu2025uq_bem] A model producing accurate point predictions with no indication of when they are unreliable is insufficient for decision-critical use here; probabilistic predictions, ensembles, Bayesian methods, or calibrated confidence estimates are the usual routes to closing this gap. That this is achievable with [foundation models](../appendices/a-glossary.html#foundation-model) specifically, rather than only with purpose-built probabilistic models, is shown for building energy systems by the same study cited under dimension 2, which treats probabilistic forecasting alongside zero-shot and fine-tuned prediction as part of one evaluation.[^park2025probforecasting]

**7. Computational benefit.** Foundation models for the electric power grid have been proposed partly to replace or accelerate expensive repeated calculations while staying adaptable across applications.[^hamann2024foundation] The equivalent case here: replacing expensive simulation calls with a surrogate, accelerating optimisation, enabling scenario exploration, supporting real-time control. But speed is not a standalone virtue — a faster model whose errors lead to materially different energy-system decisions is not a better model. See the amortisation argument in [§2.1](2-1-what-defines-an-fm.html#surrogates-vs-fms) and [§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html#dispatch) for when the trade actually pays off.

**8. Social and risk properties.** A foundation model is also judged by what it is trained on and what can be done to it, not only by how well it predicts. Four questions apply in this domain:

- *Representativeness.* Whose buildings and households are in the training data? The largest open building-load corpus is "900K simulated buildings representing the U.S. building stock",[^emami2023buildingsbench] and a widely used real-meter benchmark covers 1,636 non-residential buildings from 19 sites in North America and Europe.[^miller2020bdg2] A model trained on such data may transfer poorly to other countries, building types or households, and no peer-reviewed study comparing load-forecast error across socio-demographic groups was found.
- *Privacy.* Meter data reveals how people live: second-level data from three homes revealed "how many people are in the home, sleeping routines, eating routines",[^molinamarkham2010memoirs] and half-hourly data predicts household characteristics.[^beckel2014household] Federated learning combined with differential privacy and secure aggregation kept residential forecasting accurate while preserving privacy,[^delgadofernandez2022federated] and personalised federated adaptation of time-series foundation models across 50 buildings outperformed both global federated and local training.[^nihalchandani2026fedtsfm] No study of memorisation or membership inference in an energy foundation model was found.
- *Explainability.* Operators must be able to justify decisions,[^machlev2022xai] and explanations can be computed for time-series foundation models: for [Chronos-2](../appendices/d-model-index.html#chronos-2) and [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) on transmission-level load, they showed the models using weather and calendar information in line with domain knowledge.[^hertel2026explainable]
- *Robustness to manipulation.* Injecting false temperatures through weather-forecast APIs can move load forecasts "in arbitrary directions",[^chen2019adversarialload] four forecasting models all failed under large data-integrity attacks,[^luo2018integrity] and six time-series foundation models proved steerable by small input perturbations, more so with longer context.[^zhang2025tsfmrobust] Covariate-informed models take weather and other inputs from outside, which is exactly this attack surface.

## Reading these eight together

None of the eight substitutes for another. A model can be general (1) without being transferable (2); transferable across buildings (2) without being transferable across task types (3); physically consistent (4) while providing no uncertainty estimate (6); fast (7) while being wrong in a way that changes a decision; and accurate on all of these while being unrepresentative, opaque or easy to manipulate (8). A UES foundation-model claim should be read as a claim across all eight, not a claim on whichever one the authors chose to report.

{: .warning }
Treat this as a checklist for reading and writing UES-FM claims, not as a validated benchmark suite with agreed metrics per dimension — no such suite exists yet for this domain (see [Chapter 6's open gaps](../chapter-6-outlook/6-1-open-gaps.html), particularly [G4](../chapter-6-outlook/6-1-open-gaps.html#g4)). Building one is exactly the kind of contribution a UES-FM benchmark paper could make.

[^ma2025piml_bem]: Ma, Z., Jiang, G., Hu, Y., Chen, J. (2025). [A review of physics-informed machine learning for building energy modeling](https://doi.org/10.1016/j.apenergy.2024.125169). *Applied Energy*, 381, 125169.
[^karniadakis2021piml]: Karniadakis, G. E., Kevrekidis, I. G., Lu, L. et al. (2021). [Physics-informed machine learning](https://doi.org/10.1038/s42254-021-00314-5). *Nature Reviews Physics*, 3(6), 422–440.
[^xu2025uq_bem]: Xu, X., Hu, Y., Atamturktur, S. et al. (2025). [Systematic review on uncertainty quantification in machine learning-based building energy modeling](https://doi.org/10.1016/j.rser.2025.115817). *Renewable and Sustainable Energy Reviews*, 218, 115817.
[^park2025probforecasting]: Park, Y.-J., Germain, F., Liu, J. et al. (2025). [Probabilistic forecasting for building energy systems using time-series foundation models](https://doi.org/10.1016/j.enbuild.2025.116446). *Energy and Buildings*, 348, 116446.
[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.
[^emami2023buildingsbench]: Emami, P., Sahu, A., Graf, P. (2023). [BuildingsBench: A large-scale dataset of 900K buildings and benchmark for short-term load forecasting](https://arxiv.org/abs/2307.00142). NeurIPS 2023, Datasets and Benchmarks Track. arXiv:2307.00142.
[^miller2020bdg2]: Miller, C., Kathirgamanathan, A., Picchetti, B. et al. (2020). [The Building Data Genome Project 2, energy meter data from the ASHRAE Great Energy Predictor III competition](https://doi.org/10.1038/s41597-020-00712-x). *Scientific Data*, 7(1), 368.
[^molinamarkham2010memoirs]: Molina-Markham, A., Shenoy, P., Fu, K. et al. (2010). [Private memoirs of a smart meter](https://doi.org/10.1145/1878431.1878446). *Proceedings of the 2nd ACM Workshop on Embedded Sensing Systems for Energy-Efficiency in Building (BuildSys '10)*, 61–66.
[^beckel2014household]: Beckel, C., Sadamori, L., Staake, T., Santini, S. (2014). [Revealing household characteristics from smart meter data](https://doi.org/10.1016/j.energy.2014.10.025). *Energy*, 78, 397–410.
[^delgadofernandez2022federated]: Delgado Fernández, J., Potenciano Menci, S., Lee, C. M. et al. (2022). [Privacy-preserving federated learning for residential short-term load forecasting](https://doi.org/10.1016/j.apenergy.2022.119915). *Applied Energy*, 326, 119915. arXiv:2111.09248.
[^nihalchandani2026fedtsfm]: Nihalchandani, P., Srivastava, N., Ojha, V. et al. (2026). [Personalized federated sparse adaptation of time-series foundation models](https://arxiv.org/abs/2608.04695). arXiv:2608.04695.
[^machlev2022xai]: Machlev, R., Heistrene, L., Perl, M. et al. (2022). [Explainable Artificial Intelligence (XAI) techniques for energy and power systems: Review, challenges and opportunities](https://doi.org/10.1016/j.egyai.2022.100169). *Energy and AI*, 9, 100169.
[^hertel2026explainable]: Hertel, M., Nikoltchovska, A., Pütz, S. et al. (2026). [Explainable load forecasting with covariate-informed time series foundation models](https://doi.org/10.1145/3744255.3811724). *Proceedings of the 17th ACM International Conference on Future and Sustainable Energy Systems (e-Energy '26)*, 612–626. arXiv:2604.28149.
[^chen2019adversarialload]: Chen, Y., Tan, Y., Zhang, B. (2019). [Exploiting vulnerabilities of load forecasting through adversarial attacks](https://doi.org/10.1145/3307772.3328314). *Proceedings of the Tenth ACM International Conference on Future Energy Systems (e-Energy '19)*, 1–11.
[^luo2018integrity]: Luo, J., Hong, T., Fang, S.-C. (2018). [Benchmarking robustness of load forecasting models under data integrity attacks](https://doi.org/10.1016/j.ijforecast.2017.08.004). *International Journal of Forecasting*, 34(1), 89–104.
[^zhang2025tsfmrobust]: Zhang, J., Zhang, Z., Zheng, S. et al. (2025). [Are time-series foundation models deployment-ready? A systematic study of adversarial robustness across domains](https://arxiv.org/abs/2505.19397). arXiv:2505.19397.

---
[← Previous: 2.7 Multimodal Models](2-7-multimodal-models.html) · [Back to Chapter 2](index.html) · [Next: Chapter 3 — Simulation and Optimisation in UES →](../chapter-3-sim-opt/index.html)
