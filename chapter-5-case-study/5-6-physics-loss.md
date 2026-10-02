---
title: "5.6 Physics Loss"
parent: Chapter 5 — Case Study
nav_order: 6
status: draft
last_reviewed: 2026-09-11
---

# 5.6 Physics Loss, Attached to Tokens
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Applying the general physics-enforcement mechanisms from [§4.10.2](../chapter-4-directions/4-10-building-it.html#4102-enforcing-physics) to the token schema of [§5.5](5-5-token-schema.html), the physics loss for this representation covers:

- Per-carrier nodal balance at every bus and [patch](../appendices/a-glossary.html#patch)
- Conversion relations, `out = η(part-load, boundary conditions) × in`, with temperature-dependent COP
- Storage continuity with self-discharge and cyclic / seasonal boundary conditions
- Capacity, ramp, and minimum-uptime bounds
- Transport losses including thermal time delay
- **No-upgrade penalty** on any flow violating the quality ordering (the `quality_order` edge type in [§5.5.1](5-5-token-schema.html#551-token-schema))
- Emissions and primary-energy accounting

Every term references a quantity the token actually exposes — the test a representation has to pass, per [§5.2.1(e)](5-2-representation-problem.html#521-the-causal-chain-representation--data--capability). This is why the schema explicitly carries `exergy_factor`, `quality`, and `eta_params` as static token fields: each physics term above needs one of them, and a term that could not be written this way would be a sign the schema is missing a field, not that the physics should be dropped.

---
[← Previous: 5.5 Token Schema](5-5-token-schema.html) · [Next: 5.7 Module and Task Decomposition →](5-7-module-decomposition.html)
