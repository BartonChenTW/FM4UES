---
title: "3.10 Social Dimensions"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 10
status: draft
last_reviewed: 2026-09-29
---

# 3.10 Social Dimensions: Behaviour, Adoption and Distributional Outcomes
{: .no_toc }

{% include page-status.html %}

Framed for an ML reader: where people enter an energy-system model — as inputs whose behaviour must be modelled, and as the groups across whom outcomes are distributed — what shape that data has, and why it screens differently from the physics.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Two roles for people in a model

Everything else in this chapter models devices, buildings and networks. People appear in two further roles, and they are easy to conflate:

1. **As inputs.** How occupants use a building, and whether owners and households adopt a heat pump, PV, an EV or a retrofit. These are modelled quantities with their own models (T11 in [§3.1](3-1-taxonomy-of-tasks.html)).
2. **As the population across whom outcomes fall.** Who pays, who benefits, who is left in energy poverty. These are outcomes, computed after or alongside the technical model (part of T9).

A review of how energy models represent social aspects found that they enter mainly as exogenous assumptions and in the discussion of outputs, rather than inside the optimisation or simulation itself; all model types represent behaviour and lifestyle in some form, some address public acceptance, none address transformation dynamics — and only agent-based models represent the heterogeneity of actors.[^krumm2022social] That review maps where social aspects currently sit in energy models; it does not propose how to move them inside. It is the baseline this page starts from.

## People as inputs

### Occupant behaviour

The input already named as T1's persistent weakness in [§3.1](3-1-taxonomy-of-tasks.html): an inappropriate occupant-behaviour model can oversize district systems and is one of the main causes of the performance gap.[^doma2023occupant] One LLM-based treatment of occupancy schedules is discussed in [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html).

### Technology adoption and investment decisions

Whether and when households and owners invest decides what the technical models get to optimise. The standard tool is an **agent-based model (ABM)**: a population of simulated decision-makers, each with its own attributes and decision rule, interacting (through neighbours, prices, policy) over time. An empirically initialised ABM of residential PV adoption in Austin, Texas, over 2004–2013, validated against temporal, spatial and demographic criteria, found that modelling only the financial side of the decision predicted the rate and scale of adoption well, but that agent-level attitudes and social interactions were needed to predict its spatial and demographic pattern.[^rai2015abm] One technology, one city, one decade of observed history: it shows which parts of the decision matter for which question, not that the calibrated rules carry over elsewhere.

The same structure applies to buildings. AgentHomeID represents owner-occupiers, private landlords and institutional owners separately, with willingness-to-pay parameters estimated from empirical decision-maker studies, on both archetypes and GIS-derived real buildings. For Germany to 2045, it found subsidy allocation and investment diverging sharply across owner types and income quartiles, with the lowest quartiles persistently under-investing; at regional scale, bottom-up heat-pump uptake was spatially concentrated and differed from aggregated top-down projections in both magnitude and location.[^ganal2026agenthomeid] It is a preprint, and its willingness-to-pay parameters come from German decision-maker studies. Its relevance here is that it is the stock-level version of [§3.9](3-9-retrofit-and-whole-life-carbon.html)'s retrofit question: *which owners will actually adopt the measures* — and the answer shapes the grid loads ([T6](3-1-taxonomy-of-tasks.html)) that follow.

**The mathematical object** is a stochastic simulation of many interacting decision rules, calibrated to surveys and observed uptake and run over many random seeds and scenarios. It sits inside T8: an adoption trajectory is one of the assumptions a scenario rests on.

## People as the population outcomes fall on

### Energy poverty

Energy poverty is framed in the social-science literature as the inability to attain a socially and materially necessitated level of domestic energy services, tied to how the socio-technical pathways that meet household energy needs actually operate — a framing that covers fuel poverty in richer countries and energy poverty in poorer ones within one condition.[^bouzarovski2015energypoverty] That is a conceptual framework, not a metric; quantitative work uses indicators such as energy burden (share of income spent on energy) and its inequality across households (see the example in [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html)).

### Energy justice

Energy justice organises the question around three tenets: **distributional** (who bears costs and receives benefits), **recognition** (which groups are seen and represented) and **procedural** (who takes part in decisions).[^jenkins2016energyjustice] Of the three, only distributional justice maps directly onto something a model computes. A review of energy-system optimisation models, supplemented by a workshop with modellers and social scientists, found that exploring alternatives to the cost-optimal solution — typically by *modelling to generate alternatives* — is receiving growing attention; that equality (equal distribution) is the most common formalised equity principle, with little reflection on the choice and its impact; and that participatory approaches are seen as a promising future direction.[^vagero2023justice]

**The consequence for modelling:** a distributional outcome is not a single number to predict. It depends on which equity principle is applied, which is a normative choice rather than an empirical fact — so two correct models can disagree about whether the same system is just.

### Where outcomes enter the computation

| Where | How | Needs |
| :--- | :--- | :--- |
| After the model (T9) | Disaggregate costs, bills, comfort or emissions by household or group | Outputs resolved per household, plus who lives where |
| As a constraint or objective (T5) | Cap energy burden, or search near-optimal alternatives for fairer ones | An explicit equity principle |
| In the process | Stakeholders choose among alternatives | Models fast enough to explore alternatives interactively |

