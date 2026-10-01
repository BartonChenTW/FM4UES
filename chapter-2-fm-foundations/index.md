---
title: Chapter 2 — Foundation Knowledge of FMs
nav_order: 3
has_children: true
status: draft
last_reviewed: 2026-09-11
---

# Chapter 2 — Foundation Knowledge of Foundation Models
{: .no_toc }

{% include page-status.html %}

The conceptual toolkit to judge any foundation-model proposal, including basic machine learning concepts for readers arriving from the energy-systems side.
{: .fs-6 .fw-300 }

```mermaid
flowchart TD
    A["2.1 What defines a foundation model"] --> B["2.2 The five design decisions"]
    B --> C["2.3 Choosing a basic element"]
    C --> D["2.4 Existing FMs relevant to energy"]
    D --> E["2.5 What does not exist yet"]
    F["2.6 Self-supervision, fine-tuning, scaling laws"] --> B
    G["2.7 Architectures: transformers, GNNs, neural operators"] --> B
    H["2.8 Surrogates vs foundation models"] --> A
    H --> I["2.9 Evaluation criteria for UES FMs"]
```

## In this chapter

| § | Page | Covers |
| :--- | :--- | :--- |
| 2.1 | [What actually defines a foundation model](2-1-what-defines-an-fm.html) | Three required properties; surrogate vs FM |
| 2.2 | [The five design decisions](2-2-five-design-decisions.html) | Unit of observation, tokenisation, architecture, objective, evaluation |
| 2.3 | [Choosing a basic element](2-3-choosing-a-basic-element.html) | **The core argument** — a criterion for choosing a basic element, applied to buildings |
| 2.4 | [Existing FMs relevant to energy](2-4-existing-fms-relevant-to-energy.html) | Landing page for the sub-sections below |
| 2.4.1 | [— Time-series FMs](2-4-1-time-series-fms.html) | [Chronos](../appendices/d-model-index.html#chronos), [Moirai](../appendices/d-model-index.html#moirai), [TimesFM](../appendices/d-model-index.html#timesfm), [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) and the current generation |
| 2.4.2 | [— Power-grid FMs](2-4-2-power-grid-fms.html) | [GridFM-v0](../appendices/d-model-index.html#gridfm) and the closest analogue to this book's project |
| 2.4.3 | [— Clean-energy forecasting FMs](2-4-3-clean-energy-forecasting-fms.html) | Multi-modal fusion for renewables forecasting |
| 2.4.4 | [— Tabular FMs](2-4-4-tabular-fms.html) | The cell as a basic element |
| 2.4.5 | [— Geospatial & weather FMs](2-4-5-geospatial-weather-fms.html) | [GraphCast](../appendices/d-model-index.html#graphcast), [Prithvi](../appendices/d-model-index.html#prithvi), and relevance to urban microclimate |
| 2.4.6 | [— Load & smart-meter forecasting FMs](2-4-6-load-forecasting-fms.html) | Load-pretrained models (BuildingsBench, [EnergyFM](../appendices/d-model-index.html#energyfm), [PowerPM](../appendices/d-model-index.html#powerpm)) and general FMs tested on load, from single buildings to whole grids |
| 2.5 | [What does not exist yet](2-5-what-does-not-exist-yet.html) | The gaps this book is written into |
| 2.6 | [Self-supervised pretraining, fine-tuning, scaling laws](2-6-scaling-laws.html) | ML basics for readers without an ML background |
| 2.7 | [Architectures: transformers, GNNs, neural operators](2-7-architectures.html) | ML basics, continued; how multimodal models combine several kinds of data |
| 2.8 | [Surrogates vs foundation models](2-8-surrogates-vs-fms.html) | The contrast UES readers already understand half of |
| 2.9 | [Evaluation criteria for UES foundation models](2-9-ues-fm-evaluation-criteria.html) | Seven dimensions for judging a UES-FM proposal beyond the generic three-property test |

---
[← Previous: Chapter 1 — Background](../chapter-1-background/index.html) · [Next: Chapter 3 — Simulation and Optimisation in UES →](../chapter-3-sim-opt/index.html)
