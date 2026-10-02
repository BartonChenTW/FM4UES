---
title: "1.1 What an Urban Energy System Contains"
parent: Chapter 1 — Background
nav_order: 1
status: draft
last_reviewed: 2026-09-11
redirect_from: /01-the-domain.html
---

# 1.1 What an Urban Energy System Contains
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

An urban energy system is a spatially bounded set of energy demands, conversion technologies, storage, and networks, coupled across multiple energy carriers. The scales usually distinguished, following the building/district/city taxonomy used in urban building energy modelling (UBEM) reviews:[^ferrando2020ubem]

| Scale | Typical extent | What dominates |
| :--- | :--- | :--- |
| Building | one building | envelope physics, HVAC, occupant behaviour |
| Block / cluster | 5–50 buildings | shared supply, local networks, diversity effects |
| District | 50–5,000 buildings | network topology, district heating/cooling, storage |
| City | 10⁴–10⁶ buildings | aggregation, spatial heterogeneity, transport coupling |
| Region / national | many cities | policy, imports/exports, macro-scenarios |

The defining feature versus classical power systems: **multiple carriers, coupled**. Electricity, heat (often at several temperature levels), cooling, gas, hydrogen, and increasingly mobility demand — interacting through conversion devices (CHP, heat pumps, electrolysers, boilers, chillers) and storage of different types.

The **[energy hub](../appendices/a-glossary.html#energy-hub)** abstraction is the standard formalism: a node where multiple input carriers are converted, stored and dispatched to meet multiple output demands, represented by a coupling matrix mapping inputs to outputs.[^geidl2007opf] Most district-scale optimisation models are, structurally, either a single hub or a network of hubs.

## What the boundary contains beyond the hub

The hub formalism describes the *conversion* layer cleanly, but an urban system boundary drawn in practice encloses four further things, each of which a review literature treats as constitutive rather than peripheral:

**Demand, generation and networks, jointly.** Urban-scale modelling tools are surveyed as *multi-domain* precisely because building demand, local generation and distribution networks cannot be modelled in isolation without losing the interactions that make the system urban.[^sola2020multidomain] The data side carries the same conclusion: the inputs span building stock, transport, and geography, and assembling them is itself a recognised obstacle rather than a preliminary.[^bishop2024multidomaindata]

**Decentralised resources and partial autonomy.** The supply side is no longer only a connection to a transmission grid. Distributed resources and microgrids let a district or community operate with varying degrees of energy autonomy, and the modelling literature on decentralised autonomy is substantial enough to have its own review.[^weinand2020decentralized]

**The local climate the system sits in.** Urban energy systems are exposed to the climate they operate in — not only as a weather input, but as a resilience question under extreme events and long-run change.[^nik2021climateresilient]

**And a control layer.** Balancing multiple carriers in practice depends on metering, demand-side management and automated control, which is where the "smart city" tooling literature overlaps this domain.[^martins2021smartcitytools]

{: .note }
**Why this matters for the rest of the book, and not only as a definition.** Each item above widens the boundary, and every widening costs something a [foundation model](../appendices/a-glossary.html#foundation-model) must pay for. Multi-domain scope means the training corpus must span sources that were never collected together ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html), [§3.7](../chapter-3-sim-opt/3-7-schemas-and-standards.html)). Decentralisation means the *configuration* varies between instances, so a model has to transfer across system designs rather than only across time ([§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html), dimension 2). Climate exposure puts the boundary conditions themselves under uncertainty ([§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html), dimension 6). **This is the breadth that makes the basic-element question in [§2.3](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) hard**: the grid bus works as an element because a power network is one domain with one carrier, and none of the four items above holds for it.

[^geidl2007opf]: Geidl, M. and Andersson, G. (2007). [Optimal power flow of multiple energy carriers](https://doi.org/10.1109/TPWRS.2006.888988). *IEEE Transactions on Power Systems*, 22(1), 145–155.
[^ferrando2020ubem]: Ferrando, M., Causone, F., Hong, T., Chen, Y. (2020). [Urban building energy modeling (UBEM) tools: A state-of-the-art review of bottom-up physics-based approaches](https://arxiv.org/abs/2103.01761). *Sustainable Cities and Society*, 62, 102408.
[^sola2020multidomain]: Sola, A., Corchero, C., Salom, J., Sanmarti, M. (2020). [Multi-domain urban-scale energy modelling tools: A review](https://doi.org/10.1016/j.scs.2019.101872). *Sustainable Cities and Society*, 54, 101872.
[^bishop2024multidomaindata]: Bishop, D., Gallardo, P., Williams, B. L. M. (2024). [A review of multi-domain urban energy modelling data](https://doi.org/10.70322/ces.2024.10016). *Clean Energy and Sustainability*, 2, 10016.
[^weinand2020decentralized]: Weinand, J. M., Scheller, F., McKenna, R. (2020). [Reviewing energy system modelling of decentralized energy autonomy](https://doi.org/10.1016/j.energy.2020.117817). *Energy*, 203, 117817.
[^nik2021climateresilient]: Nik, V. M., Perera, A. T. D., Chen, D. (2021). [Towards climate resilient urban energy systems: a review](https://doi.org/10.1093/nsr/nwaa134). *National Science Review*, 8(3). Published online 2020.
[^martins2021smartcitytools]: Martins, F., Patrão, C., Moura, P., de Almeida, A. T. (2021). [A review of energy modeling tools for energy efficiency in smart cities](https://doi.org/10.3390/smartcities4040075). *Smart Cities*, 4(4), 1420–1436.

---
[← Back to Chapter 1](index.html) · [Next: 1.2 FMs in One Page →](1-2-fms-in-one-page.html)
