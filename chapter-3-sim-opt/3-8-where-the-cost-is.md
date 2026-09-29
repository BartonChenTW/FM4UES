---
title: "3.8 Where the Computational Cost Actually Is"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 8
status: draft
last_reviewed: 2026-09-11
---

# 3.8 Where the Computational Cost Actually Is
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Order-of-magnitude brackets. The spread is the point.

| Task/configuration | Typical runtime |
| :--- | :--- |
| LP dispatch, single node, typical days | sub-second – seconds |
| LP dispatch, full 8760 h, district | seconds – minute |
| MILP with unit commitment | minutes – hours |
| Dynamic physical (Modelica, DH hydraulics) | tens of minutes – hours |
| UBEM, full stock, annual | minutes – hours |
| Design optimisation with dispatch inner loop | hours – days |
| AC-OPF, large network | seconds, but called thousands of times |

{: .important }
**Single runs are usually affordable. Loops are not.** Design optimisation, uncertainty quantification across weather years, and Monte Carlo risk assessment all call an inner model 10³–10⁶ times. That is where surrogates and foundation models earn their keep — and where the [amortisation argument](3-5-design-sizing-optimisation.html#the-amortisation-argument) applies.

---
[← Previous: 3.7 Schemas and Data Standards](3-7-schemas-and-standards.html) · [Back to Chapter 3](index.html) · [Next: 3.9 Building Retrofit and Whole-Life Carbon →](3-9-retrofit-and-whole-life-carbon.html)
