---
title: "4.6 Screening the Tasks"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 6
status: draft
last_reviewed: 2026-09-29
---

# 4.6 Screening the Tasks
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Applying the five criteria from [§4.5](4-5-screening-fields.html) to the task taxonomy T1–T11 from [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html):

| Task | S1 ground truth | S2 homogeneity | S3 transfer | S4 bottleneck | S5 evaluable | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1 UBEM demand | ✔ simulator | ◐ archetype-dependent | ✔ many buildings | ◐ | ✔ | **Good** — but crowded, and representation-limited |
| T2 Resource | ✔ | ✔ | ✔ | ✘ already fast | ✔ | Weak — no bottleneck |
| T3 Forecasting | ✔ observed | ✔ | ✔ | ◐ | ✔ | **Solved** — mature FMs exist (see [§4.1](4-1-off-the-shelf-fms.html)) |
| **T4 Dispatch** | ✔ solver | ✔ strong | ✔ strong | ✔ in loops | ✔ energy balance | **Strongest candidate** |
| **T5 Design/sizing** | ✔ solver | ◐ | ✔ | ✔ severe | ✔ optimality gap | **Strong, harder** |
| T6 Network sim | ✔ | ◐ topology-specific | ✔ | ✔ | ✔ | **Good** — neural-operator territory |
| T7 Control | ◐ | ◐ | ✔ | ✔ real-time | ◐ | Moderate — RL territory |
| T8 Scenario/pathway | ✘ no ground truth | ✘ | ✔ | ✔ | ✘ | **Weak** — representation problem lives here instead |
| T9 Impact assessment | ✔ | ✔ | ◐ | ✘ | ✔ | Weak — no bottleneck |
| T10 Retrofit | ◐ simulator + LCA data per candidate; optimum needs a solver | ◐ shared measure library, instance-specific constraints | ✔ many buildings | ✔ combinatorial loop over T1 | ◐ per-candidate outcomes yes; "best plan" depends on objectives | **Promising, representation-blocked** — see [§4.7](4-7-reading-the-screen.html) |
| T11 Behaviour/adoption | ✘ no simulator of people; observational only | ◐ | ✔ many households | ◐ Monte Carlo over seeds and scenarios | ◐ one observed history; equity is normative | **Weak as an FM target** — LLMs as bounded tools instead (see [§4.7](4-7-reading-the-screen.html)) |

---
[← Previous: 4.5 Screening Sub-Fields](4-5-screening-fields.html) · [Next: 4.7 Reading the Screen →](4-7-reading-the-screen.html)
