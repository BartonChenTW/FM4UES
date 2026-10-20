---
title: "2.4.2 Power-Grid FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 2
status: draft
last_reviewed: 2026-10-20
---

# 2.4.2 Power-Grid Foundation Models (First Released Models, Moving Fast)
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

The power-systems community has already made the move this document is about. Grid foundation models for benchmarking AC-OPF [surrogate](../appendices/a-glossary.html#surrogate) learning now exist,[^hamann2024foundation] alongside work on scaling laws of machine learning for optimal power flow,[^liu2026scalingopf] and work on data scaling laws for multi-task electric energy system intelligence with limited [fine-tuning](../appendices/a-glossary.html#fine-tuning).[^liu2025multitask]

**This is the single most important reference point.** It means (a) the concept is validated, and (b) the analogous work for urban *multi-carrier* systems is conspicuously absent — which is the gap these notes' [case study in Chapter 5](../chapter-5-case-study/index.html) addresses.

{: .note }
Read together with [§2.3.1](2-3-choosing-a-basic-element.html#231-the-criterion): what makes this domain tractable is not that power systems had more data, but that the bus supplies a [basic element](../appendices/a-glossary.html#basic-element) satisfying all four requirements. Sub-domains without such an element should not expect the same recipe to work.

## The first released pretrained models (2026)

During 2026 the idea became working, released software. Several pretrained models now solve power flow or optimal power flow on grids they were not trained on:

- **[GridSFM](../appendices/d-model-index.html#gridsfm)** is a 15-million-parameter graph network pretrained on 54 grid topologies of 500 to 4,000 buses. [Zero-shot](../appendices/a-glossary.html#zero-shot), it reaches a 2.45% generation-cost error on a held-out 10,000-bus case, and with only 100 solved instances it adapts to unseen grids of up to 10,000 buses. Models, data and code are released.[^bhan2026gridsfm]
- **[GENCO](../appendices/d-model-index.html#genco)** handles power flow, optimal power flow and state estimation in one architecture, and was tested on real Hydro-Québec SCADA data. It reports up to 30× speedups over Newton-Raphson for power flow and up to 85× over the IPOPT solver for optimal power flow, and ships with an open development framework and datasets of millions of scenarios.[^puech2026genco]
- **[LUMINA](../appendices/d-model-index.html#lumina)** draws design principles for constrained "scientific foundation models" from controlled experiments on AC optimal power flow: physics-invariant representations that still respect each system's constraints, accuracy without sacrificing constraint satisfaction, and reliability in high-impact operating regimes.[^li2026lumina]
- **Heterogeneous graph foundation models** trained on about three million grid graphs from ten benchmark cases of 14 to 13,659 buses, on up to 1,024 nodes of the Frontier supercomputer, compare six graph-network families and adapt to downstream tasks such as predicting voltages after a single outage.[^lupopasini2026heterogfm]
- **Distillation** shrinks a 20-million-parameter grid foundation model 32-fold so it can run at the edge, next to the measurement, within one synchrophasor reporting frame.[^sanduleac2026gridfmdistil]

One caution carries over from earlier learning-to-optimise work: on two years of real operating data from Uruguay's grid, learned dispatch models showed a significant increase in prediction error compared with synthetic inputs.[^boero2025orpd] Results on benchmark grids do not yet show performance in real operation.

## The demand side has moved too — and shows the gap precisely

The same domain-specific turn is visible on the metering side. **[EnergyFM](../appendices/d-model-index.html#energyfm)** is a family of energy-domain time-series foundation models pretrained on 1.26 billion hourly smart-meter readings from 76,217 buildings, and evaluated across forecasting, anomaly detection and appliance classification.[^arjunan2026energyfm] It is surveyed with the other demand-side models in [§2.4.5](2-4-5-load-forecasting-fms.html). That combination — large-scale pretraining on real energy data, then transfer to several distinct downstream tasks — is the foundation-model pattern proper ([§2.1](2-1-what-defines-an-fm.html)), not a surrogate with an FM label ([§2.1](2-1-what-defines-an-fm.html#surrogates-vs-fms)).

**It is also the clearest available statement of what is still missing.** EnergyFM's basic element is a meter time series: one channel, one building, electricity only. It does not represent conversion between carriers, storage state, network topology, or the discrete design decisions that define a multi-carrier system ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)). So the demand side and the grid side each now have a working domain FM built on an element that suits them — and the multi-carrier layer between them, which is where urban energy systems actually live, still has neither an agreed element nor a corpus. That gap is the subject of [Chapter 5](../chapter-5-case-study/index.html), and the reason [§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields) ranks the hub FM as the least tractable of the candidates rather than the most obvious next step.

## Related tooling

- **gridfm-datakit** — a Python library for scalable and realistic power flow and OPF data generation, supporting FM pretraining at scale.[^puech2025gridfmdatakit]
- **PowerGraph** — a power grid benchmark dataset for graph neural network classification and cascading-failure tasks.[^varbella2024powergraph]
- **PGLib-OPF** — the curated AC-OPF test-case library that GridFM-style benchmarks build on.[^babaeinejadsarookolaee2019pglib]

[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.
[^puech2025gridfmdatakit]: Puech, A., Mazzonelli, M., Cintas, C. et al. (2025). [gridfm-datakit-v1: A Python library for scalable and realistic power flow and OPF data generation](https://arxiv.org/abs/2512.14658). arXiv:2512.14658.
[^varbella2024powergraph]: Varbella, A., Amara, K., Gjorgiev, B. et al. (2024). [PowerGraph: A power grid benchmark dataset for graph neural networks](https://doi.org/10.6084/m9.figshare.22820534). NeurIPS 2024, Datasets and Benchmarks Track.
[^babaeinejadsarookolaee2019pglib]: Babaeinejadsarookolaee, S., Birchfield, A., Christie, R. D. et al. (2019). [The power grid library for benchmarking AC optimal power flow algorithms](https://arxiv.org/abs/1908.02788). arXiv:1908.02788.
[^liu2026scalingopf]: Liu, X., He, X., Chen, Y. (2026). [Scaling laws of machine learning for optimal power flow](https://arxiv.org/abs/2601.02706). arXiv:2601.02706.
[^liu2025multitask]: Liu, S., Dong, L., Tian, C., Xie, L. (2025). [Unlocking multi-task electric energy system intelligence: Data scaling laws and performance with limited fine-tuning](https://arxiv.org/abs/2503.20040). arXiv:2503.20040.
[^arjunan2026energyfm]: Arjunan, P., Srivastava, N., Kumar, K. et al. (2026). [EnergyFM: Pretrained models for energy meter data analytics](https://doi.org/10.1145/3744255.3798119). *e-Energy '26*, 556–568.
[^bhan2026gridsfm]: Bhan, L., Yang, W., Capetz, M. et al. (2026). [GridSFM: A Foundation Model for Solving AC Optimal Power Flow](https://arxiv.org/abs/2609.30173). arXiv:2609.30173.
[^puech2026genco]: Puech, A., Mazzonelli, M., Govindasamy, T. R. et al. (2026). [GENCO - A Unified Neural Solver Embedded in a Development Framework for Steady-State Grid Analysis](https://arxiv.org/abs/2608.09921). arXiv:2608.09921.
[^li2026lumina]: Li, Y., Memon, Z., Jin, H. et al. (2026). [LUMINA: Foundation Models for Topology Transferable ACOPF](https://arxiv.org/abs/2603.04300). arXiv:2603.04300.
[^lupopasini2026heterogfm]: Lupo Pasini, M., Li, Y., Kim, K. et al. (2026). [Scalable Heterogeneous Graph Foundation Models for Data-Driven Optimal Power Flow in Smart Grids](https://arxiv.org/abs/2605.23194). arXiv:2605.23194.
[^sanduleac2026gridfmdistil]: Sănduleac, V. A., Puthanpurayil, S. R. R., Khan, N. et al. (2026). [Physics-Aware Distillation of a Grid Foundation Model for Real-Time Edge Inference](https://arxiv.org/abs/2610.21833). arXiv:2610.21833.
[^boero2025orpd]: Boero, I., Diaz, S., Vázquez, T. et al. (2025). [Learning to Optimally Dispatch Power: Performance on a Nation-Wide Real-World Dataset](https://doi.org/10.1109/ICPRS66293.2025.11302858). *ICPRS 2025*, 1–7. arXiv:2505.24505.

---
[← Previous: 2.4.1 Time-Series FMs](2-4-1-time-series-fms.html) · [Back to Chapter 2](index.html) · [Next: 2.4.3 Weather, Geospatial & Generation FMs →](2-4-3-clean-energy-forecasting-fms.html)
