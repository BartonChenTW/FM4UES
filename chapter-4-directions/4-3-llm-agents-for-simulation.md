---
title: "4.3 LLMs and Agents That Build or Run Simulation Models"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 3
status: draft
last_reviewed: 2026-09-29
---

# 4.3 LLMs and Agents That Build or Run Simulation Models
{: .no_toc }

{% include page-status.html %}

{: .note }
**Still a stub for the general case**, but with one specific, recent example now discussed below — an LLM agent that supplies one category of simulation input (occupant behaviour) rather than configuring a whole model — and a short survey of language models standing in for people more broadly (respondents, adopters, policy agents). Both sharpen the verification question below rather than answering it.

1. TOC
{:toc}

---

## The direction

Everything elsewhere in this book treats a foundation model as something that predicts a *quantity* — a trajectory, a cost, a decision. A structurally different direction uses a large language model, generally used agentically (able to call tools, write and run code, inspect results, and iterate), to **produce or operate the simulation itself**: setting up an EnergyPlus or Modelica model from a natural-language description of a building, configuring an energy-hub optimisation from a project brief, or driving an existing tool's API to explore a design space without a human writing the configuration by hand.

This is not the same claim as the rest of this book. Elsewhere, an FM is trained to approximate what a simulator or solver would output. Here, the model is generating the *inputs* to a conventional simulator or solver — assumptions, geometry, topology, parameter choices — which then runs unchanged. The two are complementary: an agent could plausibly configure a model whose dispatch is then evaluated by one of this book's Tier 1–3 approaches ([§4.9](4-9-methods-landing.html)).

## Why this matters, and the problem it creates

