---
title: "4.5 Screening Sub-Fields and Tasks"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 5
status: draft
last_reviewed: 2026-09-29
redirect_from:
  - /05-screening.html
  - /chapter-4-directions/4-6-screening-tasks.html
---

# 4.5 Screening: Which Sub-Fields and Tasks Fit the Foundation-Model Pattern
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## Screening criteria

A task is a plausible foundation-model target if it scores well on all five. These are the questions to ask before committing.

| # | Criterion | Test |
| :--- | :--- | :--- |
| S1 | **Ground-truth generatability** | Can I produce unlimited correct labels? (Usually: is there a simulator?) |
| S2 | **Task homogeneity** | Do instances share enough structure that transfer is plausible? |
| S3 | **Transfer value** | Are there many instances, such that training once and reusing pays back? |
| S4 | **Bottleneck worth solving** | Is the existing method actually too slow or too costly, *in the loop where it is used*? |
| S5 | **Evaluability** | Is there an objective, checkable success criterion? |

{: .important }
These five screen the **task**. They do not screen the **representation**, and a task can pass all five while remaining unviable because no [basic element](../appendices/a-glossary.html#basic-element) satisfies the criterion in [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion). Run both screens; they are independent.

## Applying the screen at sub-field level

Before applying this screen task-by-task (done in [§4.5](4-5-screening-fields.html#screening-the-tasks)), it is worth applying it at the level of whole UES sub-fields, since some sub-fields already have a natural basic element and others manifestly do not:

| Sub-field | Basic element | Self-supervision task | Public pretraining data | Maturity |
| :--- | :--- | :--- | :--- | :--- |
| **Load / smart-meter FM** | Windowed [patch](../appendices/a-glossary.html#patch) of a meter time series | Masked / next-value reconstruction | EnergyBench, [BuildingsBench](../appendices/d-model-index.html#buildingsbench) (see [§3.2](../chapter-3-sim-opt/3-2-building-simulation-data.html)) | Mature — several such models already exist ([§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html)) |
| **Grid FM** ([GridFM-v0](../appendices/d-model-index.html#gridfm)) | A bus carrying (p, q, v, δ) as a graph node; lines and transformers as edges | Masked node-feature reconstruction + AC power-flow physics loss | PGLIB-OPF, IEEE cases, gridfm-datakit | Emerging but active — see [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html) |
| **UBEM / simulator-grounded FM** | A building (envelope, geometry, HVAC, occupancy) paired with its simulated load | Conditional generation, attribute-to-profile mapping | Privately generable only | Not a found-data FM — simulator-grounded generative model |
| **Urban microclimate / geospatial-energy FM** | Satellite pixel/patch over space-time | Masked spatiotemporal reconstruction | HLS, Sentinel-2, ERA5 | Emerging, adjacent, not yet fused with load or grid data — see [§2.4.3](../chapter-2-fm-foundations/2-4-3-clean-energy-forecasting-fms.html#weather-and-geospatial) |
| **District multi-energy hub** | Not yet defined | Not yet defined | Essentially none public | Immature — the subject of [Chapter 5](../chapter-5-case-study/index.html) |
| **Retrofit / [whole-life carbon](../appendices/a-glossary.html#whole-life-carbon)** | Not yet defined — a building *plus* the set of measures feasible on it ([G9](../chapter-6-outlook/6-1-open-gaps.html#g9)) | Not yet defined | Impact factors per material are published (e.g. KBOB); paired building–measure–outcome corpora privately generable only | Immature — domain side in [§3.5](../chapter-3-sim-opt/3-5-retrofit-and-whole-life-carbon.html) |
| **Behaviour, adoption and social outcomes** | For people, not settled — a household or owner as an agent; for text sources, the language model's own tokens | For agents, none (no simulator of people); for text, existing LLM pretraining | Surveys (small, periodic), observed adoption (one history), meter data (privacy-constrained), text (abundant, unstructured) | Off-the-shelf LLMs usable as bounded tools; validity unresolved — see [§3.6](../chapter-3-sim-opt/3-6-social-dimensions.html), [§4.3](4-3-llm-agents-for-simulation.html) |

**Assessment.** Load FM and grid FM cleanly qualify: each has a natural atomic element, a natural masking-based pretext task, and either real or physically-simulated broad data. UBEM qualifies in spirit but is data-generation-bottlenecked rather than found-data-abundant. **The multi-carrier hub layer currently has no clean basic element** — which is itself the central finding motivating [Chapter 5](../chapter-5-case-study/index.html). **Retrofit fails for a related reason**: its basic element has to carry a [decision space](../appendices/a-glossary.html#decision-space) as well as a state, which no existing energy FM does. **Behaviour and social outcomes fail differently**: there is no simulator of people to generate ground truth, so the route is using existing language models as checked tools rather than pretraining a new model.

## Screening the tasks
{: #screening-the-tasks}

This page applies the five screening criteria of [§4.5](4-5-screening-fields.html) to each of the eleven modelling tasks (T1–T11) of [§3.1](../chapter-3-sim-opt/3-1-taxonomy-of-tasks.html). The criteria ask:

- **S1 ground truth:** can unlimited correct labels be produced, usually by running a simulator or solver?
- **S2 homogeneity:** do instances of the task share enough structure for a model to transfer between them?
- **S3 transfer:** are there enough instances that training once and reusing pays back?
- **S4 bottleneck:** is the current method too slow or costly *in the loop where it is used*?
- **S5 evaluable:** is there an objective way to check a result?

✔ means the task passes the criterion, ◐ that it passes partly, and ✘ that it fails. The verdicts are these notes' own assessment, reached by applying the criteria. [§4.6](4-6-reading-the-screen.html) explains each row, with the evidence behind it.

| Task | S1 ground truth | S2 homogeneity | S3 transfer | S4 bottleneck | S5 evaluable | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1 UBEM demand | ✔ simulator | ◐ archetype-dependent | ✔ many buildings | ◐ | ✔ | **Good** — but crowded, and representation-limited |
| T2 Resource | ✔ | ✔ | ✔ | ✘ already fast | ✔ | Weak — no bottleneck |
| T3 Forecasting, aggregated load | ✔ observed | ✔ | ✔ | ◐ accuracy, not speed | ✔ | **Largely solved** — [zero-shot](../appendices/a-glossary.html#zero-shot) FMs are competitive (see [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html), [§4.1](4-1-off-the-shelf-fms.html)) |
| T3 Forecasting, single building | ✔ observed | ◐ buildings differ in ways the series does not show | ✔ | ◐ accuracy, not speed | ✔ | **Open** — zero-shot accuracy is unreliable (see [§2.4.5](../chapter-2-fm-foundations/2-4-5-load-forecasting-fms.html)) |
| **T4 Dispatch** | ✔ solver | ✔ strong | ✔ strong | ✔ in loops | ✔ energy balance | **Strongest candidate** |
| **T5 Design/sizing** | ✔ solver | ◐ | ✔ | ✔ severe | ✔ optimality gap | **Strong, harder** |
| T6 Network sim | ✔ | ◐ topology-specific | ✔ | ✔ | ✔ | **Good** — neural-operator territory |
| T7 Control | ◐ | ◐ | ✔ | ✔ real-time | ◐ | Moderate — RL territory |
| T8 Scenario/pathway | ✘ no ground truth | ✘ | ✔ | ✔ | ✘ | **Weak** — representation problem lives here instead |
| T9 Impact assessment | ✔ | ✔ | ◐ | ✘ | ✔ | Weak — no bottleneck |
| T10 Retrofit | ◐ simulator + [LCA](../appendices/a-glossary.html#lca) data per candidate; optimum needs a solver | ◐ shared measure library, instance-specific constraints | ✔ many buildings | ✔ combinatorial loop over T1 | ◐ per-candidate outcomes yes; "best plan" depends on objectives | **Promising, representation-blocked** — see [§4.6](4-6-reading-the-screen.html) |
| T11 Behaviour/adoption | ✘ no simulator of people; observational only | ◐ | ✔ many households | ◐ Monte Carlo over seeds and scenarios | ◐ one observed history; equity is normative | **Weak as an FM target** — LLMs as bounded tools instead (see [§4.6](4-6-reading-the-screen.html)) |


---
[← Previous: 4.4 Generative Design](4-4-generative-design.html) · [Back to Chapter 4](index.html) · [Next: 4.6 Reading the Screen: Where to Aim →](4-6-reading-the-screen.html)
