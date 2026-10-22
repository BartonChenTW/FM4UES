---
title: "6.1 Open Gaps"
parent: Chapter 6 — Outlook
nav_order: 1
status: draft
last_reviewed: 2026-09-17
redirect_from: /10-open-gaps.html
---

# 6.1 Open Gaps
{: .no_toc }

{% include page-status.html %}

Ordered by how defensible they are as research contributions.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

### G1 — Multi-carrier temporal tokenisation {#g1}

How to represent carriers whose characteristic times span minutes to seasons in one architecture without aliasing or loss of physical structure. Direct analogue of a documented unsolved problem in Earth-system coupling; no energy-domain treatment exists. Addressed directly by the temporal hierarchy proposed in [§5.3.5](../chapter-5-case-study/5-3-concrete-representation.html#535-temporal-hierarchy), though not yet validated at scale.

### G2 — Cross-configuration transfer for multi-energy operation {#g2}

Existing [surrogates](../appendices/a-glossary.html#surrogate) are bespoke; no work tailors the ML procedure to multi-energy properties, and small-data regimes dominate. Power systems has made this move ([§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html)); multi-carrier urban systems have not.

### G3 — Constrained state variables over long horizons {#g3}

Storage state of charge as a slow, bounded, path-dependent variable. Not handled by any general time-series foundation model. See [§4.7.1(a)](../chapter-4-directions/4-7-1-methods-tier1.html#where-the-genuine-research-contribution-sits).

### G4 — Benchmarks {#g4}

None exist for urban multi-carrier operation or design. This is the cheapest high-value artefact available and the one most likely to outlive its author. See [Phase 0](../chapter-5-case-study/5-1-roadmap.html#phase-0-year-01--representation-and-the-data-engine) and the downstream benchmark suite in [§5.4](../chapter-5-case-study/5-4-data-modules-and-tasks.html#modules-and-tasks).

The building-scale precedent already exists: time-series foundation models have been benchmarked on public IoT and building-energy datasets, with the heterogeneity of that data and the physical constraints of buildings identified as the persistent difficulties.[^lin2024tsfmbuilding] **What that work demonstrates is also what it bounds** — it evaluates single-modality sequence models on metered building data, so a generic time-series benchmark can establish that an FM forecasts a building well without saying anything about whether it respects a carrier-conversion constraint, a storage balance, or a network topology. A UES benchmark therefore cannot be assembled by pointing existing FM benchmarks at energy data; it has to score the things [§2.8](../chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.html) lists that generic benchmarks do not — physical consistency and multi-carrier transfer in particular.

### G5 — Feasibility guarantees for multi-carrier design surrogates {#g5}

Established for power flow; open for multi-carrier hubs with discrete decisions. See [§4.7.3](../chapter-4-directions/4-7-3-methods-tier3.html).

### G6 — Assumption representation {#g6}

Not a foundation-model problem (see [§4.6](../chapter-4-directions/4-6-reading-the-screen.html)) but the binding constraint on any corpus built from *published studies* rather than simulator output: two models with identical structure and data give different answers because of choices documented nowhere. A corpus without this layer trains on a confounded signal.

### G7 — Verification of agent-built models {#g7}

As natural-language model setup commoditises, the open problem shifts from generation to verification — whether the assumptions an agent silently chose were defensible. Work on AI agents has moved toward measuring reliability rather than single successes.[^rabanser2026agentreliability] In the building-simulation studies found so far, agents that work through validated tools handle complex model changes that agents working alone fail, and a large share of models that run still give wrong results. [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html) collects that evidence and proposes a nine-point verification checklist.

### G8 — The basic element for buildings, and the zoning ambiguity underneath it {#g8}

No building decomposition satisfies the four requirements of [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion). The most principled option — the building as a network of connected parts — is blocked because thermal zoning is a modelling convention rather than a property of the building. That community's own systematic review reaches the same conclusion from the other direction, finding competing definitions of a zone and naming a well-documented zoning method as outstanding research.[^shin2019zoning] Resolving this is a building simulation problem before it is a machine learning one, which makes it unusually well suited to that community and unusually unlikely to be solved by the ML community first. Defensible as a research contribution on its own.

### G9 — Representing a decision space alongside a state space {#g9}

Every existing energy foundation model represents what a system *is* or *does*. None represents what could be *done to it* — the discrete, combinatorial, constraint-bound space of possible interventions. This is required for any FM targeting retrofit, investment or design support (Tier 3, [§4.7.3](../chapter-4-directions/4-7-3-methods-tier3.html)), has no counterpart in the grid literature to borrow from, and is the least developed question in these notes. See also [§4.4 Generative Design](../chapter-4-directions/4-4-generative-design.html), and [§3.5](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html) for the domain side: how [retrofit measures](../appendices/a-glossary.html#retrofit-measure) are chosen today and how embodied carbon enters the trade-off.

### G10 — Learned flexibility: predicting how a system responds to signals it has not seen {#g10}

[Flexibility](../appendices/a-glossary.html#flexibility) assessment (T12 in [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)) asks how much an EV fleet, a data centre or a building can shift or shed when a price or the grid asks it to. Today this is measured and optimised case by case ([§3.7](../chapter-3-sim-opt/3-7-flexible-loads.html)), and one study found far more flexibility available with perfect foresight of a data centre's job queue than without it.[^ji2026gpuflexibility] No learned model of flexibility for either load was found (dated search in §3.7). The obstacle is counterfactual: forecasters do well when an intervention repeats one they have seen and much worse when it is new.[^ashok2026whatifbench] The contribution would be a model of flexible-load response, trained on simulators that pair loads with grids and evaluated on interventions held out from training. Ranked by defensibility, it sits between G4 and G5: simulators that pair flexible loads with grids already exist to train on, and the shortfall to beat is measured, but no benchmark of flexible-load response exists yet. It keeps the label G10, added in v3.1, so that the labels G5–G9 used across these notes do not change.

### G11 — Privacy audit of energy foundation models {#g11}

No published study tests whether a pretrained or fine-tuned energy foundation model memorises or leaks the households and buildings it was trained on. The attacks exist and work on smaller models trained on meter data: [membership inference](../appendices/a-glossary.html#membership-inference) against deep load forecasters,[^johansson2025tsmia] property inference from query access alone,[^aly2026propertyinference] reconstruction of training data in federated load forecasting,[^meijer2025tsinverse] and membership inference against models fine-tuned on meter data from public pretrained weights.[^taleb2026lbrm] EU guidance makes such testing the evidence that a model trained on personal data can be treated as anonymous.[^edpb2024aimodels] The contribution would be a structured privacy audit of an energy foundation model fine-tuned on household meter data, using openly licensed data such as Low Carbon London so that the audit itself can be shared ([§4.8.1](../chapter-4-directions/4-8-building-it.html#data-that-cannot-leave-its-owner)). Ranked by defensibility, it sits with G4 and G10, ahead of G5: the attacks, the open data and the legal test all exist, so the work is to apply them. It is numbered G11, added in v3.3, so that the existing labels do not change.

[^lin2024tsfmbuilding]: Lin, X., Prabowo, A., Razzak, I. et al. (2024). [Exploring capabilities of time series foundation models in building analytics](https://arxiv.org/abs/2411.08888). arXiv:2411.08888.
[^shin2019zoning]: Shin, M., Haberl, J. S. (2019). [Thermal zoning for building HVAC design and energy simulation: A literature review](https://doi.org/10.1016/j.enbuild.2019.109429). *Energy and Buildings*, 203, 109429.
[^ji2026gpuflexibility]: Ji, Y., Crozier, C., Liska, M. (2026). [Quantifying and Attributing Power Flexibility from GPU-Heavy Data Centers](https://arxiv.org/abs/2603.27831). arXiv:2603.27831.
[^ashok2026whatifbench]: Ashok, A., Parmar, M., Goyal, P. et al. (2026). [WhatIf-Bench: Benchmarking Intervention-Aware Time Series Forecasting](https://arxiv.org/abs/2610.26582). arXiv:2610.26582.
[^rabanser2026agentreliability]: Rabanser, S., Kapoor, S., Kirgis, P. et al. (2026). [Towards a science of AI agent reliability](https://arxiv.org/abs/2602.16666). arXiv:2602.16666. Accepted at ICML 2026.
[^johansson2025tsmia]: Johansson, N., Olsson, T., Nilsson, D. et al. (2025). [Privacy risks in time series forecasting: User- and record-level membership inference](https://arxiv.org/abs/2509.04169). arXiv:2509.04169.
[^aly2026propertyinference]: Aly, H., Al-Ali, A., Al-Ali, A. et al. (2026). [A blackbox access to load forecasting models is all you need to breach privacy](https://doi.org/10.1145/3856299). *ACM Transactions on Knowledge Discovery from Data*, 3856299. Published online 8 October 2026; volume and issue not yet assigned.
[^meijer2025tsinverse]: Meijer, C., Huang, J., Sharma, S. et al. (2025). [TS-Inverse: A gradient inversion attack tailored for federated time series forecasting models](https://doi.org/10.1109/SaTML64287.2025.00014). *2025 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)*, 110–124. arXiv:2503.20952.
[^taleb2026lbrm]: Taleb, F., Gazeau, I., Laurent, M. (2026). [Uncovering memorization in timeseries imputation models: LBRM membership inference and its link to attribute leakage](https://arxiv.org/abs/2603.24213). arXiv:2603.24213.
[^edpb2024aimodels]: European Data Protection Board (2024). [Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models](https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf). *EDPB opinion*. Adopted 17 December 2024.

---
[← Previous: Chapter 6 — Outlook](index.html) · [Back to Chapter 6](index.html) · [Next: 6.2 How to Contribute →](6-2-how-to-contribute.html)
