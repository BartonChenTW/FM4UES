---
title: "5.8 Risks and Unsettled Design Questions"
parent: Chapter 5 — Case Study
nav_order: 8
status: draft
last_reviewed: 2026-09-11
---

# 5.8 Risks and Unsettled Design Questions
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## 5.8.1 Five risks most likely to kill the programme

1. **Label degeneracy.** Cost-optimal dispatch has many equally-optimal solutions. Mitigation: predict objective values, active sets, and distributions rather than argmins — see D3 and D4 in [§5.7](5-7-module-decomposition.html), and the "not only cost-optimal" data-generation guidance in [§5.3](5-3-data-generation.html).
2. **Discrete decisions do not interpolate.** Mitigation: treat installation as classification over a fixed technology vocabulary, not regression on a capacity vector (see the device vocabulary decision in [§5.2.2](5-2-representation-problem.html#522-the-five-decisions-the-paper-must-make-explicit)).
3. **Seasonal coupling breaks windowing.** Requires the hierarchical tokenisation in [§5.5.2](5-5-token-schema.html#552-temporal-hierarchy); this is an open architectural problem, not a solved one.
4. **No real data, ever.** Multi-carrier district data is scarcer than grid data and more privacy-encumbered. Synthetic-first is the only path (see [§5.3](5-3-data-generation.html)), so validation against any available real operating-building data is the credibility anchor for the whole programme.
5. **You may be building a very expensive interpolator.** If Phase 1 surrogates ([§5.1](5-1-roadmap.html)) do not beat a well-tuned reduced-order model on held-out topologies, the FM premise fails. This is why the [minimum viable v0](5-5-token-schema.html#555-minimum-viable-v0) builds this kill criterion in explicitly, and why the amortisation argument in [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) only pays off if transfer actually holds.

## 5.8.2 Three genuinely unsettled design questions

- **Shadow prices as features.** Including solver duals (see the `shadow_price` field in [§5.5.1](5-5-token-schema.html#551-token-schema)) gives rich supervision for free and they are what regulators actually need, but they may encode solver artefacts and degeneracy tiebreaks rather than physics. Recommendation: include as an auxiliary prediction head rather than an input feature, so they can be ablated.
- **Heterogeneous graph transformers are the weak link.** Almost every successful FM uses one token type. This design needs two plus three edge types (see [§5.5.1](5-5-token-schema.html#551-token-schema)). This machinery is far less battle-tested than sequence transformers (see [§2.7](../chapter-2-fm-foundations/2-7-architectures.html)), and is the assumption most likely to cost a year.
- **Quality discretisation is arbitrary at the boundaries.** Is 60 °C its own level or does it round to 75? Continuous temperature is physically honest but makes the ordering constraint harder to express as a differentiable penalty. Current lean: discrete levels with continuous temperature as an auxiliary feature — but not settled. See the carrier-quality-encoding decision in [§5.2.2](5-2-representation-problem.html#522-the-five-decisions-the-paper-must-make-explicit).

{: .note }
These risks and open questions are deliberately kept separate from [Chapter 6's open gaps](../chapter-6-outlook/6-1-open-gaps.html), which are framed as research contributions available to the wider field. The items here are specific to this one case study's engineering choices, not general statements about what UES-FM research needs.

## 5.8.3 Reading this proposal against the seven evaluation dimensions

[§2.9](../chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.html) sets out seven dimensions for judging any UES foundation-model claim. Applying them here, honestly, rather than only to a hypothetical future proposal:

| Dimension | Where this case study stands |
| :--- | :--- |
| Generality | Designed for it — the token schema ([§5.5](5-5-token-schema.html)) and module decomposition ([§5.7](5-7-module-decomposition.html)) target dispatch, design and sizing together — but this is a design intent, not yet a demonstrated result. No task has been run. |
| Transferability | The entire premise (see [§5.2](5-2-representation-problem.html)) — untested. Risk 5 above (*"a very expensive interpolator"*) is precisely the failure mode where this claim would not hold. |
| Task generality | Same status as generality: designed for, not demonstrated. |
| Physical consistency | Addressed directly by the physics loss in [§5.6](5-6-physics-loss.html) — the most concretely specified dimension of the seven, for this proposal. |
| Data efficiency | Unaddressed. Risk 4 (*"no real data, ever"*) means this cannot even be measured against a real baseline yet, only against synthetic data's own generating assumptions. |
| Uncertainty awareness | Not designed in. The `shadow_price` auxiliary head (unsettled question above) is the closest thing to it, and that is about supervision signal, not calibrated uncertainty. This is a genuine gap in the current proposal, not only a general field gap. |
| Computational benefit | The whole roadmap ([§5.1](5-1-roadmap.html)) is staked on this, per the amortisation argument in [§3.5](../chapter-3-sim-opt/3-5-design-sizing-optimisation.html) — but, again, per risk 5, unproven until Phase 1 actually beats a tuned reduced-order model on held-out topologies.

**The honest summary: two of seven dimensions (physical consistency, computational benefit as a design target) are concretely addressed; two (generality, task generality) are designed for but undemonstrated; three (transferability, data efficiency, uncertainty awareness) are either the central open bet of the whole programme or not yet addressed at all.** Any claim from this case study that it "is" a UES foundation model, rather than a proposal for one, should be read against this table, not against the roadmap's aspirations alone.

---
[← Previous: 5.7 Module and Task Decomposition](5-7-module-decomposition.html) · [Back to Chapter 5](index.html) · [Next: Chapter 6 — Outlook →](../chapter-6-outlook/index.html)
