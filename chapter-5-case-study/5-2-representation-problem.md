---
title: "5.2 The Representation Problem"
parent: Chapter 5 — Case Study
nav_order: 2
status: draft
last_reviewed: 2026-09-11
---

# 5.2 The Representation Problem
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## 5.2.1 The causal chain: representation → data → capability

**(a) It defines what counts as one sample, which can change effective dataset size by three orders of magnitude.**
A dataset of tens of thousands of buildings can be read as tens of millions of samples (building-days), tens of thousands of samples (building-years), or a few hundred samples (district-years) — identical underlying data, entirely different regime (see the same point made for a specific dataset in [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)). The first supports pretraining, the third supports fine-tuning at best. For hubs the escape is to make the *device* or *carrier-bus* the token and the district merely the graph they sit in, so one district-year contributes thousands of tokens rather than one sample. This decision alone determines whether the corpus is viable.

**(b) It determines whether a self-supervised task exists at all.**
Masking (see [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html)) works only when the masked part is predictable from the remainder but not trivially so. Too coarse and there is nothing to hide; too fine and the task collapses into interpolation and the model learns smoothing rather than physics. GridFM sits in the sweet spot because masking a bus's (p, q, v, δ) is genuinely equivalent to solving power flow at that node. **The test for hubs: is masking one carrier-bus's flows equivalent to solving something?**

**(c) It determines what transfers zero-shot.**
You can only generalise along axes the representation makes structural rather than parametric. GridFM transfers to unseen topologies because topology lives in the graph, not the weights (see [§4.9.2](../chapter-4-directions/4-9-2-methods-tier2.html)). For transfer across hub configurations, device *class* must be an embedding shared across hubs, and hub identity must not appear in the parameters.

**(d) It sets a hard ceiling on context, and this is where hubs break.**
Attention is quadratic (see [§2.7](../chapter-2-fm-foundations/2-7-architectures.html)); patching exists to buy context length. TimesFM 1.0 handled up to 512 time points, 2.0 up to 2048, and 2.5 reaches 16 k context at around 200 M parameters; Moirai handles up to 5000 steps. One year of hourly data is 8760 steps. For seasonal thermal storage this is fatal, not inconvenient: the charge decision in June is only justified by the discharge in January, and any representation that chops the year into independent windows destroys the coupling that makes multi-carrier hubs interesting. This is what motivates the temporal hierarchy in [§5.5](5-5-token-schema.html).

**(e) It determines what physics can go in the loss.**
The loss can only reference quantities the token exposes. If carrier quality is not a token dimension, you cannot write a constraint forbidding free upgrading of 35 °C heat to 80 °C, and the model will violate thermodynamics wherever data is sparse. See [§5.6](5-6-physics-loss.html).

**(f) It silently deletes information you may need later.**
Instance normalisation gives time-series FMs their scale invariance and cross-domain transfer, but discards absolute magnitude. A normalised load embedding cannot tell you whether a transformer is overloaded, because "how many kW" was normalised away. If load-FM embeddings are ever handed to a grid FM as boundary conditions, magnitude must be carried separately. This is a representation-level bug that no amount of fine-tuning fixes.

## 5.2.2 The five decisions the paper must make explicit

1. **Sample granularity** — device-week, hub-day, or hub-year. Determines corpus viability.
2. **Carrier quality encoding** — continuous temperature, discrete quality levels, or exergy factor. Continuous is physically honest but makes the permitted-conversion constraint harder to express; discrete is cleaner but arbitrary at boundaries.
3. **Temporal hierarchy** — how hourly, daily, and seasonal scales nest given the context ceiling.
4. **Device vocabulary** — a fixed technology-class set makes installation a clean classification problem but generalises badly to technologies invented after training; a continuous parameter space generalises but invites interpolation to physically nonexistent devices. Probably: fixed class embedding plus continuous parameter conditioning within class.
5. **Heterogeneity** — the biggest unproven bet. Nearly every successful FM uses a single token type; this needs at least two plus multiple edge types, putting it in heterogeneous graph transformer territory where the machinery is far less battle-tested.

## 5.2.3 Why this makes a good research contribution rather than a good appendix

Language, vision, and weather all had their representations handed to them. Words existed before LLMs; pixels before ViT; the sphere's geometry before GraphCast; MATPOWER and the bus abstraction decades before GridFM (see [§3.6](../chapter-3-sim-opt/3-6-tool-landscape.html)). Urban multi-carrier energy systems have no such inheritance, and every existing formalism — the energy hub coupling matrix ([§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html)), ESDL, CIM ([§3.7](../chapter-3-sim-opt/3-7-schemas-and-standards.html)) — was designed for solvers or interoperability rather than for learning. Arguing that **the tokenisation is the bottleneck, and that it is a research problem rather than an engineering detail**, is a claim that is both true and unclaimed.

---
[← Previous: 5.1 Roadmap](5-1-roadmap.html) · [Next: 5.3 Data Generation →](5-3-data-generation.html)
