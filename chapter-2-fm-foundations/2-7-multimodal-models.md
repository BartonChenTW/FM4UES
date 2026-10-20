---
title: "2.7 Multimodal Models"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 7
status: draft
last_reviewed: 2026-10-20
---

# 2.7 Multimodal Models: Combining Time Series with Other Kinds of Data
{: .no_toc }

{% include page-status.html %}

How a model can read a load series together with what explains it: building attributes, images, networks and text. In these notes' view, this may be the approach that matters most for urban energy systems, and it is the least tested.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Why this matters for urban energy systems

A time-series foundation model reads a load series in short [patches](../appendices/a-glossary.html#patch), and a patch carries nothing about the building that produced it ([§2.3.2](2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings)). That is why [zero-shot](../appendices/a-glossary.html#zero-shot) forecasting works for aggregated load but not reliably for a single building ([§2.4.5](2-4-5-load-forecasting-fms.html)). What explains one building's load lies outside its series: its construction, its heating system, its occupants, the weather over it, the network it hangs on. Those are other kinds of data, and a model that combines several kinds is **[multimodal](../appendices/a-glossary.html#multimodality)**.

Most of the directions these notes propose depend on it: the metadata-conditioned load model and the grid-load bridge ([§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields)), the case study's encoder stack ([§5.4](../chapter-5-case-study/5-4-data-modules-and-tasks.html#modules-and-tasks)) and its "multimodal conditioning" phase ([§5.1](../chapter-5-case-study/5-1-roadmap.html#phase-2-year-24--multimodal-conditioning)), and the single-model shape of the ecosystem in [§4.9](../chapter-4-directions/4-9-ecosystem.html). This page sets out what multimodality is, what has been tried with time series, what the evidence shows, and why it is hard.

## What a modality is

A **modality** is one kind of data with its own structure. In urban energy systems the usual ones are:

- **time series:** a meter reading every hour, a temperature record
- **attributes:** a building's floor area, construction year and heating system, which do not change from hour to hour
- **fields and images:** a weather map, a satellite or sky-camera image
- **graphs:** a grid or pipe network
- **text:** a planning document, a market notice, a survey answer

**Several time series are not yet multimodal.** A load series with a temperature series is *multivariate*: one modality with several channels, which general forecasters handle as covariates ([§2.4.1](2-4-1-time-series-fms.html)). It becomes multimodal when a time series is combined with data of a different kind.

## How models combine modalities

No single architecture suits every modality, so a multimodal model usually gives each one its own **encoder**: a time-series encoder for the meter data, a small network for the attributes, a vision model for images, a [GNN](2-6-architectures.html#graph-neural-networks-gnns) for the network. Each encoder turns its input into tokens of the same size. A review of energy forecasting models, in its section on multimodal fusion, describes this as the usual design, with the encoders' outputs merged at a later stage, for example a convolutional network for satellite cloud images alongside a [transformer](../appendices/a-glossary.html#transformer) for a PV plant's history.[^ferdaus2025cleanenergy] The tokens are then combined in one of three common ways:

- **A shared space.** Separate encoders are trained so that matching inputs land close together. [CLIP](../appendices/d-model-index.html#clip) trains an image encoder and a text encoder to predict which caption goes with which image, on 400 million pairs, and can then classify images it was never trained on by comparing them with text descriptions.[^radford2021clip]
- **[Cross-attention](../appendices/a-glossary.html#cross-attention).** One modality's tokens attend to another's, so the second changes how the first is read ([§2.6](2-6-architectures.html)). This is the pattern these notes propose most often. The same review calls its use in energy foundation models "still in its infancy".[^ferdaus2025cleanenergy]
- **One token stream.** All modalities are turned into tokens and processed together by a single transformer. [Janus](../appendices/d-model-index.html#janus) does this for images and text, with separate visual encoders for understanding an image and for generating one, both feeding one shared transformer.[^wu2024janus]

## A worked example from this domain

Suppose the task is to forecast one building's electricity use for the next day. Three modalities are available:

1. **Meter history** (time series). A pretrained time-series encoder ([§2.4.1](2-4-1-time-series-fms.html)) turns the last few weeks into patch tokens. These carry the building's habits: its daily and weekly rhythm, its base load.
2. **Building attributes** (attributes). An attribute encoder turns floor area, construction year, heating system and occupancy type into a handful of tokens. These say *why* the building behaves as it does. They also give the model something to go on for a building with little or no history.
3. **Weather forecast** (time series, known in advance). Its own encoder, or a set of covariates, turns tomorrow's temperature and irradiance into tokens.

The meter tokens then cross-attend to the attribute and weather tokens. A cold morning raises the forecast more for a poorly insulated building with electric heating than for a well-insulated one with a gas boiler, because the attributes change how the model reads the weather. This example is illustrative, not a published result.

## What has been tried with time series

### Time series with attributes

The established architecture for this is the Temporal Fusion Transformer, built for inputs that mix "static (i.e. time-invariant) covariates, known future inputs, and other exogenous time series".[^lim2021tft] Among [foundation models](../appendices/a-glossary.html#foundation-model), [TabPFN-TS](../appendices/d-model-index.html#tabpfn-ts) takes static metadata alongside a series,[^hoo2025tabpfnts] and [Tyan-WP](../appendices/d-model-index.html#tyan-wp) embeds each wind site's coordinates, terrain and ecoregion ([§2.4.3](2-4-3-clean-energy-forecasting-fms.html)).[^huang2026tyanwp] Adapters are a third route: UniCA adds categorical and other non-numeric inputs to a frozen time-series foundation model while keeping its ability to generalise.[^han2025unica]

For buildings, the evidence is thin:

- **[BuildingsBench](../appendices/d-model-index.html#buildingsbench)**, the largest pretrained building-load model, conditions on very little: per the paper's method section, the location of the building's area and whether it is residential or commercial. Adding the location improved accuracy by only 0.1–1%, and the authors list the effect of building metadata as future work.[^emami2023buildingsbench]
- **SysCaps** describes each simulated system in plain text, generated from simulation metadata by a language model, and conditions a load [surrogate](../appendices/a-glossary.html#surrogate) on that text. On building and wind-farm simulators, the text-conditioned surrogates were more accurate on held-out systems than conventional ones.[^emami2025syscaps] It is the closest published precedent for the metadata-conditioned load model in [§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields).
- **A large heating-load benchmark** found that adding static features gave "only minor, often statistically non-significant, and sometimes slightly negative" gains. Those features were derived from the load data (feature importances and load-pattern metrics), not register attributes such as floor area, so the question for real building attributes is still open.[^neubauer2026heatingtl]

### Time series with images and spatial fields

Solar forecasting is where this is furthest along, because a camera or satellite sees the clouds that drive the output:

- **CrossViViT** forecasts day-ahead irradiance at ground stations from satellite imagery plus the station series, released a paired satellite-and-series dataset, and was tested zero-shot at stations it had not seen.[^boussif2023crossvivit]
- **SolCloudLLM** fuses sky-image patches with time-series patches. It reports up to 25.4% lower error, with the gains concentrated in cloudy conditions, and in few-shot settings a simple physical method often beat the deep models.[^chen2026solcloudllm]
- **Baguan-solar** fuses a global weather foundation model's forecasts with high-resolution satellite imagery for kilometre-scale, 24-hour irradiance forecasts. It reports 16% lower error than baselines including the ECMWF forecast, and has been in operational use since July 2025.[^ma2026baguansolar]
- Paired data is the bottleneck: the authors of one sky-image dataset note that "there are few publicly available standardized benchmark datasets for image-based solar forecasting".[^nie2023skippd]

In weather, multimodality is the norm: [Aurora](../appendices/d-model-index.html#aurora) is pretrained on more than a million hours of diverse geophysical data ([§2.4.3](2-4-3-clean-energy-forecasting-fms.html)),[^bodnar2025aurora] and Aardvark Weather goes further, ingesting observations directly and producing both gridded and local station forecasts in one model.[^allen2025aardvark] For buildings, one study used a vision-language model to read roof age and building density from satellite images and estimate urban heat demand from them. It predicts annual demand rather than a time series, but shows images being turned into building attributes.[^thota2026heatprompt]

### Time series with text

Language models have been used as forecasters, by writing a series as a string of digits[^gruver2023llmtime] or by reprogramming a frozen language model with a text prompt as a prefix.[^jin2024timellm] ChatTime is a foundation model that reads and writes both time series and text.[^wang2025chattime] Benchmarks pair series with text: Time-MMD covers nine domains,[^liu2024timemmd] and Context is Key builds tasks that can only be solved by reading the accompanying text.[^williams2025cik] Time-MMD's "Energy" domain is weekly US gasoline prices with government energy reports, so neither benchmark contains electricity load, building or grid data.[^liu2024timemmd]

The critical evidence is strong, and it is the main reason for caution:

- Removing the language model from three popular LLM-based forecasters, or replacing it with a basic attention layer, "does not degrade forecasting performance — in most cases, the results even improve".[^tan2024lmuseful]
- Across 16 tasks, "the benefits of multimodality are highly condition-dependent". Text helped when it carried information the series did not, when enough training data was available, and with weaker time-series models.[^zhang2025whenmultimodal]
- On Time-MMD, swapping each row's text for any other text, even empty text, changed error by less than 0.5%. The reported gains came back when a numeric column shipped with the data was removed.[^sridhar2026textsensitivity]
- A benchmark of 14 datasets found numeric-only time-series models leading overall, and that "incorrect or temporally misaligned context degrades performance".[^chen2026musebench]

In energy, the results are small and narrow:

- **Building and city load:** an early study wrote consumption data as sentences and fine-tuned a language model on them.[^xue2023lmload]
- **Electricity prices with market news:** news gave classical models marginal gains, and language models gained modestly while also producing "fabricated and malformed price sequences".[^bi2025nswepnews]
- **Prices with official operational text:** the text cut upper-tail error by a median 7.4%, but feeding the text of a different day reversed the gain.[^yi2026traceepf]
- **Power systems:** one model combines text, a causal graph of power-system variables and time series for imputation, forecasting and super-resolution.[^zhou2026cmllm]

## What the evidence says

These notes read three points from this literature:

1. **A second modality helps when it carries what the series cannot see.** Clouds in a sky image do this for solar, which is why that strand works. For buildings, attributes should do the same, but no study has yet tested real register attributes in a pretrained load model.
2. **Text is the weakest case so far.** Several careful studies find that text adds little, or that reported gains come from something else. For UES, text is plausible mainly where it carries scheduled information a series cannot show, such as outages, tariffs or market notices.
3. **Attributes are the most promising and least tested modality for UES.** The largest building model barely uses them, and the one positive result (SysCaps) is on simulated systems. This is the gap a metadata-conditioned load model would fill.

## Why it is hard

- **Different rates and timing.** Attributes are fixed, weather is hourly, meters may be every 15 minutes, satellite images every five. Real multimodal series are "irregular, multimodal, and messy, with varying sampling rates, asynchronous modalities, and pervasive missingness", which most benchmarks assume away.[^chang2025timeimm]
- **Missing modalities.** In practice a modality is often absent for some instances, through sensor limits, cost or privacy, which degrades performance unless the model is built for it.[^wu2024missingmodality] Most buildings have no household survey, and many have no reliable register entry.
- **Paired data.** Training needs the modalities paired instance by instance, and large paired corpora are scarce even outside energy.[^chen2026horai] For buildings, measured load rarely comes with the building's attributes ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)), and where it does, licences often prevent pooling it ([§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields)).
- **Misalignment.** Context from the wrong time does worse than no context at all.[^chen2026musebench] [^yi2026traceepf]

{: .note }
**Dated search** (arXiv, 20 October 2026). Abstracts with "multimodal" and "foundation model" and any of electricity, power system, power grid, energy system, building energy or load forecasting: 4 results, of which one is a forecasting model (Baguan-solar). "Multimodal" with district heating, heat demand, [energy hub](../appendices/a-glossary.html#energy-hub), multi-energy or integrated energy system: 10 results, none a multimodal foundation model. **No multimodal foundation model for buildings, districts, grids or multi-carrier energy hubs has been published.**

## Where these notes use it

- [§2.3.3](2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions): describing a building's time series by its attributes.
- [§4.6](../chapter-4-directions/4-6-reading-the-screen.html#candidate-sub-fields): the metadata-conditioned load FM, which is the worked example above at scale, and the grid-load bridge, which pairs load tokens with a grid graph.
- [§5.4](../chapter-5-case-study/5-4-data-modules-and-tasks.html#modules-and-tasks) and [§5.1](../chapter-5-case-study/5-1-roadmap.html#phase-2-year-24--multimodal-conditioning): the case study's encoder stack for demand, weather, technology, topology and market, and the roadmap phase that fuses them.
- [§4.9](../chapter-4-directions/4-9-ecosystem.html): whether one multimodal model could cover the whole urban energy system, and why that is harder than for weather.

[^radford2021clip]: Radford, A., Kim, J. W., Hallacy, C. et al. (2021). [Learning transferable visual models from natural language supervision](https://arxiv.org/abs/2103.00020). *ICML 2021*, PMLR 139, 8748–8763. arXiv:2103.00020.
[^wu2024janus]: Wu, C., Chen, X., Wu, Z. et al. (2024). [Janus: Decoupling visual encoding for unified multimodal understanding and generation](https://arxiv.org/abs/2410.13848). arXiv:2410.13848.
[^bodnar2025aurora]: Bodnar, C., Bruinsma, W. P., Lucic, A. et al. (2025). [A foundation model for the Earth system](https://doi.org/10.1038/s41586-025-09005-y). *Nature*, 641, 1180–1187.
[^emami2023buildingsbench]: Emami, P., Sahu, A., Graf, P. (2023). [BuildingsBench: A large-scale dataset of 900K buildings and benchmark for short-term load forecasting](https://arxiv.org/abs/2307.00142). NeurIPS 2023, Datasets and Benchmarks Track. arXiv:2307.00142.
[^ferdaus2025cleanenergy]: Ferdaus, M. M., Dam, T., Sarkar, M. R. et al. (2026). [Foundation models for clean energy forecasting: A comprehensive review](https://doi.org/10.1016/j.rser.2025.116452). *Renewable and Sustainable Energy Reviews*, 226, 116452. arXiv:2507.23147.
[^hoo2025tabpfnts]: Hoo, S. B., Müller, S., Salinas, D., Hutter, F. (2025). [From tables to time: Extending TabPFN-v2 to time series forecasting](https://arxiv.org/abs/2501.02945). arXiv:2501.02945.
[^huang2026tyanwp]: Huang, J., Luo, A., Liu, L. et al. (2026). [Tyan-WP: A wind power foundation model for ultra-short-term probabilistic forecasting](https://arxiv.org/abs/2606.08630). arXiv:2606.08630.
[^lim2021tft]: Lim, B., Arık, S. Ö., Loeff, N. et al. (2021). [Temporal Fusion Transformers for interpretable multi-horizon time series forecasting](https://doi.org/10.1016/j.ijforecast.2021.03.012). *International Journal of Forecasting*, 37(4), 1748–1764. arXiv:1912.09363.
[^emami2025syscaps]: Emami, P., Li, Z., Sinha, S. et al. (2025). [SysCaps: Language interfaces for simulation surrogates of complex systems](https://arxiv.org/abs/2405.19653). *International Conference on Learning Representations (ICLR)*. arXiv:2405.19653.
[^neubauer2026heatingtl]: Neubauer, A., Yu, M., Babakhani, P. et al. (2026). [Transfer learning and explainable AI for heating load forecasting: A large-scale benchmark with SHAP-based static features](https://doi.org/10.1016/j.egyai.2026.100722). *Energy and AI*, 24, 100722.
[^han2025unica]: Han, L., Liu, Y., Li, L. et al. (2025). [UniCA: Unified covariate adaptation for time series foundation model](https://arxiv.org/abs/2506.22039). arXiv:2506.22039.
[^boussif2023crossvivit]: Boussif, O., Boukachab, G., Assouline, D. et al. (2023). [Improving day-ahead solar irradiance time series forecasting by leveraging spatio-temporal context](https://doi.org/10.52202/075280-0109). *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2342–2367. arXiv:2306.01112.
[^nie2023skippd]: Nie, Y., Li, X., Scott, A. et al. (2023). [SKIPP'D: A SKy Images and Photovoltaic Power Generation Dataset for short-term solar forecasting](https://doi.org/10.1016/j.solener.2023.03.043). *Solar Energy*, 255, 171–179. arXiv:2207.00913.
[^chen2026solcloudllm]: Chen, K., Perera, M., Wang, W. et al. (2026). [Bidirectional multimodal fusion of sky images and time-series for solar forecasting with large language models](https://arxiv.org/abs/2609.11135). arXiv:2609.11135.
[^ma2026baguansolar]: Ma, Z., Ying, K., Gu, X. et al. (2026). [Integrating weather foundation model and satellite to enable fine-grained solar irradiance forecasting](https://doi.org/10.1145/3770855.3818436). *Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2*, 7785–7796. arXiv:2603.14845.
[^allen2025aardvark]: Allen, A., Markou, S., Tebbutt, W. et al. (2025). [End-to-end data-driven weather prediction](https://doi.org/10.1038/s41586-025-08897-0). *Nature*, 641(8065), 1172–1179. arXiv:2404.00411.
[^thota2026heatprompt]: Thota, K., Mu, X., Schlachter, T. et al. (2026). [HeatPrompt: Zero-shot vision-language modeling of urban heat demand from satellite images](https://doi.org/10.1109/GreenTech68285.2026.11471546). *2026 IEEE Green Technologies Conference (GreenTech)*, 423–428. arXiv:2602.20066.
[^gruver2023llmtime]: Gruver, N., Finzi, M., Qiu, S. et al. (2023). [Large language models are zero-shot time series forecasters](https://doi.org/10.52202/075280-0861). *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 19622–19635. arXiv:2310.07820.
[^jin2024timellm]: Jin, M., Wang, S., Ma, L. et al. (2024). [Time-LLM: Time series forecasting by reprogramming large language models](https://arxiv.org/abs/2310.01728). *International Conference on Learning Representations (ICLR)*. arXiv:2310.01728.
[^wang2025chattime]: Wang, C., Qi, Q., Wang, J. et al. (2025). [ChatTime: A unified multimodal time series foundation model bridging numerical and textual data](https://doi.org/10.1609/aaai.v39i12.33384). *Proceedings of the AAAI Conference on Artificial Intelligence*, 39(12), 12694–12702. arXiv:2412.11376.
[^liu2024timemmd]: Liu, H., Xu, S., Zhao, Z. et al. (2024). [Time-MMD: Multi-domain multimodal dataset for time series analysis](https://doi.org/10.52202/079017-2476). *Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Datasets and Benchmarks Track*, 77888–77933. arXiv:2406.08627.
[^williams2025cik]: Williams, A. R., Ashok, A., Marcotte, É. et al. (2025). [Context is Key: A benchmark for forecasting with essential textual information](https://arxiv.org/abs/2410.18959). *Proceedings of the 42nd International Conference on Machine Learning (ICML)*, 267. arXiv:2410.18959.
[^tan2024lmuseful]: Tan, M., Merrill, M. A., Gupta, V. et al. (2024). [Are language models actually useful for time series forecasting?](https://doi.org/10.52202/079017-1922). *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, 60162–60191. arXiv:2406.16964.
[^zhang2025whenmultimodal]: Zhang, X., Han, B., Fang, H. et al. (2025). [When does multimodality lead to better time series forecasting?](https://arxiv.org/abs/2506.21611). arXiv:2506.21611.
[^sridhar2026textsensitivity]: Sridhar, K., Gupta, A., Pradhan, N. et al. (2026). [Semantics or structure? Auditing text sensitivity in multimodal time-series forecasting](https://arxiv.org/abs/2608.22321). arXiv:2608.22321.
[^chen2026musebench]: Chen, P., Zhuang, Z., Chen, H. et al. (2026). [Beyond numerical time series: A unified benchmark for multimodal forecasting with heterogeneous context](https://arxiv.org/abs/2609.15087). arXiv:2609.15087.
[^xue2023lmload]: Xue, H., Salim, F. D. (2023). [Utilizing language models for energy load forecasting](https://doi.org/10.1145/3600100.3623730). *Proceedings of the 10th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys '23)*, 224–227. arXiv:2310.17788.
[^bi2025nswepnews]: Bi, Z., Huang, L., Jin, H. et al. (2025). [NSW-EPNews: A news-augmented benchmark for electricity price forecasting with LLMs](https://arxiv.org/abs/2506.11050). arXiv:2506.11050.
[^yi2026traceepf]: Yi, X., Yuan, Z., Lestas, I. (2026). [TRACE: A reproducible benchmark for electricity price forecasting with official operational text](https://arxiv.org/abs/2610.02256). arXiv:2610.02256.
[^zhou2026cmllm]: Zhou, Z., Li, Y., Yu, X. et al. (2026). [A causal-guided multimodal large language model for generalized power system time-series data analytics](https://doi.org/10.1109/TSG.2026.3714202). *IEEE Transactions on Smart Grid*. arXiv:2511.07777.
[^chang2025timeimm]: Chang, C., Hwang, J., Shi, Y. et al. (2025). [Time-IMM: A dataset and benchmark for irregular multimodal multivariate time series](https://doi.org/10.52202/085713-1533). *Advances in Neural Information Processing Systems 38 (NeurIPS 2025), Datasets and Benchmarks Track*, 51421–51470. arXiv:2506.10412.
[^wu2024missingmodality]: Wu, R., Wang, H., Chen, H. et al. (2024). [Deep multimodal learning with missing modality: A survey](https://arxiv.org/abs/2409.07825). *Transactions on Machine Learning Research*. arXiv:2409.07825.
[^chen2026horai]: Chen, P., Wang, S., Hu, S. et al. (2026). [Empowering time series analysis with large-scale multimodal pretraining](https://arxiv.org/abs/2602.05646). arXiv:2602.05646.

---
[← Previous: 2.6 Architectures: Transformers, GNNs, Neural Operators](2-6-architectures.html) · [Back to Chapter 2](index.html) · [Next: 2.8 Evaluation Criteria for UES Foundation Models →](2-8-ues-fm-evaluation-criteria.html)
