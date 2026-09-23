---
title: Home
layout: home
nav_order: 1
---

# Foundation Models for Urban Energy Systems
{: .fs-9 }

A working textbook: what gets simulated, what could be learned, and how to build it.
{: .fs-6 .fw-300 }

Version 2.0 — 11 September 2026
{: .label }

Initiated by [Barton Chen](https://github.com/BartonChenTW) from the [Urban Energy Systems Lab](https://www.empa.ch/web/s313) at [Empa](https://www.empa.ch/) — open for anyone to contribute. See [how to contribute](chapter-6-outlook/6-2-how-to-contribute.html). Most content was drafted and edited with AI assistance under Barton Chen's direction and review.
{: .fs-3 }

Drafted and edited with AI assistance (Claude Opus 5 and Claude Sonnet 5, Anthropic) under Barton Chen's direction and review — see [`CONTRIBUTING.md`](https://github.com/BartonChenTW/FM4UES/blob/main/CONTRIBUTING.md) for how claims are sourced and checked.
{: .fs-2 }

---

## How to use this document

This is written for someone who knows urban energy systems well and machine learning less well (or vice versa). It has four jobs:

1. **Map the domain** — what actually gets modelled and simulated in urban energy systems, what mathematical object each task is, and which tools do it.
2. **Give the FM toolkit** — the conceptual grounding needed to judge any foundation-model proposal, including basic ML concepts for readers without that background.
3. **Survey the directions** — of all the tasks in the domain, which could plausibly support a foundation model, broadly and neutrally.
4. **Work through one case study in depth** — a specific, concrete proposal for a foundation model for multi-carrier energy hubs.

**If you read only one page**, read [Choosing a Basic Element](chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) (§2.3) — it gives the criterion for deciding whether a foundation model is viable in a sub-domain at all, before any question of architecture or compute.

The **[Methods by Problem Class](chapter-4-directions/4-9-methods-landing.html)** pages (§4.9) are the operational core of the directions survey: three tiers of increasing difficulty (single-hub dispatch → multi-hub multi-carrier dispatch → design and sizing optimisation), each with a concrete build path.

{: .warning }
**The field moves fast.** Publication counts on LLM-and-energy alone went from roughly 1 (2022) to 13 (2023) to 128 (2024) to 464 (2025), with 348 already indexed in the first half of 2026 (a Scopus search run 11 July 2026 — query and source in [§1.3](chapter-1-background/1-3-fm-landscape-by-domain.html)). Re-check anything that reads as a landscape or novelty claim before it is used to justify a proposal or paper.

---

## Contents

| Chapter | Page | Covers |
| :--- | :--- | :--- |
| 1 | [Background: UES and FMs](chapter-1-background/index.html) | What the domain is, what FMs are, why the two should meet now |
| 2 | [Foundation Knowledge of FMs](chapter-2-fm-foundations/index.html) | What makes a model a foundation model; [Choosing a Basic Element](chapter-2-fm-foundations/2-3-choosing-a-basic-element.html); the FM landscape today; ML basics (self-supervision, transformers, GNNs, neural operators); surrogates vs FMs; evaluation criteria for UES FMs |
| 3 | [Simulation and Optimisation in UES](chapter-3-sim-opt/index.html) | Task taxonomy, building simulation data, the energy hub formalism, dispatch and design optimisation, the tool landscape, where cost lives |
| 4 | [Directions for FMs in UES](chapter-4-directions/index.html) | A broad, neutral survey: off-the-shelf FMs, building-stock FMs, LLM agents, generative design, screening, and methods by problem tier |
| 5 | [Case Study: A Foundation Model for Multi-Carrier Energy Hubs](chapter-5-case-study/index.html) | One concrete proposal — representation, token schema, module decomposition, a phased roadmap, risks |
| 6 | [Outlook](chapter-6-outlook/index.html) | Nine open gaps; how to contribute |
| — | [Glossary](appendices/a-glossary.html) | Plain-language definitions of every ML term used |
| — | [Pre-Project Checklist](appendices/b-checklist.html) | Thirteen questions to ask before starting |
