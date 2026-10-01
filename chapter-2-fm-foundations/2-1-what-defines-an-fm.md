---
title: "2.1 What Defines a Foundation Model"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 1
status: draft
last_reviewed: 2026-09-11
redirect_from: /02-fm-fundamentals.html
---

# 2.1 What Makes a Model a "Foundation Model"
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

The term was coined to describe models trained on broad data at scale that can be adapted to a wide range of downstream tasks.[^bommasani2021opportunities] The pattern has since been surveyed at length across text, image, graph and other modalities.[^zhou2023pfmsurvey] This book uses three properties, all required, as the operational version of that idea:

1. **Pretrained on a broad distribution**, not on the single instance it will be used on.
2. **Transfers** — it is useful on instances it has never seen, [zero-shot](../appendices/a-glossary.html#zero-shot) or with light adaptation.
3. **Serves multiple downstream tasks**, not one.

The contrast that matters here is with a **[surrogate](../appendices/a-glossary.html#surrogate)**: a surrogate is trained on one system to approximate one model, and it is discarded when that study ends.[^alizadeh2020surrogate] A [foundation model](../appendices/a-glossary.html#foundation-model) is trained once across many systems and amortised across many studies. See [§2.8](2-8-surrogates-vs-fms.html) for this contrast in full.

Both are approximation. The difference is entirely in the training distribution and the transfer claim. **This distinction is the whole argument for doing foundation-model work in this domain**, because the existing multi-energy surrogate literature is almost entirely of the first kind.

{: .note }
Property 3 is the one most often quietly dropped. A model that amortises one solve for one task family is a transferable surrogate, not a foundation model. This matters for framing: calling it an FM without multi-task evidence invites exactly the criticism that is hardest to answer.

[^bommasani2021opportunities]: Bommasani, R., Hudson, D. A., Adeli, E. et al. (2021). [On the opportunities and risks of foundation models](https://arxiv.org/abs/2108.07258). arXiv:2108.07258.
[^zhou2023pfmsurvey]: Zhou, C., Li, Q., Li, C. et al. (2023). [A comprehensive survey on pretrained foundation models: A history from BERT to ChatGPT](https://arxiv.org/abs/2302.09419). arXiv:2302.09419.
[^alizadeh2020surrogate]: Alizadeh, R., Allen, J. K., Mistree, F. (2020). [Managing computational complexity using surrogate models: A critical review](https://doi.org/10.1007/s00163-020-00336-7). *Research in Engineering Design*, 31(3), 275–298.

---
[← Back to Chapter 2](index.html) · [Next: 2.2 The Five Design Decisions →](2-2-five-design-decisions.html)
