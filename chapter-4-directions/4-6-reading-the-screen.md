---
title: "4.6 Reading the Screen: Where to Aim"
parent: "Chapter 4 — Directions for FMs in UES"
nav_order: 6
status: draft
last_reviewed: 2026-09-29
redirect_from:
  - /chapter-4-directions/4-7-reading-the-screen.html
  - /chapter-4-directions/4-8-candidate-subfields.html
---

# 4.6 Reading the Screen: Where to Aim
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

This page explains each row of the screen in [§4.5](4-5-screening-fields.html#screening-the-tasks), grouped by verdict. The verdicts are these notes' own reading of the criteria; the evidence for each is in the sections linked.

## The strongest candidates

**T4 (dispatch) is the strongest candidate: it is the only task that passes all five criteria without qualification.** An optimisation solver produces unlimited correct answers, dispatch problems share the same structure from one system to the next, there are many systems to transfer between, dispatch becomes a bottleneck when it runs thousands of times inside a design or scenario loop, and every answer can be checked against energy balance. See [§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html#dispatch) for the problem and [§4.7.1](4-7-1-methods-tier1.html) and [§4.7.2](4-7-2-methods-tier2.html) for the proposed build path.

**T5 (design and sizing) is the highest-value target, but harder.** It contains dispatch as an inner problem, so it is naturally approached *through* T4, and its instances share less structure because each design problem has its own constraints. See [§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html#design-and-sizing) and [§4.7.3](4-7-3-methods-tier3.html).

## Pass, with a caveat

**T1 (UBEM demand) passes the task screen but is crowded and representation-limited.** Novelty here cannot rest on being the first to build a fast [surrogate](../appendices/a-glossary.html#surrogate): surrogate modelling of buildings is an established field, and one review alone tabulates 57 studies.[^westermann2019surrogate] Most of that work takes the building's description as given, a fixed list of attributes per building. What is open is the representation question of [§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings): what the model should treat as the building's parts.

**T6 (network simulation) passes, with transfer between networks as the hard part.** Power-flow and district-heating solvers generate ground truth, and the physics is the same in every network, which is what [neural operators](../appendices/a-glossary.html#neural-operator) are built to exploit: they learn a solution operator for a whole family of equations rather than one instance.[^li2020fno] What varies is the topology, so a model has to generalise to networks it has not seen. Graph neural networks are the usual answer; see [§4.7.2](4-7-2-methods-tier2.html) and, for the grid case, [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html).

**T3 (forecasting) splits in two.** Its bottleneck is accuracy rather than speed: forecasting is already fast, and the question is whether a pretrained model forecasts better than one trained on the target series. For **aggregated load** (feeders, networks, regions) the evidence says yes, often [zero-shot](../appendices/a-glossary.html#zero-shot). For **a single building** it is mixed, because buildings differ in ways a load series alone does not show, so zero-shot accuracy is unreliable and [fine-tuning](../appendices/a-glossary.html#fine-tuning) or building attributes are needed. The studies behind both statements are collected in [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html); the practical route is [§4.1](4-1-off-the-shelf-fms.html).

**T10 (retrofit) is where the task screen and the representation screen disagree most.** On the task screen it does reasonably: the measure library is shared across buildings, the loop over candidate combinations is a real bottleneck, and each candidate's operational and embodied outcome can be computed (see [§3.5](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html)). On the representation screen it inherits two open problems at once: the building itself has no settled [basic element](../appendices/a-glossary.html#basic-element) ([G8](../chapter-6-outlook/6-1-open-gaps.html#g8)), and the plan is a [decision space](../appendices/a-glossary.html#decision-space) rather than a state ([G9](../chapter-6-outlook/6-1-open-gaps.html#g9)). The near-term route is therefore through T1 — a fast demand surrogate evaluated inside a conventional search over measures — rather than a model that proposes the plan directly.

## Moderate

**T7 (control) is moderate.** A simulator can generate training experience, and control is time-critical, so there is a real bottleneck. But a review of reinforcement learning for building control found it still largely at the research stage, with 11% of studies tested in real buildings. It named poor generalisation between buildings as one of three main barriers, alongside slow, data-hungry training and robustness.[^wang2020rlcontrol] Those barriers are why S2 and S5 are only partly met: controllers transfer poorly, and a good result in simulation is not a check of real performance.

**T12 ([flexibility](../appendices/a-glossary.html#flexibility) assessment) is open, for a reason the forecasting results make clear.** Forecasting a flexible load is close to solved where it is aggregated ([§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html), [§3.7](../chapter-3-sim-opt/3-7-flexible-loads.html)). Flexibility asks something different: how the load would respond to a price or grid signal it has not received before. A benchmark built on simulators of data centres, power grids, traffic and water networks found every forecaster skilful when an intervention repeated one seen before (48–85% skill over a naive baseline), but only −7% to 50% when it was new.[^ashok2026whatifbench] Simulators supply ground truth for the response, so the task is not blocked the way T8 is, but it needs models judged on new interventions. This is [gap G10](../chapter-6-outlook/6-1-open-gaps.html#g10).

## Fail the screen

**T2 (resource assessment) and T9 (impact assessment) fail on the bottleneck.** Both are fast already. Resource assessment is a geometric and radiative calculation, and impact assessment is mostly the output of other tasks multiplied by cost and emission factors ([§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)). A learned model would replace a method that is not the slow step.

**T8 (scenario/pathway) fails the screen for foundation-model treatment**, and this is worth stating plainly because it is where much of the intellectual interest in the domain sits. There is no ground truth (scenarios describe futures that have not occurred), instances are heterogeneous, and success is not objectively checkable. **A scenario is defensible, not correct.** The productive research problem in T8 is not a [foundation model](../appendices/a-glossary.html#foundation-model) — it is *representation*: making the assumptions inside scenarios explicit, comparable and machine-processable (see [gap G6](../chapter-6-outlook/6-1-open-gaps.html#g6)). That is a different project with a different method, and the two are easily conflated.

**T11 (behaviour and adoption) fails S1 for the same reason T8 fails it, and it is worth separating the two.** There is no simulator of people: an agent-based adoption model is itself a calibrated hypothesis, validated against the one history that actually happened, so it cannot manufacture ground truth the way a physics simulator does. The distributional outcomes these models feed are normative as well as empirical — they depend on which equity principle is applied ([§3.6](../chapter-3-sim-opt/3-6-social-dimensions.html)). What the screen does *not* rule out is using an existing language model as a component — to structure behavioural assumptions or stand in for respondents — provided its output is checked; that is the direction in [§4.3](4-3-llm-agents-for-simulation.html), and its open problem is validity, not scale.

## Candidate sub-fields for a new foundation model
{: #candidate-sub-fields}

### Most promising near-term, limited by data licensing

- **Metadata-conditioned load FM** — [cross-attending](../appendices/a-glossary.html#cross-attention) meter time series with building-register attributes and household survey [covariates](../appendices/a-glossary.html#covariate) (on why meter data and household attributes are entangled, see [§3.6](../chapter-3-sim-opt/3-6-social-dimensions.html#data-shapes)). Mature tooling (efficient time-series FMs as baselines — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)), EnergyBench as anchor dataset[^energybench] ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)), and labels paired with simulated buildings as the differentiator, for example from CESAR-P, an open-source dynamic urban building energy simulation tool.[^orehounig2022cesarp] The method is within reach; the limitation is data. Meter readings paired with building and household attributes are usually held under licences that restrict pooling them into a shared training corpus, and measured data rarely comes paired with building attributes in the first place ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)). The closest published precedent is SysCaps, which conditions a building-load surrogate on a plain-text description of each simulated building and was more accurate on held-out buildings than conventional surrogates.[^emami2025syscaps] How models combine the modalities, and the evidence so far, are in [§2.7](../chapter-2-fm-foundations/2-7-multimodal-models.html).

### Novel intersections, in rough order of tractability

1. **Grid-load bridge FM** — cross-attend load-FM embeddings (demand side) with a grid FM's graph representation (topology and physics side; [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html)).[^hamann2024foundation] Building and aggregate loads are literally the boundary condition grid-level OPF solves against. Risk: coupling two different basic elements (a time-series [patch](../appendices/a-glossary.html#patch) and a graph node) is an open architectural question — the general form of which is the interface problem in [§4.9](4-9-ecosystem.html).
2. **Simulation-grounded UBEM FM** — formalise simulator-generated building→load pairs (e.g. from CESAR-P, see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)) as a deliberate pretraining corpus for a conditional generative FM, rather than treating simulator output only as fine-tuning or evaluation data.
3. **Flexibility model** — learn how a flexible load (an EV fleet, a data centre, a building's heat pumps) responds to price and grid signals, trained on simulators such as OpenG2G[^chung2026openg2g] and judged on interventions it has not seen ([§3.7](../chapter-3-sim-opt/3-7-flexible-loads.html), [G10](../chapter-6-outlook/6-1-open-gaps.html#g10)). Ranked third because simulators already supply training data and the shortfall of current forecasters is measured, though no learned flexibility model or shared benchmark of flexible-load response exists yet.
4. **Weather / microclimate-conditioned building energy FM** — fuse a geospatial FM (see [§2.4.3](../chapter-2-fm-foundations/2-4-3-clean-energy-forecasting-fms.html#weather-and-geospatial)) with load or UBEM data, since urban heat islands drive peak cooling load and grid stress simultaneously. No existing paired dataset at FM scale; you would build the corpus, not just the model.
5. **Multi-carrier [energy hub](../appendices/a-glossary.html#energy-hub) FM** — not yet FM-ready in the strict sense. No established basic element, no public data, and discrete decision structure resists replacement by a learned representation. Longer-horizon research question, and the subject of [Chapter 5](../chapter-5-case-study/index.html).
6. **Retrofit and whole-life-carbon FM** — given a building, propose measure combinations scored on cost, operational and [embodied emissions](../appendices/a-glossary.html#embodied-emissions) ([§3.5](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html)). Listed last because it needs both the building representation of [G8](../chapter-6-outlook/6-1-open-gaps.html#g8) and the decision-space representation of [G9](../chapter-6-outlook/6-1-open-gaps.html#g9). Its training data is generable — a stock simulator on one side, [LCA](../appendices/a-glossary.html#lca) impact factors on the other — but the quantity take-off linking the two is archetype-approximated.

[^westermann2019surrogate]: Westermann, P. and Evins, R. (2019). [Surrogate modelling for sustainable building design – A review](https://doi.org/10.1016/j.enbuild.2019.05.057). *Energy and Buildings*, 198, 170–186.
[^li2020fno]: Li, Z., Kovachki, N., Azizzadenesheli, K. et al. (2021). [Fourier neural operator for parametric partial differential equations](https://arxiv.org/abs/2010.08895). ICLR 2021. arXiv:2010.08895.
[^wang2020rlcontrol]: Wang, Z. and Hong, T. (2020). [Reinforcement learning for building controls: The opportunities and challenges](https://doi.org/10.1016/j.apenergy.2020.115036). *Applied Energy*, 269, 115036.
[^emami2025syscaps]: Emami, P., Li, Z., Sinha, S. et al. (2025). [SysCaps: Language interfaces for simulation surrogates of complex systems](https://arxiv.org/abs/2405.19653). *ICLR 2025*. arXiv:2405.19653.
[^ashok2026whatifbench]: Ashok, A., Parmar, M., Goyal, P. et al. (2026). [WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting](https://arxiv.org/abs/2610.26582). arXiv:2610.26582.
[^chung2026openg2g]: Chung, J. W., Liang, Z., Mao, Y. et al. (2026). [OpenG2G: A Simulation Platform for AI Datacenter-Grid Runtime Coordination](https://arxiv.org/abs/2605.05519). arXiv:2605.05519.
[^energybench]: AI-IoT Lab, IISc Bangalore. [EnergyBench](https://huggingface.co/datasets/ai-iot/EnergyBench). Hugging Face dataset, CC-BY-SA-4.0.
[^orehounig2022cesarp]: Orehounig, K., Fierz, L., Allan, J. et al. (2022). [CESAR-P: A dynamic urban building energy simulation tool](https://doi.org/10.21105/joss.04261). *Journal of Open Source Software*, 7(78), 4261.
[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.

---
[← Previous: 4.5 Screening Sub-Fields and Tasks](4-5-screening-fields.html) · [Back to Chapter 4](index.html) · [Next: 4.7 A Proposed Development Path →](4-7-methods-landing.html)
