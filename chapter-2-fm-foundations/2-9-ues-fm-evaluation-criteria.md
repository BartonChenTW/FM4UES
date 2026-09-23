---
title: "2.9 Evaluation Criteria for UES Foundation Models"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 9
status: draft
last_reviewed: 2026-09-13
---

# 2.9 Evaluation Criteria for UES Foundation Models
{: .no_toc }

{% include page-status.html %}

§2.1 gives the generic three-property test. This section sharpens it into seven questions specific to physical, decision-critical systems — the standard a UES foundation-model proposal should be held to, not just a general-purpose one.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## Why the generic definition is not enough here

The three-property definition in [§2.1](2-1-what-defines-an-fm.html) — broad pretraining, transfer, multi-task — is necessary but not sufficient once the model's outputs feed into physical, decision-critical systems. A model can satisfy all three properties and still be useless or dangerous in this domain: it can transfer across buildings while producing physically infeasible predictions, or generalise across tasks while giving no indication of when it is unreliable. The seven dimensions below make that gap concrete.

{: .note }
This framework does not replace the surrogate/FM contrast in [§2.8](2-8-surrogates-vs-fms.html) — it assumes that contrast, then asks a further question: given that something clears the FM bar, how good an FM is it for *this* domain specifically?

## The seven dimensions

**1. Generality.** Does the model support multiple downstream applications — demand forecasting, load disaggregation, anomaly detection, flexibility estimation, retrofit assessment, renewable-generation prediction, dispatch, design — rather than one narrowly defined task? Evaluate at the level of reusable capabilities, not the number of variables a single model happens to output.

**2. Transferability.** Buildings, neighbourhoods, cities, climates, technologies and carriers differ substantially in this domain. Relevant transfer tests: unseen buildings, unseen neighbourhoods or cities, different climates, different archetypes, different technology configurations, different carriers, future time periods. A model that only performs well within its training distribution has not demonstrated this. A building-energy study of time-series foundation models makes the point concretely: zero-shot performance can fall short when the target system differs from the pretraining distribution, while fine-tuning — including parameter-efficient fine-tuning — recovers much of the gap.[^park2025probforecasting] **Transferability is therefore a property to be measured on held-out systems, not inferred from the fact that a model was pretrained broadly.**

**3. Task generality.** Transfer across *instances* (dimension 2) is not the same as transfer across *task types*. A stronger test is whether the same pretrained representation can be adapted to substantially different downstream tasks — forecasting, classification, simulation, optimisation, control — not just re-run on a new building for the same task it was trained on.

**4. Physical consistency.** Purely data-driven models can produce physically infeasible predictions, and physics-informed machine learning provides established ways to prevent this — as physics-informed inputs, loss functions, architectural design, or ensemble models.[^ma2025piml_bem] (The broader physics-informed ML literature this specific taxonomy sits within is surveyed in [^karniadakis2021piml].) Ask whether a model's outputs satisfy conservation principles, respect technological operating constraints, and remain physically meaningful when transferred to new conditions — not whether the whole model is architecturally a physics-informed neural network. Physics can equally enter through the training data, the loss, the architecture, or coupling with a conventional simulator at inference time. See [§5.6](../chapter-5-case-study/5-6-physics-loss.html) for how this book's own case study handles it.

**5. Data efficiency.** Energy data in this domain is often heterogeneous, incomplete, proprietary, or expensive to collect — see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html). The relevant measurement is how much local data is needed to adapt a pretrained model to a new building, neighbourhood, technology, climate, or task — compared against a task-specific baseline trained from scratch, not assumed from model size alone.

**6. Uncertainty awareness.** Energy-system decisions are made under uncertainty from weather, occupancy, technology performance, prices, and behaviour. A systematic review of uncertainty quantification in ML-based building energy modelling identifies three primary uncertainty sources — building operations, simulation tools, and the ML model itself — and categorises their contributing factors into aleatoric and epistemic uncertainty.[^xu2025uq_bem] A model producing accurate point predictions with no indication of when they are unreliable is insufficient for decision-critical use here; probabilistic predictions, ensembles, Bayesian methods, or calibrated confidence estimates are the usual routes to closing this gap. That this is achievable with foundation models specifically, rather than only with purpose-built probabilistic models, is shown for building energy systems by the same study cited under dimension 2, which treats probabilistic forecasting alongside zero-shot and fine-tuned prediction as part of one evaluation.[^park2025probforecasting]

**7. Computational benefit.** Foundation models for the electric power grid have been proposed partly to replace or accelerate expensive repeated calculations while staying adaptable across applications.[^hamann2024foundation] The equivalent case here: replacing expensive simulation calls with a surrogate, accelerating optimisation, enabling scenario exploration, supporting real-time control. But speed is not a standalone virtue — a faster model whose errors lead to materially different energy-system decisions is not a better model. See the amortisation argument in [§2.8](2-8-surrogates-vs-fms.html) and [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html) for when the trade actually pays off.

## Reading these seven together

None of the seven substitutes for another. A model can be general (1) without being transferable (2); transferable across buildings (2) without being transferable across task types (3); physically consistent (4) while providing no uncertainty estimate (6); and fast (7) while being wrong in a way that changes a decision. A UES foundation-model claim should be read as a claim across all seven, not a claim on whichever one the authors chose to report.

{: .warning }
Treat this as a checklist for reading and writing UES-FM claims, not as a validated benchmark suite with agreed metrics per dimension — no such suite exists yet for this domain (see [Chapter 6's open gaps](../chapter-6-outlook/6-1-open-gaps.html), particularly [G4](../chapter-6-outlook/6-1-open-gaps.html#g4)). Building one is exactly the kind of contribution a UES-FM benchmark paper could make.

[^ma2025piml_bem]: Ma, Z., Jiang, G., Hu, Y., Chen, J. (2025). [A review of physics-informed machine learning for building energy modeling](https://doi.org/10.1016/j.apenergy.2024.125169). *Applied Energy*, 381, 125169.
[^karniadakis2021piml]: Karniadakis, G. E., Kevrekidis, I. G., Lu, L. et al. (2021). [Physics-informed machine learning](https://doi.org/10.1038/s42254-021-00314-5). *Nature Reviews Physics*, 3(6), 422–440.
[^xu2025uq_bem]: Xu, X., Hu, Y., Atamturktur, S. et al. (2025). [Systematic review on uncertainty quantification in machine learning-based building energy modeling](https://doi.org/10.1016/j.rser.2025.115817). *Renewable and Sustainable Energy Reviews*, 218, 115817.
[^park2025probforecasting]: Park, Y.-J., Germain, F., Liu, J. et al. (2025). [Probabilistic forecasting for building energy systems using time-series foundation models](https://doi.org/10.1016/j.enbuild.2025.116446). *Energy and Buildings*, 348, 116446.
[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.

---
[← Previous: 2.8 Surrogates vs Foundation Models](2-8-surrogates-vs-fms.html) · [Back to Chapter 2](index.html) · [Next: Chapter 3 — Simulation and Optimisation in UES →](../chapter-3-sim-opt/index.html)
