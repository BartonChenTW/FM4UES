---
title: Appendix A — Glossary
parent: Appendices
nav_order: 1
status: draft
last_reviewed: 2026-09-29
redirect_from: /appendix-a-glossary.html
---

# Appendix A — Glossary
{: .no_toc }

{% include page-status.html %}

| Term | Meaning |
| :--- | :--- |
| **Agent-based model (ABM)** | Simulation of many individual decision-makers, each with its own attributes and decision rule, interacting over time; the standard tool for technology adoption. See [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html) |
| **Amortised optimisation** | Learning to produce optimisation solutions directly, paying training cost once |
| **Any-variate attention** | Attention scaling to arbitrary numbers of input series |
| **Basic element** | The unit a model treats as indivisible — the learned-model counterpart of an element in a discretised simulation. Judged against the four requirements in [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion) |
| **Cell** | A single entry in a table, where one row meets one column; the basic element of tabular foundation models ([§2.4.4](../chapter-2-fm-foundations/2-4-4-tabular-fms.html)) |
| **Co-simulation** | Running separate sub-models that exchange data at a coupling interface, rather than one integrated solver ([§3.6](../chapter-3-sim-opt/3-6-tool-landscape.html)); the template for coupling foundation models by physical quantities ([§4.11](../chapter-4-directions/4-11-ecosystem.html)) |
| **Cross-attention** | Mechanism by which one set of information (e.g. building attributes) modulates how another is interpreted (e.g. a demand profile), rather than simply being appended to it |
| **DAE** | Differential-algebraic equations — the structure of Modelica-type models |
| **Decision space** | The set of possible interventions on a system, as distinct from its state space; see [G9](../chapter-6-outlook/6-1-open-gaps.html#g9) |
| **DINO** (self-distillation with no labels) | Self-supervised vision transformer trained by having a student network match a teacher's output with no labelled data. See [§1.3](../chapter-1-background/1-3-fm-landscape-by-domain.html) |
| **Embodied emissions** | Greenhouse-gas emissions from producing, transporting, installing, replacing and disposing of building materials and equipment, as opposed to operating the building. See [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html) |
| **Energy burden** | Share of a household's income spent on energy; a common quantitative indicator of energy poverty |
| **Energy hub** | Node converting/storing/dispatching multiple carriers via a coupling matrix ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)) |
| **Energy justice** | Framework assessing energy systems on distributional, recognition and procedural justice. See [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html) |
| **Energy poverty** | Inability of a household to attain a socially and materially necessary level of domestic energy services. See [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html) |
| **EPD** (Environmental Product Declaration) | Product-specific declaration of life-cycle environmental impacts, structured by the EN 15804 information modules. See [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html) |
| **Fine-tuning** | Adjusting a pretrained model to a specific case with a small amount of additional data — comparable to calibrating a model against measurements. See [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html) |
| **Foundation model** | Pretrained on a broad distribution; transfers to unseen instances; serves multiple tasks |
| **In-context learning** | Making predictions by conditioning on labelled examples supplied at inference time, with no parameter updates |
| **LCA** (life cycle assessment) | Quantifying a product's or building's environmental impacts across its life cycle, from raw materials to end of life. For buildings, standardised in EN 15978. See [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html) |
| **LCI database** (life-cycle inventory) | Background dataset of material and energy flows per process (e.g. ecoinvent) from which LCA impact factors are computed |
| **MILP** | Mixed-integer linear program — LP plus discrete decisions |
| **Neural operator** | Network learning mappings between function spaces rather than finite vectors. See [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) |
| **Patch** | A contiguous block of timesteps treated as one token |
| **PFN (prior-data fitted network)** | Model pretrained across a distribution of synthetic tasks so that conditioning on a context approximates Bayesian inference under the learned prior |
| **Retrofit measure** | One intervention on an existing building — envelope insulation, window replacement, heating-system replacement, PV — chosen from a shared library but constrained per building. See [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html) |
| **ROM** | Reduced-order model — compresses high-dimensional state to a latent manifold |
| **SAM** (Segment Anything Model) | Vision foundation model that segments any object in an image given a prompt (a point, box, or mask), pretrained on over a billion masks. See [§1.3](../chapter-1-background/1-3-fm-landscape-by-domain.html) |
| **Self-supervised pretraining** | Training on labels manufactured from the input itself (masking, next-step prediction), rather than hand-labelled targets. See [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html) |
| **Silicon sample** | Synthetic survey respondents produced by conditioning a language model on demographic personas; averages can match real surveys while variance and relationships do not. See [§4.3](../chapter-4-directions/4-3-llm-agents-for-simulation.html) |
| **Surrogate** | Fast approximation of an expensive model, usually system-specific. Contrasted with a foundation model in [§2.8](../chapter-2-fm-foundations/2-8-surrogates-vs-fms.html) |
| **Tokenisation** | Deciding what the basic elements are; the learned-model equivalent of choosing a discretisation |
| **Transformer** | Architecture built on attention, letting any token's representation be updated in light of any other. See [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) |
| **TSFM** | Time-series foundation model |
| **TTM** (Tiny Time Mixers) | Lightweight, non-transformer time-series foundation model family (1–5M parameters, CPU-capable) — the efficiency counterpart to billion-parameter TSFMs. See [§1.4](../chapter-1-background/1-4-fm-field-directions.html) |
| **Unit of observation** | What constitutes one training example |
| **ViT** (Vision Transformer) | Architecture that treats an image as a sequence of fixed-size patches and processes them with a standard transformer, rather than a convolutional network. See [§1.3](../chapter-1-background/1-3-fm-landscape-by-domain.html) and [§2.7](../chapter-2-fm-foundations/2-7-architectures.html) |
| **Whole-life carbon** | Operational plus embodied emissions over a building's life cycle; operational energy is module B6 in EN 15978 |
| **Zero-shot** | Applied to a new instance with no additional training |
| **Zoning ambiguity** | The property that decomposing a building into thermal zones is a modelling decision rather than a fact about the building; the reason zone-based representations fail the unambiguity requirement ([§2.3.2b](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings)) |

---
[← Back to Appendices](index.html) · [Next: Appendix B — Pre-Project Checklist →](b-checklist.html)
