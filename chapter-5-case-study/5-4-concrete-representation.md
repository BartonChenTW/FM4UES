---
title: "5.4 A Concrete Proposed Representation"
parent: Chapter 5 — Case Study
nav_order: 4
status: draft
last_reviewed: 2026-09-11
---

# 5.4 A Concrete Proposed Representation
{: .no_toc }

{% include page-status.html %}

**In one line:** a heterogeneous bipartite graph of carrier-bus tokens and device tokens, with carrier quality as an explicit ordered dimension, over a three-level temporal hierarchy with a storage carry channel.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## 5.4.1 Why bipartite rather than conversion-on-edges

An edge has exactly two endpoints, so a CHP (gas in → electricity *and* heat out) or a heat pump (electricity + ambient source → heat) cannot be one edge. Making devices first-class nodes with typed ports to multiple carrier-buses handles multi-input/multi-output cleanly and gives a place to attach technology embeddings — which is what lets the model generalise to a hub containing a device configuration never seen during pretraining.

## 5.4.2 What makes this different from GridFM, not a relabelling

1. **Carrier quality is not fungible.** Heat at 80 °C and heat at 35 °C are different commodities with an ordering between them. Electricity has no analogue. The physics loss must forbid free upgrading, and the quality ordering can be encoded structurally as a directed edge. See [§5.6](5-6-physics-loss.html).
2. **The token must carry a time window, not a snapshot.** GridFM-v0 is snapshot-based — one solved power flow per sample. Hubs are inherently inter-temporal because of storage, and seasonal storage means the year cannot be chopped into independent windows. See the temporal hierarchy in [§5.5](5-5-token-schema.html).

## 5.4.3 Worked example — a 50-building district

**Carrier-buses**

| ID | Carrier | Quality | Role |
| :--- | :--- | :--- | :--- |
| B1 | Electricity | 0.4 kV | Internal LV |
| B2 | Electricity | MV | Grid connection / import |
| B3 | Heat | 75 °C | DH supply |
| B4 | Heat | 45 °C | DH return / LT loop |
| B5 | Gas | — | Import |
| B6 | Ambient | ~12 °C | Ground source |

**Devices**

| ID | Technology | Ports |
| :--- | :--- | :--- |
| D1 | CHP | B5 in → B1, B3 out |
| D2 | Heat pump | B1, B6 in → B4 out |
| D3 | Boiler | B5 in → B3 out |
| D4 | PV | exogenous irradiance → B1 out |
| D5 | Battery | B1 ↔ B1, state |
| D6 | Hot water tank | B3 ↔ B3, state |
| D7 | Borehole seasonal storage | B4 ↔ B6, state, large time constant |
| D8 | Transformer | B2 ↔ B1 |

**Quality edges:** B3 → B4 permitted (downgrade via load and mixing); B4 → B3 forbidden without a device. This one-way relation has no analogue in GridFM and is the clearest illustration of why multi-carrier systems need a different token from a grid bus (see [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html)).

**The numbers work.** A 50-building district with ~30 carrier-buses and ~40 devices is 70 node tokens. Per year that is 365 × 70 ≈ 25,000 tokens — within reach given TimesFM 2.5 already runs 16 k context at 200 M parameters,[^das2024timesfm] and cross-day attention only needs to be dense for the handful of storage nodes (see the temporal hierarchy in [§5.5](5-5-token-schema.html)). The flat alternative is 8760 × 70 ≈ 613,000 tokens, which is not tractable.

[^das2024timesfm]: Das, A., Kong, W., Sen, R., Zhou, Y. (2024). [A decoder-only foundation model for time-series forecasting](https://arxiv.org/abs/2310.10688). ICML 2024. arXiv:2310.10688. TimesFM 2.5's 16k-context, 200M-parameter release is a later version documented at the [project repository](https://github.com/google-research/timesfm), not in the original paper.

---
[← Previous: 5.3 Data Generation](5-3-data-generation.html) · [Next: 5.5 Token Schema and Temporal Hierarchy →](5-5-token-schema.html)
