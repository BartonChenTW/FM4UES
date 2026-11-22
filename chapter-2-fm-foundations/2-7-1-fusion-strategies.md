---
title: "2.7.1 Fusion Strategies"
parent: "2.7 Multimodal Models"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 1
status: draft
last_reviewed: 2026-11-22
---

# 2.7.1 Fusion Strategies: Where and How Modalities Are Combined
{: .no_toc }

{% include page-status.html %}

Once each modality has its own encoder, three choices remain: where in the network the encoders meet, by what mechanism, and what the model does when a modality arrives at another rate or not at all. These are the design choices behind every "cross-attend X with Y" in these notes.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Fusion is one problem among several

[§2.7](2-7-multimodal-models.html#how-models-combine-modalities) introduced three common ways to combine modalities. This page goes one level down.

A widely cited survey of [multimodal](../appendices/a-glossary.html#multimodality) machine learning splits the field into five challenges: representation, translation, alignment, fusion and co-learning.[^baltrusaitis2019mmlsurvey] Two of them matter most here:

- **Alignment** finds which parts of one modality correspond to which parts of another: which satellite image goes with which hour of a PV series, which building record goes with which meter.
- **Fusion** integrates information from several modalities to predict an outcome, such as a class or a continuous value.

The survey notes that in deep networks "the line between multimodal representation and fusion has been blurred", because the representation is learned together with the prediction. The distinction is still useful for urban energy systems. Contrastive training in the style of [CLIP](../appendices/d-model-index.html#clip) ([§2.7](2-7-multimodal-models.html#how-models-combine-modalities)) aligns two encoders in a shared space, but that alone does not say how a building's attributes should change its load forecast. That is a fusion question.

The same survey gives three reasons to fuse at all: more robust predictions when several modalities observe the same thing, complementary information that no single modality shows, and a system that still works when one modality is missing.[^baltrusaitis2019mmlsurvey] For urban energy systems the second reason is the one that counts. The evidence in [§2.7](2-7-multimodal-models.html#what-the-evidence-says) is that a second modality helps when it carries what the series cannot see.

## Where to fuse: early, intermediate or late

The classic split is by the stage at which modalities meet:[^baltrusaitis2019mmlsurvey]

| Stage | What is combined | Strength | Weakness |
| :--- | :--- | :--- | :--- |
| **Early** | Features just after extraction, often by concatenation | Can learn interactions between low-level features; one model to train | Harder to use when a modality is missing |
| **Intermediate** ("mid") | The hidden tokens of separate encoders, from a chosen layer onwards | Each encoder first learns its own modality's patterns, then they exchange information | The layer at which they meet has to be tuned |
| **Late** | Each modality's own prediction, by averaging, weighting or a learned model | A different model per modality; easier when a modality is missing; can even be trained without paired data | Ignores interactions between the modalities |

Which stage works best is an empirical question. In audio-visual classification, Nagrani et al. varied the layer at which the modalities first exchange information and found that mid fusion beat both early and late fusion. They also note that this layer "may need to be tuned specifically for different tasks and datasets".[^nagrani2021mbt] It is an audio-visual result: for load and weather data the fusion layer is something to tune, not to copy.

In energy forecasting, the best stage depends on how quickly the second modality's signal decays and how reliable each sensor is. For very-short-term solar irradiance forecasting from sky images and meteorological records, an early feature-level transformer with gating improved the balanced accuracy of ramp events over a late-fusion CNN baseline by 9.43% at a 2-minute horizon and 3.91% at 6 minutes, because cloud edges and irradiance drops interact directly; beyond 10 minutes, however, the spatial information in a single sky image stopped adding value.[^zhang2023skyfusion] On a building energy monitoring dataset with nine heterogeneous sensors, comparing early fusion, late fusion and attention-weighted fusion across chronological splits found that all three beat single-model baselines: late fusion gave stable performance across strongly correlated loads, while attention-weighted fusion was more robust when sensors differed in predictive reliability.[^hasan2026multisensor]

**Reading for urban energy systems.** Late fusion is the natural fallback. A series-only forecaster and an attribute-based estimate can be combined even when they were trained on different datasets, which matters because measured load rarely comes paired with building attributes ([§2.7](2-7-multimodal-models.html#why-it-is-hard)). Its cost is that the attributes can no longer change *how* the series is read. The cold-morning example in [§2.7](2-7-multimodal-models.html#a-worked-example-from-this-domain), where insulation and heating system change the response to weather, needs that interaction, so it needs early or intermediate fusion.

## How to merge: the mechanisms

Roughly from cheapest to most expressive:

- **Concatenation.** Append one modality's features to another's. The survey calls this the simplest joint representation, "also referred to as early fusion".[^baltrusaitis2019mmlsurvey] It is the baseline every other mechanism should beat.
- **Gating.** Learned gates decide how much each modality or input contributes. The Gated Multimodal Unit "learns to decide how modalities influence the activation of the unit using multiplicative gates", and outperformed other fusion strategies, including mixtures of experts, on classifying film genres from plot and poster.[^arevalo2017gmu] The Temporal Fusion Transformer uses separate variable selection networks for static, past and known-future inputs, and static covariate encoders that produce context vectors "to condition temporal dynamics".[^lim2021tft] Gating suits urban energy systems when there are many candidate [covariates](../appendices/a-glossary.html#covariate), some of them irrelevant for a given building.
- **Feature-wise conditioning (FiLM).** A small network turns the conditioning input into a scale and a shift for each feature of another network, "a simple, feature-wise affine transformation based on conditioning information". On a visual-reasoning benchmark it halved the previous best error.[^perez2018film] It fits a fixed context modulating a time series: building attributes could set how a load encoder's features respond, at the cost of two vectors per layer and no attention over attribute tokens. Two 2026 energy studies apply FiLM directly, though neither tests external building attributes on a pretrained load model. In multi-station photovoltaic forecasting, a Physical FiLM layer conditions a cross-variable time-series transformer on each site's installed capacity as a static prior, cutting mean squared error by 21.6% against [PatchTST](../appendices/d-model-index.html#patchtst) and 44.0% against Autoformer — a single scalar site attribute across stations rather than heterogeneous building metadata.[^xie2026pvfilm] For residential smart-meter load, a behaviour-conditioned Attentive Neural Process uses FiLM in its decoder on user-disjoint splits of the Smart Grid, Smart City (SGSC) dataset, reducing MAE by 7.9% and CRPS by 6.9% over a label-agnostic baseline; it trains from scratch and conditions on behavioural classes inferred from the load context under clustering weak supervision rather than on external register attributes (preprint).[^soleimani2026bcnp] FiLM conditioning of a pretrained load model on real building-register attributes therefore remains untested.
- **[Cross-attention](../appendices/a-glossary.html#cross-attention).** The tokens of one modality query the tokens of another ([§2.6](2-6-architectures.html)). The Multimodal Transformer (MulT) builds fusion from "directional pairwise crossmodal attention" and learns directly from unaligned streams whose sampling rates differ, without aligning them first.[^tsai2019mult] The cost grows with the product of the two token counts. It fits when the second modality has structure worth attending to, in time (a sequence of cloud images) or in space (the nodes of a grid).
- **Bottleneck fusion.** Information between modalities must pass through a few shared latent tokens. Nagrani et al. report that this "avoids the quadratic scaling cost of full pairwise attention, and leads to performance gains with less compute".[^nagrani2021mbt] The Perceiver uses a related idea for any input, distilling inputs "into a tight latent bottleneck" so that it scales to hundreds of thousands of inputs.[^jaegle2021perceiver] It fits when several modalities must be fused at once.
- **One token stream.** Everything goes into one [transformer](../appendices/a-glossary.html#transformer), as in [Janus](../appendices/d-model-index.html#janus) ([§2.7](2-7-multimodal-models.html#how-models-combine-modalities)). This is the most expressive option and needs the most paired data.

## Fusing into a pretrained model

A [foundation model](../appendices/a-glossary.html#foundation-model) adds a question that classic fusion work does not face: whether the pretrained parts are kept as they are. There are three routes:

1. **Train the encoders and the fusion together, from scratch.** The Temporal Fusion Transformer[^lim2021tft] and the lightweight text-and-time-series model in SysCaps[^emami2025syscaps] are built this way.
2. **Keep a pretrained time-series foundation model frozen and train a fusion adapter.** UniCA turns heterogeneous covariates (categorical variables, images, text) into series-like representations and fuses them with an attention-based mechanism, "while preserving the generalization ability" of the frozen model.[^han2025unica]
3. **Pretrain the multimodal model as a whole on paired data.** HORAI pretrains a cross-modality encoder on MM-TS, a multimodal time-series corpus of up to one billion points in six domains, and reports state-of-the-art [zero-shot](../appendices/a-glossary.html#zero-shot) forecasting.[^chen2026horai]

**Reading for urban energy systems.** Route 2 is the realistic starting point. Pretrained load and time-series encoders exist ([§2.4.1](2-4-1-time-series-fms.html), [§2.4.5](2-4-5-load-forecasting-fms.html)); a large corpus of load paired with building attributes does not ([§2.7](2-7-multimodal-models.html#why-it-is-hard)). Route 3 is what a multimodal UES foundation model would eventually need, and it is blocked by that missing corpus, not by architecture.

## Different rates and missing modalities

### Different rates

Building attributes are fixed, weather is hourly, meters may report every 15 minutes and satellite images every five ([§2.7](2-7-multimodal-models.html#why-it-is-hard)). Resampling everything to one grid is the simplest answer, but it either discards resolution or invents values. Three published alternatives:

- **Broadcast what does not change.** The Temporal Fusion Transformer encodes static covariates once, into context vectors that condition the whole sequence.[^lim2021tft]
- **Attend across time without aligning.** MulT's crossmodal attention was designed for streams with "variable sampling rates" and works on unaligned data directly.[^tsai2019mult]
- **Embed time itself.** Multi-Time Attention Networks learn an embedding of continuous time and use attention to turn a variable number of observations into a fixed-length representation.[^shukla2021mtan] They were built for sparse, irregularly sampled health records, which is close to a meter series with gaps.

### Missing modalities

- **Drop modalities during training.** ModDrop randomly drops whole modality channels during training, so that the network produces meaningful predictions from any subset of them. On gesture recognition it made the network much more stable when signals were noisy or missing.[^neverova2016moddrop]
- **Fall back on late fusion.** Late fusion makes it easier to predict when one or more modalities are missing.[^baltrusaitis2019mmlsurvey]
- A survey of deep learning with missing modalities reviews the wider set of methods, their applications and datasets.[^wu2024missingmodality]

**Reading for urban energy systems.** Most buildings have no household survey, and many have no reliable register entry. A model trained only on complete pairs will be used mostly on incomplete ones. Training with dropped modalities is the cheap remedy. The target is that a building with no attributes gets a forecast no worse than the series-only model's.

## Checking that the fusion does anything

[§2.7](2-7-multimodal-models.html#time-series-with-text) found that reported multimodal gains can come from something other than the added modality. The studies there suggest three cheap checks for any fused UES model:

1. **Beat the best single-modality model.** Removing the language model from three LLM-based forecasters did not degrade them.[^tan2024lmuseful] The comparison has to be with a strong series-only foundation model, not a weak baseline.
2. **Shuffle the second modality.** Swapping each row's text for any other text, even empty text, changed error by less than 0.5% on one benchmark.[^sridhar2026textsensitivity] For electricity prices, feeding the text of a different day reversed the gain.[^yi2026traceepf] For buildings, the analogue is to give each meter series another building's attributes: a model that really uses them should get worse.
3. **Report results by what is available.** Score buildings with full, partial and no attributes separately, so that a gain on the well-documented minority is not mistaken for a gain everywhere.

These belong alongside the evaluation criteria in [§2.8](2-8-ues-fm-evaluation-criteria.html).

## Matching patterns to UES pairings

The first pattern these notes would try for each pairing. Only the solar rows rest on published energy results.

| Pairing | Structure | Starting pattern | Evidence |
| :--- | :--- | :--- | :--- |
| Building attributes → building load | Fixed vector vs. hourly series | FiLM or gating on a frozen load encoder; modality dropout for buildings without attributes | Conditioning on text generated from simulation metadata worked on simulated buildings (SysCaps);[^emami2025syscaps] FiLM has been demonstrated for static PV capacity[^xie2026pvfilm] and context-inferred residential load behaviour (preprint),[^soleimani2026bcnp] while real building-register attributes remain untested ([§2.7](2-7-multimodal-models.html#what-the-evidence-says)) |
| Weather forecast → load | Time series known in advance | Not multimodal: a known-future [covariate](../appendices/a-glossary.html#covariate) ([§2.4.1](2-4-1-time-series-fms.html)) | Established |
| Sky or satellite images ↔ PV and irradiance | Image sequence vs. series | Align image and series [patches](../appendices/a-glossary.html#patch), then cross-attend | SolCloudLLM aligns sky-image patches with time-series patches and fuses them in both directions;[^chen2026solcloudllm] Baguan-solar fuses a weather FM's forecasts with satellite imagery in two stages[^ma2026baguansolar] |
| Grid graph ↔ load | Graph nodes vs. series patches | Cross-attention between bus tokens and the load tokens connected to them | None; proposed as the grid-load bridge in [§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields) |
| Operational text → prices | Irregular text vs. hourly series | Text as context tokens, with the shuffle check above | Small and condition-dependent ([§2.7](2-7-multimodal-models.html#time-series-with-text)) |
| The five encoders of the case study | Series, fields, attributes, a graph, rules | Bottleneck fusion to keep cost bounded, with modality dropout because not every hub has every modality | None; a proposal ([§5.4](../chapter-5-case-study/5-4-data-modules-and-tasks.html#modules-and-tasks)) |

## Where these notes use it

- [§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields): the metadata-conditioned load FM (first row of the table above), the grid-load bridge (fourth row) and the weather-conditioned building energy FM.
- [§5.1](../chapter-5-case-study/5-1-roadmap.html#phase-2-year-24--multimodal-conditioning) and [§5.4](../chapter-5-case-study/5-4-data-modules-and-tasks.html#modules-and-tasks): the case study's phase that fuses its five encoders (last row).
- [§2.8](2-8-ues-fm-evaluation-criteria.html): where the checks above would sit in an evaluation.

[^baltrusaitis2019mmlsurvey]: Baltrušaitis, T., Ahuja, C., Morency, L.-P. (2019). [Multimodal machine learning: A survey and taxonomy](https://doi.org/10.1109/TPAMI.2018.2798607). *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 41(2), 423–443. arXiv:1705.09406.
[^nagrani2021mbt]: Nagrani, A., Yang, S., Arnab, A. et al. (2021). [Attention bottlenecks for multimodal fusion](https://arxiv.org/abs/2107.00135). *Advances in Neural Information Processing Systems 34 (NeurIPS 2021)*. arXiv:2107.00135.
[^arevalo2017gmu]: Arevalo, J., Solorio, T., Montes-y-Gómez, M., González, F. A. (2017). [Gated multimodal units for information fusion](https://arxiv.org/abs/1702.01992). arXiv:1702.01992.
[^lim2021tft]: Lim, B., Arık, S. Ö., Loeff, N. et al. (2021). [Temporal Fusion Transformers for interpretable multi-horizon time series forecasting](https://doi.org/10.1016/j.ijforecast.2021.03.012). *International Journal of Forecasting*, 37(4), 1748–1764. arXiv:1912.09363.
[^perez2018film]: Perez, E., Strub, F., de Vries, H. et al. (2018). [FiLM: Visual reasoning with a general conditioning layer](https://doi.org/10.1609/aaai.v32i1.11671). *Proceedings of the AAAI Conference on Artificial Intelligence*, 32(1). arXiv:1709.07871.
[^tsai2019mult]: Tsai, Y.-H. H., Bai, S., Liang, P. P. et al. (2019). [Multimodal Transformer for unaligned multimodal language sequences](https://doi.org/10.18653/v1/P19-1656). *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)*, 6558–6569. arXiv:1906.00295.
[^jaegle2021perceiver]: Jaegle, A., Gimeno, F., Brock, A. et al. (2021). [Perceiver: General perception with iterative attention](https://arxiv.org/abs/2103.03206). *Proceedings of the 38th International Conference on Machine Learning (ICML 2021)*, PMLR 139. arXiv:2103.03206.
[^emami2025syscaps]: Emami, P., Li, Z., Sinha, S. et al. (2025). [SysCaps: Language interfaces for simulation surrogates of complex systems](https://arxiv.org/abs/2405.19653). *International Conference on Learning Representations (ICLR)*. arXiv:2405.19653.
[^han2025unica]: Han, L., Liu, Y., Li, L. et al. (2025). [UniCA: Unified covariate adaptation for time series foundation model](https://arxiv.org/abs/2506.22039). arXiv:2506.22039.
[^chen2026horai]: Chen, P., Wang, S., Hu, S. et al. (2026). [Empowering time series analysis with large-scale multimodal pretraining](https://arxiv.org/abs/2602.05646). arXiv:2602.05646.
[^shukla2021mtan]: Shukla, S. N., Marlin, B. M. (2021). [Multi-time attention networks for irregularly sampled time series](https://arxiv.org/abs/2101.10318). *International Conference on Learning Representations (ICLR)*. arXiv:2101.10318.
[^neverova2016moddrop]: Neverova, N., Wolf, C., Taylor, G., Nebout, F. (2016). [ModDrop: Adaptive multi-modal gesture recognition](https://doi.org/10.1109/TPAMI.2015.2461544). *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 38(8), 1692–1706. arXiv:1501.00102.
[^wu2024missingmodality]: Wu, R., Wang, H., Chen, H. et al. (2024). [Deep multimodal learning with missing modality: A survey](https://arxiv.org/abs/2409.07825). *Transactions on Machine Learning Research* (2026). arXiv:2409.07825.
[^tan2024lmuseful]: Tan, M., Merrill, M. A., Gupta, V. et al. (2024). [Are language models actually useful for time series forecasting?](https://doi.org/10.52202/079017-1922). *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, 60162–60191. arXiv:2406.16964.
[^sridhar2026textsensitivity]: Sridhar, K., Gupta, A., Pradhan, N. et al. (2026). [Semantics or structure? Auditing text sensitivity in multimodal time-series forecasting](https://arxiv.org/abs/2608.22321). ICML 2026 Workshop on Foundation Models for Structured Data. arXiv:2608.22321.
[^yi2026traceepf]: Yi, X., Yuan, Z., Lestas, I. (2026). [TRACE: A reproducible benchmark for electricity price forecasting with official operational text](https://arxiv.org/abs/2610.02256). arXiv:2610.02256.
[^chen2026solcloudllm]: Chen, K., Perera, M., Wang, W. et al. (2026). [Bidirectional multimodal fusion of sky images and time-series for solar forecasting with large language models](https://arxiv.org/abs/2609.11135). arXiv:2609.11135.
[^ma2026baguansolar]: Ma, Z., Ying, K., Gu, X. et al. (2026). [Integrating weather foundation model and satellite to enable fine-grained solar irradiance forecasting](https://doi.org/10.1145/3770855.3818436). *Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2*, 7785–7796. arXiv:2603.14845.
[^zhang2023skyfusion]: Zhang, L., Wilson, R., Sumner, M., Wu, Y. (2023). [Advanced multimodal fusion method for very short-term solar irradiance forecasting using sky images and meteorological data: A gate and transformer mechanism approach](https://doi.org/10.1016/j.renene.2023.118952). *Renewable Energy*, 216, 118952.
[^hasan2026multisensor]: Hasan, R., Mansouri, M., Arkhangelski, J., Abdou Tankari, M. (2026). [Interpretable multi-sensor fusion for short-term energy consumption forecasting](https://doi.org/10.3390/en19092230). *Energies*, 19(9), 2230.
[^xie2026pvfilm]: Xie, C., Chen, M., Wang, Y. et al. (2026). [A cross-variable time-series transformer architecture integrating physical features for photovoltaic energy forecasting](https://doi.org/10.3390/a19080646). *Algorithms*, 19(8), 646.
[^soleimani2026bcnp]: Soleimani, R., Visentin, A., Pesch, D. (2026). [Behaviour-conditioned neural processes for adaptive residential short-term load forecasting](https://arxiv.org/abs/2607.16168). arXiv:2607.16168.

---
[← Previous: 2.7 Multimodal Models](2-7-multimodal-models.html) · [Back to Chapter 2](index.html) · [Next: 2.8 Evaluation Criteria for UES Foundation Models →](2-8-ues-fm-evaluation-criteria.html)
