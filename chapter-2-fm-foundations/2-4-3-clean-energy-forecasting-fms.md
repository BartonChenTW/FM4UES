---
title: "2.4.3 Clean-Energy Forecasting FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 3
status: draft
last_reviewed: 2026-09-16
---

# 2.4.3 Clean-Energy Forecasting Foundation Models (Mature)
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Renewable generation forecasting is the second sub-domain, after the grid ([§2.4.2](2-4-2-power-grid-fms.html)), where domain-specific [foundation models](../appendices/a-glossary.html#foundation-model) have moved past proposal into working systems. Foundation models here integrate heterogeneous data through multi-modal fusion, and use patch-based [tokenisation](../appendices/a-glossary.html#tokenisation) grouping consecutive timesteps to address the quadratic complexity of self-attention.[^ferdaus2025cleanenergy]

The reason this family matured early is worth stating plainly, because it is the same mechanism [§2.3.1](2-3-choosing-a-basic-element.html#231-the-criterion) sets out: **a generation site is a good [basic element](../appendices/a-glossary.html#basic-element).** A wind farm is a wind farm in Texas and in Scotland; the metadata that conditions its output is a short, standardised list (coordinates and terrain for wind, tilt and azimuth for PV); sites aggregate into portfolios by summation; and the same element serves one plant or a hundred thousand. Unambiguous, stable in meaning, composable, scale-independent — all four hold, and nobody had to argue for a convention to make them hold. Contrast the building case of [§2.3.2](2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings), where no candidate element satisfies all four.

## What has been demonstrated

**Wind.** **[WindFM](../appendices/d-model-index.html#windfm)** is pretrained autoregressively on the NREL WIND Toolkit — roughly 150 billion timesteps from more than 126,000 sites — using a tokeniser that discretises continuous multivariate observations into hierarchical tokens. At 8.1M parameters it reports state-of-the-art [zero-shot](../appendices/a-glossary.html#zero-shot) performance on deterministic and probabilistic tasks against both specialised models and larger general-purpose FMs, and holds up on out-of-distribution data from a different continent.[^fan2025windfm] **[Tyan-WP](../appendices/d-model-index.html#tyan-wp)** targets ultra-short-term probabilistic forecasting on the same corpus, adding static site embedding (coordinate, terrain, ecoregion) and a fusion module for interactions between historical power and meteorological covariates; it reports cross-geography generalisation from U.S. pretraining to U.K. sites.[^huang2026tyanwp]

**Solar.** **[SPIRIT](../appendices/d-model-index.html#spirit)** addresses the cold-start case — a new PV farm with no operating history, where the conventional approach needs five or more years of site-specific irradiance data — and reports roughly 70% improvement over prior state of the art in zero-shot transfer, improving further with [fine-tuning](../appendices/a-glossary.html#fine-tuning) as local data accumulates.[^mishra2025spirit] A complementary result takes the opposite route: rather than a domain-pretrained model, it generates a *synthetic* production history from plant metadata and weather covariates, then conditions general-purpose [TSFMs](../appendices/a-glossary.html#tsfm) on it at inference time. Across 440 PV sites in four climate regimes, covariate-aware general models ([TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts), [Chronos-2](../appendices/d-model-index.html#chronos-2) — see [§2.4.1](2-4-1-time-series-fms.html)) beat classical baselines by 1.7–2×, and performance was largely insensitive to which generator produced the synthetic history.[^longarini2026coldstart]

That last finding is the useful one for these notes' purposes: what mattered was the availability of plausible temporal context, not the fidelity of the thing that produced it.

## What this family does not settle

**A shared public corpus did the work, and UES has no equivalent.** WindFM and Tyan-WP are both built on the WIND Toolkit. The element was clean *and* someone had already published a hundred thousand sites of it under a single schema. The multi-carrier urban case has neither half of that — no agreed element ([§2.3](2-3-choosing-a-basic-element.html)) and no corpus ([§2.5](2-5-what-does-not-exist-yet.html)). Reading this sub-section as evidence that "energy FMs work, so a UES FM will work" inverts the actual lesson.

**These models forecast an exogenous input, not the system.** Generation from wind and sun is weather-driven and, from the perspective of an urban energy system, largely uncontrollable. A renewable forecast is a boundary condition entering a dispatch or design problem — valuable, and directly usable as a covariate, but it does not represent conversion between carriers, storage state, network topology, or any discrete decision ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)). It sits upstream of the hub, in the same relation as the weather models of [§2.4.5](2-4-5-geospatial-weather-fms.html), one step closer to the meter.

**Single-carrier, single-task.** Each model above predicts one quantity — power output at a site — over short horizons. That is a narrower target than the multi-task transfer ([§2.1](2-1-what-defines-an-fm.html)) that distinguishes a foundation model from a well-generalising [surrogate](../appendices/a-glossary.html#surrogate) ([§2.8](2-8-surrogates-vs-fms.html)). The pretraining-plus-zero-shot-transfer pattern is genuine; the breadth of downstream tasks is not yet there.

{: .note }
**Practical consequence.** For a UES modeller today, this is the most directly usable family in [§2.4](2-4-existing-fms-relevant-to-energy.html): renewable generation is an input most urban models need, the models are zero-shot at new sites, and WindFM's weights are public. Taking a forecast from one of these and feeding it into a conventional model is the off-the-shelf path of [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html) — not a step toward a UES foundation model.

[^ferdaus2025cleanenergy]: Ferdaus, M. M., Dam, T., Sarkar, M. R. et al. (2026). [Foundation models for clean energy forecasting: A comprehensive review](https://doi.org/10.1016/j.rser.2025.116452). *Renewable and Sustainable Energy Reviews*, 226, 116452. arXiv:2507.23147.
[^fan2025windfm]: Fan, H., Shi, Y., Fu, Z. et al. (2025). [WindFM: An open-source foundation model for zero-shot wind power forecasting](https://arxiv.org/abs/2509.06311). arXiv:2509.06311.
[^huang2026tyanwp]: Huang, J., Luo, A., Liu, L. et al. (2026). [Tyan-WP: A wind power foundation model for ultra-short-term probabilistic forecasting](https://arxiv.org/abs/2606.08630). arXiv:2606.08630.
[^mishra2025spirit]: Mishra, A., Ravindra, T., Iyengar, S. et al. (2025). [SPIRIT: Short-term prediction of solar irradiance for zero-shot transfer learning using foundation models](https://arxiv.org/abs/2502.10307). arXiv:2502.10307.
[^longarini2026coldstart]: Longarini, L., Rongoni, A., Silenzi, S. et al. (2026). [Time series foundation models based on physics-informed synthetic histories for cold-start photovoltaic forecasting](https://arxiv.org/abs/2606.07457). 2nd ICML Workshop on Foundation Models for Structured Data. arXiv:2606.07457.

---
[← Previous: 2.4.2 Power-Grid FMs](2-4-2-power-grid-fms.html) · [Next: 2.4.4 Tabular FMs →](2-4-4-tabular-fms.html)
