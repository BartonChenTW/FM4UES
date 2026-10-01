---
title: Chapter 4 — Directions for FMs in UES
nav_order: 5
has_children: true
status: draft
last_reviewed: 2026-09-29
---

# Chapter 4 — Directions for Foundation Models in Urban Energy Systems
{: .no_toc }

{% include page-status.html %}

A broad, neutral survey of which problems a foundation model could plausibly learn in this domain, and how — not one specific programme. For a single concrete proposal worked through in full depth, see [Chapter 5 — Case Study](../chapter-5-case-study/index.html).
{: .fs-6 .fw-300 }

{: .note }
**Chapter 4 vs Chapter 5.** This chapter surveys the field broadly: what's already usable off the shelf, which sub-fields pass a screening test, and the methods landscape by problem tier. It does not commit to one representation or one roadmap. [Chapter 5](../chapter-5-case-study/index.html) does exactly that, for one specific case — a foundation model for multi-carrier energy hubs.

```mermaid
quadrantChart
    title Screening UES sub-fields: data x basic element
    x-axis Scarce public data --> Abundant public data
    y-axis No clean basic element --> Clean basic element
    quadrant-1 Already FM-ready
    quadrant-2 "Element exists; generate the data"
    quadrant-3 Not yet FM-ready
    quadrant-4 "Data exists; fusion missing"
    Load FM: [0.88, 0.90]
    Grid FM: [0.74, 0.84]
    Weather / microclimate: [0.78, 0.46]
    UBEM: [0.22, 0.62]
    Multi-carrier hub: [0.12, 0.16]
    Retrofit / whole-life carbon: [0.30, 0.10]
    Behaviour and social outcomes: [0.40, 0.28]
```

The chapter's argument is this screen, not the reading order. **Load** and **grid** already have a natural basic element and public (or physically simulated) pretraining data. **UBEM** has an element but is data-generation-bottlenecked. **Weather / microclimate** has abundant geospatial data that is not yet fused with load or grid. The **multi-carrier hub** fails both axes — which is why it is the [Chapter 5](../chapter-5-case-study/index.html) case study rather than a near-term product. **Retrofit / whole-life carbon** sits beside it: impact factors per material are published, but its basic element would have to carry a decision space as well as a state (see [§3.9](../chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.html)). **Behaviour and social outcomes** have text data that language models already handle, but no simulator of people, so the direction is existing models used as checked tools (see [§3.10](../chapter-3-sim-opt/3-10-social-dimensions.html)). Task-level verdicts (T1–T11, including T4 dispatch as the strongest candidate) are in [§4.6](4-6-screening-tasks.html) and [§4.7](4-7-reading-the-screen.html). How the sub-fields would fit together — as one ecosystem of models rather than a list of candidates — is the closing synthesis in [§4.11](4-11-ecosystem.html).

## In this chapter

| § | Page | Covers |
| :--- | :--- | :--- |
| 4.1 | [Using existing FMs off the shelf](4-1-off-the-shelf-fms.html) | Zero-shot load forecasting with [Chronos](../appendices/d-model-index.html#chronos)/[TimesFM](../appendices/d-model-index.html#timesfm) — the most useful direction to practitioners today |
| 4.2 | [FMs for whole building stocks](4-2-fms-for-building-stocks.html) | Stock-level rather than single-building representation |
| 4.3 | [LLMs and agents that build or run simulation models](4-3-llm-agents-for-simulation.html) | Natural-language model setup; ties to gap G7 |
| 4.4 | [Generative design](4-4-generative-design.html) | Generating candidate system designs rather than only evaluating them |
| 4.5 | [Screening: which sub-fields fit the FM pattern](4-5-screening-fields.html) | The FM-pattern fit test, applied at sub-field level |
| 4.6 | [Screening the tasks](4-6-screening-tasks.html) | The five-criterion screen applied to the T1–T11 taxonomy |
| 4.7 | [Reading the screen](4-7-reading-the-screen.html) | What the screen implies for where to invest |
| 4.8 | [Candidate sub-fields for a new FM](4-8-candidate-subfields.html) | Load FM, grid-load bridge, UBEM FM, weather-conditioned FM, hub FM |
| 4.9 | [Methods by problem class](4-9-methods-landing.html) | Landing page for the three tiers below |
| 4.9.1 | [— Tier 1: single hub, dispatch](4-9-1-methods-tier1.html) | Build path, baselines, architecture choice |
| 4.9.2 | [— Tier 2: multi-hub, multi-carrier](4-9-2-methods-tier2.html) | Graph neural networks, neural operators, topology generalisation |
| 4.9.3 | [— Tier 3: design and sizing](4-9-3-methods-tier3.html) | Amortised optimisation, feasibility guarantees, the decision-space problem |
| 4.10 | [Building it: data, physics, evaluation, budget](4-10-building-it.html) | Data generation, physics enforcement, evaluation protocol, realistic budgets |
| 4.11 | [Putting it together: a future ecosystem of UES FMs](4-11-ecosystem.html) | Which models, on which basic elements, passing what to each other; three shapes the ecosystem could take |

---
[← Previous: Chapter 3 — Simulation and Optimisation in UES](../chapter-3-sim-opt/index.html) · [Next: Chapter 5 — Case Study →](../chapter-5-case-study/index.html)
