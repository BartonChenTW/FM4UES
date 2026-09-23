---
title: "1.3 The FM Landscape Today, by Domain"
parent: Chapter 1 — Background
nav_order: 3
status: draft
last_reviewed: 2026-09-11
---

# 1.3 The Foundation Model Landscape Today, by Domain
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

The term and the underlying pattern were named and surveyed at length by the Stanford Center for Research on Foundation Models — the reference point for the "broad pretraining, transfer, multi-task" definition used throughout this book (see [§2.1](../chapter-2-fm-foundations/2-1-what-defines-an-fm.html)).[^bommasani2021opportunities] The table below is this book's own snapshot of where that pattern has and hasn't landed, organised by domain rather than by architecture. The "what they learn" column describes the models named in the row to its left — its citation is theirs, not a separate claim; rows with no citation (Language, Robotics/embodied) name a class of model rather than one specific paper, and the description is a characterisation of the class rather than a reported result.

| Domain | Representative models | What they learn |
| :--- | :--- | :--- |
| Language | GPT-5-class, Gemini, Claude, Llama | Sequences of text tokens |
| Vision | ViT (Vision Transformer), SAM/SAM2 (Segment Anything Model),[^kirillov2023sam] DINO (self-**DI**stillation with **NO** labels)[^caron2021dino] | Sequences of image patches |
| Multimodal | Unified generation-and-understanding models, e.g. Janus[^wu2024janus] | Cross-modal alignment across text, image, audio |
| Weather / climate | GraphCast,[^lam2023graphcast] FengWu,[^chen2023fengwu] Aurora[^bodnar2025aurora] | Physical fields on a spatiotemporal grid |
| Geospatial / remote sensing | Prithvi,[^jakubik2023prithvi] ScaleMAE,[^reed2023scalemae] Granite-GFM | Satellite pixels and patches over space and time |
| Time series | TimesFM,[^das2024timesfm] Chronos,[^ansari2024chronos] Moirai,[^woo2024moirai] TTM (Tiny Time Mixers),[^ekambaram2024ttm] Toto,[^cohen2025toto] TimeGPT[^garza2023timegpt] | Numeric sequences |
| Graph-structured systems | Emerging graph FMs, GridFM-v0[^hamann2024foundation] | Node/edge-structured data |
| Robotics / embodied | Vision-language-action models | Vision, language, touch, force, proprioception |

Granite-GFM is built on the Prithvi-SWIN-L Earth observation foundation model and uses a Swin Transformer backbone to estimate land surface temperature at 30 m resolution and hourly frequency for arbitrary cities.[^szwarcman2024prithvieo2]

{: .warning }
**The field moves fast.** Publication counts on LLM-and-energy alone went from roughly 1 (2022) to 13 (2023) to 128 (2024) to 464 (2025), with 348 already indexed in the first half of 2026 — a Scopus title/abstract/keyword search combining LLM and power-system terms, run 11 July 2026.[^naeem2026llmpower] Re-check anything in this table before it is used to justify a novelty claim.

Two families are directly relevant to this book and get dedicated treatment: [time-series FMs](../chapter-2-fm-foundations/2-4-1-time-series-fms.html) and [power-grid FMs](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html), in [§2.4](../chapter-2-fm-foundations/index.html).

