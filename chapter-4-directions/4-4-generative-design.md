---
title: "4.4 Generative Design"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 4
status: draft
last_reviewed: 2026-10-20
---

# 4.4 Generative Design
{: .no_toc }

{% include page-status.html %}

{: .note }
**Still open for energy-hub design itself.** A second search, on 20 October 2026, still found no generative model that proposes energy-hub or multi-energy configurations. This page now covers the two pieces that do exist: methods that make generated network designs feasible, and ways of representing a discrete design space so a model can learn over it.

1. TOC
{:toc}

---

## The direction

[§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html#design-and-sizing) and [§4.7.3 (Tier 3)](4-7-3-methods-tier3.html) treat design and sizing as an *optimisation* problem: search a space of candidate designs (device choices, capacities, topology) and return the best one against a stated objective. **Generative design** is a related but distinct framing: rather than searching a fixed [decision space](../appendices/a-glossary.html#decision-space) for an optimum, a generative model proposes novel candidate designs directly — sampling from a learned distribution over plausible system configurations, potentially including topologies or technology combinations not explicitly enumerated in advance.

This distinction matters because it changes what the model needs to represent. Tier 3's amortised-optimisation approaches ([§4.7.3](4-7-3-methods-tier3.html)) predict *within* a decision space that is defined and bounded ahead of time. A generative approach needs the decision space itself to be represented well enough that sampling from it produces valid, buildable designs — which is a direct application of the **decision space** problem named in [§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html) and logged as [gap G9](../chapter-6-outlook/6-1-open-gaps.html#g9).

## Relationship to the rest of these notes

Generative design for energy systems is the design-space analogue of what diffusion and other generative models already do for images[^ho2020ddpm] and molecules:[^hoogeboom2022edm] propose plausible new instances rather than only score given ones. No existing energy foundation model surveyed in [§2.4](../chapter-2-fm-foundations/2-4-existing-fms-relevant-to-energy.html) attempts this for multi-carrier hub design; it is a genuinely open direction rather than an established one.

**The searches.** The first search, on arXiv on 19 September 2026, combined "generative design" with "energy system", "energy hub" or "power system", plus a pass for diffusion models. The second, on 20 October 2026, extended it on arXiv to diffusion, GAN, variational-autoencoder, language-model and graph-generative methods combined with [energy hubs](../appendices/a-glossary.html#energy-hub), multi-energy systems, microgrids, district heating and grid planning, and added OpenAlex for journal papers. Neither found a generative model of energy-hub or multi-energy configurations or sizing. The second search did find work on the two sub-problems below.

## The adjacent-domain precedent, and how close it already is

The first search surfaced one precedent that is closer to these notes' subject than "adjacent engineering domain" usually implies. A generative-design framework pairs a candidate-design generator with a performance estimator, using graph learning so the generator can mine good structural properties from existing systems rather than search a fixed enumerated space — and it is validated on IEEE power-system test cases specifically, not a generic mechanical or structural benchmark.[^wu2022generativeresilience]

**What transfers and what does not.** The framing — generator plus fast performance estimator, iterated — is directly reusable, and the target domain (power-system topology) is one carrier of the multi-carrier picture. What does not transfer without new work: it optimises for network *resilience* under disruption, not the cost, emissions or feasibility objectives an energy-hub design problem uses, and single-carrier grid topology is not multi-carrier device selection — the discrete technology and connection choices [§3.3](../chapter-3-sim-opt/3-3-energy-hub-formalism.html#design-and-sizing) and [§4.7.3](4-7-3-methods-tier3.html) treat as the object have no counterpart in a network-topology framing.

No work was found that re-targets a generator-plus-estimator of this kind from resilience to cost or feasibility for multi-carrier systems. The feasibility half of that question now has evidence from grid generators (next section). The cost half has none, so whether the pattern is a viable starting point for hub design remains untested.

## In-domain examples, and the distinction they clarify

A generative model has also already been used *within* these notes' domain, but for a different purpose that is worth naming precisely. A deep generative network produces synthetic annual solar-irradiance time series on building facades, to give building-integrated-photovoltaics design a stochastic ensemble of plausible irradiance scenarios rather than one deterministic simulation run.[^zhang2023solargan] This generates an uncertain **input** to a design process — the same "agent supplies inputs, conventional tool runs unchanged" distinction [§4.3](4-3-llm-agents-for-simulation.html) draws for LLM agents — not the design (device combination, topology, sizing) itself.

The one in-domain example found that generates **decisions** rather than inputs is for buildings, not hubs. Variational autoencoders trained on a simulated renovation dataset for institutional buildings generate whole-building renovation scenarios, scored on total energy consumption and life-cycle cost.[^sharif2021renovationvae]

The distinction matters here specifically: the nearer a generative technique sits to producing decision variables rather than boundary conditions, the more directly it engages the decision-space problem in [G9](../chapter-6-outlook/6-1-open-gaps.html#g9). SolarGAN sits at the boundary-condition end. The renovation-scenario generator and Wu & Wang's design generator sit at the decision-variable end.

## Feasibility of generated designs

A generated device combination that cannot be built or connected is not useful, and unconstrained generators produce many of them. The clearest figure comes from generating electricity distribution feeders: without constraint handling, only 13.7% of generated feeders passed strict checks for electrical compatibility and radial structure. Adding the constraints to the generation process as soft masks, followed by a final projection step that rebuilds a connected, rule-compliant network, raised the pass rate to 96.8%, and the generated networks convert into runnable feeder models.[^qin2026pgdigress] These are realistic synthetic feeders, not cost-optimal designs, but they show the size of the feasibility problem and one way to close it.

The methods found fall into four groups.

| Approach | How it works | Example |
| :--- | :--- | :--- |
| **Constrain during generation** | Mask or project each sample during generation so that it satisfies the constraints | Feeder generation, above.[^qin2026pgdigress] Projected diffusion recasts sampling as a constrained optimisation and can certify that convex and some non-convex constraints hold.[^christopher2024projdiffusion] |
| **Generate in stages** | Generate the structure first, then each later attribute conditioned on the stages before it, checking feasibility at each stage | Power-grid synthesis that generates topology, then bus loads, then other attributes, reaching 98.9% power-flow convergence.[^he2025powergrow] |
| **Learn from infeasible designs** | Train the generator on examples of what to avoid as well as what to produce | In engineering design, this gave one-sixth as many constraint-violating samples using one-eighth as much data in some problems (preprint).[^regenwetter2023ndgm] |
| **Generator proposes, optimiser repairs** | Pass generated candidates to a solver that enforces the constraints | The arrangement [§4.7.3](4-7-3-methods-tier3.html) recommends for design (Family 3, where the solver keeps its guarantees), and that of the policy agent in [§4.3](4-3-llm-agents-for-simulation.html) |

A review of deep generative models in engineering design names handling constraints and objectives as one of the field's main open challenges.[^regenwetter2022dgmreview] For hub design the last approach is the cheapest to start with: a sizing MILP already rejects infeasible designs, and each rejection could also be kept as a negative training example for the third.

## Representing the decision space

A generator can only sample from a decision space that is represented in a form a model can learn over. That is the unsolved part of [G9](../chapter-6-outlook/6-1-open-gaps.html#g9). Methods from machine learning for combinatorial optimisation give three usable pieces.

- **The problem as a graph.** A mixed-integer linear program (MILP) can be written as a bipartite graph, with one set of nodes for the variables, one for the constraints, and an edge wherever a variable appears in a constraint. Graph networks trained on this representation learned branching decisions for the solver that generalised to instances much larger than those seen in training.[^gasse2019learn2branch] A hub-sizing [MILP](../appendices/a-glossary.html#milp) can be represented the same way.
- **Problems as the training data.** A survey of the field frames each optimisation problem as one data point and asks which distribution of problems a model should learn from.[^bengio2021mlco] For hub design that question is G9 itself: which population of hub-design problems, with which carriers, technologies and sites, a model should be trained on.
- **Diffusion over binary decisions.** Graph-based diffusion models can generate solutions to combinatorial problems written as vectors of 0/1 decisions; on travelling-salesman problems with 500 cities, one cut the gap to the best solutions from 1.76% to 0.46%.[^sun2023difusco] The technology-selection decisions of hub design are vectors of the same kind: build this device or not.

None of these has been applied to energy-hub design. Together they give a concrete form to G9: the decision space is the variable-constraint graph of the design MILP, and the training data is a defined population of such problems.

## What would still need to be added here

- A generative model that proposes energy-hub or multi-energy configurations at all; none was found on 20 October 2026.
- A test of the generator-plus-estimator pattern with a cost objective, which would answer whether Wu & Wang's approach transfers.
- A corpus of solved hub-design problems, in the graph form above, from which such a model could learn.

[^ho2020ddpm]: Ho, J., Jain, A., Abbeel, P. (2020). [Denoising diffusion probabilistic models](https://arxiv.org/abs/2006.11239). NeurIPS 2020. arXiv:2006.11239
[^hoogeboom2022edm]: Hoogeboom, E., Satorras, V. G., Vignac, C., Welling, M. (2022). [Equivariant diffusion for molecule generation in 3D](https://arxiv.org/abs/2203.17003). ICML 2022. arXiv:2203.17003
[^wu2022generativeresilience]: Wu, J., Wang, P. (2022). [Generative design for resilience of interdependent network systems](https://doi.org/10.1115/1.4056078). *Journal of Mechanical Design*, 145(3), 031705.
[^zhang2023solargan]: Zhang, Y., Schlüter, A., Waibel, C. (2023). [SolarGAN: Synthetic annual solar irradiance time series on urban building facades via deep generative networks](https://doi.org/10.1016/j.egyai.2022.100223). *Energy and AI*, 12, 100223.
[^sharif2021renovationvae]: Sharif, S. A., Hammad, A., Eshraghi, P. (2021). [Generation of whole building renovation scenarios using variational autoencoders](https://doi.org/10.1016/j.enbuild.2020.110520). *Energy and Buildings*, 230, 110520.
[^qin2026pgdigress]: Qin, Y., Glaws, A., Latif, A. et al. (2026). [From graphs to feeders: Constraint-guided diffusion for rule-compliant feeder generation](https://arxiv.org/abs/2609.29879). arXiv:2609.29879.
[^christopher2024projdiffusion]: Christopher, J. K., Baek, S., Fioretto, F. (2024). [Constrained synthesis with projected diffusion models](https://arxiv.org/abs/2402.03559). NeurIPS 2024. arXiv:2402.03559.
[^he2025powergrow]: He, X., Xiao, C., Li, H. et al. (2025). [PowerGrow: Feasible co-growth of structures and dynamics for power grid synthesis](https://arxiv.org/abs/2509.12212). arXiv:2509.12212.
[^regenwetter2023ndgm]: Regenwetter, L., Giannone, G., Srivastava, A. et al. (2023). [Constraining generative models for engineering design with negative data](https://arxiv.org/abs/2306.15166). arXiv:2306.15166.
[^regenwetter2022dgmreview]: Regenwetter, L., Nobari, A. H., Ahmed, F. (2022). [Deep generative models in engineering design: A review](https://doi.org/10.1115/1.4053859). *Journal of Mechanical Design*, 144(7), 071704. arXiv:2110.10863.
[^gasse2019learn2branch]: Gasse, M., Chételat, D., Ferroni, N. et al. (2019). [Exact combinatorial optimization with graph convolutional neural networks](https://arxiv.org/abs/1906.01629). NeurIPS 2019. arXiv:1906.01629.
[^bengio2021mlco]: Bengio, Y., Lodi, A., Prouvost, A. (2021). [Machine learning for combinatorial optimization: A methodological tour d'horizon](https://doi.org/10.1016/j.ejor.2020.07.063). *European Journal of Operational Research*, 290(2), 405–421. arXiv:1811.06128.
[^sun2023difusco]: Sun, Z., Yang, Y. (2023). [DIFUSCO: Graph-based diffusion solvers for combinatorial optimization](https://arxiv.org/abs/2302.08224). NeurIPS 2023. arXiv:2302.08224.

---
[← Previous: 4.3 LLMs and Agents That Build or Run Simulation Models](4-3-llm-agents-for-simulation.html) · [Back to Chapter 4](index.html) · [Next: 4.5 Screening Sub-Fields and Tasks →](4-5-screening-fields.html)
