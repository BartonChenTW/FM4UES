---
title: "3.7 Schemas and Data Standards"
parent: Chapter 3 — Simulation and Optimisation in UES
nav_order: 7
status: draft
last_reviewed: 2026-09-11
---

# 3.7 Schemas and Data Standards
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

Two interoperability schemas already exist in this space, and both are relevant to a foundation model's data pipeline without being sufficient for it.

**ESDL (Energy System Description Language)**, maintained by TNO and Netbeheer Nederland, is a schema for describing multi-carrier energy systems — assets, networks, carriers — designed for interoperability between planning and simulation tools.[^tno2026esdl]

**CIM (Common Information Model)**, IEC 61970/61968, is the power-systems industry's interoperability standard for grid asset and topology data.[^iec61970]

## Why neither is ML-ready as-is

Both schemas were designed for **interoperability between software tools**, not for **learning**. Concretely:

- Neither defines a basic element in the sense of [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion) — they specify what fields an asset record has, not what a model should treat as its atomic, poolable unit of training data.
- Neither carries a canonical tokenisation or normalisation convention — two ESDL files describing equivalent systems are not guaranteed to be numerically comparable without additional processing.
- Neither preserves the *assumptions* behind a value alongside the value itself (see [gap G6](../chapter-6-outlook/6-1-open-gaps.html#g6)) — a schema can record a device's rated capacity, but not why that capacity was chosen or what scenario it was studied under.

This is the schema-level version of the "MATPOWER moment" gap: power systems had MATPOWER and the bus abstraction decades before [GridFM](../appendices/d-model-index.html#gridfm); multi-carrier urban energy systems have ESDL and CIM, but neither plays the equivalent role for a learned model. Closing this gap — a schema, a canonical benchmark set, and a data-generation library analogous to `gridfm-datakit` — is Phase 0 of the roadmap in [§5.1](../chapter-5-case-study/5-1-roadmap.html).

[^tno2026esdl]: TNO. [ESDL — Energy System Description Language](https://www.esdl.nl/en/).
[^iec61970]: International Electrotechnical Commission. [IEC 61970 — Energy management system application program interface (EMS-API)](https://webstore.iec.ch/en/publication/6208).

---
[← Previous: 3.6 The Tool Landscape](3-6-tool-landscape.html) · [Next: 3.8 Where the Computational Cost Actually Is →](3-8-where-the-cost-is.html)
