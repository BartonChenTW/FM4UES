---
title: "1.4 Why Now, and How to Use These Notes"
parent: "Chapter 1 — Background"
nav_order: 4
status: draft
last_reviewed: 2026-09-11
redirect_from:
  - /chapter-1-background/1-5-why-ues-why-now.html
  - /chapter-1-background/1-6-scope-and-how-to-use.html
---

# 1.4 Why Urban Energy Systems, Why Now, and How to Use These Notes
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## Why urban energy systems, why now
{: #why-now}

### The computational cost is already the bottleneck

Order-of-magnitude brackets on typical runtimes in this domain. The spread is the point.

| Task/configuration | Typical runtime |
| :--- | :--- |
| LP dispatch, single node, typical days | sub-second – seconds |
| LP dispatch, full 8760 h, district | seconds – minute |
| [MILP](../appendices/a-glossary.html#milp) with unit commitment | minutes – hours |
| Dynamic physical (Modelica, DH hydraulics) | tens of minutes – hours |
| UBEM, full stock, annual | minutes – hours |
| Design optimisation with dispatch inner loop | hours – days |
| AC-OPF, large network | seconds, but called thousands of times |

{: .important }
**Single runs are usually affordable. Loops are not.** Design optimisation, uncertainty quantification across weather years, and Monte Carlo risk assessment all call an inner model 10³–10⁶ times. That is where [surrogates](../appendices/a-glossary.html#surrogate) and [foundation models](../appendices/a-glossary.html#foundation-model) earn their keep — see [§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html#dispatch) and the [amortisation argument](../chapter-5-case-study/5-1-roadmap.html).

### Why the timing works now, not five years ago

Three things converged only recently:

1. **The recipe has been validated in an adjacent, structurally similar domain.** Power-grid foundation models now exist,[^hamann2024foundation] demonstrating that a physical network domain with hard constraints can support the foundation-model pattern. This is the single most important reference point for these notes — see [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html).
2. **Time-series foundation models have matured to production grade.** Off-the-shelf [zero-shot](../appendices/a-glossary.html#zero-shot) forecasting is now a viable starting point rather than a research artefact — see [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html).
3. **Simulation tooling for this domain is mature enough to act as a cheap, unlimited label generator.** Building energy simulation, UBEM, and energy-hub optimisation tools (surveyed in [Chapter 3](../chapter-3-sim-opt/index.html)) can synthesise arbitrarily large, fully-labelled training corpora — something real measured data essentially never offers in this domain (see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)).

What has **not** converged yet is a [basic element](../appendices/a-glossary.html#basic-element) for multi-carrier urban energy systems analogous to the grid bus — that gap, and what to do about it, is the subject of [Chapter 4](../chapter-4-directions/index.html) and [Chapter 5](../chapter-5-case-study/index.html).

## Scope of these notes and how to use them
{: #scope-and-how-to-use}

### What these notes are

These are working notes, not a textbook: a record of learning the field, organised so that others can follow the same path. Every claim cites a checkable source, but the selection of topics and the conclusions drawn are the author's, and nothing here has been peer-reviewed. Where the notes argue for something of their own rather than surveying the field, they say so: the proposed development path in [§4.7](../chapter-4-directions/4-7-methods-landing.html), the ecosystem synthesis in [§4.9](../chapter-4-directions/4-9-ecosystem.html), and the case study in [Chapter 5](../chapter-5-case-study/index.html).

### What they cover

The notes are written for someone who knows urban energy systems well and machine learning less well (or vice versa). They have four jobs:

1. **Map the domain** — what actually gets modelled and simulated in urban energy systems, what mathematical object each task is, and which tools do it. [Chapter 3](../chapter-3-sim-opt/index.html).
2. **Give the FM toolkit** — the conceptual grounding needed to judge any foundation-model proposal in this space, including basic machine learning concepts for readers without that background. [Chapter 2](../chapter-2-fm-foundations/index.html).
3. **Survey the directions** — of all the tasks in the domain, which could plausibly support a foundation model, broadly and neutrally, without committing to one specific programme. [Chapter 4](../chapter-4-directions/index.html).
4. **Work through one case study in depth** — a specific, concrete proposal for a foundation model for multi-carrier [energy hubs](../appendices/a-glossary.html#energy-hub): representation, roadmap, module decomposition, and risks. [Chapter 5](../chapter-5-case-study/index.html).

**If you read only one page**, read [Choosing a Basic Element](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) (§2.3) — it gives the criterion for deciding whether a foundation model is viable in a sub-domain at all, before any question of architecture or compute.

The **[proposed development path](../chapter-4-directions/4-7-methods-landing.html)** (§4.7) is the notes' own proposal, set apart from the surrounding survey: three tiers of increasing difficulty (single-hub dispatch → multi-hub multi-carrier dispatch → design and sizing optimisation), each with a concrete build path.

**Chapter 4 versus Chapter 5, explicitly.** Chapter 4 is a neutral survey: what the field as a whole knows about applying foundation models across UES sub-domains, without endorsing one direction over another. Chapter 5 is a specific, opinionated case study — one concrete proposal for a multi-carrier energy hub foundation model, including a token schema, module decomposition, and a phased roadmap. Readers who want "what does the field know" should read Chapter 4; readers who want "here is one worked proposal in full technical depth" should read Chapter 5. The two are kept deliberately separate so the reader can always tell what is established, what is being explored broadly, and what is one group's specific bet.

[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.

---
[← Previous: 1.3 The FM Landscape and Where It Is Heading](1-3-fm-landscape-by-domain.html) · [Back to Chapter 1](index.html) · [Next: Chapter 2 — Foundation Knowledge of FMs →](../chapter-2-fm-foundations/index.html)
