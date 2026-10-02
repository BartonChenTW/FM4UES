---
title: "1.5 Why UES, Why Now"
parent: Chapter 1 — Background
nav_order: 5
status: draft
last_reviewed: 2026-09-11
---

# 1.5 Why Urban Energy Systems, Why Now
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## The computational cost is already the bottleneck

Order-of-magnitude brackets on typical runtimes in this domain. The spread is the point.

| Task/configuration | Typical runtime |
| :--- | :--- |
| LP dispatch, single node, typical days | sub-second – seconds |
| LP dispatch, full 8760 h, district | seconds – minute |
| [MILP](../appendices/a-glossary.html#milp) with unit commitment | minutes – hours |
| Dynamic physical (Modelica, DH hydraulics) | tens of minutes – hours |
| UBEM, full stock, annual | minutes – hours |
| Design optimisation with dispatch inner loop | hours – days |
| AC-OPF, large network | seconds, but called thousands of times |

{: .important }
**Single runs are usually affordable. Loops are not.** Design optimisation, uncertainty quantification across weather years, and Monte Carlo risk assessment all call an inner model 10³–10⁶ times. That is where [surrogates](../appendices/a-glossary.html#surrogate) and [foundation models](../appendices/a-glossary.html#foundation-model) earn their keep — see [§3.4](../chapter-3-sim-opt/3-4-dispatch-optimisation.html) and the [amortisation argument](../chapter-5-case-study/5-1-roadmap.html).

## Why the timing works now, not five years ago

Three things converged only recently:

1. **The recipe has been validated in an adjacent, structurally similar domain.** Power-grid foundation models now exist,[^hamann2024foundation] demonstrating that a physical network domain with hard constraints can support the foundation-model pattern. This is the single most important reference point for these notes — see [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html).
2. **Time-series foundation models have matured to production grade.** Off-the-shelf [zero-shot](../appendices/a-glossary.html#zero-shot) forecasting is now a viable starting point rather than a research artefact — see [§4.1](../chapter-4-directions/4-1-off-the-shelf-fms.html).
3. **Simulation tooling for this domain is mature enough to act as a cheap, unlimited label generator.** Building energy simulation, UBEM, and energy-hub optimisation tools (surveyed in [Chapter 3](../chapter-3-sim-opt/index.html)) can synthesise arbitrarily large, fully-labelled training corpora — something real measured data essentially never offers in this domain (see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)).

What has **not** converged yet is a [basic element](../appendices/a-glossary.html#basic-element) for multi-carrier urban energy systems analogous to the grid bus — that gap, and what to do about it, is the subject of [Chapter 4](../chapter-4-directions/index.html) and [Chapter 5](../chapter-5-case-study/index.html).

[^hamann2024foundation]: Hamann, H. F., Gjorgiev, B., Brunschwiler, T. et al. (2024). [Foundation models for the electric power grid](https://doi.org/10.1016/j.joule.2024.11.002). *Joule*, 8(12), 3245–3258.

---
[← Previous: 1.4 Directions the Field Is Moving](1-4-fm-field-directions.html) · [Next: 1.6 Scope of These Notes →](1-6-scope-and-how-to-use.html)
