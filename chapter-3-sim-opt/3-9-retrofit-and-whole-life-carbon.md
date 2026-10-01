---
title: "3.9 Building Retrofit and Whole-Life Carbon"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 9
status: draft
last_reviewed: 2026-09-29
---

# 3.9 Building Retrofit Analysis and Whole-Life Carbon
{: .no_toc }

{% include page-status.html %}

Framed for an ML reader: what a retrofit decision is, which other tasks it calls, how the embodied carbon of building materials enters it, and what shape the data has.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## The task

Retrofit analysis (T10 in [§3.1](3-1-taxonomy-of-tasks.html)) starts from an existing building, or a stock of them, and asks which interventions to make: insulate the envelope, replace windows, replace the heating system, add PV or storage — in which combination, to what level, and when. The building literature frames the generic retrofit problem as identifying the most cost-effective measures for a particular project out of a wide range of readily available technologies, through a sequence of activities: energy audit, building performance assessment, quantification of energy benefits, economic analysis, risk assessment, and measurement and verification of the savings.[^ma2012retrofit] That review describes the decision process for one project at a time. It does not offer a method that carries over from one building to the next, which is the part that matters for this book.

The mathematical object is a **search over a discrete set of measures, with a simulation in the loop**. Each candidate combination is a modified building description; evaluating it means running demand modelling (T1) on that description; choosing among candidates means trading off objectives. Formulated as multi-objective optimisation, the task minimises energy use at acceptable cost while meeting occupant requirements — demonstrated on a single existing house needing refurbishment.[^asadi2012retrofit] One building and one measure library: it shows the structure of the problem, not how that structure behaves across a stock.

### How it composes with the other tasks

| Scale | What is decided | Tasks called |
| :--- | :--- | :--- |
| One building | Which measures, at which level | T1 per candidate; T5 when a measure is a system to be sized (heat pump, PV, storage); T9 for cost and emissions |
| A stock or district | Which buildings first, at what rate, under which policy | T1 across the stock; T8 for the scenarios |

At stock scale the question becomes a scenario question. CESAR, a bottom-up building stock model for Swiss districts, pairs an EnergyPlus-based demand model with a retrofitting model that applies energy-transformation scenarios based on the Swiss Energy Strategy 2050 to project future demand and emissions. Applied to an urban, a suburban and a rural district, it found that under business-as-usual only a small number of buildings reach the 2050 primary-energy and emissions targets.[^wang2018cesar] The retrofitting model applies *scenarios* rather than optimising measures building by building, so at stock level it inherits T8's lack of ground truth ([§4.7](../chapter-4-directions/4-7-reading-the-screen.html)) while still needing T1 for every building. Its dynamic-simulation successor, CESAR-P, is the simulator-grounded data generator described in [§3.2](3-2-building-simulation-data.html). Which owners actually take up the measures, and at what rate, is an adoption question — T11, in [§3.10](3-10-social-dimensions.html).

### The measure library is shared; the feasible subset is not

