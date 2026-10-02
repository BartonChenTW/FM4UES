---
title: "4.6 Screening the Tasks"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 6
status: draft
last_reviewed: 2026-10-03
---

# 4.6 Screening the Tasks
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

This page applies the five screening criteria of [§4.5](4-5-screening-fields.html) to each of the eleven modelling tasks (T1–T11) of [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html). The criteria ask:

- **S1 ground truth:** can unlimited correct labels be produced, usually by running a simulator or solver?
- **S2 homogeneity:** do instances of the task share enough structure for a model to transfer between them?
- **S3 transfer:** are there enough instances that training once and reusing pays back?
- **S4 bottleneck:** is the current method too slow or costly *in the loop where it is used*?
- **S5 evaluable:** is there an objective way to check a result?

✔ means the task passes the criterion, ◐ that it passes partly, and ✘ that it fails. The verdicts are these notes' own assessment, reached by applying the criteria. [§4.7](4-7-reading-the-screen.html) explains each row, with the evidence behind it.

| Task | S1 ground truth | S2 homogeneity | S3 transfer | S4 bottleneck | S5 evaluable | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1 UBEM demand | ✔ simulator | ◐ archetype-dependent | ✔ many buildings | ◐ | ✔ | **Good** — but crowded, and representation-limited |
| T2 Resource | ✔ | ✔ | ✔ | ✘ already fast | ✔ | Weak — no bottleneck |
| T3 Forecasting, aggregated load | ✔ observed | ✔ | ✔ | ◐ accuracy, not speed | ✔ | **Largely solved** — [zero-shot](../appendices/a-glossary.html#zero-shot) FMs are competitive (see [§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html), [§4.1](4-1-off-the-shelf-fms.html)) |
| T3 Forecasting, single building | ✔ observed | ◐ buildings differ in ways the series does not show | ✔ | ◐ accuracy, not speed | ✔ | **Open** — zero-shot accuracy is unreliable (see [§2.4.6](../chapter-2-fm-foundations/2-4-6-load-forecasting-fms.html)) |
| **T4 Dispatch** | ✔ solver | ✔ strong | ✔ strong | ✔ in loops | ✔ energy balance | **Strongest candidate** |
| **T5 Design/sizing** | ✔ solver | ◐ | ✔ | ✔ severe | ✔ optimality gap | **Strong, harder** |
| T6 Network sim | ✔ | ◐ topology-specific | ✔ | ✔ | ✔ | **Good** — neural-operator territory |
| T7 Control | ◐ | ◐ | ✔ | ✔ real-time | ◐ | Moderate — RL territory |
| T8 Scenario/pathway | ✘ no ground truth | ✘ | ✔ | ✔ | ✘ | **Weak** — representation problem lives here instead |
| T9 Impact assessment | ✔ | ✔ | ◐ | ✘ | ✔ | Weak — no bottleneck |
| T10 Retrofit | ◐ simulator + [LCA](../appendices/a-glossary.html#lca) data per candidate; optimum needs a solver | ◐ shared measure library, instance-specific constraints | ✔ many buildings | ✔ combinatorial loop over T1 | ◐ per-candidate outcomes yes; "best plan" depends on objectives | **Promising, representation-blocked** — see [§4.7](4-7-reading-the-screen.html) |
| T11 Behaviour/adoption | ✘ no simulator of people; observational only | ◐ | ✔ many households | ◐ Monte Carlo over seeds and scenarios | ◐ one observed history; equity is normative | **Weak as an FM target** — LLMs as bounded tools instead (see [§4.7](4-7-reading-the-screen.html)) |

---
[← Previous: 4.5 Screening Sub-Fields](4-5-screening-fields.html) · [Next: 4.7 Reading the Screen →](4-7-reading-the-screen.html)
