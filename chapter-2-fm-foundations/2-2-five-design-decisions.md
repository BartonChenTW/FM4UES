---
title: "2.2 The Five Design Decisions"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 2
status: draft
last_reviewed: 2026-09-11
---

# 2.2 The Five Design Decisions
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Every foundation model, in any domain, is defined by five choices. Getting these explicit is most of the intellectual work.

## D1 — Unit of observation

What is *one training example*? Language: a token sequence. Vision: a patch grid. Weather: a gridded state at time t.

For energy systems this is genuinely unresolved for planning models, and only obvious for some operational ones. Candidates at system level:

- one timestep of system state
- one (configuration, boundary conditions, trajectory) triple
- one whole model instance
- one modelling decision

{: .note }
Listing candidates is not the same as choosing between them. [§2.3 Choosing a Basic Element](2-3-choosing-a-basic-element.html) supplies a criterion for doing so, and applies it at building level, where the candidates are different and the answer is harder.

## D2 — Tokenisation / encoding

How is a training example turned into something the architecture consumes?

**A useful framing for domain readers:** tokenisation is a discretisation choice. Every simulation begins by deciding what the object is made of — zones, nodes, cells — and that choice fixes what the model can represent, what it must approximate, and how well it carries to a different case. A learned model faces the identical decision. This analogy is the most effective way to explain the problem to a building simulation or energy systems audience, because they have argued about discretisation for decades.

This is where domain-specific difficulty concentrates. Evidence from adjacent fields:

- **Float-heavy data** needs purpose-built handling; GridFM-v0 adopts a specially designed float discretisation-and-tokenisation scheme, adapted from vision-language-action models, so that a transformer can process float-rich grid state alongside text.[^hamann2024foundation]
- **Structured codes** break standard schemes: subword tokenisation optimised for natural language fails to capture the hierarchical and compositional structure of structured medical codes, and dedicated tokenisation recovers measurable performance.[^dwivedi2024unistruct]
- **Multi-domain data** risks structural loss: tokenisation strategies that combine incompatible spatial discretisations risk losing physical adjacency and introducing aliasing effects in attention layers.[^kaselimi2026coupling]
- **Multi-resolution data** needs explicit handling: Moirai pairs a multi-patch-size projection scheme handling minute-to-year-scale data with an any-variate attention mechanism that scales to arbitrary numbers of variables.[^woo2024moirai]

**A representation is not one decision but at least four**, and this framing recurs whenever this book proposes a concrete representation (see [§5.2](../chapter-5-case-study/5-2-representation-problem.html)):

| Family | Atomic unit | Structure | Discrete/continuous | Invariance |
| :--- | :--- | :--- | :--- | :--- |
| LLM | Subword token | 1D sequence position | Discrete, ~50–200 k vocab | None; order is meaning |
| ViT[^dosovitskiy2020vit] / SAM[^kirillov2023sam] | 16×16 patch, linearly projected | 2D grid position | Continuous | Weak translation |
| TimesFM / PatchTST[^nie2023patchtst] / TTM[^ekambaram2024ttm] | Patch of N consecutive values, instance-normalised | 1D position | Continuous | Scale, via normalisation |
| Chronos[^ansari2024chronos] | A quantized value bin | 1D sequence | Discrete codebook | Scale |
| GraphCast[^lam2023graphcast] / Aurora[^bodnar2025aurora] | Grid cell, all variables at all pressure levels | Icosahedral multi-mesh | Continuous | Spherical geometry |
| GridFM-v0[^hamann2024foundation] | A bus carrying (p, q, v, δ) | Graph; lines and transformers as edges | Continuous | Permutation over buses |

## D3 — Architecture

Transformer, graph neural network, neural operator, state-space model, or hybrid. Determined largely by what structure the data has (sequence? graph? function?). See [§2.7](2-7-architectures.html) for what each of these architecture families actually does, aimed at readers without an ML background.

**State-space models** are the one family [§2.7](2-7-architectures.html) does not cover, and they matter here for a specific reason: they process a sequence in time linear in its length rather than quadratic, by carrying a recurrent state instead of attending to every pair of positions.[^gu2022s4] Selective state-space models make that state input-dependent, recovering much of the modelling power attention provides.[^gu2023mamba] The relevance to this domain is the seasonal-storage problem — an 8760-hour year at hourly resolution is long enough that quadratic attention cost is a real constraint (see the timescale table in [§4.9.1](../chapter-4-directions/4-9-1-methods-tier1.html)). **What this does not resolve** is the multi-carrier coupling that motivates cross-variate attention in the first place: a cheaper way to handle length says nothing about how carriers exchange information, so the two decisions have to be made separately.

## D4 — Pretraining objective

Next-step prediction, masked reconstruction, supervised imitation of a solver, or self-supervised contrastive. For simulation surrogates this is usually supervised regression on solver output; for sequence models, next-token or next-patch prediction. See [§2.6](2-6-scaling-laws.html) for what "self-supervised" means in practice.

