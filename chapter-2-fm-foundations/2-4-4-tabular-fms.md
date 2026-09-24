---
title: "2.4.4 Tabular FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 4
status: draft
last_reviewed: 2026-09-24
---

# 2.4.4 Tabular Foundation Models — the Cell as a Basic Element
{: .no_toc }

{% include page-status.html %}

A distinct family, and a distinct answer to the representation question. Worth understanding properly because it is a serious competing hypothesis to any bespoke building representation.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

**What the cell is.** A cell is a single entry in a table — the value where one row meets one column (building #47's construction year, 1962). Most machine learning treats the **row** as the basic unit: a building becomes a feature vector read as one thing. Tabular FMs go one level finer. Each individual value gets its own representation, and the model attends in two directions — across the row (how does this building's construction year relate to its floor area and heating system?) and down the column (how does it compare to the construction years of all other buildings?). TabPFN v2 assigns a representation to each table cell and applies row-wise and column-wise attention, which its authors report makes the architecture invariant to the order of both samples and features.[^hollmann2025tabpfnv2] The original TabPFN still took each training sample — a whole row — as one item of a set-valued input;[^hollmann2022tabpfn] the per-cell design arrived with v2.

**Why it matters.** It removes the fixed schema. A conventional surrogate needs the same columns in the same order every time; change the input list and you refit. If the model reads cells and treats column order as arbitrary, a table with different columns is still readable — one pretrained model applied to a Swiss dataset, then a Dutch one recording different attributes, without retraining. TabPFN v2 introduced a randomised feature-token mechanism to handle heterogeneous feature spaces and support transfer across datasets with differing feature semantics, and is pretrained entirely on synthetic data generated from structural causal models rather than any real table.[^hollmann2025tabpfnv2] **This is a direct attack on the mixed-information-types problem** described in [§2.3.2](2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings).

**Mechanism.** These are prior-data fitted networks: pretrained on a large distribution of synthetic tasks so that conditioning on a context table at test time approximates Bayesian inference under the learned prior. Prediction happens in a single forward pass on labelled examples, with no dataset-specific gradient updates.

**Against the four requirements.**

- *Unambiguous:* yes, cleanly — a cell is a recorded value, involving no modeller's judgement, unlike a thermal zone.
- *Stable in meaning:* partly — the model must infer what a column means from the values in it rather than being told.
- *Composable:* yes, trivially.
- *Scale-independent:* bounded — context size limits how much table fits at once.

It therefore scores better than any element in §2.3.2(a)–(d), which is why it belongs in the analysis rather than being dismissed.

**Where it breaks for energy systems.** A cell holds one value. An hourly profile is 8760 values — not a cell, not a row, and not the table shape at all. Either collapse the profile into summary statistics, losing the temporal structure that matters for retrofit and dispatch assessment, or spread it across 8760 columns, which defeats the purpose and exhausts the context budget.

**Sharpened statement:** the cell is a very good basic element for describing what a system *is*, and no help at all for what it *does* over time.

**Documented limitations to design around.**

- Highly sensitive to distribution shift; incorporating source data with a differing distribution can cause negative transfer and degrade target accuracy.[^lin2026contextconstrained] This maps directly onto the held-out-typology test (P3 in [§2.3.3](2-3-choosing-a-basic-element.html#233-representation-strategies-and-testable-predictions)).
- Bounded by maximum context size. TabPFN-2.5 scaled in-context learning to roughly 50,000 samples and 2,000 features;[^priorlabs2025tabpfn25] TabICL uses a two-stage, column-then-row attention architecture reaching around 500,000 samples on affordable hardware.[^qu2025tabicl]

**Predicted profile:** strong on scalar outcomes (P1), structurally weak on hourly profiles (P2), questionable across unseen typologies (P3). Tabular FMs are best understood as **R1 with a foundation model attached** — which makes them a more informative baseline than gradient boosting alone.

[^hollmann2022tabpfn]: Hollmann, N., Müller, S., Eggensperger, K., Hutter, F. (2023). [TabPFN: A transformer that solves small tabular classification problems in a second](https://arxiv.org/abs/2207.01848). ICLR 2023. arXiv:2207.01848
[^hollmann2025tabpfnv2]: Hollmann, N., Müller, S., Purucker, L. et al. (2025). [Accurate predictions on small data with a tabular foundation model](https://doi.org/10.1038/s41586-024-08328-6). *Nature*, 637, 319–326.
[^priorlabs2025tabpfn25]: Prior Labs (2025). [TabPFN-2.5: Advancing the state of the art in tabular foundation models](https://arxiv.org/abs/2511.08667). arXiv:2511.08667
[^qu2025tabicl]: Qu, J., Holzmüller, D., Varoquaux, G., Le Morvan, M. (2025). [TabICL: A tabular foundation model for in-context learning on large data](https://arxiv.org/abs/2502.05564). ICML 2025. arXiv:2502.05564
[^lin2026contextconstrained]: Lin, Y., Li, S. (2026). [Context-constrained transfer learning for tabular foundation models via data distillation](https://arxiv.org/abs/2607.04809). arXiv:2607.04809

---
[← Previous: 2.4.3 Clean-Energy Forecasting FMs](2-4-3-clean-energy-forecasting-fms.html) · [Next: 2.4.5 Geospatial & Weather FMs →](2-4-5-geospatial-weather-fms.html)
