---
title: "1.4 Directions the FM Field Is Moving"
parent: Chapter 1 — Background
nav_order: 4
status: draft
last_reviewed: 2026-09-11
---

# 1.4 Directions the Foundation Model Field Is Moving
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

- **Time series has matured.** By 2026 the major families — Google [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5),[^google2025timesfm25] Amazon [Chronos-2](../appendices/d-model-index.html#chronos-2),[^ansari2025chronos2] Salesforce [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0),[^liu2025moirai2] Datadog [Toto 2.0](../appendices/d-model-index.html#toto-2-0),[^khwaja2026toto2] IBM's TTM (released under IBM's Granite name), Nixtla [TimeGPT-2](../appendices/d-model-index.html#timegpt-2),[^nixtla2025timegpt2] NVIDIA [NV-Tesseract](../appendices/d-model-index.html#nv-tesseract) (since renamed Kumo-TS)[^nvidia2025nvtesseract] — have all been refreshed. They have not converged on one architecture. [TimesFM](../appendices/d-model-index.html#timesfm) and Moirai 2.0 are decoder-only [transformers](../appendices/a-glossary.html#transformer),[^das2024timesfm] [^liu2025moirai2] Chronos-2 is encoder-only,[^ansari2025chronos2] [TimeGPT](../appendices/d-model-index.html#timegpt) is an encoder-decoder transformer,[^garza2023timegpt] TTM is not a transformer at all but an MLP-mixer,[^ekambaram2024ttm] and [TiRex](../appendices/d-model-index.html#tirex) is a recurrent model.[^auer2025tirex] The practical question has shifted from "how do I train a model" to "which pretrained model do I select." See [§2.4.1](../chapter-2-fm-foundations/2-4-1-time-series-fms.html).
- **Scaling laws now hold for time series.** Toto 2.0 is reported as the first time-series model where classic scaling behaviour (more data and parameters → predictably better performance) has been demonstrated across a 625× range of model size.[^khwaja2026toto2] This matters because scaling laws are what justified the FM bet in language in the first place — see [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html).
- **[Multimodality](../appendices/a-glossary.html#multimodality) is becoming the default**, not a special case. [Cross-attending](../appendices/a-glossary.html#cross-attention) heterogeneous inputs is now standard design (explained with an energy example in [§2.7](../chapter-2-fm-foundations/2-7-architectures.html#multimodal-models)).
- **Physics-informed / hybrid FMs** are emerging wherever domain equations are known. [GridFM-v0](../appendices/d-model-index.html#gridfm)'s masked-reconstruction-plus-power-flow-loss is the archetype in power systems — see [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html).
- **Efficiency is a parallel axis to scale.** IBM's [TTM](../appendices/d-model-index.html#ttm) family runs at 1–5 M parameters and is CPU-capable[^ekambaram2024ttm] — the opposite bet from billion-parameter LLMs.
- **Synthetic and simulation-grounded pretraining** is rising wherever real annotated data is scarce or privacy-constrained.
- **Graph FMs are a genuinely new frontier**, less mature than sequence FMs. GridFM-v0 sits at this edge.

[^ekambaram2024ttm]: Ekambaram, V., Jati, A., Dayama, P. et al. (2024). [Tiny Time Mixers (TTMs): Fast pre-trained models for enhanced zero/few-shot forecasting](https://arxiv.org/abs/2401.03955). NeurIPS 2024. arXiv:2401.03955.
[^ansari2025chronos2]: Ansari, A. F., Shchur, O., Küken, J. et al. (2025). [Chronos-2: From univariate to universal forecasting](https://arxiv.org/abs/2510.15821). arXiv:2510.15821.
[^liu2025moirai2]: Liu, C., Aksu, T., Liu, J. et al. (2025). [Moirai 2.0: When less is more for time series forecasting](https://arxiv.org/abs/2511.11698). arXiv:2511.11698.
[^google2025timesfm25]: Google Research (2025). [TimesFM 2.5 (timesfm-2.5-200m)](https://huggingface.co/google/timesfm-2.5-200m-pytorch). Hugging Face model card; no paper. Released September 2025.
[^nixtla2025timegpt2]: Nixtla (2025). [TimeGPT-2: Next generation time series model](https://www.nixtla.io/blog/timegpt-2-announcement). Announcement, October 2025; no paper or public architecture details.
[^nvidia2025nvtesseract]: NVIDIA (2025). [New NVIDIA NV-Tesseract time series models advance dataset processing and anomaly detection](https://developer.nvidia.com/blog/new-nvidia-nv-tesseract-time-series-models-advance-dataset-processing-and-anomaly-detection). NVIDIA Technical Blog, 6 May 2025; no paper. The project is now [Kumo-TS](https://github.com/NVIDIA/Kumo-TS).
[^das2024timesfm]: Das, A., Kong, W., Sen, R., Zhou, Y. (2024). [A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688). ICML 2024. arXiv:2310.10688.
[^auer2025tirex]: Auer, A., Podest, P., Klotz, D. et al. (2025). [TiRex: Zero-shot forecasting across long and short horizons with enhanced in-context learning](https://arxiv.org/abs/2505.23719). NeurIPS 2025. arXiv:2505.23719.
[^garza2023timegpt]: Garza, A., Challu, C., Mergenthaler-Canseco, M. (2023). [TimeGPT-1](https://arxiv.org/abs/2310.03589). arXiv:2310.03589.
[^khwaja2026toto2]: Khwaja, E., Lettieri, C., Woo, G. et al. (2026). [Toto 2.0: Time series forecasting enters the scaling era](https://arxiv.org/abs/2605.20119). arXiv:2605.20119.

---
[← Previous: 1.3 The FM Landscape by Domain](1-3-fm-landscape-by-domain.html) · [Next: 1.5 Why UES, Why Now →](1-5-why-ues-why-now.html)
