---
title: "2.6 Self-Supervision, Fine-Tuning, Scaling Laws"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 6
status: draft
last_reviewed: 2026-09-11
---

# 2.6 Self-Supervised Pretraining, Fine-Tuning, and Scaling Laws
{: .no_toc }

{% include page-status.html %}

ML-basics content for readers arriving from the energy-systems side. If you already work with these concepts, skip ahead to [§2.7](2-7-architectures.html).
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Self-supervised pretraining

Conventional supervised learning needs a human (or a solver) to label every training example: this input, this correct output. Labels are the expensive part — for many domains, far more expensive than the raw data itself.

**Self-supervision sidesteps this by manufacturing labels from the data itself.** The recipe: take an unlabelled example, deliberately hide part of it, and train the model to predict the hidden part from what remains. No external labelling step is needed, because the "label" is just the part that was hidden.

Two common patterns:

- **Masking.** Hide a random subset of the input (a word in a sentence, a [patch](../appendices/a-glossary.html#patch) in an image, a bus's state in a grid) and train the model to reconstruct it from context. This is how [GridFM-v0](../appendices/d-model-index.html#gridfm) pretrains — see [§2.4.2](2-4-2-power-grid-fms.html).
- **Next-step / autoregressive prediction.** Show the model a prefix and train it to predict what comes next (the next word, the next timestep). This is how [Chronos](../appendices/d-model-index.html#chronos) and most language models pretrain.

The point of self-supervision is not that it is free — pretraining runs are large and expensive in compute — but that it removes the *labelling* bottleneck, which lets pretraining scale to enormous, broad, cheaply-collected datasets in a way that supervised learning on hand-labelled data cannot.

{: .note }
In these notes' domain, simulators are an alternative to both: a simulator can generate unlimited *labelled* examples (configuration in, trajectory out) without any human labelling step at all. This is why [§4.10.1](../chapter-4-directions/4-10-building-it.html#4101-data-generation-and-sampling-design) treats "the training distribution is a design decision" as the central data question here, rather than "how do we get labels" — see also the discussion of synthetic data limits in [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html).

## Fine-tuning

[Fine-tuning](../appendices/a-glossary.html#fine-tuning) takes a pretrained model and adjusts it — usually with a comparatively small amount of additional, task-specific data — so that it performs well on a narrower target. The pretrained weights are not thrown away; they are the starting point, and typically only a modest number of additional gradient updates are needed to specialise.

**The domain analogy that works well here:** fine-tuning is comparable to calibrating a general model against local measurements. A building simulation model built from generic assumptions about materials and occupancy becomes more accurate for one specific building once it is calibrated against a few months of that building's actual meter data. Fine-tuning is the same move applied to a learned model: the broad pretraining supplies general structure, and a small amount of local data adapts it.

Two adaptation regimes worth distinguishing:

- **Full fine-tuning** updates all of the model's parameters. Most accurate, most compute, and the risk of forgetting general capability while over-fitting to the small local set.
- **Parameter-efficient fine-tuning (PEFT)**, such as LoRA (Low-Rank Adaptation, which injects small trainable rank-decomposition matrices into each layer instead of updating the full weight matrices),[^hu2021lora] updates only a small additional set of parameters while freezing the pretrained ones. Cheaper, faster, and the usual practical choice at modest compute budgets — see [§4.9.1](../chapter-4-directions/4-9-1-methods-tier1.html) for where this is recommended in these notes' build paths.

**[Zero-shot](../appendices/a-glossary.html#zero-shot)** means using the pretrained model on a new instance with no additional training at all — the strongest form of transfer, and the first thing worth trying before any fine-tuning effort (see [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html)).

## Scaling laws

A scaling law is an empirical relationship between a model's size (or its training data volume, or the compute spent training it) and its performance — typically, error falls off as a predictable power-law function of these quantities as they grow. Scaling laws were first established clearly for language models, where cross-entropy loss was shown to scale as a power law with model size, dataset size, and training compute across more than seven orders of magnitude,[^kaplan2020scaling] and are part of what justified the foundation-model bet there: if performance improves predictably with scale, spending more compute is a reliable way to buy capability.

**Why this matters for judging any FM proposal, including the case study in [Chapter 5](../chapter-5-case-study/index.html):** a scaling law is not guaranteed to hold in a new domain. It has to be demonstrated, and demonstrating it early is cheap relative to committing to a large model. [§4.9.3 (Tier 3)](../chapter-4-directions/4-9-3-methods-tier3.html) recommends running a small scaling study — training on 10², 10³, 10⁴ samples and fitting the error curve — before committing to a large data-generation campaign, for exactly this reason.

Time-series foundation models are a directly relevant recent example: [Toto 2.0](../appendices/d-model-index.html#toto-2-0) is reported as the first time-series model to demonstrate classic scaling-law behaviour, with a single training recipe producing reliable forecast-quality improvements across a 625× range of model size (4M to 2.5B parameters).[^khwaja2026toto2] That this needed demonstrating, and was notable when it was, is itself informative — scaling behaviour in a new data modality is a finding, not an assumption.

**And "scale" does not only mean parameters.** An empirical study on commercial building energy consumption, spanning architectures from RNNs through fine-tuned open-source [foundation models](../appendices/a-glossary.html#foundation-model), reports that dataset heterogeneity and model architecture affected post-training forecasting performance more than parameter count did — isolated by comparing two curated ComStock subsets identical in size and region but differing in building-type diversity.[^bose2024rnnstofm] For these notes that reframes the planning question in [§4.10.1](../chapter-4-directions/4-10-building-it.html#4101-data-generation-and-sampling-design): the open question for urban energy systems is not "how large a model" but **what kind of diversity in the training distribution actually produces transferable knowledge** — which is a sampling-design decision, made before any model is trained, not a budget decision made after.

[^khwaja2026toto2]: Khwaja, E., Lettieri, C., Woo, G. et al. (2026). [Toto 2.0: Time series forecasting enters the scaling era](https://arxiv.org/abs/2605.20119). arXiv:2605.20119.
[^kaplan2020scaling]: Kaplan, J., McCandlish, S., Henighan, T. et al. (2020). [Scaling laws for neural language models](https://arxiv.org/abs/2001.08361). arXiv:2001.08361.
[^hu2021lora]: Hu, E. J., Shen, Y., Wallis, P. et al. (2021). [LoRA: Low-rank adaptation of large language models](https://arxiv.org/abs/2106.09685). arXiv:2106.09685.
[^bose2024rnnstofm]: Bose, S., Li, Y., Van Sant, A., Zhang, Y., Kim, K. (2024). [From RNNs to foundation models: An empirical study on commercial building energy consumption](https://arxiv.org/abs/2411.14421). arXiv:2411.14421. NeurIPS 2024 Workshop on Time Series in the Age of Large Models.

---
[← Previous: 2.5 What Does Not Exist Yet](2-5-what-does-not-exist-yet.html) · [Next: 2.7 Architectures →](2-7-architectures.html)
