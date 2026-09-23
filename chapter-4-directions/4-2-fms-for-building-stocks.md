---
title: "4.2 FMs for Whole Building Stocks"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 2
status: draft
last_reviewed: 2026-09-19
---

# 4.2 Foundation Models for Whole Building Stocks
{: .no_toc }

{% include page-status.html %}

{: .note }
**Still a stub, but now a checked one.** A dated search (below) confirms no stock-level foundation model has been published; the nearest empirical result is discussed and cited for what it does and does not establish.

1. TOC
{:toc}

---

## The direction

Everything in [§2.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) and most of this book's case study in [Chapter 5](../chapter-5-case-study/index.html) treats a single building or a single hub as the unit of interest. A different and complementary direction treats the **building stock** — a whole city or region's worth of buildings — as the object, with the individual building as R4's "stock-level" basic element (see [§2.3.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions)).

This changes the questions that are answerable. Instead of "what will this building's demand be," the target becomes portfolio-level: aggregate demand under a retrofit policy, stock-wide emissions trajectories, or which archetypes in a city-scale stock are under-represented in a training corpus. Large physics-based stock models — **ResStock**[^wilson2022resstock] and **ComStock**[^parker2023comstock] (NREL) — already generate the kind of fully-labelled, large-N corpora (see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)) that a stock-level foundation model would pretrain on.

## Relationship to the rest of this book

R4 in [§2.3.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions) already names this trade-off precisely: a stock-level representation is unambiguous and composable *at the stock level*, and generalises across stocks, but gives up within-building resolution — it cannot answer "what will happen to this specific building's hourly profile," only "what will happen in aggregate." This makes it a genuinely different target from the case study in [Chapter 5](../chapter-5-case-study/index.html), which is deliberately building/hub-resolved.

## What exists, and what it does not establish

A dated search (arXiv title/abstract, "ResStock" or "ComStock" combined with "foundation model", "pretrained" or "pretraining"; and separately "building stock" combined with "foundation model"; run 19 September 2026) returns exactly one relevant result and confirms there is no published stock-level foundation model to survey yet.

The one result is not itself a stock-level FM, but it is the closest empirical grounding for what one would need to handle. An architecture comparison spanning RNNs through fine-tuned open-source time-series FMs, run on ComStock-derived commercial-building data, found that dataset heterogeneity and architecture affected post-training performance more than parameter count — isolated by comparing two curated ComStock subsets equal in size and region but differing in building-type diversity.[^bose2024rnnstofm] That is a finding about what a *pretraining corpus drawn from a stock* needs to contain, not a demonstration of a model that treats the stock itself as the unit — but it is directly relevant to the "what pretraining objective" and "what corpus composition" questions any stock-level FM would face first.

## What would still need to be added here

- The comparison above is architecture-vs-heterogeneity on one U.S. commercial-building stock (ComStock). No equivalent exists for residential stock, for European stock datasets, or across more than two curated subsets.
- A worked comparison of stock-level versus building-level representation against the four requirements in [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion), analogous to the building-level analysis already done in [§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings).
- Discussion of how stock-level and building-level representations could be composed (e.g. a stock-level model providing priors that a building-level model fine-tunes against).

[^wilson2022resstock]: Wilson, E., Parker, A., Fontanini, A. et al. (2022). [End-use load profiles for the U.S. building stock: Methodology and results of model calibration, validation, and uncertainty quantification](https://doi.org/10.2172/1854582). NREL/TP-5500-80889.
[^parker2023comstock]: Parker, A., Horsey, H., Dahlhausen, M. et al. (2023). [ComStock reference documentation (V.1)](https://doi.org/10.2172/1967948). NREL/TP-5500-83819.
[^bose2024rnnstofm]: Bose, S., Li, Y., Van Sant, A., Zhang, Y., Kim, K. (2024). [From RNNs to foundation models: An empirical study on commercial building energy consumption](https://arxiv.org/abs/2411.14421). arXiv:2411.14421. NeurIPS 2024 Workshop on Time Series in the Age of Large Models.

---
[← Previous: 4.1 Off-the-Shelf FMs](4-1-off-the-shelf-fms.html) · [Next: 4.3 LLM Agents for Simulation →](4-3-llm-agents-for-simulation.html)
