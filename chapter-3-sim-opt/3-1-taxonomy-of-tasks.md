---
title: "3.1 Taxonomy of Modelling Tasks"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 1
status: draft
last_reviewed: 2026-09-29
---

# 3.1 Taxonomy of Modelling Tasks
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## What an energy-system model computes

[§1.1](../chapter-1-background/1-1-what-is-ues.html) described what an urban energy system *contains* — demands, conversion technologies, storage and networks, coupled across carriers. This chapter is about what a *model* of one computes. At a high level, that is a mapping:

**System description + external conditions → model → system outcomes**

The inputs may include building characteristics, technology parameters, weather, occupancy, energy prices, network characteristics, or technology availability. The outputs may include energy demand, generation, energy flows, temperatures, equipment operation, investment decisions, operating costs, or emissions. Which inputs and which outputs is exactly what distinguishes one task from another — and that is what the taxonomy below organises.

### Simulation and optimisation answer different questions

The mapping above hides a distinction that runs through the whole chapter. **Simulation** asks:

> *Given the system and its conditions, what happens?*

A building simulation takes the envelope, HVAC system, occupancy, weather and control assumptions, and estimates heating and cooling demand or indoor conditions over time.[^crawley2008simulation] At larger scales, simulations represent energy flows through multiple technologies, buildings or networks.

**Optimisation** asks:

> *Given the system, objectives and constraints, what should we do?*

An optimisation model may decide how a heat pump, battery and grid connection should be operated to minimise cost or emissions subject to technical constraints, formalised through decision variables, constraints and an objective function.[^conejo2010decision] A design optimisation instead decides which technologies to install and at what capacity.

The two are closely related but not interchangeable. A simulation *evaluates* a specified system under specified conditions; an optimisation *searches* among possible decisions for one that satisfies the constraints and scores well on the objective. That difference drives different mathematical formulations, different computational costs, and different opportunities for machine learning — which is why T1/T2/T6 and T4/T5/T8 below behave so differently as learning targets.

### Why this framing matters for foundation models

Viewed this way, many energy-system computations are structured mappings from inputs to outputs, which is what makes them candidates for learned approximation at all — replacing an expensive simulation, or amortising a repeatedly-called solver ([§1.5](../chapter-1-background/1-5-why-ues-why-now.html)).

But they are not ordinary black-box prediction problems. They encode conservation laws, engineering constraints, operational limits, discrete decisions, objective functions, and assumptions about uncertain human behaviour. A foundation model here has to interact with that structure rather than merely fit an input–output relation. The recurring question, taken up as a screening test in [§4.6](../chapter-4-directions/4-6-screening-tasks.html), is **which parts of energy-system modelling can benefit from foundation-model approaches, and what structure must be preserved when they are learned or approximated.**

## The eleven tasks

Each row is a distinct *task* with a distinct mathematical structure — and foundation-model potential differs sharply between them. This table is used again in [§4.6 Screening the Tasks](../chapter-4-directions/4-6-screening-tasks.html).

| # | Task | Question answered | Mathematical object | Typical runtime |
| :--- | :--- | :--- | :--- | :--- |
| T1 | **Demand modelling (UBEM)** | How much energy does this building stock need, when? | DAE / RC networks / statistical regression | minutes–hours (stock) |
| T2 | **Renewable resource assessment** | How much PV/solar/wind is available here? | geometric + radiative computation | seconds–hours |
| T3 | **Forecasting** | What will demand/generation be in the next hours–days? | time-series regression | milliseconds–seconds |
| T4 | **Dispatch / operation optimisation** | Given a fixed system, how should it run? | LP / MILP | sub-second–hours |
| T5 | **Design / sizing optimisation** | What should we build, and how big? | MILP / MINLP / bilevel | minutes–days |
| T6 | **Network simulation** | Do flows, pressures, temperatures and voltages hold? | nonlinear algebraic / PDE / DAE | seconds–hours |
| T7 | **Control** | What setpoints now, given uncertainty? | MPC / RL | real-time constraint |
| T8 | **Scenario & pathway analysis** | What futures are plausible, under what assumptions? | recursive optimisation + narrative | hours–days |
| T9 | **Impact assessment** | Emissions, cost, equity, comfort outcomes | post-processing / LCA | seconds–hours |
| T10 | **Retrofit analysis & planning** | Which measures should this existing building (or stock) get, and when? | combinatorial, multi-objective search over a discrete measure set, T1 in the loop | minutes–days |
| T11 | **Behaviour & adoption modelling** | How do people use buildings, and who adopts which technology, when? | agent-based simulation / behavioural models, calibrated to surveys and observed uptake | minutes–hours |

