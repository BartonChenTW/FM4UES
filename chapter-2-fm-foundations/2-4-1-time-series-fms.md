---
title: "2.4.1 Time-Series FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 1
status: draft
last_reviewed: 2026-09-11
---

# 2.4.1 Time-Series Foundation Models (Mature)
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

A well-populated field with production-grade options. The current generation includes [Chronos-2](../appendices/d-model-index.html#chronos-2),[^ansari2025chronos2] [Moirai 2.0](../appendices/d-model-index.html#moirai-2-0),[^liu2025moirai2] [TimesFM 2.5](../appendices/d-model-index.html#timesfm-2-5), [TiRex](../appendices/d-model-index.html#tirex),[^auer2025tirex] [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts),[^hoo2025tabpfnts] [Lag-Llama](../appendices/d-model-index.html#lag-llama),[^rasul2023laglama] [Time-MoE](../appendices/d-model-index.html#time-moe),[^shi2024timemoe] [Toto](../appendices/d-model-index.html#toto),[^cohen2025toto] [MOMENT](../appendices/d-model-index.html#moment),[^goswami2024moment] [Timer](../appendices/d-model-index.html#timer)[^liu2024timer] and [TTM](../appendices/d-model-index.html#ttm).[^ekambaram2024ttm]

Architecturally distinct approaches worth knowing:

- **[Chronos](../appendices/d-model-index.html#chronos)** converts continuous values into discrete tokens via uniform binning and forecasts recursively with a T5 encoder–decoder;[^ansari2024chronos] **Chronos-2** adds multivariate support and covariate handling, using time and group attention layers to exchange information across series, and is pretrained on synthetic multivariate data.[^ansari2025chronos2]
- **[Moirai](../appendices/d-model-index.html#moirai)** handles an arbitrary number of input series through an any-variate attention mechanism, with mixture-distribution outputs for uncertainty;[^woo2024moirai] **Moirai 2.0** shows smaller, better-trained models can match larger predecessors via multi-token prediction and improved tokenisation.[^liu2025moirai2]
- **[TimesFM](../appendices/d-model-index.html#timesfm)** is a patch-based decoder-only model;[^das2024timesfm] TimesFM-2.0 extends context to 2048 points.
- **TiRex** is a decoder-only model built on the xLSTM recurrent architecture rather than a transformer, marking future timesteps as masked and letting the recurrent hidden state carry forward both point forecast and uncertainty.[^auer2025tirex]
- **Time-MoE** scales a decoder-only architecture to 2.4B parameters using a sparse mixture-of-experts design that activates only a subset of the network per prediction, pretrained on a 300-billion-point corpus spanning nine domains.[^shi2024timemoe]
- **MOMENT** and **Timer** are both GPT-style, patch/token-based pretrained models aimed at a broader set of time-series tasks (forecasting, imputation, anomaly detection, classification) rather than forecasting alone.[^goswami2024moment][^liu2024timer]
- **TabPFN-TS** is a tabular foundation model pretrained on millions of synthetic regression tasks, adapted to time series by combining lightweight temporal featurisation with the pretrained TabPFN-v2,[^hoo2025tabpfnts] and is notable as the only one in some benchmarks that additionally incorporates **static metadata** (e.g. peak power, tilt, azimuth for a PV plant). See [§2.4.4](2-4-4-tabular-fms.html) for the underlying model family, which is a distinct representational proposition rather than just another TSFM.

**Covariate handling is the key differentiator and it is uneven.** The first generation lacked native covariate handling except Moirai. TiRex and Moirai 2.0 remain univariate with respect to covariates; TimesFM 2.5 combines a pretrained univariate backbone with an auxiliary linear regressor on covariates estimated at inference; Chronos-2 and TabPFN-TS model target and covariates jointly.

**Known limitations to design around:**

- **Long-horizon degradation.** All models degrade beyond their trained maximum prediction length.
- **Covariate usage is under-verified.** Recent work notes that benchmark results offer limited insight into actual covariate usage, and finds that TabPFN-TS captures simple, deliberately-constructed covariate–target relationships more reliably than Chronos-2 does — despite Chronos-2's stronger aggregate benchmark scores.[^berthelier2026covariate]

{: .note }
Using these models off the shelf, zero-shot, for load forecasting is covered as a practical direction in [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html), and as a build path in [§4.9.1 (Tier 1)](../chapter-4-directions/4-9-1-methods-tier1.html).

[^ansari2024chronos]: Ansari, A. F., Stella, L., Turkmen, C. et al. (2024). [Chronos: Learning the language of time series](https://arxiv.org/abs/2403.07815). *Transactions on Machine Learning Research*. arXiv:2403.07815.
[^woo2024moirai]: Woo, G., Liu, C., Kumar, A. et al. (2024). [Unified training of universal time series forecasting transformers](https://arxiv.org/abs/2402.02592). ICML 2024. arXiv:2402.02592.
[^das2024timesfm]: Das, A., Kong, W., Sen, R., Zhou, Y. (2024). [A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688). ICML 2024. arXiv:2310.10688.
[^ansari2025chronos2]: Ansari, A. F., Shchur, O., Küken, J. et al. (2025). [Chronos-2: From univariate to universal forecasting](https://arxiv.org/abs/2510.15821). arXiv:2510.15821.
[^liu2025moirai2]: Liu, C., Aksu, T., Liu, J. et al. (2025). [Moirai 2.0: When less is more for time series forecasting](https://arxiv.org/abs/2511.11698). arXiv:2511.11698.
[^auer2025tirex]: Auer, A., Podest, P., Klotz, D. et al. (2025). [TiRex: Zero-shot forecasting across long and short horizons with enhanced in-context learning](https://arxiv.org/abs/2505.23719). NeurIPS 2025. arXiv:2505.23719.
[^hoo2025tabpfnts]: Hoo, S. B., Müller, S., Salinas, D., Hutter, F. (2025). [From tables to time: Extending TabPFN-v2 to time series forecasting](https://arxiv.org/abs/2501.02945). arXiv:2501.02945.
[^rasul2023laglama]: Rasul, K., Ashok, A., Williams, A. R. et al. (2023). [Lag-Llama: Towards foundation models for probabilistic time series forecasting](https://arxiv.org/abs/2310.08278). arXiv:2310.08278.
[^shi2024timemoe]: Shi, X., Wang, S., Nie, Y. et al. (2024). [Time-MoE: Billion-scale time series foundation models with mixture of experts](https://arxiv.org/abs/2409.16040). ICLR 2025. arXiv:2409.16040.
[^cohen2025toto]: Cohen, B., Khwaja, E., Doubli, Y. et al. (2025). [This time is different: An observability perspective on time series foundation models](https://arxiv.org/abs/2505.14766). arXiv:2505.14766.
[^goswami2024moment]: Goswami, M., Szafer, K., Choudhry, A. et al. (2024). [MOMENT: A family of open time-series foundation models](https://arxiv.org/abs/2402.03885). ICML 2024. arXiv:2402.03885.
[^liu2024timer]: Liu, Y., Zhang, H., Li, C. et al. (2024). [Timer: Generative pre-trained transformers are large time series models](https://arxiv.org/abs/2402.02368). ICML 2024. arXiv:2402.02368.
[^ekambaram2024ttm]: Ekambaram, V., Jati, A., Dayama, P. et al. (2024). [Tiny Time Mixers (TTMs): Fast pre-trained models for enhanced zero/few-shot forecasting](https://arxiv.org/abs/2401.03955). NeurIPS 2024. arXiv:2401.03955.
[^berthelier2026covariate]: Berthelier, G., Baranova, M., Pantea, A.-T. et al. (2026). [Investigating simple target-covariate relationships for Chronos-2 and TabPFN-TS](https://arxiv.org/abs/2605.12200). arXiv:2605.12200.

---
[← Previous: 2.4 Existing FMs Relevant to Energy](2-4-existing-fms-relevant-to-energy.html) · [Next: 2.4.2 Power-Grid FMs →](2-4-2-power-grid-fms.html)
