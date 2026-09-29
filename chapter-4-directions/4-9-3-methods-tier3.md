---
title: "4.9.3 Tier 3 — Design & Sizing"
parent: "4.9 Methods by Problem Class"
grand_parent: Chapter 4 — Directions for FMs in UES
nav_order: 3
status: draft
last_reviewed: 2026-09-11
redirect_from: /08-methods-tier3.html
---

# 4.9.3 Tier 3 — Design and Sizing Optimisation
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## Why this is structurally different

Tiers 1 and 2 approximate a **simulation**: given inputs, predict outputs. Tier 3 approximates an **optimisation**: given a problem instance, predict the optimal decision. See [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) for the bilevel problem structure and the amortisation argument in full — this section covers the methods, given that framing.

Characteristically, evaluating the value function and gradient of the inner-loop optimisation is computationally expensive — which is the general statement of the difficulty.

{: .note }
Tier 3 is also where the decision layer of [§2.3.2](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#232-basic-elements-for-buildings) becomes unavoidable. The model must represent the space of possible designs, not only system states. This is logged as [G9](../chapter-6-outlook/6-1-open-gaps.html#g9) and is the least-developed representation question in this book — see also [§4.4 Generative Design](4-4-generative-design.html).

## Three families of method

**Family 1 — Surrogate the inner objective (most established).** Learn a mapping from design vector → operating cost (and other objectives), then run the outer search against the surrogate. This has direct precedent in energy hubs: an ANN-based surrogate combined with an Actual Engineering Model for system sizing optimisation in energy hubs, using supervised and transfer learning to bypass the computationally intensive engineering model, adaptable across scenarios with different solar and wind potentials.[^perera2019mlsurrogate] The same approach has been applied at national scale, surrogating EnergyPLAN to speed up country-level optimisation.[^prina2024energyplan]

*Strength:* simple, proven. *Weakness:* one surrogate per system — the bespoke trap (see [§2.8](../chapter-2-fm-foundations/2-8-surrogates-vs-fms.html)). **The foundation-model contribution would be making this transferable across systems rather than rebuilt each time.**

**Family 2 — Learn the solution map (amortised optimisation).** Learn instance → optimal decision directly. Fast, because the solver is bypassed entirely. Direct approaches learn a mapping between grid parameters and the OPF solution and are typically much faster than conventional solvers or hybrid approaches, **but offer no feasibility guarantees**. The survey literature on end-to-end constrained optimisation learning makes the same trade explicit across combinatorial domains: integrating solvers with learned architectures buys fast approximate solutions, and the recurring open problem is enforcing the constraints that a purely learned map will otherwise violate.[^kotary2021survey]

**Family 3 — Hybrid (recommended default).** Predict information that helps a conventional solver converge faster — warm starts, active-set prediction, variable fixing. Hybrid approaches predict information to help a conventional optimisation solver converge to a solution faster, retaining the solver's guarantees.

The warm-start case is established in power systems: a neural network trained to predict AC-OPF solutions, used to initialise the solver rather than replace it, reduces the number of solver iterations while leaving the optimality and feasibility guarantees entirely with the solver.[^baker2019warmstart] **What that result does not settle is the part that matters for multi-carrier design.** It warm-starts a continuous nonlinear problem; the binding cost in energy-hub design is the *discrete* layer — which technologies install, which units commit — where a warm start must supply integer assignments and a bad guess can send branch-and-bound down a worse tree rather than merely costing an iteration. Whether predicted binaries help or hurt at UES scale is untested, and is one of the more tractable experiments available here (see [D4 in §5.7](../chapter-5-case-study/5-7-module-decomposition.html)).

A particularly clean pattern worth studying: replace only the *physics constraints* with a learned surrogate while preserving the optimisation backbone and all remaining constraints. One implementation learns only the voltage–power mapping, circumventing the feasibility and generalisation issues of end-to-end approaches while requiring substantially less training data, and encodes the neural network exactly as MILP via Big-M constraints, preserving global optimality guarantees of the surrogate-constrained problem — unlike penalty- or projection-based feasibility restoration. Reported result: substantially reduced computation time versus nonlinear OPF on a realistic LV network with PV, EVs and heat pumps.[^panagi2026nnsurrogate]

**A fourth option, sitting between Families 2 and 3: make the optimisation itself a layer.** Rather than penalising constraint violations in the loss (no hard guarantee) or handing a prediction to an external solver, the optimisation problem can be embedded *inside* the network as a differentiable layer, with gradients taken through the solve via implicit differentiation.[^amos2017optnet] Trained end-to-end, this lets the model optimise the decision quality it is ultimately judged on rather than a proxy prediction error — demonstrated on, among other things, a grid-scheduling and a storage-arbitrage task.[^donti2017taskbased]

**Two caveats before reaching for it here.** The established formulations differentiate through *convex* programs (quadratic programs in the original work); the integer decisions that define hub design are exactly what they do not cover, so the discrete layer of [G9](../chapter-6-outlook/6-1-open-gaps.html#g9) is not solved by adopting this machinery. And each forward pass now contains a solve, so the inference speedup that motivated the amortisation argument in [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html#the-amortisation-argument) is partly given back. Treat it as the right tool when the constraint set is convex and feasibility must hold exactly at every forward pass, not as a general replacement for Family 3.

**For multi-energy design, Family 3 is the sensible default**, because design decisions carry investment consequences and silent infeasibility is unacceptable.

{: .important }
**Practical corollary for building retrofit.** A surrogate imitating a constrained optimiser inherits that optimiser's constraints only implicitly. It can therefore propose measures a specific instance cannot accept: PV without sufficient roof area, a heat pump beyond the electrical connection limit. This is a deployment risk rather than an academic nitpick, and any decision-support application needs a stated handling — post-hoc constraint filtering, inference-time masking, or reporting violation rate as a headline metric alongside accuracy. The retrofit task and its constraints are described in [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html).

## Scaling behaviour

Recent power-systems work establishes both scaling laws of machine learning for optimal power flow[^liu2026scalingopf] and data scaling laws for multi-task energy system intelligence with limited fine-tuning[^liu2025multitask] (see [§2.6](../chapter-2-fm-foundations/2-6-scaling-laws.html) for what a scaling law is). **Before committing to a large data-generation campaign, run a small scaling study**: train on 10², 10³, 10⁴ samples and fit the error curve. This tells you the required *N* rather than guessing, and it is cheap.

[^perera2019mlsurrogate]: Perera, A. T. D., Wickramasinghe, P. U., Nik, V. M., Scartezzini, J.-L. (2019). [Machine learning methods to assist energy system optimization](https://doi.org/10.1016/j.apenergy.2019.03.202). *Applied Energy*, 243, 191–205.
[^prina2024energyplan]: Prina, M. G., Dallapiccola, M., Moser, D., Sparber, W. (2024). [Machine learning as a surrogate model for EnergyPLAN: Speeding up energy system optimization at the country level](https://doi.org/10.1016/j.energy.2024.132735). *Energy*, 307, 132735.
[^panagi2026nnsurrogate]: Panagi, S., Spanias, C., Aristidou, P. (2026). [Enhanced optimal power flow using a trained neural network surrogate for distribution grid constraints](https://arxiv.org/abs/2604.12422). arXiv:2604.12422
[^liu2026scalingopf]: Liu, X., He, X., Chen, Y. (2026). [Scaling laws of machine learning for optimal power flow](https://arxiv.org/abs/2601.02706). arXiv:2601.02706
[^liu2025multitask]: Liu, S., Dong, L., Tian, C., Xie, L. (2025). [Unlocking multi-task electric energy system intelligence: Data scaling laws and performance with limited fine-tuning](https://arxiv.org/abs/2503.20040). arXiv:2503.20040
[^kotary2021survey]: Kotary, J., Fioretto, F., Van Hentenryck, P., Wilder, B. (2021). [End-to-end constrained optimization learning: A survey](https://doi.org/10.24963/ijcai.2021/610). *IJCAI-21*, 4475–4482.
[^baker2019warmstart]: Baker, K. (2019). [Learning warm-start points for AC optimal power flow](https://doi.org/10.1109/mlsp.2019.8918690). *IEEE MLSP 2019*, 1–6.
[^amos2017optnet]: Amos, B., Kolter, J. Z. (2017). [OptNet: Differentiable optimization as a layer in neural networks](https://arxiv.org/abs/1703.00443). arXiv:1703.00443. ICML 2017.
[^donti2017taskbased]: Donti, P. L., Amos, B., Kolter, J. Z. (2017). [Task-based end-to-end model learning in stochastic optimization](https://arxiv.org/abs/1703.04529). arXiv:1703.04529. NeurIPS 2017.

---
[← Previous: 4.9.2 Tier 2](4-9-2-methods-tier2.html) · [Next: 4.10 Building It →](4-10-building-it.html)
