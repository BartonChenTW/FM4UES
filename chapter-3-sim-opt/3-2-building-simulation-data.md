---
title: "3.2 Building Simulation: Loads, Datasets, Benchmarks"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 2
status: draft
last_reviewed: 2026-09-11
---

# 3.2 Building Energy Simulation: Loads, Datasets, Benchmarks
{: .no_toc }

{% include page-status.html %}

Framed for an ML reader: what's learnable at building scale, what shape the data has, and where the existing benchmarks and datasets sit.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## What's learnable

Building energy simulation (T1 in [§3.1](3-1-taxonomy-of-tasks.html)) produces, for a given building description and boundary conditions, a time-resolved trajectory of energy demand — typically hourly, sometimes sub-hourly, for one or more end uses (heating, cooling, electricity, domestic hot water). The learnable mapping is: (building description, weather, occupancy) → demand trajectory. This is a regression problem onto a high-dimensional, structured output (a full year is 8760 values per end use), not a single scalar.

## Data shapes

- **Real measured data** — smart meter or utility billing records. Abundant for electricity, sparser for heat. Carries real heterogeneity but almost never comes paired with the building attributes that would explain it (construction year, envelope, systems) — see the limitation below.
- **Simulator-generated data** — output of a physics-based tool (EnergyPlus, CitySim, TRNSYS; see [§3.6](3-6-tool-landscape.html)) run over a sampled set of building descriptions. Fully labelled by construction, since the input description is known exactly. This is the basis for any controlled study of representation — see [§5.3](../chapter-5-case-study/5-3-data-generation.html) for sampling design.

## Datasets and benchmarks

- **[BuildingsBench](../appendices/d-model-index.html#buildingsbench)** (NREL) — a large-scale dataset of 900K buildings and benchmark for short-term load forecasting, derived from NREL's End-Use Load Profiles database.[^emami2023buildingsbench] Provides profiles without paired ground-truth building attributes, which limits its use for representation studies specifically (see the limitation below) while making it a strong forecasting benchmark in its own right.
- **EnergyBench** (AI-IoT Lab, IISc Bangalore) — a Hugging Face dataset release of roughly 78,000 real buildings (commercial and residential) plus synthetic tiers, around 1.26 billion hourly electricity-consumption readings, CC-BY-SA-4.0.[^energybench]
- **ResStock / ComStock** (NREL) — large-scale, physics-based housing and commercial building stock models producing simulated hourly load data with full building metadata, widely used as pretraining or benchmarking corpora for building-stock-scale work (see [§4.2](../chapter-4-directions/4-2-fms-for-building-stocks.html)).
- **CESAR-P** (Empa) — a dynamic urban building energy simulation tool used as a simulator-grounded data generator, producing building-attribute-to-load-profile pairs.[^orehounig2022cesarp]

{: .important }
**The sample-granularity trap.** EnergyBench's ~78,000 buildings can be read as ~28 million samples (building-days), 78,000 samples (building-years), or roughly 200 samples (district-years) depending on what you call one example — identical underlying data, entirely different regime. The first supports pretraining; the third supports [fine-tuning](../appendices/a-glossary.html#fine-tuning) at best. This decision alone can determine whether a corpus is viable for a given training objective, and it recurs directly in the case study's token-schema design (see [§5.5](../chapter-5-case-study/5-5-token-schema.html)).

## The core limitation: measured data without attributes

Public building load collections mostly provide profiles without ground-truth attributes, which makes them unsuitable for any controlled study of representation, because the input side of the mapping is missing. This is why simulator-generated corpora, despite their own limitations (see next), are indispensable for representation work specifically, even though real measured data is otherwise preferable wherever it is available.

**What synthetic, archetype-derived data buys and what it does not.** Simulator-generated corpora have one decisive advantage: they are **fully labelled**. But **archetype-derived data supports interpolation across archetype space, which is not the same as generalisation to real heterogeneity.** A model that performs well across simulated archetypes has demonstrated something narrower than it appears. Where possible, validate against measurements from real instances, and report how many and how diverse. A second inherited limitation: the corpus absorbs the generating optimiser's or simulator's assumptions — cost curves, discount rates, technology sets, occupancy models. Changing any of them requires regenerating the data, and the model silently encodes the originals until you do.

[^emami2023buildingsbench]: Emami, P., Sahu, A., Graf, P. (2023). [BuildingsBench: A large-scale dataset of 900K buildings and benchmark for short-term load forecasting](https://arxiv.org/abs/2307.00142). NeurIPS 2023, Datasets and Benchmarks Track. arXiv:2307.00142.
[^orehounig2022cesarp]: Orehounig, K., Fierz, L., Allan, J. et al. (2022). [CESAR-P: A dynamic urban building energy simulation tool](https://doi.org/10.21105/joss.04261). *Journal of Open Source Software*, 7(78), 4261.
[^energybench]: AI-IoT Lab, IISc Bangalore. [EnergyBench](https://huggingface.co/datasets/ai-iot/EnergyBench). Hugging Face dataset, CC-BY-SA-4.0.

---
[← Previous: 3.1 Modelling Tasks and Their Mathematical Structure](3-1-taxonomy-of-tasks.html) · [Next: 3.3 Multi-Carrier Energy Hub Formalism →](3-3-energy-hub-formalism.html)
