---
title: "3.3 The Energy Hub: Formalism, Dispatch, Design"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 3
status: draft
last_reviewed: 2026-09-11
redirect_from:
  - /chapter-3-sim-opt/3-4-dispatch-optimisation.html
  - /chapter-3-sim-opt/3-5-design-sizing-optimisation.html
  - /chapter-3-sim-opt/3-8-where-the-cost-is.html
---

# 3.3 The Multi-Carrier Energy Hub: Formalism, Dispatch and Design
{: .no_toc }

{% include page-status.html %}

The classical, non-learned formalism a multi-carrier hub foundation model would need to either subsume or interoperate with.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## The energy hub

The [energy hub](../appendices/a-glossary.html#energy-hub) concept formalises a node where multiple input energy carriers (electricity, gas, heat, ...) are converted, stored, and dispatched to meet multiple output demands, via a **coupling matrix** that maps inputs to outputs through device efficiencies.[^geidl2007opf][^geidl2007future] Structurally:

```
[P_out] = [C] [P_in]
```

where `C` is the coupling matrix whose entries encode conversion efficiencies (and dispatch factors, where a device can split its input across multiple outputs). This is the formalism underlying most multi-carrier optimisation tools surveyed in [§3.4](3-4-tools-and-standards.html#tool-landscape) (ehubX, hub formulations in Calliope/oemof), and it is the object [§3.3](3-3-energy-hub-formalism.html#dispatch) and [§3.3](3-3-energy-hub-formalism.html#design-and-sizing) treat as an optimisation problem.

An earlier formulation treats the operational and structural optimisation of multi-carrier energy systems jointly — sizing and dispatch as one combined problem rather than sequential ones.[^geidl2006operational]

## Why this formalism, on its own, is not learning-ready

The coupling-matrix formalism is designed for solvers: it specifies constraints and an objective for a mathematical program, and a human or automated process assembles the matrix from a known set of devices and topology. It was never designed to be read or produced by a learned model, and three properties make the gap explicit:

- **It has no notion of a reusable, learnable token.** The matrix is bespoke to one hub's device set and topology; nothing in it is designed to be shared across hubs the way a grid bus is shared across networks.
- **It does not carry carrier quality as a first-class quantity.** Heat at 80°C and heat at 35°C are both just "heat" in the coupling matrix unless the modeller manually adds separate carriers for each temperature band — see [§5.2](../chapter-5-case-study/5-2-representation-problem.html) for why this matters for a learned representation specifically.
- **It has no standard machine-readable interchange format.** Two tools implementing the hub formalism (ehubX, Calliope, oemof) do not share a common schema; each assembles its own coupling matrix internally. [§3.4](3-4-tools-and-standards.html#schemas-and-standards) covers the closest existing attempts (ESDL, CIM) and why neither closes this gap.

This is the classical-formalism counterpart to the representation problem developed at length in [§5.2](../chapter-5-case-study/5-2-representation-problem.html) — the energy hub gives humans and solvers a working formalism; it does not by itself give a learned model a [basic element](../appendices/a-glossary.html#basic-element).

## Operation and dispatch optimisation
{: #dispatch}

### The problem

Given a fixed system configuration — devices, capacities, topology — and boundary conditions (weather, demand, prices, carbon intensity), decide how the system should run: device outputs, storage states, imports/exports, cost, emissions (T4 in [§3.1](3-1-taxonomy-of-tasks.html)). Usually formulated as a linear program (LP) if conversion efficiencies are linear and no on/off decisions are needed, or a mixed-integer linear program ([MILP](../appendices/a-glossary.html#milp)) once unit commitment, minimum part-load, or discrete states enter. In the energy-hub literature the operational model is commonly a MILP that balances demand and supply across carriers by choosing conversion and storage schedules, extended with efficiencies, storage losses and operating limits to make schedules more realistic.[^evins2014energyhub] Overviews of multi-energy system models cover both this operational stage and planning.[^mancarella2014mes]

This is the workhorse task of the domain: it is the inner object called repeatedly by design optimisation (T5, [below](#design-and-sizing)), control (T7), and scenario analysis (T8).

### What kind of ML problem this is

**Multivariate time series with exogenous [covariates](../appendices/a-glossary.html#covariate).** Precisely:

- **Variate dimension** = carriers and devices
- **Sequence dimension** = time
- **Known-future covariates** = weather, demand, prices (known because you are simulating, not forecasting)
- **Static covariates** = installed capacities, efficiencies, storage sizes
- **Target** = operational trajectory

This is a well-studied shape in machine learning — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html) for the [foundation models](../appendices/a-glossary.html#foundation-model) that already target exactly this shape. Framed this way, dispatch as a learning target means choosing and adapting an architecture, not inventing one.

**Why this matters for the amortisation argument.** Because dispatch is called so many times inside outer loops (design search, scenario evaluation, uncertainty quantification), even a modest per-call speedup compounds. This is where the amortisation argument first becomes concrete: paying a one-off training cost to replace a repeatedly-called solver call with a learned approximation. The full arithmetic, and its caveats, is developed in [§3.3](3-3-energy-hub-formalism.html#design-and-sizing) and revisited for the case study in [Chapter 5](../chapter-5-case-study/index.html).

**Flexible loads enter here.** EV fleets and data centres appear in dispatch as loads whose timing and size can be chosen within limits; how much they can move is assessed in [§3.7](3-7-flexible-loads.html) (task T12).

**Where this is developed as a build path.** This page frames dispatch as a learning problem; the concrete methods, architecture choices and build path for single-hub dispatch (Tier 1) and multi-hub multi-carrier dispatch (Tier 2) are given in [§4.7.1](../chapter-4-directions/4-7-1-methods-tier1.html) and [§4.7.2](../chapter-4-directions/4-7-2-methods-tier2.html), once [Chapter 4](../chapter-4-directions/index.html) has established which sub-fields pass the FM screen at all.

## Design and sizing optimisation
{: #design-and-sizing}

### Why this is structurally different from dispatch

The dispatch problem [above](#dispatch) approximates a **simulation**: given inputs, predict outputs. Design and sizing optimisation (T5 in [§3.1](3-1-taxonomy-of-tasks.html)) approximates an **optimisation**: given a problem instance, predict the optimal decision — what to build, and how big.

The canonical structure is bilevel or two-stage. Design studies of multi-energy systems typically formulate it as a MILP, which over a full year at hourly resolution means a very large number of decision variables, binary ones included,[^gabrielli2018seasonal] or as a two-stage stochastic MILP in which sizing comes first and operation is solved under uncertain prices, demands and weather; treating the problem deterministically underestimated system cost in a ten-building Swiss case.[^mavromatidis2018twostage] Multi-level formulations split building design, system sizing and operation, with a genetic algorithm searching the design and a MILP solving operation,[^evins2015multilevel] and decomposition methods become necessary at scale: for networks of 5–100 cogeneration systems the monolithic MILP could not find solutions that the decomposed problem did.[^wakui2021decomposition]

```
outer:  choose capacities x  →  minimise  investment(x) + operating_cost(x)

inner:                              operating_cost(x) = min over dispatch, subject to physics
```

The inner problem — dispatch, from [above](#dispatch) — is called once per candidate design. With evolutionary or many-objective outer search, that is 10³–10⁶ dispatch solves. **This is the single most expensive loop in the domain and the clearest justification for [surrogate](../appendices/a-glossary.html#surrogate) and foundation-model work.**

### The amortisation argument

**This is the argument that justifies foundation-model framing over bespoke surrogates, and it must be made explicitly whenever it is invoked.**

Building a training set costs *N* simulator runs. If *N* = 10,000 and each run takes a minute, that is roughly a week of compute before anything is returned. A surrogate for **one** system used within **one** study rarely repays this — which is precisely why the existing multi-energy surrogate literature is bespoke, small-data and discarded at project end (see [§2.1](../chapter-2-fm-foundations/2-1-what-defines-an-fm.html#surrogates-vs-fms)).

A foundation model changes the arithmetic: the cost is paid once, across a distribution of systems, and amortised over every subsequent study. Formally, it pays back when

```
N_train × t_sim  <  Σ over future studies ( N_evaluations × t_sim )
```


{: .warning }
**Caveat.** The arithmetic only holds if the model actually transfers. Amortisation assumes reuse across systems, and reuse depends on the basic element satisfying [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion). Where it does not, what looks like a foundation model is a collection of memorised cases and the payback never arrives. **Check the representation before running the amortisation calculation.**

### Where this is developed further

This page frames design/sizing as a learning problem and states the economic argument for it. The three families of method (surrogating the inner objective, learning the solution map directly, and hybrid warm-starting), the scaling-behaviour evidence, and the decision-space problem specific to this task are given in [§4.7.3 (Tier 3)](../chapter-4-directions/4-7-3-methods-tier3.html), once [Chapter 4](../chapter-4-directions/index.html) has screened which sub-fields are worth this investment at all.

## Where the computational cost actually is
{: #where-the-cost-is}

Order-of-magnitude brackets, as these notes' own estimates rather than measured values; the spread is the point. The usual way to make the expensive rows tractable is time-series aggregation, solving on a few representative periods instead of the full year. It reduces computation markedly, though averaged periods underestimate real system cost,[^kotzur2018impact] and across many hundreds of model runs, standard aggregation gave a tenfold speedup within 2% cost deviation, and a newer method a hundredfold.[^hoffmann2022pareto]

| Task/configuration | Typical runtime |
| :--- | :--- |
| LP dispatch, single node, typical days | sub-second – seconds |
| LP dispatch, full 8760 h, district | seconds – minute |
| MILP with unit commitment | minutes – hours |
| Dynamic physical (Modelica, DH hydraulics) | tens of minutes – hours |
| UBEM, full stock, annual | minutes – hours |
| Design optimisation with dispatch inner loop | hours – days |
| AC-OPF, large network | seconds, but called thousands of times |

{: .important }
**Single runs are usually affordable. Loops are not.** Design optimisation, uncertainty quantification across weather years, and Monte Carlo risk assessment all call an inner model 10³–10⁶ times. That is where surrogates and foundation models earn their keep — and where the [amortisation argument](3-3-energy-hub-formalism.html#the-amortisation-argument) applies.

[^geidl2007opf]: Geidl, M. and Andersson, G. (2007). [Optimal power flow of multiple energy carriers](https://doi.org/10.1109/TPWRS.2006.888988). *IEEE Transactions on Power Systems*, 22(1), 145–155.
[^geidl2007future]: Geidl, M., Koeppel, G., Favre-Perrod, P. et al. (2007). [Energy hubs for the future](https://doi.org/10.1109/MPAE.2007.264850). *IEEE Power and Energy Magazine*, 5(1), 24–30.
[^geidl2006operational]: Geidl, M. and Andersson, G. (2006). [Operational and structural optimization of multi-carrier energy systems](https://doi.org/10.1002/etep.112). *European Transactions on Electrical Power*, 16(5), 463–477.
[^evins2014energyhub]: Evins, R., Orehounig, K., Dorer, V. et al. (2014). [New formulations of the 'energy hub' model to address operational constraints](https://doi.org/10.1016/j.energy.2014.06.029). *Energy*, 73, 387–398.
[^mancarella2014mes]: Mancarella, P. (2014). [MES (multi-energy systems): An overview of concepts and evaluation models](https://doi.org/10.1016/j.energy.2013.10.041). *Energy*, 65, 1–17.
[^gabrielli2018seasonal]: Gabrielli, P., Gazzani, M., Martelli, E. et al. (2018). [Optimal design of multi-energy systems with seasonal storage](https://doi.org/10.1016/j.apenergy.2017.07.142). *Applied Energy*, 219, 408–424.
[^mavromatidis2018twostage]: Mavromatidis, G., Orehounig, K., Carmeliet, J. (2018). [Design of distributed energy systems under uncertainty: A two-stage stochastic programming approach](https://doi.org/10.1016/j.apenergy.2018.04.019). *Applied Energy*, 222, 932–950.
[^evins2015multilevel]: Evins, R. (2015). [Multi-level optimization of building design, energy system sizing and operation](https://doi.org/10.1016/j.energy.2015.07.007). *Energy*, 90, 1775–1789.
[^wakui2021decomposition]: Wakui, T., Hashiguchi, M., Yokoyama, R. (2021). [Structural design of distributed energy networks by a hierarchical combination of variable- and constraint-based decomposition methods](https://doi.org/10.1016/j.energy.2021.120099). *Energy*, 224, 120099.
[^kotzur2018impact]: Kotzur, L., Markewitz, P., Robinius, M. et al. (2018). [Impact of different time series aggregation methods on optimal energy system design](https://doi.org/10.1016/j.renene.2017.10.017). *Renewable Energy*, 117, 474–487. arXiv:1708.00420.
[^hoffmann2022pareto]: Hoffmann, M., Kotzur, L., Stolten, D. (2022). [The Pareto-optimal temporal aggregation of energy system models](https://doi.org/10.1016/j.apenergy.2022.119029). *Applied Energy*, 315, 119029. arXiv:2111.12072.

---
[← Previous: 3.2 Building Simulation: Loads, Datasets, Benchmarks](3-2-building-simulation-data.html) · [Back to Chapter 3](index.html) · [Next: 3.4 Tools and Data Standards →](3-4-tools-and-standards.html)
