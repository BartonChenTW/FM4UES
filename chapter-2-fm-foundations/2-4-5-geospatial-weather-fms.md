---
title: "2.4.5 Geospatial & Weather FMs"
parent: "2.4 Existing FMs Relevant to Energy"
grand_parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 5
status: draft
last_reviewed: 2026-09-11
---

# 2.4.5 Geospatial & Weather Foundation Models
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

A family that does not target energy systems directly but is a plausible input encoder for them, and is worth knowing for that reason.

**[GraphCast](../appendices/d-model-index.html#graphcast)** performs medium-range global weather forecasting with a graph neural network (encode-process-decode) operating on an icosahedral multi-mesh over the sphere.[^lam2023graphcast] It and similar models ([FengWu](../appendices/d-model-index.html#fengwu), [Aurora](../appendices/d-model-index.html#aurora)) demonstrate that physical fields on a spatiotemporal grid support the foundation-model pattern at global scale.

**[Prithvi](../appendices/d-model-index.html#prithvi)** is a Vision Transformer masked-autoencoder pretrained over multispectral, multitemporal satellite patches, developed by NASA and IBM Research.[^jakubik2023prithvi] **[Prithvi-EO-2.0](../appendices/d-model-index.html#prithvi-eo-2-0)** scales this up.[^szwarcman2024prithvieo2] **[Granite-GFM](../appendices/d-model-index.html#granite-gfm)** is built on [Prithvi-SWIN-L](../appendices/d-model-index.html#prithvi-swin-l), a Swin Transformer version of the Prithvi model, and estimates land surface temperature at 30 m resolution and hourly frequency for arbitrary cities.[^bhamjee2024granitelst] No paper describes Prithvi-SWIN-L itself: IBM's model card points to the original Prithvi paper, which covers the Vision Transformer version and mentions Swin only as future work.

**Relevance to urban energy systems.** Urban heat islands drive peak cooling load and grid stress simultaneously, which makes a weather- or microclimate-conditioned building energy model a plausible fusion target. No existing paired dataset couples geospatial/weather foundation model output with building load or UBEM data at foundation-model scale — this would need to be built as a corpus, not simply assembled from existing releases. This is flagged as a candidate direction in [§4.2](../chapter-4-directions/4-2-fms-for-building-stocks.html) and is one of the less mature intersections surveyed in this book.

{: .note }
This sub-section is intentionally brief: geospatial/weather FMs are adjacent rather than core to this book's subject, and the honest state of the art here is "plausible encoder, no demonstrated fusion with UES data yet."

[^lam2023graphcast]: Lam, R., Sanchez-Gonzalez, A., Willson, M. et al. (2023). [Learning skillful medium-range global weather forecasting](https://doi.org/10.1126/science.adi2336). *Science*, 382(6677), 1416–1421.
[^jakubik2023prithvi]: Jakubik, J., Roy, S., Phillips, C. E. et al. (2023). [Foundation models for generalist geospatial artificial intelligence](https://arxiv.org/abs/2310.18660). arXiv:2310.18660.
[^szwarcman2024prithvieo2]: Szwarcman, D., Roy, S., Fraccaro, P. et al. (2024). [Prithvi-EO-2.0: A versatile multi-temporal foundation model for Earth observation applications](https://arxiv.org/abs/2412.02732). arXiv:2412.02732.
[^bhamjee2024granitelst]: Bhamjee, M., Gaffoor, Z., Govindasamy, T. et al. (2024). [granite-geospatial-land-surface-temperature](https://huggingface.co/ibm-granite/granite-geospatial-land-surface-temperature). IBM Research, Hugging Face model card, Apache-2.0.

---
[← Previous: 2.4.4 Tabular FMs](2-4-4-tabular-fms.html) · [Next: 2.4.6 Load & Smart-Meter Forecasting FMs →](2-4-6-load-forecasting-fms.html)
