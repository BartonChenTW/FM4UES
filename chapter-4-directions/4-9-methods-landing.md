---
title: "4.9 A Proposed Development Path"
parent: Chapter 4 — Directions for FMs in UES
has_children: true
nav_order: 9
status: draft
last_reviewed: 2026-09-11
redirect_from: /06-methods-tier1.html
---

# 4.9 A Proposed Development Path: Methods by Problem Class
{: .no_toc }

{% include page-status.html %}

The book's own proposal for how a foundation model for multi-carrier (multi-vector) energy systems could be developed, in three tiers of increasing difficulty.
{: .fs-6 .fw-300 }

{: .important }
**A proposal, not a survey.** The rest of this chapter surveys what exists and screens what could work, without choosing between the options. This section does choose. It sets out one possible route to a foundation model for multi-carrier energy systems: start with a single energy hub's operation (Tier 1), extend it to several connected hubs and carriers (Tier 2), then take on design and sizing decisions (Tier 3). Each tier gives a build plan: which baselines to run, which existing models to try, and when a custom architecture is justified. The route has not been built or tested as a whole. Read it as a research plan to argue with, not as established practice. [Chapter 5](../chapter-5-case-study/index.html) works through one concrete version of the same goal in full depth.

```mermaid
flowchart LR
    A["Tier 1<br/>Single hub, dispatch"] --> B["Tier 2<br/>Multi-hub, multi-carrier"]
    B --> C["Tier 3<br/>Design & sizing"]
```

- [4.9.1 — Tier 1: single hub, dispatch only](4-9-1-methods-tier1.html)
- [4.9.2 — Tier 2: multi-hub, multi-carrier, dispatch only](4-9-2-methods-tier2.html)
- [4.9.3 — Tier 3: design and sizing optimisation](4-9-3-methods-tier3.html)

---
[← Previous: 4.8 Candidate Sub-Fields](4-8-candidate-subfields.html) · [Next: 4.9.1 Tier 1 →](4-9-1-methods-tier1.html)