## Data shapes

- **Surveys** — time-use surveys, household and decision-maker surveys, willingness-to-pay studies. Small, costly, periodic, and the only direct source for attitudes and decision rules. The American Time Use Survey is what grounds the occupant agents in [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html).
- **Registers and census data** — socio-demographics at aggregate or small-area level; the "who lives where" needed to disaggregate outcomes.
- **Observed adoption** — installation records over time. The ground truth for an adoption model, but only one realisation of history, and a lagged one.
- **Meter data as a social signal.** A supervised-learning system applied to 30-minute smart-meter data from 4,232 Irish households estimated characteristics related to socio-economic status, dwelling and appliance stock, with more than 70% accuracy for many characteristics and above 80% for some; the authors discuss the privacy implications.[^beckel2014household] It is one national dataset and a pre-deep-learning method; the point that survives both is that **load data and social attributes are not separable** — a model that learns from one partly learns the other, which is a representation opportunity and a privacy constraint at once.
- **Text** — interviews, public consultations, policy documents, survey free-text. The one social data modality for which foundation models already exist off the shelf.

## Why this matters for foundation models

- **It screens like T8, not like T4.** There is no simulator for people. An ABM is itself a calibrated hypothesis, so it cannot supply unlimited ground truth the way a physics simulator does ([§4.5](../chapter-4-directions/4-5-screening-fields.html)'s S1), and a distributional outcome depends on a normative choice, so "correct" is not checkable (S5). T11's verdict in [§4.6](../chapter-4-directions/4-6-screening-tasks.html) follows from that.
- **Heterogeneity is the signal, not noise.** Both adoption studies above find that *who* decides changes the answer — attitudes and social ties in one, owner type and income in the other. A stock-level model that represents buildings but not their owners and occupants ([§4.2](../chapter-4-directions/4-2-fms-for-building-stocks.html)) cannot answer a distributional question at all.
- **So the realistic role for FMs is as tools inside these models, not as a "social FM".** Language models can structure behavioural assumptions, stand in for survey respondents, or act as policy agents — each with a validity question attached. That direction is surveyed in [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html).
- **The literature is thin.** A dated search (arXiv title/abstract, run 29 September 2026) combining "foundation model" with "energy poverty", "energy justice" or "energy equity" returns no result; combining "large language model" or "LLM" with "energy poverty", "energy justice" or "energy burden" returns one relevant result; combining it with "agent-based", "adoption" and "energy" returns one. Both are discussed in [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html).

[^krumm2022social]: Krumm, A., Süsser, D., Blechinger, P. (2022). [Modelling social aspects of the energy transition: What is the current representation of social factors in energy models?](https://doi.org/10.1016/j.energy.2021.121706) *Energy*, 239, 121706.
[^doma2023occupant]: Doma, A., Ouf, M. (2023). [Modelling occupant behaviour for urban scale simulation: Review of available approaches and tools](https://doi.org/10.1007/s12273-022-0939-3). *Building Simulation*, 16, 169–184.
[^rai2015abm]: Rai, V., Robinson, S. A. (2015). [Agent-based modeling of energy technology adoption: Empirical integration of social, behavioral, economic, and environmental factors](https://doi.org/10.1016/j.envsoft.2015.04.014). *Environmental Modelling & Software*, 70, 163–177.
[^ganal2026agenthomeid]: Ganal, H., Becker, S., Holzhauer, S. et al. (2026). [AgentHomeID — Agent-based modelling of building stock transformation: A multi-scale framework for policy assessment and infrastructure planning](https://arxiv.org/abs/2609.05763). arXiv:2609.05763.
[^bouzarovski2015energypoverty]: Bouzarovski, S., Petrova, S. (2015). [A global perspective on domestic energy deprivation: Overcoming the energy poverty–fuel poverty binary](https://doi.org/10.1016/j.erss.2015.06.007). *Energy Research & Social Science*, 10, 31–40.
[^jenkins2016energyjustice]: Jenkins, K., McCauley, D., Heffron, R., Stephan, H., Rehner, R. (2016). [Energy justice: A conceptual review](https://doi.org/10.1016/j.erss.2015.10.004). *Energy Research & Social Science*, 11, 174–182.
[^vagero2023justice]: Vågerö, O., Zeyringer, M. (2023). [Can we optimise for justice? Reviewing the inclusion of energy justice in energy system optimisation models](https://doi.org/10.1016/j.erss.2022.102913). *Energy Research & Social Science*, 95, 102913.
[^beckel2014household]: Beckel, C., Sadamori, L., Staake, T., Santini, S. (2014). [Revealing household characteristics from smart meter data](https://doi.org/10.1016/j.energy.2014.10.025). *Energy*, 78, 397–410.

---
[← Previous: 3.9 Building Retrofit and Whole-Life Carbon](3-9-retrofit-and-whole-life-carbon.html) · [Back to Chapter 3](index.html) · [Next: Chapter 4 — Directions for FMs in UES →](../chapter-4-directions/index.html)
