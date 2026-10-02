---
title: "4.7 Reading the Screen"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 7
status: draft
last_reviewed: 2026-10-03
---

# 4.7 Reading the Screen
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

This page explains each row of the screen in [§4.6](4-6-screening-tasks.html), grouped by verdict. The verdicts are these notes' own reading of the criteria; the evidence for each is in the sections linked.

## The strongest candidates

**T4 (dispatch) is the strongest candidate: it is the only task that passes all five criteria without qualification.** An optimisation solver produces unlimited correct answers, dispatch problems share the same structure from one system to the next, there are many systems to transfer between, dispatch becomes a bottleneck when it runs thousands of times inside a design or scenario loop, and every answer can be checked against energy balance. See [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html) for the problem and [§4.9.1](4-9-1-methods-tier1.html) and [§4.9.2](4-9-2-methods-tier2.html) for the proposed build path.

**T5 (design and sizing) is the highest-value target, but harder.** It contains dispatch as an inner problem, so it is naturally approached *through* T4, and its instances share less structure because each design problem has its own constraints. See [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) and [§4.9.3](4-9-3-methods-tier3.html).

## Pass, with a caveat

**T1 (UBEM demand) passes the task screen but is crowded and representation-limited.** Novelty here cannot rest on being the first to build a fast [surrogate](../appendices/a-glossary.html#surrogate): surrogate modelling of buildings is an established field, and one review alone tabulates 57 studies.[^westermann2019surrogate] Most of that work takes the building's description as given, a fixed list of attributes per building. What is open is the representation question of [§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings): what the model should treat as the building's parts.

**T6 (network simulation) passes, with transfer between networks as the hard part.** Power-flow and district-heating solvers generate ground truth, and the physics is the same in every network, which is what [neural operators](../appendices/a-glossary.html#neural-operator) are built to exploit: they learn a solution operator for a whole family of equations rather than one instance.[^li2020fno] What varies is the topology, so a model has to generalise to networks it has not seen. Graph neural networks are the usual answer; see [§4.9.2](4-9-2-methods-tier2.html) and, for the grid case, [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html).

**T3 (forecasting) splits in two.** Its bottleneck is accuracy rather than speed: forecasting is already fast, and the question is whether a pretrained model forecasts better than one trained on the target series. For **aggregated load** (feeders, networks, regions) the evidence says yes, often [zero-shot](../appendices/a-glossary.html#zero-shot). For **a single building** it is mixed, because buildings differ in ways a load series alone does not show, so zero-shot accuracy is unreliable and [fine-tuning](../appendices/a-glossary.html#fine-tuning) or building attributes are needed. The studies behind both statements are collected in [§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html); the practical route is [§4.1](4-1-off-the-shelf-fms.html).

**T10 (retrofit) is where the task screen and the representation screen disagree most.** On the task screen it does reasonably: the measure library is shared across buildings, the loop over candidate combinations is a real bottleneck, and each candidate's operational and embodied outcome can be computed (see [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html)). On the representation screen it inherits two open problems at once: the building itself has no settled [basic element](../appendices/a-glossary.html#basic-element) ([G8](../chapter-6-outlook/6-1-open-gaps.html#g8)), and the plan is a [decision space](../appendices/a-glossary.html#decision-space) rather than a state ([G9](../chapter-6-outlook/6-1-open-gaps.html#g9)). The near-term route is therefore through T1 — a fast demand surrogate evaluated inside a conventional search over measures — rather than a model that proposes the plan directly.

## Moderate

**T7 (control) is moderate.** A simulator can generate training experience, and control is time-critical, so there is a real bottleneck. But a review of reinforcement learning for building control found it still largely at the research stage, with 11% of studies tested in real buildings. It named poor generalisation between buildings as one of three main barriers, alongside slow, data-hungry training and robustness.[^wang2020rlcontrol] Those barriers are why S2 and S5 are only partly met: controllers transfer poorly, and a good result in simulation is not a check of real performance.

## Fail the screen

**T2 (resource assessment) and T9 (impact assessment) fail on the bottleneck.** Both are fast already. Resource assessment is a geometric and radiative calculation, and impact assessment is mostly the output of other tasks multiplied by cost and emission factors ([§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)). A learned model would replace a method that is not the slow step.

**T8 (scenario/pathway) fails the screen for foundation-model treatment**, and this is worth stating plainly because it is where much of the intellectual interest in the domain sits. There is no ground truth (scenarios describe futures that have not occurred), instances are heterogeneous, and success is not objectively checkable. **A scenario is defensible, not correct.** The productive research problem in T8 is not a [foundation model](../appendices/a-glossary.html#foundation-model) — it is *representation*: making the assumptions inside scenarios explicit, comparable and machine-processable (see [gap G6](../chapter-6-outlook/6-1-open-gaps.html#g6)). That is a different project with a different method, and the two are easily conflated.

**T11 (behaviour and adoption) fails S1 for the same reason T8 fails it, and it is worth separating the two.** There is no simulator of people: an agent-based adoption model is itself a calibrated hypothesis, validated against the one history that actually happened, so it cannot manufacture ground truth the way a physics simulator does. The distributional outcomes these models feed are normative as well as empirical — they depend on which equity principle is applied ([§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html)). What the screen does *not* rule out is using an existing language model as a component — to structure behavioural assumptions or stand in for respondents — provided its output is checked; that is the direction in [§4.3](4-3-llm-agents-for-simulation.html), and its open problem is validity, not scale.

[^westermann2019surrogate]: Westermann, P. and Evins, R. (2019). [Surrogate modelling for sustainable building design – A review](https://doi.org/10.1016/j.enbuild.2019.05.057). *Energy and Buildings*, 198, 170–186.
[^li2020fno]: Li, Z., Kovachki, N., Azizzadenesheli, K. et al. (2021). [Fourier neural operator for parametric partial differential equations](https://arxiv.org/abs/2010.08895). ICLR 2021. arXiv:2010.08895.
[^wang2020rlcontrol]: Wang, Z. and Hong, T. (2020). [Reinforcement learning for building controls: The opportunities and challenges](https://doi.org/10.1016/j.apenergy.2020.115036). *Applied Energy*, 269, 115036.

---
[← Previous: 4.6 Screening the Tasks](4-6-screening-tasks.html) · [Next: 4.8 Candidate Sub-Fields for a New FM →](4-8-candidate-subfields.html)
