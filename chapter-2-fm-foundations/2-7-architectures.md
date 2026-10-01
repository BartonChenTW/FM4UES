---
title: "2.7 Architectures: Transformers, GNNs, Neural Operators"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 7
status: draft
last_reviewed: 2026-10-01
---

# 2.7 Architectures: Transformers, Graph Neural Networks, Neural Operators
{: .no_toc }

{% include page-status.html %}

ML-basics content for readers arriving from the energy-systems side. Covers what each architecture family actually does, aimed at the level needed to follow [Chapter 4](../chapter-4-directions/index.html) and [Chapter 5](../chapter-5-case-study/index.html) — not a complete technical treatment.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

Architecture (D3 in [§2.2](2-2-five-design-decisions.html)) is determined largely by what structure the data has. This section covers the three families used throughout this book, and how they are combined when a model takes in several kinds of data at once.

## Transformers and attention

A transformer processes a set of tokens (see [§2.2](2-2-five-design-decisions.html) for what a token is in this domain) using a mechanism called **attention**: for every token, the model computes how much it should "attend to" every other token when forming its own updated representation, dispensing with recurrence and convolution entirely.[^vaswani2017attention] Concretely, this lets a heat pump's token be updated in light of the electricity bus it draws from and the heat bus it feeds, without the architecture needing to be told in advance which tokens are related — the model learns the relevant relationships from data.

This is why transformers dominate sequence and largely-unstructured data: attention is a general-purpose way to let any element influence any other, at the cost of computing a relationship for every pair of tokens (**quadratic cost** in the number of tokens), which is the practical limit on how many tokens a transformer can process at once. Patching — grouping several raw values into one token, as time-series FMs do (see [§2.4.1](2-4-1-time-series-fms.html)) — is the standard way to buy longer effective context within this budget.

**Cross-attention**, used repeatedly in this book (e.g. [§2.3.3](2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions), R2), is the same mechanism applied between two different sets of tokens: one set (say, building attributes) modulates how another set (a demand profile) is interpreted, rather than simply being appended to it as extra input columns.

## Graph neural networks (GNNs)

Where a transformer's attention considers all pairs of tokens by default, a **graph neural network** works on data that already has an explicit relational structure — a graph of nodes and edges — and restricts computation to follow that structure. The standard mechanism is **message passing**: each node updates its representation by aggregating information from its immediate neighbours, and stacking several such layers lets information propagate further across the graph.