## Notes on each task's structure

**T1 — Demand modelling.** Bottom-up physics-based Urban Building Energy Modelling (UBEM) simulates buildings at large scale from geometry, envelope and usage archetypes. Reviews of these tools compare them along required inputs, reported outputs, workflow, applicability and intended users — and note that choosing a tool while balancing complexity, accuracy, usability and computing needs remains a genuine challenge for users.[^ferrando2020ubem] A persistent and important weakness: occupant behaviour. Inappropriate choice of occupant-behaviour model can lead to oversized district energy systems, over-investment and low operational efficiency — one of the main causes of the building "performance gap".[^doma2023occupant]

{: .note }
T1 also carries a representation problem the other tasks do not, because the decomposition of a building into elements is itself a modelling choice rather than a property of the object. See [§2.3 Choosing a Basic Element](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html).

**T4 — Dispatch.** Usually LP if conversion efficiencies are linear and no on/off decisions are needed; MILP once unit commitment, minimum part-load, or discrete states enter. This is the workhorse: it is the inner object of T5, T7 and T8. Treated as an ML problem shape in [§3.4](3-4-dispatch-optimisation.html).

**T5 — Design/sizing.** The literature consolidates around deterministic programming (LP/MILP/MINLP) for transparent, reproducible co-optimisation of capacity investment and operational dispatch, alongside evolutionary and swarm methods for nonconvex, mixed-variable, simulation-driven sizing problems — while flagging the need for rigorous constraint handling and transparent reporting of computational budgets. Hybrid strategies that integrate global search with exact dispatch solvers, surrogate-assisted learning, decomposition and control–co-design are identified as the most promising direction. Treated in [§3.5](3-5-design-sizing-optimisation.html).

**T6 — Networks.** Electrical (AC/DC power flow), thermal (hydraulics + heat transfer, with transport delays), gas (pressure dynamics). These are where genuine PDE/DAE structure lives, and where runtimes explode.

**T9 — Impact assessment.** Mostly post-processing: the flows computed by the other tasks, multiplied by cost and emission factors. For buildings, LCA adds a second axis — the embodied emissions of materials and equipment, which the operational tasks never see. Treated with T10 in [§3.9](3-9-retrofit-and-whole-life-carbon.html). Its equity outcomes — who pays, who benefits, energy poverty — need outputs resolved per household and an explicit equity principle; see [§3.10](3-10-social-dimensions.html).

**T10 — Retrofit.** A decision over which measures to apply to an existing building, evaluated by running T1 on each candidate and scored on cost, operational and embodied emissions (T9). At stock scale it turns into a T8 scenario question. It is the most concrete instance of the decision space in [gap G9](../chapter-6-outlook/6-1-open-gaps.html#g9). Treated in [§3.9](3-9-retrofit-and-whole-life-carbon.html).

**T11 — Behaviour and adoption.** Models of the people in the system rather than the devices: occupant behaviour (an input to T1) and technology-adoption and investment decisions (an input to T8, and at stock level the rate at which T10's measures are actually taken up). Usually agent-based, calibrated to surveys and observed uptake. Unlike every other task here, there is no physics simulator to generate ground truth. Treated in [§3.10](3-10-social-dimensions.html).

[^ferrando2020ubem]: Ferrando, M., Causone, F., Hong, T., Chen, Y. (2020). [Urban building energy modeling (UBEM) tools: A state-of-the-art review of bottom-up physics-based approaches](https://arxiv.org/abs/2103.01761). *Sustainable Cities and Society*, 62, 102408.
[^doma2023occupant]: Doma, A., Ouf, M. (2023). [Modelling occupant behaviour for urban scale simulation: Review of available approaches and tools](https://doi.org/10.1007/s12273-022-0939-3). *Building Simulation*, 16, 169–184.
[^crawley2008simulation]: Crawley, D. B., Hand, J. W., Kummert, M., Griffith, B. T. (2008). [Contrasting the capabilities of building energy performance simulation programs](https://doi.org/10.1016/j.buildenv.2006.10.027). *Building and Environment*, 43(4), 661–673.
[^conejo2010decision]: Conejo, A. J., Carrión, M., Morales, J. M. (2010). [Decision Making Under Uncertainty in Electricity Markets](https://doi.org/10.1007/978-1-4419-7421-1). Springer US. International Series in Operations Research & Management Science, 153.

---
[← Back to Chapter 3](index.html) · [Next: 3.2 Building Energy Simulation →](3-2-building-simulation-data.html)
