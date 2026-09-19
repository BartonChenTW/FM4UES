---
title: "4.4 Generative Design"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 4
status: draft
last_reviewed: 2026-09-19
---

# 4.4 Generative Design
{: .no_toc }

{% include page-status.html %}

{: .note }
**Still a stub for energy-hub design specifically**, but the adjacent-domain survey this section asked for is now below — including one precedent already validated on power-system test cases, and one in-domain example that clarifies the distinction this section depends on.

1. TOC
{:toc}

---

## The direction

[§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) and [§4.9.3 (Tier 3)](4-9-3-methods-tier3.html) treat design and sizing as an *optimisation* problem: search a space of candidate designs (device choices, capacities, topology) and return the best one against a stated objective. **Generative design** is a related but distinct framing: rather than searching a fixed decision space for an optimum, a generative model proposes novel candidate designs directly — sampling from a learned distribution over plausible system configurations, potentially including topologies or technology combinations not explicitly enumerated in advance.

This distinction matters because it changes what the model needs to represent. Tier 3's amortised-optimisation approaches ([§4.9.3](4-9-3-methods-tier3.html)) predict *within* a decision space that is defined and bounded ahead of time. A generative approach needs the decision space itself to be represented well enough that sampling from it produces valid, buildable designs — which is a direct application of the **decision space** problem named in [§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) and logged as [gap G9](../chapter-6-outlook/6-1-open-gaps.html#g9).

## Relationship to the rest of this book

Generative design for energy systems is the design-space analogue of what diffusion and other generative models already do for images[^ho2020ddpm] and molecules:[^hoogeboom2022edm] propose plausible new instances rather than only score given ones. No existing energy foundation model surveyed in [§2.4](../chapter-2-fm-foundations/2-4-existing-fms-relevant-to-energy.html) attempts this for multi-carrier hub design; it is a genuinely open direction rather than an established one.

## The adjacent-domain precedent, and how close it already is

A dated search (arXiv title/abstract, "generative design" combined with "energy system", "energy hub" or "power system", plus a separate diffusion-specific pass; run 19 September 2026) surfaces one precedent that is closer to this book's subject than "adjacent engineering domain" usually implies. A generative-design framework pairs a candidate-design generator with a performance estimator, using graph learning so the generator can mine good structural properties from existing systems rather than search a fixed enumerated space — and it is validated on IEEE power-system test cases specifically, not a generic mechanical or structural benchmark.[^wu2022generativeresilience]

**What transfers and what does not.** The framing — generator plus fast performance estimator, iterated — is directly reusable, and the target domain (power-system topology) is one carrier of the multi-carrier picture. What does not transfer without new work: it optimises for network *resilience* under disruption, not the cost, emissions or feasibility objectives an energy-hub design problem uses, and single-carrier grid topology is not multi-carrier device selection — the discrete technology and connection choices [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) and [§4.9.3](4-9-3-methods-tier3.html) treat as the object have no counterpart in a network-topology framing.

## An in-domain example — and the distinction it clarifies

A generative model has also already been used *within* this book's domain, but for a different purpose that is worth naming precisely. A deep generative network produces synthetic annual solar-irradiance time series on building facades, to give building-integrated-photovoltaics design a stochastic ensemble of plausible irradiance scenarios rather than one deterministic simulation run.[^zhang2023solargan] This generates an uncertain **input** to a design process — the same "agent supplies inputs, conventional tool runs unchanged" distinction [§4.3](4-3-llm-agents-for-simulation.html) draws for LLM agents — not the design (device combination, topology, sizing) itself. The distinction matters here specifically: the nearer a generative technique sits to producing decision variables rather than boundary conditions, the more directly it engages the decision-space problem in [G9](../chapter-6-outlook/6-1-open-gaps.html#g9); SolarGAN sits at the boundary-condition end, Wu & Wang's design generator sits at the decision-variable end.

## What would still need to be added here

- Discussion of feasibility: a generatively-proposed design still needs the feasibility guarantees discussed in [§4.9.3](4-9-3-methods-tier3.html) — a generated device combination that cannot actually be built or connected is not useful.
- How this direction would interact with the decision-space representation problem in [G9](../chapter-6-outlook/6-1-open-gaps.html#g9), which is currently unsolved rather than merely under-explored.
- Whether a graph-learning generator-plus-estimator pattern like Wu & Wang's, re-targeted from resilience to cost/feasibility, is a viable starting point — untested, and a genuinely open question rather than a survey gap.

[^ho2020ddpm]: Ho, J., Jain, A., Abbeel, P. (2020). [Denoising diffusion probabilistic models](https://arxiv.org/abs/2006.11239). NeurIPS 2020. arXiv:2006.11239
[^hoogeboom2022edm]: Hoogeboom, E., Satorras, V. G., Vignac, C., Welling, M. (2022). [Equivariant diffusion for molecule generation in 3D](https://arxiv.org/abs/2203.17003). ICML 2022. arXiv:2203.17003
[^wu2022generativeresilience]: Wu, J., Wang, P. (2022). [Generative design for resilience of interdependent network systems](https://doi.org/10.1115/1.4056078). *Journal of Mechanical Design*, 145(3), 031705.
[^zhang2023solargan]: Zhang, Y., Schlüter, A., Waibel, C. (2023). [SolarGAN: Synthetic annual solar irradiance time series on urban building facades via deep generative networks](https://doi.org/10.1016/j.egyai.2022.100223). *Energy and AI*, 12, 100223.

---
[← Previous: 4.3 LLM Agents for Simulation](4-3-llm-agents-for-simulation.html) · [Next: 4.5 Screening: Which Sub-Fields Fit the FM Pattern →](4-5-screening-fields.html)
