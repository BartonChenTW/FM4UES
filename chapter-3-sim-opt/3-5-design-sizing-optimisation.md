---
title: "3.5 Design and Sizing Optimisation"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 5
status: draft
last_reviewed: 2026-09-11
---

# 3.5 Design and Sizing Optimisation
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## Why this is structurally different from dispatch

[§3.4](3-4-dispatch-optimisation.html)'s dispatch problem approximates a **simulation**: given inputs, predict outputs. Design and sizing optimisation (T5 in [§3.1](3-1-taxonomy-of-tasks.html)) approximates an **optimisation**: given a problem instance, predict the optimal decision — what to build, and how big.

The canonical structure is bilevel or two-stage:

```
outer:  choose capacities x  →  minimise  investment(x) + operating_cost(x)

inner:                              operating_cost(x) = min over dispatch, subject to physics
```

The inner problem — dispatch, from [§3.4](3-4-dispatch-optimisation.html) — is called once per candidate design. With evolutionary or many-objective outer search, that is 10³–10⁶ dispatch solves. **This is the single most expensive loop in the domain and the clearest justification for [surrogate](../appendices/a-glossary.html#surrogate) and foundation-model work.**

## The amortisation argument

**This is the argument that justifies foundation-model framing over bespoke surrogates, and it must be made explicitly whenever it is invoked.**

Building a training set costs *N* simulator runs. If *N* = 10,000 and each run takes a minute, that is roughly a week of compute before anything is returned. A surrogate for **one** system used within **one** study rarely repays this — which is precisely why the existing multi-energy surrogate literature is bespoke, small-data and discarded at project end (see [§2.8](../chapter-2-fm-foundations/2-8-surrogates-vs-fms.html)).

A [foundation model](../appendices/a-glossary.html#foundation-model) changes the arithmetic: the cost is paid once, across a distribution of systems, and amortised over every subsequent study. Formally, it pays back when

```
N_train × t_sim  <  Σ over future studies ( N_evaluations × t_sim )
```

**Corollary that matters institutionally:** this is also the succession argument. A model that speeds up every future study creates ongoing dependence, which is the strongest mechanism by which research infrastructure survives its author.

{: .warning }
**Caveat.** The arithmetic only holds if the model actually transfers. Amortisation assumes reuse across systems, and reuse depends on the [basic element](../appendices/a-glossary.html#basic-element) satisfying [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion). Where it does not, what looks like a foundation model is a collection of memorised cases and the payback never arrives. **Check the representation before running the amortisation calculation.**

## Where this is developed further

This page frames design/sizing as a learning problem and states the economic argument for it. The three families of method (surrogating the inner objective, learning the solution map directly, and hybrid warm-starting), the scaling-behaviour evidence, and the decision-space problem specific to this task are given in [§4.9.3 (Tier 3)](../chapter-4-directions/4-9-3-methods-tier3.html), once [Chapter 4](../chapter-4-directions/index.html) has screened which sub-fields are worth this investment at all.

---
[← Previous: 3.4 Operation / Dispatch Optimisation](3-4-dispatch-optimisation.html) · [Next: 3.6 The Tool Landscape →](3-6-tool-landscape.html)