## D5 — Evaluation

What counts as success, and on what held-out distribution? For physical systems this must include **feasibility and conservation**, not only error.

The reason is that low average error and physical validity are different properties, and a model can have the first without the second. Work on learned AC-OPF proxies makes the gap explicit by reporting constraint violations alongside prediction error, and by training against the problem's Lagrangian dual so that violations are penalised rather than merely measured.[^fioretto2020acopf] Where hard constraints must hold exactly, feasibility can instead be built into the model: a completion-and-correction scheme enforces equality constraints by construction and corrects the remaining inequality violations through the network itself.[^donti2021dc3]

**Neither result removes the evaluation burden — they relocate it.** Both are demonstrated on single-carrier power flow with a fixed constraint set, whereas a multi-carrier hub adds conversion relations, storage continuity across the horizon, and discrete on/off decisions, so "feasible" is a longer list of things to check and some of them are combinatorial. The practical consequence for this book is that a feasibility number is only meaningful alongside the constraint set it was measured against: see the six-metric reporting protocol in [§4.10.3](../chapter-4-directions/4-10-building-it.html) and dimension 4 of [§2.9](2-9-ues-fm-evaluation-criteria.html).

[^dwivedi2024unistruct]: Dwivedi, V. P., Schlegel, V., Liu, A. T. et al. (2024). [Representation Learning of Structured Data for Medical Foundation Models](https://arxiv.org/abs/2410.13351). *NeurIPS 2024 Workshop on Unifying Representations in Neural Models (UniReps)*. arXiv:2410.13351. Introduces the UniStruct model.
[^kaselimi2026coupling]: Kaselimi, M. and Belehaki, A. (2026). [Toward Artificial Intelligence Enabled Earth System Coupling](https://arxiv.org/abs/2604.03289). arXiv:2604.03289.
[^woo2024moirai]: Woo, G., Liu, C., Kumar, A. et al. (2024). [Unified training of universal time series forecasting transformers](https://arxiv.org/abs/2402.02592). ICML 2024. arXiv:2402.02592.
[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.
[^dosovitskiy2020vit]: Dosovitskiy, A., Beyer, L., Kolesnikov, A. et al. (2020). [An image is worth 16x16 words: Transformers for image recognition at scale](https://arxiv.org/abs/2010.11929). arXiv:2010.11929.
[^kirillov2023sam]: Kirillov, A., Mintun, E., Ravi, N. et al. (2023). [Segment Anything](https://arxiv.org/abs/2304.02643). *ICCV 2023*. arXiv:2304.02643.
[^nie2023patchtst]: Nie, Y., Nguyen, N. H., Sinthong, P., Kalagnanam, J. (2023). [A time series is worth 64 words: Long-term forecasting with transformers](https://arxiv.org/abs/2211.14730). ICLR 2023. arXiv:2211.14730.
[^ekambaram2024ttm]: Ekambaram, V., Jati, A., Dayama, P. et al. (2024). [Tiny Time Mixers (TTMs): Fast pre-trained models for enhanced zero/few-shot forecasting](https://arxiv.org/abs/2401.03955). NeurIPS 2024. arXiv:2401.03955.
[^ansari2024chronos]: Ansari, A. F., Stella, L., Turkmen, C. et al. (2024). [Chronos: Learning the language of time series](https://arxiv.org/abs/2403.07815). *Transactions on Machine Learning Research*. arXiv:2403.07815.
[^lam2023graphcast]: Lam, R., Sanchez-Gonzalez, A., Willson, M. et al. (2023). [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336). *Science*, 382(6677), 1416–1421.
[^bodnar2025aurora]: Bodnar, C., Bruinsma, W. P., Lucic, A. et al. (2025). [A foundation model for the Earth system](https://doi.org/10.1038/s41586-025-09005-y). *Nature*, 641, 1180–1187.
[^gu2022s4]: Gu, A., Goel, K., Ré, C. (2022). [Efficiently modeling long sequences with structured state spaces](https://arxiv.org/abs/2111.00396). ICLR 2022. arXiv:2111.00396.
[^gu2023mamba]: Gu, A., Dao, T. (2023). [Mamba: Linear-time sequence modeling with selective state spaces](https://arxiv.org/abs/2312.00752). arXiv:2312.00752.
[^fioretto2020acopf]: Fioretto, F., Mak, T. W. K., Van Hentenryck, P. (2020). [Predicting AC optimal power flows: Combining deep learning and Lagrangian dual methods](https://doi.org/10.1609/aaai.v34i01.5403). *AAAI 2020*, 630–637.
[^donti2021dc3]: Donti, P. L., Rolnick, D., Kolter, J. Z. (2021). [DC3: A learning method for optimization with hard constraints](https://arxiv.org/abs/2104.12225). ICLR 2021. arXiv:2104.12225.

---
[← Previous: 2.1 What Defines an FM](2-1-what-defines-an-fm.html) · [Next: 2.3 Choosing a Basic Element →](2-3-choosing-a-basic-element.html)