This is the natural architecture whenever the data genuinely is a network — bus/line topology in power systems, or hub/pipe topology in district heating (see [§4.9.2](../chapter-4-directions/4-9-2-methods-tier2.html) for this book's treatment of GNNs at district scale). A **heterogeneous** GNN extends this to graphs with multiple distinct node and edge types (a heat pipe is not the same edge type as a power line), which is the relevant case for multi-carrier systems.

GNNs and transformers are not mutually exclusive: a common and effective pattern is local message passing for physically-local interactions, combined with a global attention layer for system-wide correlations that a purely local mechanism would take many layers to propagate (see [§4.9.2](../chapter-4-directions/4-9-2-methods-tier2.html)).

## Neural operators

Both transformers and GNNs learn mappings between finite-dimensional vectors (or sets of vectors). A **neural operator** instead learns a mapping between *functions* — for example, a mapping from a boundary-condition function to the resulting temperature field, rather than from a fixed set of sample points to another fixed set of sample points. This matters when the underlying physics is genuinely continuous (a temperature field along a pipe, a pressure field in a network), because the model can then be evaluated at any spatial resolution, not only the one it was trained on.

Two concrete families: the **Fourier Neural Operator** learns mappings between function spaces using spectral (Fourier-domain) parameterisations, targeting families of parametric partial differential equations rather than one fixed instance;[^li2020fno] **DeepONet** learns solution operators directly, splitting the network into a branch that encodes the input function and a trunk that encodes the query location, based on a universal approximation theorem for operators.[^lu2021deeponet] See [§4.9.2](../chapter-4-directions/4-9-2-methods-tier2.html) for when to choose a neural operator over a GNN in this domain.

## Multimodal models

A **modality** is one kind of data with its own structure. In urban energy systems the usual ones are:

- **time series:** a meter reading every hour, a temperature record
- **attributes:** a building's floor area, construction year and heating system, which do not change from hour to hour
- **fields:** a weather map or a satellite image over an area
- **graphs:** a grid or pipe network
- **text:** a planning document, a survey answer

A **multimodal model** takes in more than one of these and learns how they relate.

No single architecture suits all of them, so a multimodal model usually gives each modality its own **encoder**: a time-series encoder for the meter data, a small network for the attributes, a GNN for the network, and so on. Each encoder turns its input into tokens of the same size. The model then combines those tokens in one of three common ways:

- **A shared space.** Separate encoders are trained so that matching inputs land close together. CLIP trains an image encoder and a text encoder to predict which caption goes with which image, on 400 million pairs, and can then classify images it was never trained on by comparing them with text descriptions.[^radford2021clip]
- **Cross-attention.** One modality's tokens attend to another's, so the second changes how the first is read (see the transformer section above). This is the pattern this book proposes most often.
- **One token stream.** All modalities are turned into tokens and processed together by a single transformer. Janus does this for images and text, with separate visual encoders for understanding an image and for generating one, both feeding one shared transformer.[^wu2024janus]

**A worked example from this domain.** Suppose the task is to forecast one building's electricity use for the next day. Three modalities are available:

1. **Meter history** (time series). A pretrained time-series encoder ([§2.4.1](2-4-1-time-series-fms.html)) turns the last few weeks into patch tokens. These carry the building's habits: its daily and weekly rhythm, its base load.
2. **Building attributes** (attributes). An attribute encoder turns floor area, construction year, heating system and occupancy type into a handful of tokens. These say *why* the building behaves as it does. They also give the model something to go on for a building with little or no history.
3. **Weather forecast** (time series, known in advance). Its own encoder, or a set of covariates, turns tomorrow's temperature and irradiance into tokens.

The meter tokens then cross-attend to the attribute and weather tokens. A cold morning raises the forecast more for a poorly insulated building with electric heating than for a well-insulated one with a gas boiler, because the attributes change how the model reads the weather.

Three things make this harder than it sounds. The modalities change at different rates: attributes are fixed, weather is hourly, meter history may be every 15 minutes. Some modalities are often missing: most buildings have no household survey, and many have no reliable register entry. And the training data has to pair the modalities building by building, which measured data rarely does ([§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)).

**Where the book uses this.**
- [§2.3.3](2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions): describing a building's time series by its attributes.
- [§4.8](../chapter-4-directions/4-8-candidate-subfields.html): the metadata-conditioned load FM, which is the worked example above at scale, and the grid-load bridge, which pairs load tokens with a grid graph.
- [§5.7](../chapter-5-case-study/5-7-module-decomposition.html) and [§5.1](../chapter-5-case-study/5-1-roadmap.html#phase-2-year-24--multimodal-conditioning): the case study's encoder stack for demand, weather, technology, topology and market, and the roadmap phase that fuses them.
- [§4.11](../chapter-4-directions/4-11-ecosystem.html): whether one multimodal model could cover the whole urban energy system, and why that is harder than for weather.

## The common thread

All three families are ways of building in an **inductive bias** — an assumption about the data's structure baked into the architecture rather than left for the model to discover from scratch. Sequence position for transformers, graph adjacency for GNNs, function-space continuity for neural operators. Choosing badly does not make learning impossible, but it makes it need far more data to discover a structure the architecture could have been given for free — which is exactly why D1–D3 in [§2.2](2-2-five-design-decisions.html) are treated as the central design decisions in this book, not implementation detail to be settled last.

[^vaswani2017attention]: Vaswani, A., Shazeer, N., Parmar, N. et al. (2017). [Attention is all you need](https://arxiv.org/abs/1706.03762). NeurIPS 2017. arXiv:1706.03762
[^li2020fno]: Li, Z., Kovachki, N., Azizzadenesheli, K. et al. (2021). [Fourier neural operator for parametric partial differential equations](https://arxiv.org/abs/2010.08895). ICLR 2021. arXiv:2010.08895
[^radford2021clip]: Radford, A., Kim, J. W., Hallacy, C. et al. (2021). [Learning transferable visual models from natural language supervision](https://arxiv.org/abs/2103.00020). *ICML 2021*, PMLR 139, 8748–8763. arXiv:2103.00020.
[^wu2024janus]: Wu, C., Chen, X., Wu, Z. et al. (2024). [Janus: Decoupling visual encoding for unified multimodal understanding and generation](https://arxiv.org/abs/2410.13848). arXiv:2410.13848.
[^lu2021deeponet]: Lu, L., Jin, P., Pang, G. et al. (2021). [Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators](https://doi.org/10.1038/s42256-021-00302-5). *Nature Machine Intelligence*, 3(3), 218–229.

---
[← Previous: 2.6 Self-Supervision, Fine-Tuning, Scaling Laws](2-6-scaling-laws.html) · [Next: 2.8 Surrogates vs Foundation Models →](2-8-surrogates-vs-fms.html)
