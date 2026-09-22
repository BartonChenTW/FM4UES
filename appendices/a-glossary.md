---
title: Appendix A — Glossary
parent: Appendices
nav_order: 1
status: draft
last_reviewed: 2026-09-11
redirect_from: /appendix-a-glossary.html
---

# Appendix A — Glossary
{: .no_toc }

{% include page-status.html %}

| Term | Meaning |
| :--- | :--- |
| **Amortised optimisation** | Learning to produce optimisation solutions directly, paying training cost once |
| **Any-variate attention** | Attention scaling to arbitrary numbers of input series |
| **Basic element** | The unit a model treats as indivisible — the learned-model counterpart of an element in a discretised simulation. Judged against the four requirements in [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion) |
| **Cell** | A single entry in a table, where one row meets one column; the basic element of tabular foundation models ([§2.4.4](../chapter-2-fm-foundations/2-4-4-tabular-fms.html)) |
| **Cross-attention** | Mechanism by which one set of information (e.g. building attributes) modulates how another is interpreted (e.g. a demand profile), rather than simply being appended to it |
| **DAE** | Differential-algebraic equations — the structure of Modelica-type models |
| **Decision space** | The set of possible interventions on a system, as distinct from its state space; see [G9](../chapter-6-outlook/6-1-open-gaps.html#g9) |
| **DINO** (self-distillation with no labels) | Self-supervised vision transformer trained by having a student network match a teacher's output with no labelled data. See [§1.3](../chapter-1-background/1-3-fm-landscape-by-domain.html) |
| **Energy hub** | Node converting/storing/dispatching multiple carriers via a coupling matrix ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)) |
| **Fine-tuning** | Adjusting a pretrained model to a specific case with a small amount of additional data — comparable to calibrating a model against measurements. See [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html) |
| **Foundation model** | Pretrained on a broad distribution; transfers to unseen instances; serves multiple tasks |
| **In-context learning** | Making predictions by conditioning on labelled examples supplied at inference time, with no parameter updates |
| **MILP** | Mixed-integer linear program — LP plus discrete decisions |
| **Neural operator** | Network learning mappings between function spaces rather than finite vectors. See [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) |
| **Patch** | A contiguous block of timesteps treated as one token |
| **PFN (prior-data fitted network)** | Model pretrained across a distribution of synthetic tasks so that conditioning on a context approximates Bayesian inference under the learned prior |
| **ROM** | Reduced-order model — compresses high-dimensional state to a latent manifold |
| **SAM** (Segment Anything Model) | Vision foundation model that segments any object in an image given a prompt (a point, box, or mask), pretrained on over a billion masks. See [§1.3](../chapter-1-background/1-3-fm-landscape-by-domain.html) |
| **Self-supervised pretraining** | Training on labels manufactured from the input itself (masking, next-step prediction), rather than hand-labelled targets. See [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html) |
| **Surrogate** | Fast approximation of an expensive model, usually system-specific. Contrasted with a foundation model in [§2.8](../chapter-2-fm-foundations/2-8-surrogates-vs-fms.html) |
| **Tokenisation** | Deciding what the basic elements are; the learned-model equivalent of choosing a discretisation |
| **Transformer** | Architecture built on attention, letting any token's representation be updated in light of any other. See [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) |
| **TSFM** | Time-series foundation model |
| **TTM** (Tiny Time Mixers) | Lightweight, non-transformer time-series foundation model family (1–5M parameters, CPU-capable) — the efficiency counterpart to billion-parameter TSFMs. See [§1.4](../chapter-1-background/1-4-fm-field-directions.html) |
| **Unit of observation** | What constitutes one training example |
| **ViT** (Vision Transformer) | Architecture that treats an image as a sequence of fixed-size patches and processes them with a standard transformer, rather than a convolutional network. See [§1.3](../chapter-1-background/1-3-fm-landscape-by-domain.html) and [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) |
| **Zero-shot** | Applied to a new instance with no additional training |
| **Zoning ambiguity** | The property that decomposing a building into thermal zones is a modelling decision rather than a fact about the building; the reason zone-based representations fail the unambiguity requirement ([§2.3.2b](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings)) |

---
[← Back to Appendices](index.html) · [Next: Appendix B — Pre-Project Checklist →](b-checklist.html)