Every building draws on roughly the same catalogue of measures, but which of them a specific building can accept depends on that building: roof area bounds PV, the electrical connection bounds a heat pump, heritage protection can rule out external insulation. These instance-specific constraints are what make a retrofit plan a *[decision space](../appendices/a-glossary.html#decision-space)* rather than a list of options. That is [gap G9](../chapter-6-outlook/6-1-open-gaps.html#g9), and it is why a learned model that imitates a retrofit optimiser carries the deployment risk described in [§4.9.3](../chapter-4-directions/4-9-3-methods-tier3.html).

## Whole-life carbon: where building materials enter

Operational energy is only part of a building's emissions. The European standard for assessing the environmental performance of buildings, EN 15978, applies life cycle assessment ([LCA](../appendices/a-glossary.html#lca)) to new buildings, existing buildings and refurbishment projects, and builds the assessment from the information modules of Environmental Product Declarations ([EPDs](../appendices/a-glossary.html#epd)) under EN 15804.[^en15978] The life cycle is split into stages, each divided into modules:

| Stage | Modules | Operational or embodied | Where the number comes from |
| :--- | :--- | :--- | :--- |
| A — product and construction | A1–A3 raw materials, transport, manufacturing; A4–A5 transport to site, construction | Embodied | LCA database or EPD |
| B — use | B1–B5 use, maintenance, repair, replacement, refurbishment | Embodied | LCA database or EPD |
| B — use | **B6 operational energy use**; B7 operational water use | Operational | **B6 is the output of T1 / T4** |
| C — end of life | C1–C4 deconstruction, transport, waste processing, disposal | Embodied | LCA database |
| D — beyond the system boundary | Reuse, recovery and recycling potential | Reported separately | LCA database |

**B6 is the seam between this book and LCA.** Everything Chapters 3–5 simulate or optimise lands in one module. A retrofit lowers B6 and adds [embodied emissions](../appendices/a-glossary.html#embodied-emissions) of its own — the insulation, windows and equipment it installs, and their eventual replacement and disposal.

**The trade-off is not small.** A compilation of more than 650 LCA case studies (238 in the final sample) found life-cycle greenhouse-gas emissions falling as operational energy performance improves, but the embodied share rising: roughly 20–25% of life-cycle emissions for buildings built to current energy regulations, 45–50% for highly energy-efficient buildings, and above 90% in extreme cases, with a "carbon spike" at the time of production.[^rock2020embodied] It is a meta-analysis across different buildings, not a model of retrofit decisions. It establishes that optimising operational energy alone leaves a growing share of emissions out of view; it does not say what any given retrofit should be. It also reports a need for more transparent and comparable LCA studies — a data-quality warning for anyone assembling a corpus from published results.

**Counting embodied carbon changes the answer.** An integrated LCA and life-cycle-cost model, optimised robustly under uncertainty in the production, replacement and dismantling of building elements and in operational energy use, was applied to two typical Swiss buildings with low and high energy performance. Replacing the heating system was crucial for lowering environmental impact; for the building that already performed well, the investments were not repaid by operational savings; and for both buildings the robust optimum differed from the deep-renovation practice usually promoted to cut energy use.[^galimshina2021renovation] Two buildings, each optimised separately: nothing from the first solve carries over to the second. That per-instance cost is exactly what a learned model would amortise ([§3.5](3-5-design-sizing-optimisation.html#the-amortisation-argument)) — and the result is evidence that the objective has to include embodied impacts for the amortised answer to be the right one.

## Data shapes

- **Background life-cycle inventory (LCI) databases.** ecoinvent is the largest transparent unit-process [LCI database](../appendices/a-glossary.html#lci-database); version 3 separates modelling choices from raw data, so that different *system models* — cut-off, allocation at the point of substitution, and consequential — can be applied to the same raw data.[^wernet2016ecoinvent] For an ML reader the consequence is that the embodied-carbon value of a material is not a single fact. It depends on a modelling choice made upstream, which a model trained on the resulting numbers absorbs silently — the same inherited-assumption problem [§3.2](3-2-building-simulation-data.html#the-core-limitation-measured-data-without-attributes) describes for simulator-generated data.
- **National construction datasets.** Switzerland's platform for LCA data in construction (KBOB, ecobau, IPB) publishes data for building materials, building services, energy supply, transport and disposal, reporting greenhouse-gas emissions, primary energy, biogenic carbon content and an aggregate environmental-impact score. The values represent the average impact of building materials sold on the Swiss market, with manufacturer-specific entries for selected materials.[^kbob2026oekobilanz]
- **EPDs.** Product-specific declarations under EN 15804, the input EN 15978 expects.[^en15978]
- **The paired corpus.** What a learned retrofit model would train on is, for each (building, measure combination): the operational outcome from T1 and the embodied outcome from quantities × impact factors. Neither side is hard to compute once the quantities are known. The hard part is the **quantity take-off** — how many square metres of which material a measure installs on a specific building — because it depends on geometry that archetype-based stock models only approximate. Such a corpus can be generated, with a stock simulator on one side and an LCA database on the other; this book has not yet searched for a published one.

## Why this matters for foundation models

- **Embodied carbon itself is not the bottleneck.** Once quantities and impact factors are known it is a weighted sum, consistent with T9's "no bottleneck" verdict in [§4.6](../chapter-4-directions/4-6-screening-tasks.html). Learning it would be learning a lookup table.
- **The loop is.** Candidates multiply: five measure categories with three levels each, plus "do nothing", give 4⁵ = 1,024 combinations for one building, each needing a T1 run — multiplied again by the buildings in a stock, by weather or price scenarios, and by robustness samples if uncertainty is handled as in the Swiss study above. That is the 10³–10⁶-call loop of [§3.8](3-8-where-the-cost-is.html).
- **The representation is the open problem.** A model would need to represent the building ([G8](../chapter-6-outlook/6-1-open-gaps.html#g8)), the set of measures feasible on it ([G9](../chapter-6-outlook/6-1-open-gaps.html#g9)), and outcomes on two axes, operational and embodied. T10's verdict in [§4.6](../chapter-4-directions/4-6-screening-tasks.html) and its screening row in [§4.5](../chapter-4-directions/4-5-screening-fields.html) follow from that.

[^ma2012retrofit]: Ma, Z., Cooper, P., Daly, D., Ledo, L. (2012). [Existing building retrofits: Methodology and state-of-the-art](https://doi.org/10.1016/j.enbuild.2012.08.018). *Energy and Buildings*, 55, 889–902.
[^asadi2012retrofit]: Asadi, E., da Silva, M. G., Antunes, C. H., Dias, L. (2012). [Multi-objective optimization for building retrofit strategies: A model and an application](https://doi.org/10.1016/j.enbuild.2011.10.016). *Energy and Buildings*, 44, 81–87.
[^wang2018cesar]: Wang, D., Landolt, J., Mavromatidis, G., Orehounig, K., Carmeliet, J. (2018). [CESAR: A bottom-up building stock modelling tool for Switzerland to address sustainable energy transformation strategies](https://doi.org/10.1016/j.enbuild.2018.03.020). *Energy and Buildings*, 169, 9–26.
[^en15978]: CEN (2026). EN 15978:2026, *Sustainability of construction works — Assessment of environmental performance of buildings — Requirements and guidance*. [CEN-CENELEC announcement](https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-04-17-en-15978-2026/). Replaces EN 15978:2011; module definitions follow EN 15804:2012+A2:2019.
[^rock2020embodied]: Röck, M., Saade, M. R. M., Balouktsi, M. et al. (2020). [Embodied GHG emissions of buildings – The hidden challenge for effective climate change mitigation](https://doi.org/10.1016/j.apenergy.2019.114107). *Applied Energy*, 258, 114107.
[^galimshina2021renovation]: Galimshina, A., Moustapha, M., Hollberg, A. et al. (2021). [What is the optimal robust environmental and cost-effective solution for building renovation? Not the usual one](https://doi.org/10.1016/j.enbuild.2021.111329). *Energy and Buildings*, 251, 111329.
[^wernet2016ecoinvent]: Wernet, G., Bauer, C., Steubing, B., Reinhard, J., Moreno-Ruiz, E., Weidema, B. (2016). [The ecoinvent database version 3 (part I): overview and methodology](https://doi.org/10.1007/s11367-016-1087-8). *The International Journal of Life Cycle Assessment*, 21(9), 1218–1230.
[^kbob2026oekobilanz]: Plattform Ökobilanzdaten im Baubereich (KBOB, ecobau, IPB). [Ökobilanzdaten im Baubereich](https://www.kbob.admin.ch/de/oekobilanzdaten-im-baubereich). Version 9.0, 14 July 2026. In German.

---
[← Previous: 3.8 Where the Computational Cost Actually Is](3-8-where-the-cost-is.html) · [Back to Chapter 3](index.html) · [Next: 3.10 Social Dimensions →](3-10-social-dimensions.html)
