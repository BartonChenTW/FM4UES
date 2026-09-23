---
title: "2.5 What Does Not Exist Yet"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 5
status: draft
last_reviewed: 2026-09-19
---

# 2.5 What Does Not Exist Yet
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Six negative claims. A negative claim is only as good as the search behind it, so each one below is checked rather than asserted: against a dated search, and — where one exists — the nearest published result, stated alongside why it falls short of the claim.

{: .note }
**Method.** arXiv title/abstract search per claim, run 19 September 2026. Absence of a result is evidence at the strength arXiv coverage allows — a large preprint archive, not an exhaustive literature census — and is reported as that, not overclaimed.

**No foundation model for multi-carrier urban energy system operation.** A search combining "foundation model" with "multi-carrier", "multi-energy system" or "energy hub" returns exactly one paper: an existing general-purpose time-series foundation model (TabPFN-TS) evaluated zero-shot on district-heating load forecasting.[^spoek2026tabpfndh] That is a genuine result on a real UES carrier, worth citing on its own terms in [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html) — but it is single-carrier, off-the-shelf, and forecasting only: no conversion between carriers, no storage, no dispatch decision. The nearest miss confirms the gap rather than closing it.

**No foundation model for energy system design/planning models.** A search combining "foundation model" with "energy system design", "energy system planning", "sizing optimization" or "capacity planning" returns nothing on-topic. The nearest published work is single-system surrogates: an ANN trained against a full engineering model for energy-hub sizing,[^perera2019mlsurrogate] and a surrogate for EnergyPLAN at country scale[^prina2024energyplan] — both discussed in [§4.9.3](../chapter-4-directions/4-9-3-methods-tier3.html). Neither claims transfer to an unseen system, which is the property that would make either a foundation model rather than a surrogate ([§2.8](2-8-surrogates-vs-fms.html)).

**No benchmark for either.** The nearest published work is at building scale, not system scale: time-series foundation models have been benchmarked on public building and IoT datasets.[^lin2024tsfmbuilding] That benchmark scores single-modality metered data — see [G4](../chapter-6-outlook/6-1-open-gaps.html#g4) for why a multi-carrier benchmark cannot be assembled by pointing a generic one at energy data.

**No agreed representation or interchange format that preserves assumptions alongside structure.** [§3.7](../chapter-3-sim-opt/3-7-schemas-and-standards.html) covers the two schemas that do exist — ESDL and CIM — and why neither is built for this. The absence is not only an ML-side complaint: a 2026 survey from within the multi-energy-systems research community itself, motivated by discussions at the ECOS 2025 conference, concludes that adoption of any standardised case-study description framework "remains fragmented", with existing candidates (IEC 62559, the Open Energy Platform) not built for the purpose.[^vallee2026standardizing]

**No agreed basic element for buildings, and no published treatment of the choice as a research question rather than an implementation detail.** Argued at length, not merely asserted, in [§2.3.2](2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings) and [§2.3.3](2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions).

**No foundation model representing a decision space** — the set of possible interventions on a system — **alongside its state** ([G9](../chapter-6-outlook/6-1-open-gaps.html#g9)). A search combining "foundation model" and "energy" with "decision space", "intervention space" or "retrofit options" returns no result at all — the cleanest of the six searches on this page.

This is the gap the rest of this book is written into: [Chapter 4](../chapter-4-directions/index.html) surveys plausible directions broadly, and [Chapter 5](../chapter-5-case-study/index.html) works through one specific proposal — a foundation model for multi-carrier energy hubs — in depth.

[^spoek2026tabpfndh]: Spoek, B., Ben Hicham, K. K., Derzsi, K. et al. (2026). [Systematic evaluation of TabPFN-TS for zero-shot probabilistic heat load forecasting in district heating networks](https://arxiv.org/abs/2608.20024). arXiv:2608.20024.
[^perera2019mlsurrogate]: Perera, A. T. D., Wickramasinghe, P. U., Nik, V. M., Scartezzini, J.-L. (2019). [Machine learning methods to assist energy system optimization](https://doi.org/10.1016/j.apenergy.2019.03.202). *Applied Energy*, 243, 191–205.
[^prina2024energyplan]: Prina, M. G., Dallapiccola, M., Moser, D., Sparber, W. (2024). [Machine learning as a surrogate model for EnergyPLAN: Speeding up energy system optimization at the country level](https://doi.org/10.1016/j.energy.2024.132735). *Energy*, 307, 132735.
[^lin2024tsfmbuilding]: Lin, X., Prabowo, A., Razzak, I. et al. (2024). [Exploring capabilities of time series foundation models in building analytics](https://arxiv.org/abs/2411.08888). arXiv:2411.08888.
[^vallee2026standardizing]: Vallee, M., Schischke, E., Widl, E. et al. (2026). [Standardizing case study descriptions for multi-energy systems and networks modeling](https://arxiv.org/abs/2606.31343). arXiv:2606.31343.

---
[← Previous: 2.4.5 Geospatial & Weather FMs](2-4-5-geospatial-weather-fms.html) · [Next: 2.6 Self-Supervised Pretraining, Fine-Tuning, Scaling Laws →](2-6-scaling-laws.html)
