---
title: "2.8 Surrogates vs Foundation Models"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 8
status: draft
last_reviewed: 2026-09-24
---

# 2.8 Surrogate Models vs Foundation Models
{: .no_toc }

{% include page-status.html %}

UES readers already know surrogates well. The contrast with a foundation model is the fastest way in, and explains why an FM is more than a bigger surrogate.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## What a surrogate is

A surrogate model is a fast approximation of an expensive model — trained to reproduce the input-output behaviour of a simulator or optimiser without running it. Surrogates are already routine in this domain: a neural network trained to predict an energy hub's cost and other objectives as a function of design variables, standing in for a full engineering simulation inside an outer sizing loop[^perera2019mlsurrogate] (see [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html) and Family 1 in [§4.9.3](../chapter-4-directions/4-9-3-methods-tier3.html)).

## The distinction, precisely

Both a surrogate and a foundation model are approximations, fitted to data rather than derived from first principles. **The difference is entirely in the training distribution and the transfer claim** — not in the mathematics of the model itself:

| | Surrogate | Foundation model |
| :--- | :--- | :--- |
| Trained on | One system (or a narrow family) | A broad distribution of systems |
| Reused across | One study, then discarded | Many future studies, by other users |
| Transfer claim | None required — fits the system it was trained on | Central — must work on unseen instances |
| Task scope | Usually one task | Multiple downstream tasks (see [§2.1](2-1-what-defines-an-fm.html)) |

A surrogate that works beautifully on the system it was trained on, and is thrown away at the end of the project, has made no transfer claim and needs none. **Calling that a foundation model is the single most common and most damaging framing error available in this space** — it invites a scrutiny (does it generalise? is it multi-task?) that a project-scoped surrogate was never designed to survive, and that is the wrong standard to hold it to.

## Why the existing multi-energy surrogate literature is not FM work

The existing surrogate literature for multi-carrier energy hubs and districts is almost entirely bespoke: one surrogate per system, small training data, discarded at project end (see [§4.9.3](../chapter-4-directions/4-9-3-methods-tier3.html)). A 2025 study of surrogates for multi-energy system design reports that no prior work had tailored its machine-learning procedure to the design problem, that most predicted system cost and other objectives rather than the design itself, and sets out explicitly to improve performance on small datasets.[^ledee2025messurrogate] A typical case builds surrogates for one expensive, simulation-based problem — the energy system of a single building complex — and refines them as that one optimisation runs.[^aghaeipour2021interactive] The nearest thing to transfer is adaptation: an energy-system surrogate carried over to scenarios with different solar potential, wind speed and demand by transfer learning, rather than one model applied unchanged.[^perera2019mlsurrogate] This is not a criticism of that literature — bespoke surrogates are often the right tool for a single study — but it means the foundation-model claim for this domain is essentially unmade so far. **The foundation-model contribution, where it exists, is making the same class of model transferable across systems rather than rebuilt for each one** — this is the throughline connecting [Chapter 4](../chapter-4-directions/index.html)'s survey to [Chapter 5](../chapter-5-case-study/index.html)'s specific proposal.

## Moving from a surrogate to a foundation model

The contrast above says what the difference *is*. It does not say what to do about it, and the practical question a modeller arrives with is usually the other one: **I already have a working surrogate — what would it take to make it a foundation model?**

Not every surrogate should become one, and the honest first answer is often "nothing, and don't." What follows is the sequence of things that would have to change, in the order they bite. Each step is a real commitment, and the early ones are cheap while the later ones are not.

