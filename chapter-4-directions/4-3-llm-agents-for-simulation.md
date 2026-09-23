---
title: "4.3 LLMs and Agents That Build or Run Simulation Models"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 3
status: draft
last_reviewed: 2026-09-19
---

# 4.3 LLMs and Agents That Build or Run Simulation Models
{: .no_toc }

{% include page-status.html %}

{: .note }
**Still a stub for the general case**, but with one specific, recent example now discussed below — an LLM agent that supplies one category of simulation input (occupant behaviour) rather than configuring a whole model. It sharpens the verification question below rather than answering it.

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

**What this does and does not do, precisely.** It replaces one specific default (an arbitrary or generic occupancy schedule) with one grounded in a real, checkable dataset — genuine progress on that one assumption. It does **not** address the other categories G7 names: U-values, discretisation, or technology defaults are untouched, and the platform generates a behavioural *input* to a conventional simulator rather than configuring the simulator itself, which keeps it inside the "agent supplies inputs, simulator runs unchanged" framing above rather than the fuller "agent builds the model" case this section is named for.

**And grounding is not the same as verification.** A schedule sampled from ATUS population statistics is defensible in aggregate; whether it is the right schedule for *this* building's actual occupants is exactly G7's question, one level down — swapping an arbitrary default for a population-representative one narrows the range of silently wrong assumptions without eliminating the need to check the one actually in play.

## What would still need to be added here

- A survey of tools addressing the other assumption categories G7 names — thermal envelope defaults, discretisation choices, technology defaults — where no comparable example was found in a search run 19 September 2026.
- A worked example of where an agent-configured model's silent assumptions diverged from a domain expert's, to make the verification problem concrete rather than abstract.
- Discussion of what a verification protocol for agent-built energy models would need to check, connecting to the evaluation protocol in [§4.10](4-10-building-it.html).

[^jung2026buildocc]: Jung, W. (2026). [BuildOcc: A large language model occupant agent platform for building energy research](https://arxiv.org/abs/2609.02729). arXiv:2609.02729.

---
[← Previous: 4.2 FMs for Whole Building Stocks](4-2-fms-for-building-stocks.html) · [Next: 4.4 Generative Design →](4-4-generative-design.html)