As natural-language model setup commoditises, the interesting question shifts from *generation* to *verification*: were the assumptions an agent silently chose — occupancy schedules, default U-values, a discretisation, a technology default — actually defensible for the case at hand? This is exactly **[gap G7](../chapter-6-outlook/6-1-open-gaps.html#g7)**, verification of agent-built models, logged in [Chapter 6](../chapter-6-outlook/index.html). The field's own vocabulary has moved toward verifiable agentic AI and reliability benchmarking, which is the right frame for judging this direction rather than treating it as a solved convenience.

## One category, addressed: occupant-behaviour assumptions

Of the assumption categories listed above, occupant behaviour has a recent, concrete treatment. A platform grounds LLM agents playing simulated building occupants in the American Time Use Survey — each agent is instantiated with a demographic persona and an activity scheduler drawn from real population statistics, rather than a generic default schedule, and maintains a memory stream across timesteps so its choices can depend on its own history.[^jung2026buildocc]

**What this does and does not do, precisely.** It replaces one specific default (an arbitrary or generic occupancy schedule) with one grounded in a real, checkable dataset — genuine progress on that one assumption. It does **not** address the other assumptions listed above: U-values, discretisation, or technology defaults are untouched, and the platform generates a behavioural *input* to a conventional simulator rather than configuring the simulator itself, which keeps it inside the "agent supplies inputs, simulator runs unchanged" framing above rather than the fuller "agent builds the model" case this section is named for.

**And grounding is not the same as verification.** A schedule sampled from ATUS population statistics is defensible in aggregate; whether it is the right schedule for *this* building's actual occupants is the verification question again, one level down — swapping an arbitrary default for a population-representative one narrows the range of silently wrong assumptions without eliminating the need to check the one actually in play.

## Beyond occupancy: simulated respondents, adopters and policy agents

The occupant agent above is one instance of a wider idea from social science: conditioning a language model on a demographic persona so that it answers as a member of that group would. Conditioned on thousands of sociodemographic backstories from real participants in large US surveys, GPT-3 was shown to emulate the response distributions of a wide variety of subgroups — a property its authors call *algorithmic fidelity*, with the resulting synthetic respondents called "silicon samples".[^argyle2023silicon] A later test of the same idea is more cautious. ChatGPT, prompted to adopt personas, reproduced the *average* feeling-thermometer scores of the American National Election Study closely, but with less variation than real respondents, regression coefficients that often differed significantly from the survey's, sensitivity to minor changes in prompt wording, and different results from the same prompt over three months.[^bisbee2024synthetic] Both are US political-opinion surveys, not energy decisions. What carries over is the pattern: **averages can look right while variance, relationships between variables and reproducibility do not** — and variance across households is exactly what the distributional questions in [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html) depend on.

Two recent energy preprints use a language model in a deliberately bounded role rather than as a free-standing decision-maker:

- **Behavioural assumptions inside a calibrated agent-based model.** For PV adoption by Irish dairy farms, LLM-assisted specifications add interpretable behavioural rubrics (conservative, balanced, optimistic) and rule-validated scenario specifications, while keeping the calibrated techno-economic adoption mechanism. Adoption stays bounded and monotonic across behavioural regimes, with up to about 13% more adoption than the corresponding logistic case.[^faiud2026llmabm] The language model augments a validated model rather than replacing it — the authors' own answer to the interpretability, reproducibility and behavioural-validity concerns of replacing adoption models with LLM reasoning.
- **A policy agent scored on energy-poverty metrics.** In a simulated peer-to-peer market on an IEEE 33-bus distribution grid, an open-weight LLM sets price and carbon bounds and targeted subsidies for a community of household personas whose load curves are checked against real smart-meter data. Scored on energy burden, its Gini coefficient and a low-income-high-cost indicator, it lowered the Gini of energy burden from 0.351 to 0.305 and mean burden by 28% while cutting cost. With the LLM only setting bounds and a validate-and-project gate executing them, grid-constraint violations were zero, against 55 under direct LLM control.[^jadhav2026eqgrid] One simulated community on one test grid: the equity figures are a demonstration, not evidence about real households. The architectural point is the one that transfers, and it is the same as the retrofit corollary in [§4.9.3](4-9-3-methods-tier3.html): **let the learned model propose, and let something that knows the constraints decide.**

Both keep the language model where its output can be checked. That is the verification question of [gap G7](../chapter-6-outlook/6-1-open-gaps.html#g7) (verification of agent-built models) applied to social assumptions: a behavioural rubric or a persona is an assumption, and grounding it in a survey narrows the range of silently wrong choices without showing it is right for the population actually in question.

## What would still need to be added here

- A survey of tools addressing the other kinds of assumption listed at the top of this page — thermal envelope defaults, discretisation choices, technology defaults — where no comparable example was found in a search run 19 September 2026.
- A worked example of where an agent-configured model's silent assumptions diverged from a domain expert's, to make the verification problem concrete rather than abstract.
- Discussion of what a verification protocol for agent-built energy models would need to check, connecting to the evaluation protocol in [§4.10](4-10-building-it.html).
- An energy-specific test of silicon samples against a real energy survey (for example heat-pump willingness to pay), reporting variance and subgroup relationships rather than only averages.

[^jung2026buildocc]: Jung, W. (2026). [BuildOcc: A large language model occupant agent platform for building energy research](https://arxiv.org/abs/2609.02729). arXiv:2609.02729.
[^argyle2023silicon]: Argyle, L. P., Busby, E. C., Fulda, N. et al. (2023). [Out of one, many: Using language models to simulate human samples](https://doi.org/10.1017/pan.2023.2). *Political Analysis*, 31(3), 337–351.
[^bisbee2024synthetic]: Bisbee, J., Clinton, J. D., Dorff, C. et al. (2024). [Synthetic replacements for human survey data? The perils of large language models](https://doi.org/10.1017/pan.2024.5). *Political Analysis*, 32(4), 401–416.
[^faiud2026llmabm]: Faiud, I., Khaleghy, H., Schukat, M., Mason, K. (2026). [LLM-assisted behavioural and scenario augmentation for agent-based energy adoption models](https://arxiv.org/abs/2609.04866). arXiv:2609.04866.
[^jadhav2026eqgrid]: Jadhav, K., More, S. (2026). [Grounded, compute-efficient LLM policy agents for energy-poverty equity in physically-constrained peer-to-peer energy markets](https://arxiv.org/abs/2609.01918). arXiv:2609.01918.

---
[← Previous: 4.2 FMs for Whole Building Stocks](4-2-fms-for-building-stocks.html) · [Next: 4.4 Generative Design →](4-4-generative-design.html)
