---
title: "1.2 FMs in One Page"
parent: Chapter 1 — Background
nav_order: 2
status: draft
last_reviewed: 2026-09-11
---

# 1.2 FMs in One Page: What Changed in AI Since ~2018
{: .no_toc }

{% include page-status.html %}

A short, non-technical orientation for readers with no machine learning background. If you already know what a [foundation model](../appendices/a-glossary.html#foundation-model) is, skip to [§1.3](1-3-fm-landscape-by-domain.html).
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## The old way: one model per task

Before roughly 2018, a typical machine learning project trained one model for one narrow task, on data collected for that task alone. A load-forecasting model for building A was trained on building A's meter data and was not expected to say anything useful about building B. If the task changed even slightly — a new building, a new horizon, a new set of inputs — the model was retrained, often from a blank slate.

## The new way: pretrain once, adapt many times

Since around 2018, a different recipe has taken over large parts of AI: train one very large model on a very large, broad collection of data, using a [self-supervised](../appendices/a-glossary.html#self-supervised-pretraining) objective — the model learns by predicting parts of its own input that were deliberately hidden from it (a missing word, a masked [patch](../appendices/a-glossary.html#patch), the next value in a sequence), rather than needing a human to label every example. This pretraining run is expensive, but it is done once. The resulting model is then **adapted** — with a small amount of additional data, or sometimes none at all — to many different downstream uses.

This is the **foundation model** (FM) recipe: broad pretraining, transfer to new instances, reuse across many tasks. GPT-class language models, image models like [SAM](../appendices/d-model-index.html#sam),[^kirillov2023sam] and weather models like [GraphCast](../appendices/d-model-index.html#graphcast)[^lam2023graphcast] are all instances of the same underlying pattern applied to different kinds of data.

## Why this matters for a domain expert

Three consequences follow directly from the recipe, and they are the reason this book exists:

1. **The unit of learning changes.** A foundation model needs something to pretrain on that is plentiful, comparable across instances, and assembles into whole systems — a *[basic element](../appendices/a-glossary.html#basic-element)*. Text has the word/subword token; images have the patch; power grids have the bus. Finding (or failing to find) this element for a given domain is the central technical question, not an implementation detail. [Chapter 2](../chapter-2-fm-foundations/index.html) develops this in full.

2. **The economics change.** A model trained once and reused across many future studies has a fundamentally different cost structure from a bespoke model trained and discarded within a single project. This is the amortisation argument that recurs throughout the book (see [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html) and [Chapter 5](../chapter-5-case-study/index.html)).

3. **What "understanding" means changes.** A foundation model does not need to be told the equations governing a system to produce useful output — it infers regularities from data. This is powerful where equations are known but expensive to solve (a plausible substitute), and risky where the model must extrapolate beyond what it has seen, because nothing forces it to respect physics it was never shown examples of. [§15](../chapter-5-case-study/5-6-physics-loss.html) and related sections return to how this risk is managed.

{: .note }
This page deliberately does not cover architectures ([transformers](../appendices/a-glossary.html#transformer), graph neural networks, etc.) or training mechanics (self-supervision, [fine-tuning](../appendices/a-glossary.html#fine-tuning), scaling laws) — those are covered properly, with more precision, in [Chapter 2](../chapter-2-fm-foundations/index.html) once the domain motivation is established.

[^kirillov2023sam]: Kirillov, A., Mintun, E., Ravi, N. et al. (2023). Segment Anything. *ICCV 2023*. [arXiv:2304.02643](https://arxiv.org/abs/2304.02643)
[^lam2023graphcast]: Lam, R., Sanchez-Gonzalez, A., Willson, M. et al. (2023). [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336). *Science*, 382(6677), 1416–1421.

---
[← Previous: 1.1 What a UES Contains](1-1-what-is-ues.html) · [Next: 1.3 The FM Landscape by Domain →](1-3-fm-landscape-by-domain.html)
