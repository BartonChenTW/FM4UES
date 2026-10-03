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
**Partial.** A worked example with reported numbers is now below, from a published evaluation rather than a run of these notes' own. What is still missing is these notes' own benchmark run — the numbers below are one group's result on their network, not a reproduction.

1. TOC
{:toc}

---

## The direction

Before building anything bespoke, the cheapest and most immediately useful thing a UES practitioner can do is evaluate an already-pretrained, general-purpose time-series foundation model **[zero-shot](../appendices/a-glossary.html#zero-shot)** on their own forecasting problem — no training, no [fine-tuning](../appendices/a-glossary.html#fine-tuning), just point the model at the series and read off a forecast. The current generation of these models ([Chronos-2](../appendices/d-model-index.html#chronos-2), [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5), [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0), [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) — see [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html)) is production-grade and free or cheap to run.

This is directly applicable to **load forecasting** — predicting building or district electricity, heat, or cooling demand a few hours to days ahead (T3 in [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html)) — where the task screen ([§4.6](4-6-screening-tasks.html), [§4.7](4-7-reading-the-screen.html)) finds it close to solved for aggregated load but still open for a single building, on the evidence collected in [§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html).

## Why try existing models before building your own

Building and training a model of your own is a large project. Testing an existing one zero-shot needs no training at all, and the result tells you whether the larger project is worth starting. If a pretrained model already forecasts your load well enough, you can stop there.

The notes' proposed development path puts this test second in its first tier, predicting how a single [energy hub](../appendices/a-glossary.html#energy-hub) operates ([§4.9.1](4-9-1-methods-tier1.html), "Step 2"), right after setting up simple baselines. For a hub, the test is only a starting point: a hub model must also keep energy in balance and track how full the storage is, which a forecaster does not do. For load forecasting alone, the zero-shot test is often the whole job.

## A worked example: zero-shot heat-load forecasting in district heating

A published evaluation carries out exactly this exercise for one UES carrier. TabPFN-TS and Chronos-2 were run zero-shot on probabilistic heat-load forecasting for a district heating network, against trained machine-learning baselines.[^spoek2026tabpfndh] The reported configuration and numbers are specific enough to be useful rather than merely illustrative:

- **Configuration that mattered:** hourly 24-hour-ahead forecasting with a 12-week rolling context and ambient temperature as the covariate — a parsimonious setup, and longer context windows did *not* improve accuracy. This is a concrete data point for the "how far back is worth feeding in" question the [Tier 1 build path](4-9-1-methods-tier1.html) leaves open.
- **Accuracy:** TabPFN-TS reached CVRMSE 13.06% against Chronos-2's 12.48% on the main dataset — close enough to sit within the critical-difference threshold on daily-rank comparison, though Chronos-2 had the lower full-year aggregate error. TabPFN-TS was better calibrated, which matters more than point accuracy for the uncertainty-awareness criterion in [§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html) (dimension 6).
- **Transferability actually tested, not assumed:** the configuration was validated on a second, different network — precisely what [§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html) (dimension 2) asks for and what a single-network evaluation cannot show.

One caveat worth carrying forward: TabPFN-TS is pretrained on **synthetic** data rather than real time series, which sidesteps train/test leakage but leaves open whether its learned prior actually captures district-heating dynamics specifically, or transfers on general time-series structure alone — the same synthetic-vs-real question these notes raise for their own corpus in [§4.10.1](4-10-building-it.html#4101-data-generation-and-sampling-design).

## What would still need to be added here

- The comparison above is for one carrier (heat) on two networks. Published numbers for electricity, from single households to whole grids, are collected in [§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html). They show zero-shot models doing well on aggregated load and less reliably for a single building.
- Notes on which covariates (weather, calendar, building metadata) each model can actually ingest zero-shot beyond the ambient-temperature case above, referencing the covariate-handling differences in [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html).
- These notes' own benchmark run, rather than a citation of someone else's — see the caveat in the note above.

[^spoek2026tabpfndh]: Spoek, B., Ben Hicham, K. K., Derzsi, K. et al. (2026). [Systematic evaluation of TabPFN-TS for zero-shot probabilistic heat load forecasting in district heating networks](https://arxiv.org/abs/2608.20024). arXiv:2608.20024.

---
[← Back to Chapter 4](index.html) · [Next: 4.2 FMs for Whole Building Stocks →](4-2-fms-for-building-stocks.html)
