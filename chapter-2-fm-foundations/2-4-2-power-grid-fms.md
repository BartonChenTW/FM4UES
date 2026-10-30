---
title: "2.4.2 Power-Grid FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 2
status: draft
last_reviewed: 2026-10-29
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
- **[LUMINA](../appendices/d-model-index.html#lumina)**, from Argonne National Laboratory with Emory University and Sogang University, is a controlled study of how to build such a model rather than one released model. It compares eight graph-network architectures on [OPFData](#related-tooling) grids of 30 to 118 buses and draws design principles for constrained "scientific foundation models". Pretraining on several grids together transferred to an unseen grid better than training on one, and heterogeneous networks, which give buses, generators and loads their own types, held up better than homogeneous ones. Starting from a pretrained model cut the training needed on a new grid by 48.8% for the 118-bus case and by 83.6% for the 500-bus case. A training loss that penalises constraint violations (an augmented Lagrangian) cut violations on unseen grids by 3 to 80 times compared with plain squared error, at similar accuracy. Errors concentrate at high load and at highly connected buses. The limits: the grids are standard test cases of at most 500 buses for adaptation, no feasibility is guaranteed, the authors use "foundation model" in a narrow sense (pretrained across operating conditions and several grids), and the paper calls its code open source but gives no link.[^li2026lumina]
- **Heterogeneous graph foundation models** come from Oak Ridge National Laboratory with two of the LUMINA authors at Argonne. The study trains them on about three million grid graphs from ten benchmark cases of 14 to 13,659 buses, on up to 1,024 nodes of the Frontier supercomputer, compares six graph-network families and adapts them to downstream tasks such as predicting voltages after a single outage.[^lupopasini2026heterogfm]
- **Distillation** shrinks a 20-million-parameter grid foundation model 32-fold so it can run at the edge, next to the measurement, within one synchrophasor reporting frame.[^sanduleac2026gridfmdistil]

**Announced, not yet published: DynaGridFM.** In October 2026 GE Vernova Advanced Research announced a two-year, $3.43 million project, funded by the US agency ARPA-E under its Vision OPEN 2024 programme, with GE Vernova Grid Software, Pacific Northwest National Laboratory and Georgia Tech. It aims at a multi-task model that looks ahead over several operating intervals on transmission grids with AC and DC links and many inverter-based resources, flags likely voltage violations and stability risks, and recommends actions that GPU-based grid optimisers then check. That would make it the first grid model here aimed at dynamics and stability rather than power flow. No paper, data, architecture or results had been published by 29 October 2026, so it is not in [Appendix D](../appendices/d-model-index.html).[^gevernova2026dynagridfm]

One caution carries over from earlier learning-to-optimise work: on two years of real operating data from Uruguay's grid, learned dispatch models showed a significant increase in prediction error compared with synthetic inputs.[^boero2025orpd] Results on benchmark grids do not yet show performance in real operation.

## Trained on a real national grid: RTE and EnerGNN

The models above are trained on benchmark or synthetic grids. RTE (Réseau de Transport d'Électricité), the French transmission system operator, works from the other end: its R&D department, with the University of Liège, trains graph networks on the operating record of its own grid. The code is open source as **EnerGNN**, a JAX library under the MPL-2.0 licence, which became an LF Energy Sandbox project in September 2026.[^energnn2026]

- **Representation.** Every component of the grid is a hyper-edge attached to one, two or three connection points, and several components can share the same points. In the voltage-control work there are 17 classes, from buses, lines and transformers to shunts and the controllers that act on them. RTE calls this a hyper heterogeneous multi graph (H2MG). It was introduced with a companion graph network on a 60-bus Nordic test case. There, a voltage-control policy trained on a reduced variant of the grid transferred badly to the standard one (35% of operating conditions left with a violation, against 5.2% for a policy trained on the standard grid), while one policy trained on all variants together matched each specialist.[^donon2024h2mgnode]
- **The full French grid.** The same architecture was trained without labels, by trial and error against RTE's power-flow simulator, on 149,249 day-ahead forecasts of the 63–400 kV grid (up to 7,643 buses) from September to November 2024. On forecasts from the second half of December it cut the mean number of voltage violations per forecast from 38.8 to 26.6, with no change in branch overflows or losses. The baseline is a tuned uniform setpoint offset, because no other method runs at this scale. The simulator failed to converge on 3.5% of forecasts after the network's actions (1.3% for the baseline), and training took five days on one GPU without covering the whole training set. The abstract describes the training data as one year of forecasts; the dataset section gives three months.[^donon2026tvc]
- **Switching decisions.** On a 12-substation test case, the approach raises exchange capacity between two areas by 10.2% in about 100 ms per batch of eight cases, against 15.2% for a [MILP](../appendices/a-glossary.html#milp) solver that regularly hits its 10-minute limit.[^martinez2026osr] A contingency-screening model trained on one year of French snapshots is reported to flag 99% of risky outages and 86% of non-risky ones correctly, in a presentation rather than a paper.[^donon2026energnnlfe]

**How it bears on these notes.** This is the closest of the work cited here to what the Uruguay caution above asks for: graph networks trained and tested on a national grid's real operating record, with outages, split buses and renamed equipment as they actually occur. It is not a [foundation model](../appendices/a-glossary.html#foundation-model). Each use case trains its own network from scratch, no trained weights are released, and no model is tested on a grid other than the one it was trained on. Whether one H2MG encoder pretrained across RTE's tasks would beat per-task training has not been reported. Two points still carry over. The H2MG makes the [basic element](../appendices/a-glossary.html#basic-element) ([§2.3](2-3-choosing-a-basic-element.html)) the device rather than the bus, which is the form a multi-carrier network needs, since a CHP unit takes gas and delivers both electricity and heat ([§4.7.2](../chapter-4-directions/4-7-2-methods-tier2.html#architecture-family-graph-neural-networks)). And RTE has released the topology of its grid as data (RTE7000, under [Related tooling](#related-tooling) below).

## The demand side has moved too — and shows the gap precisely

The same domain-specific turn is visible on the metering side. **[EnergyFM](../appendices/d-model-index.html#energyfm)** is a family of energy-domain time-series foundation models pretrained on 1.26 billion hourly smart-meter readings from 76,217 buildings, and evaluated across forecasting, anomaly detection and appliance classification.[^arjunan2026energyfm] It is surveyed with the other demand-side models in [§2.4.5](2-4-5-load-forecasting-fms.html). That combination — large-scale pretraining on real energy data, then transfer to several distinct downstream tasks — is the foundation-model pattern proper ([§2.1](2-1-what-defines-an-fm.html)), not a surrogate with an FM label ([§2.1](2-1-what-defines-an-fm.html#surrogates-vs-fms)).

**It is also the clearest available statement of what is still missing.** EnergyFM's basic element is a meter time series: one channel, one building, electricity only. It does not represent conversion between carriers, storage state, network topology, or the discrete design decisions that define a multi-carrier system ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)). So the demand side and the grid side each now have a working domain FM built on an element that suits them — and the multi-carrier layer between them, which is where urban energy systems actually live, still has neither an agreed element nor a corpus. That gap is the subject of [Chapter 5](../chapter-5-case-study/index.html), and the reason [§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields) ranks the hub FM as the least tractable of the candidates rather than the most obvious next step.

## Related tooling

- **gridfm-datakit** — a Python library for scalable and realistic power flow and OPF data generation, supporting FM pretraining at scale.[^puech2025gridfmdatakit]
- **PowerGraph** — a power grid benchmark dataset for graph neural network classification and cascading-failure tasks.[^varbella2024powergraph]
- **PGLib-OPF** — the curated AC-OPF test-case library that GridFM-style benchmarks build on.[^babaeinejadsarookolaee2019pglib]
- **OPFData** — Google DeepMind's solved AC-OPF problems: 300,000 per grid for PGLib-OPF grids of up to 13,659 buses, each with a fixed-topology set and an N-1 set in which one generator or branch is dropped. LUMINA trains on it.[^lovett2024opfdata]
- **RTE7000** — RTE's French transmission grid (63–400 kV) in full substation detail, one snapshot every five minutes from 2021 to 2023, with element identifiers kept consistent over time. It has no power flows or injections, so it records how a real grid's topology varies, not its operating states.[^rte2025rte7000]

[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.
[^gevernova2026dynagridfm]: GE Vernova (2026). [Enabling rapid, reliable, proactive decision-making for transmission grids](https://www.gevernova.com/news/articles/enabling-rapid-reliable-proactive-decision-making-transmission-grids). News article, 19 October 2026.
[^puech2025gridfmdatakit]: Puech, A., Mazzonelli, M., Cintas, C. et al. (2025). [gridfm-datakit-v1: A Python library for scalable and realistic power flow and OPF data generation](https://arxiv.org/abs/2512.14658). arXiv:2512.14658.
[^varbella2024powergraph]: Varbella, A., Amara, K., Gjorgiev, B. et al. (2024). [PowerGraph: A power grid benchmark dataset for graph neural networks](https://doi.org/10.6084/m9.figshare.22820534). NeurIPS 2024, Datasets and Benchmarks Track.
[^babaeinejadsarookolaee2019pglib]: Babaeinejadsarookolaee, S., Birchfield, A., Christie, R. D. et al. (2019). [The power grid library for benchmarking AC optimal power flow algorithms](https://arxiv.org/abs/1908.02788). arXiv:1908.02788.
[^liu2026scalingopf]: Liu, X., He, X., Chen, Y. (2026). [Scaling laws of machine learning for optimal power flow](https://arxiv.org/abs/2601.02706). arXiv:2601.02706.
[^liu2025multitask]: Liu, S., Dong, L., Tian, C., Xie, L. (2025). [Unlocking multi-task electric energy system intelligence: Data scaling laws and performance with limited fine-tuning](https://arxiv.org/abs/2503.20040). arXiv:2503.20040.
[^arjunan2026energyfm]: Arjunan, P., Srivastava, N., Kumar, K. et al. (2026). [EnergyFM: Pretrained models for energy meter data analytics](https://doi.org/10.1145/3744255.3798119). *e-Energy '26*, 556–568.
[^bhan2026gridsfm]: Bhan, L., Yang, W., Capetz, M. et al. (2026). [GridSFM: A Foundation Model for Solving AC Optimal Power Flow](https://arxiv.org/abs/2609.30173). arXiv:2609.30173.
[^puech2026genco]: Puech, A., Mazzonelli, M., Govindasamy, T. R. et al. (2026). [GENCO - A Unified Neural Solver Embedded in a Development Framework for Steady-State Grid Analysis](https://arxiv.org/abs/2608.09921). arXiv:2608.09921.
[^li2026lumina]: Li, Y., Memon, Z., Jin, H. et al. (2026). [LUMINA: Foundation Models for Topology Transferable ACOPF](https://arxiv.org/abs/2603.04300). *ICLR 2026 Workshop on Foundation Models for Science* (poster). arXiv:2603.04300. Transfer results in Tables 1 and 3, fine-tuning in Table 2, stress tests in Section 3.5.
[^lupopasini2026heterogfm]: Lupo Pasini, M., Li, Y., Kim, K. et al. (2026). [Scalable Heterogeneous Graph Foundation Models for Data-Driven Optimal Power Flow in Smart Grids](https://arxiv.org/abs/2605.23194). arXiv:2605.23194.
[^sanduleac2026gridfmdistil]: Sănduleac, V. A., Puthanpurayil, S. R. R., Khan, N. et al. (2026). [Physics-Aware Distillation of a Grid Foundation Model for Real-Time Edge Inference](https://arxiv.org/abs/2610.21833). arXiv:2610.21833.
[^boero2025orpd]: Boero, I., Diaz, S., Vázquez, T. et al. (2025). [Learning to Optimally Dispatch Power: Performance on a Nation-Wide Real-World Dataset](https://doi.org/10.1109/ICPRS66293.2025.11302858). *ICPRS 2025*, 1–7. arXiv:2505.24505.
[^energnn2026]: Committers of EnerGNN (2026). [EnerGNN: A Graph Neural Network library for real-life energy networks](https://github.com/energnn/energnn). Open-source software, MPL-2.0. Listed as a Sandbox-stage project on the [LF Energy project page](https://lfenergy.org/projects/energnn/).
[^donon2024h2mgnode]: Donon, B., Cubélier, F., Karangelos, E. et al. (2024). [Topology-aware reinforcement learning for tertiary voltage control](https://doi.org/10.1016/j.epsr.2024.110658). *Electric Power Systems Research*, 234, 110658 (PSCC 2024). Transfer results in Table I.
[^donon2026tvc]: Donon, B., Jamgotchian, G., Kulesza, H., Wehenkel, L. (2026). [Self-supervised graph neural networks for full-scale tertiary voltage control](https://arxiv.org/abs/2604.03087). arXiv:2604.03087. Datasets in Section III-A, results in Table III.
[^martinez2026osr]: Martinez, A., Donon, B., Wehenkel, L., Karangelos, E. (2026). [Self-supervised graph neural networks for optimal substation reconfiguration](https://arxiv.org/abs/2603.23401). arXiv:2603.23401. Results in Table I.
[^donon2026energnnlfe]: Donon, B. (2026). [EnerGNN: A graph neural network library for real-life complex energy systems](https://tac.lfenergy.org/meetings/2026/2026-04-14/EnerGNN_LFE_TAC.pdf). Presentation to the LF Energy Technical Advisory Council, 14 April 2026. Slide "Contingency Screening"; not peer-reviewed.
[^lovett2024opfdata]: Lovett, S., Zgubic, M., Liguori, S. et al. (2024). [OPFData: Large-scale datasets for AC optimal power flow with topological perturbations](https://arxiv.org/abs/2406.07234). arXiv:2406.07234. Datasets distributed as JSON in a public Google Cloud bucket.
[^rte2025rte7000]: RTE (2025). [D-GITT RTE7000 nodes dataset, 2021](https://huggingface.co/datasets/OpenSynth/D-GITT-RTE7000-2021). Hugging Face, with companion records for 2022 and 2023. Node-breaker snapshots in PowSyBl XIIDM format. The dataset page lists the licence as CDLA-Permissive-2.0; check it before reuse.

---
[← Previous: 2.4.1 Time-Series FMs](2-4-1-time-series-fms.html) · [Back to Chapter 2](index.html) · [Next: 2.4.3 Weather, Geospatial & Generation FMs →](2-4-3-clean-energy-forecasting-fms.html)