**Step 0 — Check the basic element first, because it can veto everything else.** Before any of the steps below, the representation has to survive the four requirements of [§2.3.1](2-3-choosing-a-basic-element.html#231-the-criterion). This is not sequencing pedantry. If the element is not stable in meaning across systems, no amount of extra data or compute produces transfer — the model memorises cases and the payback never arrives. For buildings specifically, [§2.3.2](2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings) reaches a negative result: no candidate element satisfies all four. **A surrogate built on an element that fails the criterion cannot be upgraded into a foundation model by scaling it.** That is the cheapest possible check and it comes first.

**Step 1 — Widen the training distribution from one system to a population of them.** This is the substantive change, and the one the definition turns on. A surrogate is fitted to the system in front of you; a foundation model is fitted to a distribution you expect future systems to be drawn from. The work here is mostly corpus construction, not modelling — which is why [§2.5](2-5-what-does-not-exist-yet.html) treats the missing corpus, rather than a missing architecture, as the binding constraint for this domain. Note what made the mature families of [§2.4](2-4-existing-fms-relevant-to-energy.html) possible: a public corpus someone else had already assembled under one schema.

**Step 2 — Make the transfer claim, and then test it adversarially.** A surrogate needs no held-out *systems*, only held-out points. A foundation model lives or dies on unseen instances, so the evaluation has to change shape: hold out whole systems, whole typologies, whole countries. This is where a promising surrogate most often fails to survive promotion, and it is better to discover that here than after training. [§2.9](2-9-ues-fm-evaluation-criteria.html) sets out what such an evaluation has to demonstrate for a UES model.

**Step 3 — Broaden from one task to several.** Single-task transfer is real and useful, but it is not yet the foundation-model pattern of [§2.1](2-1-what-defines-an-fm.html) — that requires one pretrained representation serving several distinct downstream tasks. A model that transfers across systems but does exactly one thing sits in a genuine middle ground, and is worth naming as such rather than rounding up.

{: .note }
**The middle ground is legitimate and under-named.** Steps 1–3 are separable, and a model that takes only some of them is not a failed foundation model — it is its own useful thing. A *transferable surrogate* (Step 1 and 2, not 3) is already a substantial contribution, and is a more honest label than stretching "foundation model" to cover it. The renewable forecasting models of [§2.4.3](2-4-3-clean-energy-forecasting-fms.html) sit almost exactly here: pretrained across ~126,000 sites and genuinely zero-shot at new ones, but single-carrier and single-task.

**Where the existing literature actually sits.** Large-scale building-stock studies are the closest thing this domain has to Step 1 already being done: they model populations of buildings rather than one, at continental scale. Kleinebrahm et al. analyse grid defection across European single-family homes and conclude that around two million could economically abandon the grid by 2050.[^kleinebrahm2023griddefection] Work at that scale is population-level in exactly the sense Step 1 requires — and it is worth being precise about why reaching that scale is still not, by itself, foundation-model work.

**The distinction is the deliverable, not the scale.** A scenario study answers a question; a foundation model is an artefact someone else can apply to a system the authors never saw. The two are compatible — the same pipeline could produce both — but they are not the same achievement, and scale alone does not convert one into the other. Steps 2 and 3 are what separate them: held-out *systems* rather than held-out points, and a representation that serves more than the one task it was fitted for. **The gap between "modelled a population" and "produced a model of the population" is the whole of the distance this section is about**, and it is why [§4.9.3](../chapter-4-directions/4-9-3-methods-tier3.html)'s survey of existing energy-hub surrogates does not amount to foundation-model work despite the scale some of it reaches.

## The amortisation argument

The economic case for paying the higher upfront cost of foundation-model training rather than a cheaper bespoke surrogate rests on reuse: the cost is paid once, across a distribution of systems, and amortised over every subsequent study, rather than paid once per study. This argument is developed in full, with the break-even arithmetic, in [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) and revisited for the specific case study in [Chapter 5](../chapter-5-case-study/index.html).

{: .warning }
The amortisation arithmetic only holds if the model actually transfers. Where the basic element fails the criterion in [§2.3.1](2-3-choosing-a-basic-element.html#231-the-criterion), what looks like a foundation model is a collection of memorised cases, and the payback never arrives — it is a surrogate with foundation-model marketing. Check the representation before running the amortisation calculation.

[^perera2019mlsurrogate]: Perera, A. T. D., Wickramasinghe, P. U., Nik, V. M. and Scartezzini, J.-L. (2019). [Machine learning methods to assist energy system optimization](https://doi.org/10.1016/j.apenergy.2019.03.202). *Applied Energy*, 243, 191–205. An artificial-neural-network surrogate replaces the engineering model in the Pareto optimisation of an energy system's design (objectives: net present value and grid-integration level); combined with the engineering model, it reaches Pareto solutions about 17 times faster than the engineering model alone. Transfer learning then adapts the surrogate to scenarios with notably different solar potential, wind speed and demand. That is adaptation to new *conditions* — the surrogate is re-fitted, not applied unchanged, and the abstract makes no claim of transfer across system configurations.
[^ledee2025messurrogate]: Lédée, F., Crawford, C. and Evins, R. (2025). [Improved surrogate modeling for multi-energy system design: Model architecture, sampling and scaling choices](https://doi.org/10.1016/j.apenergy.2025.125812). *Applied Energy*, 390, 125812. Shows that a surrogate can directly predict optimal multi-energy system designs once the method is tailored to the problem: objective-oriented sampling, upsampling to balance the data, non-linear rescaling of outputs and a Mixture-of-Experts network, tested across climates, building types and decarbonisation goals. Its review of related work is the source of the landscape statements above. It remains surrogate work in this section's sense: the abstract makes no claim that one trained model transfers to unseen systems.
[^aghaeipour2021interactive]: Aghaei Pour, P., Rodemann, T., Hakanen, J. and Miettinen, K. (2021). [Surrogate assisted interactive multiobjective optimization in energy system design of buildings](https://doi.org/10.1007/s11081-020-09587-8). *Optimization and Engineering*, 23(1), 303–327. Replaces expensive objective functions with surrogate models inside an interactive evolutionary method, updating the surrogates according to a decision maker's preferences, and demonstrates it by finding an optimal energy-system configuration for a heterogeneous business building complex. The surrogates exist to serve that one problem — the bespoke pattern this section describes, and the right tool for a single study.
[^kleinebrahm2023griddefection]: Kleinebrahm, M., Weinand, J. M., Naber, E. et al. (2023). [Two million European single-family homes could abandon the grid by 2050](https://doi.org/10.1016/j.joule.2023.09.012). *Joule*, 7(11), 2485–2510.

---
[← Previous: 2.7 Architectures](2-7-architectures.html) · [Back to Chapter 2](index.html) · [Next: 2.9 Evaluation Criteria for UES Foundation Models →](2-9-ues-fm-evaluation-criteria.html)
