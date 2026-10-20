---
title: "4.2 FMs for Whole Building Stocks"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 2
status: draft
last_reviewed: 2026-10-20
---

# 4.2 Foundation Models for Whole Building Stocks
{: .no_toc }

{% include page-status.html %}

{: .note }
**Partial.** A dated search (below) confirms no stock-level [foundation model](../appendices/a-glossary.html#foundation-model) has been published. What does exist is covered here: models pretrained on simulated building stocks and tested on real homes, including European ones; the residential and European datasets; and established methods for combining a stock-level model with a building-level one. The comparison against the four requirements is these notes' own analysis.

1. TOC
{:toc}

---

## The direction

Everything in [§2.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) and most of these notes' case study in [Chapter 5](../chapter-5-case-study/index.html) treats a single building or a single hub as the unit of interest. A different and complementary direction treats the **building stock** — a whole city or region's worth of buildings — as the object, with the individual building as the [basic element](../appendices/a-glossary.html#basic-element): the "building as an element of a stock" representation in [§2.3.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions).

This changes the questions that are answerable. Instead of "what will this building's demand be," the target becomes portfolio-level: aggregate demand under a retrofit policy ([§3.5](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html)), stock-wide emissions trajectories, or which archetypes in a city-scale stock are under-represented in a training corpus. Large physics-based stock models — **ResStock**[^wilson2022resstock] and **ComStock**[^parker2023comstock] (NREL) — already generate the kind of fully-labelled, large-N corpora (see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)) that a stock-level foundation model would pretrain on.

## Relationship to the rest of these notes

The stock-level representation in [§2.3.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions), which treats each building as one element of a stock, already names this trade-off: it is unambiguous and composable *at the stock level*, and generalises across stocks, but gives up within-building resolution — it cannot answer "what will happen to this specific building's hourly profile," only "what will happen in aggregate." This makes it a genuinely different target from the case study in [Chapter 5](../chapter-5-case-study/index.html), which is deliberately building/hub-resolved.

## What exists, and what it does not establish

A dated search on arXiv (title and abstract: "building stock" with "foundation model", "pretrained", "pretraining" or "transfer learning"; ResStock, ComStock or End-Use Load Profiles with foundation-model and generative terms; residential and European stock terms), extended to OpenAlex for journal papers and run on 20 October 2026, confirms there is no published stock-level foundation model. A first search, on arXiv only on 19 September 2026, gave the same answer. Several models do pretrain on a stock and forecast individual buildings, and those are the closest grounding for what a stock-level model would need to handle.

**Corpus composition.** An architecture comparison spanning RNNs through fine-tuned open-source time-series FMs, run on ComStock-derived commercial-building data, found that dataset heterogeneity and architecture affected post-training performance more than parameter count — isolated by comparing two curated ComStock subsets equal in size and region but differing in building-type diversity.[^bose2024rnnstofm] That is a finding about what a *pretraining corpus drawn from a stock* needs to contain, not a demonstration of a model that treats the stock itself as the unit — but it is directly relevant to the "what pretraining objective" and "what corpus composition" questions any stock-level FM would face first.

**Residential buildings, including European ones.** [BuildingsBench](../appendices/d-model-index.html#buildingsbench) pretrains on Buildings-900K, about 900,000 simulated buildings drawn from both ResStock and ComStock, and tests the pretrained models [zero-shot](../appendices/a-glossary.html#zero-shot) on real buildings.[^emami2023buildingsbench] The real residential test set includes 713 sampled households from Low Carbon London, 255 homes in Edinburgh (IDEAL) and one household near Paris (Sceaux), so a stock-pretrained model has already been tested on European homes. The result splits by building type. On commercial buildings its largest pretrained [transformer](../appendices/a-glossary.html#transformer) reaches a normalised RMSE of 13.31% against 16.68% for a persistence baseline (repeating recent load). On residential buildings it reaches 79.34% against 77.88% for persistence, so it does **not** beat the simple baseline (figures from the project's repository, read 20 October 2026). The authors' own summary is "promising results for commercial buildings" and "areas of improvement for residential buildings". This fits the pattern in [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html): pretrained models do well on aggregated load and less reliably on a single building.

## Residential and European stock data

| Source | What it is | Scope | What it adds |
| :--- | :--- | :--- | :--- |
| **RESCAST-100K** (preprint)[^dhruva2026rescast] | Dataset of about 100,000 EnergyPlus-simulated homes derived from ResStock, with over 40 fixed building attributes, plus five real residential datasets in the same format | US homes | Domains defined by geography, climate zone, wall construction and heating equipment, so heterogeneity can be varied deliberately; the residential counterpart of the ComStock comparison above |
| **GenTL**[^raisch2025gentl] | Model of building thermal behaviour pretrained on 450 single-family houses, then fine-tuned to each target | Central Europe, single-family houses | On 144 target buildings, [fine-tuning](../appendices/a-glossary.html#fine-tuning) the pretrained model cut average RMSE by 42.1% against fine-tuning models pretrained on one source building. The abstract does not say whether the 450 houses are simulated or measured |
| **EUBUCCO**[^milojevicdupont2023eubucco] | Open database of about 202 million individual buildings | The 27 EU countries and Switzerland | Height is known for 73% of buildings, type for 46% and construction year for only 24%. Construction year is what archetype models use to assign envelope properties, so this gap limits any European stock model |
| **AutoBEM / Model America**[^li2026autobem] | Building-by-building EnergyPlus models for 122.9 million buildings, built with prototype assumptions | 97.8% of the US building stock | A stock corpus at single-building resolution, rather than a statistical sample like ResStock |

No European equivalent of ResStock or ComStock was found: a simulated stock with complete inputs and labelled outputs at that scale. EUBUCCO supplies footprints and some attributes, but not the simulation inputs and outputs a pretraining corpus needs.

## Combining stock-level and building-level models

Using a stock-level model as a prior that each building's model then adjusts to that building's data is an established practice, mostly outside the foundation-model literature. Three patterns appear.

**1. Hierarchical calibration.** The stock model and the building models are fitted together. Information from all the buildings is partially pooled: each building gets its own parameters, pulled towards the archetype's values, and more strongly when its own data says little. On the Danish residential stock, fitted on 50 buildings and tested on 100 others, the archetype model reached a normalised mean bias error of 2.9% and a [CV(RMSE)](../appendices/a-glossary.html#cv-rmse) of 7.8%.[^kristensen2018hierarchical] For 193 monitored dwellings in Leicester, England, a Bayesian calibration with data-driven priors for each group of similar dwellings cut the error in summer indoor temperature from 2.5 °C to 0.6 °C.[^petrou2024bayesianstock]

**2. Pretrain on the stock, then check coverage.** A model is pretrained on the simulated stock and fine-tuned or applied to real buildings, with an explicit test of whether each real building is covered by the stock. In one study, a variational autoencoder trained on 8,856 hourly load profiles from the New York State part of ComStock first screens which real buildings the simulated stock represents; a forecaster pretrained on the same profiles then forecasts those buildings. On 101 real buildings from BDG2, about 82–84% passed the screen, and the forecaster reached a mean CV(RMSE) of 12.07% in summer and 11.44% in winter on them.[^quan2025stars] This is the archetype-coverage concern of [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html) turned into a test applied before forecasting.

**3. The stock as a generator of building inputs.** A generative model trained on the stock fills in the attributes a particular building is missing, conditioned on what is known about it, and a physics simulator then runs. A diffusion model trained on a residential stock model of 2.2 million buildings imputes missing building characteristics from known ones, with a case study in Baltimore.[^sinha2026buildingdiffusion] A related framework uses models trained on ResStock to infer missing characteristics and produce simulation-ready inputs for district-scale modelling in URBANopt, including what-if upgrade scenarios, checked against real building characteristics.[^elkontar2026urbanai] Here the stock supplies a prior over *inputs* rather than over outputs, the same role an LLM plays when it chooses defaults in [§4.3](4-3-llm-agents-for-simulation.html), but learned from data.

What none of these does is the foundation-model version: one pretrained stock-level model that many building-level models are fine-tuned from, across stocks in different countries. The pieces exist separately.

## Stock-level and building-level representations against the four requirements

This comparison is these notes' own analysis. It applies the four requirements of [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion) to the two representations, using the evidence above.

| Requirement | Building as the element of a stock | Building on its own (building-level) | Evidence |
| :--- | :--- | :--- | :--- |
| **Unambiguous** | Mostly yes: one building is one record, although where one building ends and the next begins is a choice in dense blocks | Partly: the zoning and the boundary of what is modelled vary between modellers ([§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings)) | — |
| **Stable in meaning** | Partly: the same attributes (age, type, floor area) mean different envelopes in different countries; archetype definitions are national | Partly, for the same reason | BuildingsBench transfers to commercial but not residential buildings; EUBUCCO's construction year is known for 24% of buildings |
| **Composable** | Yes at the stock level: a stock is a sum of buildings, and stock aggregates follow | Yes within a building; aggregating to a district needs the stock's weights | Hierarchical calibration composes the two levels explicitly |
| **Scale-independent** | Yes in size (any number of buildings), but only for aggregate questions | Yes for one building, at the cost of a full model per building | — |

The two representations fail in different places, which is the argument for combining them rather than choosing one. A stock-level model is sound for aggregate questions and gives a prior. A building-level model resolves the individual building but needs that building's data. The three patterns above are ways of joining them.

## What would still need to be added here

- A stock-level foundation model itself, which does not exist yet: one model pretrained across stocks, from which building-level models are fine-tuned.
- A European simulated stock corpus comparable to ResStock or ComStock. EUBUCCO's attribute coverage shows how far existing data is from that.
- A test of whether adding European residential data to pretraining lets a stock-pretrained model beat persistence on single households, where BuildingsBench's model does not.

[^wilson2022resstock]: Wilson, E., Parker, A., Fontanini, A. et al. (2022). [End-use load profiles for the U.S. building stock: Methodology and results of model calibration, validation, and uncertainty quantification](https://doi.org/10.2172/1854582). NREL/TP-5500-80889.
[^parker2023comstock]: Parker, A., Horsey, H., Dahlhausen, M. et al. (2023). [ComStock reference documentation (V.1)](https://doi.org/10.2172/1967948). NREL/TP-5500-83819.
[^bose2024rnnstofm]: Bose, S., Li, Y., Van Sant, A., Zhang, Y., Kim, K. (2024). [From RNNs to foundation models: An empirical study on commercial building energy consumption](https://arxiv.org/abs/2411.14421). arXiv:2411.14421. NeurIPS 2024 Workshop on Time Series in the Age of Large Models.
[^emami2023buildingsbench]: Emami, P., Sahu, A., Graf, P. (2023). [BuildingsBench: A large-scale dataset of 900K buildings and benchmark for short-term load forecasting](https://arxiv.org/abs/2307.00142). NeurIPS 2023, Datasets and Benchmarks Track. arXiv:2307.00142.
[^dhruva2026rescast]: Dhruva, J., Raza, Y., Siddique, A. B. et al. (2026). [RESCAST-100K: A comprehensive dataset for cross-domain residential load and indoor temperature forecasting](https://arxiv.org/abs/2606.02852). arXiv:2606.02852.
[^raisch2025gentl]: Raisch, F., Krug, T., Goebel, C. et al. (2025). [GenTL: A general transfer learning model for building thermal dynamics](https://doi.org/10.1145/3679240.3734589). *Proceedings of the 16th ACM International Conference on Future and Sustainable Energy Systems (e-Energy '25)*, 322–333.
[^milojevicdupont2023eubucco]: Milojevic-Dupont, N., Wagner, F., Nachtigall, F. et al. (2023). [EUBUCCO v0.1: European building stock characteristics in a common and open database for 200+ million individual buildings](https://doi.org/10.1038/s41597-023-02040-2). *Scientific Data*, 10(1), 147.
[^li2026autobem]: Li, H., Chowdhury, S., Li, F. et al. (2026). [AutoBEM: A scalable framework for nationwide building energy simulation and retrofit evaluation in the United States](https://doi.org/10.1016/j.scs.2026.107700). *Sustainable Cities and Society*, 149, 107700.
[^kristensen2018hierarchical]: Kristensen, M. H., Hedegaard, R. E., Petersen, S. (2018). [Hierarchical calibration of archetypes for urban building energy modeling](https://doi.org/10.1016/j.enbuild.2018.07.030). *Energy and Buildings*, 175, 219–234.
[^petrou2024bayesianstock]: Petrou, G., Mavrogianni, A., Symonds, P. et al. (2024). [Development of a Bayesian calibration framework for archetype-based housing stock models of summer indoor temperature](https://doi.org/10.1080/19401493.2024.2421330). *Journal of Building Performance Simulation*, 18(5--6), 687–706.
[^quan2025stars]: Quan, H., Ergan, S. (2025). [Sim-to-real transfer learning for large-scale short-term building energy forecasting in sustainable cities](https://doi.org/10.1145/3736425.3772006). *Proceedings of the 12th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys '25)*, 86–95.
[^sinha2026buildingdiffusion]: Sinha, S., Cortiella, A., El Kontar, R. et al. (2026). [Conditional distribution estimation of building characteristics with diffusion models for urban energy modeling](https://doi.org/10.1016/j.enbuild.2026.117392). *Energy and Buildings*, 361, 117392. arXiv:2511.02930.
[^elkontar2026urbanai]: El Kontar, R., Almaian, M., Vaidhynathan, D. et al. (2026). [AI-based analytics and energy modeling framework for characterizing urban energy systems](https://doi.org/10.1016/j.enbuild.2026.118027). *Energy and Buildings*, 369, 118027.

---
[← Previous: 4.1 Using Existing FMs Off the Shelf](4-1-off-the-shelf-fms.html) · [Back to Chapter 4](index.html) · [Next: 4.3 LLMs and Agents That Build or Run Simulation Models →](4-3-llm-agents-for-simulation.html)
