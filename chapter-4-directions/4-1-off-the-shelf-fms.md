---
title: "4.1 Using Existing FMs Off the Shelf"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 1
status: draft
last_reviewed: 2026-09-19
---

# 4.1 Using Existing Foundation Models Off the Shelf
{: .no_toc }

{% include page-status.html %}

The most useful direction to a practitioner today, and the one requiring the least new work.
{: .fs-6 .fw-300 }

{: .note }
**Partial.** A worked example with reported numbers is now below, from a published evaluation rather than a run of this book's own. What is still missing is this book's own benchmark run — the numbers below are one group's result on their network, not a reproduction.

1. TOC
{:toc}

---

## The direction

Before building anything bespoke, the cheapest and most immediately useful thing a UES practitioner can do is evaluate an already-pretrained, general-purpose time-series foundation model **zero-shot** on their own forecasting problem — no training, no fine-tuning, just point the model at the series and read off a forecast. The current generation of these models (Chronos-2, TimesFM 2.5, Moirai 2.0, TabPFN-TS — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)) is production-grade and free or cheap to run.

This is directly applicable to **load forecasting** — predicting building or district electricity, heat, or cooling demand a few hours to days ahead (T3 in [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)) — which is already flagged as a task with mature, off-the-shelf solutions in [§4.7](4-7-reading-the-screen.html).

## Why this belongs before any bespoke build

The build path recommended for Tier 1 dispatch modelling in [§4.9.1](4-9-1-methods-tier1.html) already makes this argument formally as "Step 2 — Zero-shot TSFM evaluation," and the baseline discipline in the same section makes the general case: **run the cheapest available option first, because it tells you whether anything more elaborate is warranted at all.** For pure load forecasting (as opposed to dispatch, which additionally needs energy-balance and storage-state handling), zero-shot evaluation is frequently sufficient on its own and does not need the rest of the Tier 1 build path.

## A worked example: zero-shot heat-load forecasting in district heating

A published evaluation carries out exactly this exercise for one UES carrier. TabPFN-TS and Chronos-2 were run zero-shot on probabilistic heat-load forecasting for a district heating network, against trained machine-learning baselines.[^spoek2026tabpfndh] The reported configuration and numbers are specific enough to be useful rather than merely illustrative:

- **Configuration that mattered:** hourly 24-hour-ahead forecasting with a 12-week rolling context and ambient temperature as the covariate — a parsimonious setup, and longer context windows did *not* improve accuracy. This is a concrete data point for the "how far back is worth feeding in" question the [Tier 1 build path](4-9-1-methods-tier1.html) leaves open.
- **Accuracy:** TabPFN-TS reached CVRMSE 13.06% against Chronos-2's 12.48% on the main dataset — close enough to sit within the critical-difference threshold on daily-rank comparison, though Chronos-2 had the lower full-year aggregate error. TabPFN-TS was better calibrated, which matters more than point accuracy for the uncertainty-awareness criterion in [§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html) (dimension 6).
- **Transferability actually tested, not assumed:** the configuration was validated on a second, different network — precisely what [§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html) (dimension 2) asks for and what a single-network evaluation cannot show.

One caveat worth carrying forward: TabPFN-TS is pretrained on **synthetic** data rather than real time series, which sidesteps train/test leakage but leaves open whether its learned prior actually captures district-heating dynamics specifically, or transfers on general time-series structure alone — the same synthetic-vs-real question this book raises for its own corpus in [§4.10.1](4-10-building-it.html#4101-data-generation-and-sampling-design).

## What would still need to be added here

- The comparison above is for one carrier (heat) on two networks. A UES practitioner working with electricity, gas, or a different demand profile has no equivalent published number yet to anchor expectations against.
- Notes on which covariates (weather, calendar, building metadata) each model can actually ingest zero-shot beyond the ambient-temperature case above, referencing the covariate-handling differences in [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html).
- This book's own benchmark run, rather than a citation of someone else's — see the caveat in the note above.

[^spoek2026tabpfndh]: Spoek, B., Ben Hicham, K. K., Derzsi, K. et al. (2026). [Systematic evaluation of TabPFN-TS for zero-shot probabilistic heat load forecasting in district heating networks](https://arxiv.org/abs/2608.20024). arXiv:2608.20024.

---
[← Back to Chapter 4](index.html) · [Next: 4.2 FMs for Whole Building Stocks →](4-2-fms-for-building-stocks.html)
