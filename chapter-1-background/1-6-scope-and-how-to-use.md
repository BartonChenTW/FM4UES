---
title: "1.6 Scope and How to Use These Notes"
parent: Chapter 1 — Background
nav_order: 6
status: draft
last_reviewed: 2026-09-11
---

# 1.6 Scope of These Notes and How to Use Them
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## What these notes are

These are working notes, not a textbook: a record of learning the field, organised so that others can follow the same path. Every claim cites a checkable source, but the selection of topics and the conclusions drawn are the author's, and nothing here has been peer-reviewed. Where the notes argue for something of their own rather than surveying the field, they say so: the proposed development path in [§4.9](../chapter-4-directions/4-9-methods-landing.html), the ecosystem synthesis in [§4.11](../chapter-4-directions/4-11-ecosystem.html), and the case study in [Chapter 5](../chapter-5-case-study/index.html).

## What they cover

The notes are written for someone who knows urban energy systems well and machine learning less well (or vice versa). They have four jobs:

1. **Map the domain** — what actually gets modelled and simulated in urban energy systems, what mathematical object each task is, and which tools do it. [Chapter 3](../chapter-3-sim-opt/index.html).
2. **Give the FM toolkit** — the conceptual grounding needed to judge any foundation-model proposal in this space, including basic machine learning concepts for readers without that background. [Chapter 2](../chapter-2-fm-foundations/index.html).
3. **Survey the directions** — of all the tasks in the domain, which could plausibly support a [foundation model](../appendices/a-glossary.html#foundation-model), broadly and neutrally, without committing to one specific programme. [Chapter 4](../chapter-4-directions/index.html).
4. **Work through one case study in depth** — a specific, concrete proposal for a foundation model for multi-carrier [energy hubs](../appendices/a-glossary.html#energy-hub): representation, roadmap, module decomposition, and risks. [Chapter 5](../chapter-5-case-study/index.html).

**If you read only one page**, read [Choosing a Basic Element](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) (§2.3) — it gives the criterion for deciding whether a foundation model is viable in a sub-domain at all, before any question of architecture or compute.

The **[proposed development path](../chapter-4-directions/4-9-methods-landing.html)** (§4.9) is the notes' own proposal, set apart from the surrounding survey: three tiers of increasing difficulty (single-hub dispatch → multi-hub multi-carrier dispatch → design and sizing optimisation), each with a concrete build path.

**Chapter 4 versus Chapter 5, explicitly.** Chapter 4 is a neutral survey: what the field as a whole knows about applying foundation models across UES sub-domains, without endorsing one direction over another. Chapter 5 is a specific, opinionated case study — one concrete proposal for a multi-carrier energy hub foundation model, including a token schema, module decomposition, and a phased roadmap. Readers who want "what does the field know" should read Chapter 4; readers who want "here is one worked proposal in full technical depth" should read Chapter 5. The two are kept deliberately separate so the reader can always tell what is established, what is being explored broadly, and what is one group's specific bet.

---
[← Previous: 1.5 Why UES, Why Now](1-5-why-ues-why-now.html) · [Back to Chapter 1](index.html) · [Next: Chapter 2 →](../chapter-2-fm-foundations/index.html)