[^szwarcman2024prithvieo2]: Szwarcman, D., Roy, S., Fraccaro, P. et al. (2024). [Prithvi-EO-2.0: A versatile multi-temporal foundation model for Earth observation applications](https://arxiv.org/abs/2412.02732). arXiv:2412.02732.
[^kirillov2023sam]: Kirillov, A., Mintun, E., Ravi, N. et al. (2023). [Segment Anything](https://arxiv.org/abs/2304.02643). *ICCV 2023*. arXiv:2304.02643
[^lam2023graphcast]: Lam, R., Sanchez-Gonzalez, A., Willson, M. et al. (2023). [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336). *Science*, 382(6677), 1416–1421.
[^chen2023fengwu]: Chen, K., Han, T., Gong, J. et al. (2023). [FengWu: Pushing the skillful global medium-range weather forecast beyond 10 days lead](https://arxiv.org/abs/2304.02948). arXiv:2304.02948
[^bodnar2025aurora]: Bodnar, C., Bruinsma, W. P., Lucic, A. et al. (2025). [A foundation model for the Earth system](https://doi.org/10.1038/s41586-025-09005-y). *Nature*, 641, 1180–1187.
[^jakubik2023prithvi]: Jakubik, J., Roy, S., Phillips, C. E. et al. (2023). [Foundation models for generalist geospatial artificial intelligence](https://arxiv.org/abs/2310.18660). arXiv:2310.18660
[^reed2023scalemae]: Reed, C. J., Gupta, R., Li, S. et al. (2023). [Scale-MAE: A scale-aware masked autoencoder for multiscale geospatial representation learning](https://arxiv.org/abs/2212.14532). *ICCV 2023*. arXiv:2212.14532
[^das2024timesfm]: Das, A., Kong, W., Sen, R., Zhou, Y. (2024). [A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688). ICML 2024. arXiv:2310.10688
[^ansari2024chronos]: Ansari, A. F., Stella, L., Turkmen, C. et al. (2024). [Chronos: Learning the language of time series](https://arxiv.org/abs/2403.07815). *Transactions on Machine Learning Research*. arXiv:2403.07815
[^woo2024moirai]: Woo, G., Liu, C., Kumar, A. et al. (2024). [Unified training of universal time series forecasting transformers](https://arxiv.org/abs/2402.02592). ICML 2024. arXiv:2402.02592
[^ekambaram2024ttm]: Ekambaram, V., Jati, A., Dayama, P. et al. (2024). [Tiny Time Mixers (TTMs): Fast pre-trained models for enhanced zero/few-shot forecasting](https://arxiv.org/abs/2401.03955). NeurIPS 2024. arXiv:2401.03955
[^cohen2025toto]: Cohen, B., Khwaja, E., Doubli, Y. et al. (2025). [This time is different: An observability perspective on time series foundation models](https://arxiv.org/abs/2505.14766). arXiv:2505.14766
[^garza2023timegpt]: Garza, A., Challu, C., Mergenthaler-Canseco, M. (2023). [TimeGPT-1](https://arxiv.org/abs/2310.03589). arXiv:2310.03589
[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.
[^naeem2026llmpower]: Naeem, Z., Cirrincione, G., Favuzza, S. et al. (2026). [Large language models in power systems: From grid operations to home energy management](https://doi.org/10.3390/en19163769). *Energies*, 19(16), 3769.
[^caron2021dino]: Caron, M., Touvron, H., Misra, I. et al. (2021). [Emerging properties in self-supervised vision transformers](https://arxiv.org/abs/2104.14294). *ICCV 2021*. arXiv:2104.14294
[^wu2024janus]: Wu, C., Chen, X., Wu, Z. et al. (2024). [Janus: Decoupling visual encoding for unified multimodal understanding and generation](https://arxiv.org/abs/2410.13848). arXiv:2410.13848
[^bommasani2021opportunities]: Bommasani, R., Hudson, D. A., Adeli, E. et al. (2021). [On the opportunities and risks of foundation models](https://arxiv.org/abs/2108.07258). arXiv:2108.07258. The paper that coined "foundation model"; defines it as a model "trained on broad data at scale" and "adaptable to a wide range of downstream tasks" — closely paralleling this book's own three-property definition in [§2.1](../chapter-2-fm-foundations/2-1-what-defines-an-fm.html).

---
[← Previous: 1.2 FMs in One Page](1-2-fms-in-one-page.html) · [Next: 1.4 Directions the Field Is Moving →](1-4-fm-field-directions.html)
