---
title: "2.3 Choosing a Basic Element"
parent: Chapter 2 — Foundation Knowledge of FMs
nav_order: 3
status: draft
last_reviewed: 2026-09-17
redirect_from: /03-basic-elements.html
---

# 2.3 Choosing a Basic Element
{: .no_toc }

{% include page-status.html %}

If you read only one page in this book, read this one. It gives the criterion for deciding whether a foundation model is viable in a given sub-domain at all — before any question of architecture, data volume, or compute.
{: .fs-6 .fw-300 }

1. TOC
{:toc}

---

## 2.3.1 The criterion

D1 — Unit of observation (what is one training example?) and D2 — Tokenisation/encoding (how is a training example turned into something the architecture consumes?), see [§2.2](2-2-five-design-decisions.html), are usually treated as implementation detail. They are not. The choice of basic element determines what transfers, and no amount of architecture or compute compensates for a bad one.

**Why grid foundation models work.** Power networks supply their own basic element. A bus is a bus in Switzerland and in Texas, at 20 kV and at 380 kV. Two engineers decomposing the same network produce the same buses and lines. Networks are assembled from these elements by known rules. The model therefore learns *the element* and its interactions, and an unseen network is a new arrangement of familiar parts. Tokenisation is essentially given by the domain.

**Four requirements**, derived from that case. These are the criterion; they are stated in ordinary modelling language and can be applied to any proposed representation, including ones this document does not consider.

| Requirement | Plain statement | Analogy | Grid bus |
| :--- | :--- | :--- | :--- |
| **Unambiguous** | Two modellers given the same object produce the same decomposition | A mesh that does not depend on who drew it | ✓ |
| **Stable in meaning** | The element means the same thing in a different system, country or scale | A wall is a wall | ✓ |
| **Composable** | Whole systems assemble from the elements by known rules | Nodes connected by known transfer paths | ✓ |
| **Scale-independent** | The same element serves a single case and a large portfolio | One node type, any network size | ✓ |

When all four hold, the model learns the element and transfer follows. When one fails, the model is forced to memorise whole cases instead. **That is the entire mechanism behind transfer**, and it is the thing to check before committing to a foundation-model framing in any sub-domain.

## 2.3.2 Basic elements for buildings

Applying the criterion to buildings gives a negative result worth stating plainly:

{: .important }
**No candidate satisfies all four requirements.**

**(a) The whole building.** Each building as one indivisible item described by its attributes. Unambiguous — every dataset already does this — but not composable: the model learns nothing smaller than a complete building, so a typology absent from training has no parts it recognises. In practice it memorises archetypes and interpolates between them.

**(b) The thermal zone.** Physically motivated and composable, and the natural instinct for anyone from building simulation. But it fails the first requirement, for a reason this field already knows: **zoning is a modelling decision, not a property of the building.** The same building yields different zone layouts under different conventions, tools and levels of effort. A model trained across many zoned buildings partly learns the conventions of whoever zoned them.

This is not an inference from the ML side. A systematic review of thermal zoning for building energy simulation finds multiple competing *definitions* of what a zone is, and concludes that a well-documented, accurate zoning method remains something future research still has to produce.[^shin2019zoning] **A basic element whose own community has not converged on a definition cannot be unambiguous in the sense the criterion requires** — and the absence of an agreed method is precisely what makes the ambiguity systematic rather than a matter of individual care.

{: .note }
This is the most persuasive entry point available when explaining the representation problem to a building simulation audience, because it is a debate they have lived rather than an ML abstraction they must take on trust.

**(c) The building component** — wall, window, heat pump. Unambiguous and composable. But the relationship between components and energy performance is neither local nor sparse: performance emerges from envelope, systems, climate and occupancy acting together. A component-level decomposition pushes essentially all the physics into the interaction terms, which is the hardest thing to learn from data.

**(d) The time interval / patch.** A fixed-length slice of hourly output. Unambiguous, stable and scale-independent — this is what time-series foundation models use (see [§2.4.1](2-4-1-time-series-fms.html)). But it describes the *output*, not the object. A slice of a demand profile carries no information about the building that produced it, so building characteristics must be attached from outside.

**(e) The cell.** A single entry in a table — where one row meets one column. Scores better against the four requirements than (a)–(d) and fails on time-resolved output. Treated in full in [§2.4.4](2-4-4-tabular-fms.html).

### Two further difficulties specific to buildings

**Mixed information types at one level.** A building description combines continuous quantities (floor area, U-values), categories (construction type, heating system), discrete choices (which retrofit measures, which technologies), and long continuous series (8760 hourly values). These do not naturally share a common form. Grid models, by contrast, handle uniformly numerical quantities.

**The decision layer.** A model intended to support retrofit or investment decisions must represent not only what a building **is** but what could be **done to it** — insulation packages, heat pumps, PV, storage, and their combinations. This is a large, discrete, constraint-bound space with no counterpart in grid state representation. **A decision space is not a state space, and no existing energy foundation model represents one.** This is arguably the deepest structural difference from GridFM and is logged as [gap G9](../chapter-6-outlook/6-1-open-gaps.html#g9).

### The resulting claim

Any building foundation model makes a deliberate trade-off among the four requirements, whether or not its authors say so. That trade-off — not model size, data volume, or compute budget — decides what transfers to buildings the model has not seen.

## 2.3.3 Representation strategies and testable predictions

**Four strategies**, with what each makes transferable and what it forecloses.

| | Unambiguous | Composable | Carries to new typologies | Handles decisions | Produces hourly profiles |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R1** Attribute list | ✓ | ✗ | ✗ | crudely | ✗ |
| **R2** Segments + attributes | ✓ | partly | partly | ✓ | ✓ |
| **R3** Network of parts | ✗ | ✓ | ✓ | ✓ | ✓ |
| **R4** Stock-level | ✓ | ✓ (stock) | ✓ (stock) | portfolio only | aggregate only |

**R1 — Building as an attribute list.** The classical metamodel input: one fixed-length row per building. Simple, well understood, strong within the range it was fitted to. Nothing structural transfers to an unseen typology.

**R2 — Time series in segments, described by building attributes.** Hourly output cut into segments; attributes supplied alongside so the model reads the profile *in the light of* the building description (mechanism: cross-attention). Inherits the machinery of general time-series models. Carries temporal structure well, building structure partially.

**R3 — Building as a network of connected parts.** Zones or components as nodes, thermal and hydraulic couplings as edges — closest to how building physics already models. Highest transfer potential, and pays the zoning ambiguity cost of §2.3.2(b) in full. **The more principled option, currently blocked by an unsolved problem belonging to the building simulation community rather than the ML one** — that community's own review literature names the missing zoning method as open research, not settled practice.[^shin2019zoning]

**R4 — Building as an element of a stock.** Individual buildings as the basic element within a portfolio. Suits stock-level questions; gives up within-building resolution. See also [§4.2](../chapter-4-directions/4-2-fms-for-building-stocks.html) for FMs targeting whole building stocks specifically.

### Three predictions

The analysis implies where the choice matters. Stated so they can be checked, with disconfirming conditions.

> **P1 — Simple outcomes will not distinguish the options.** For annualised cost, CO₂, and position on a cost–emission trade-off curve, a plain attribute list should match anything more elaborate. These are smooth functions of a few descriptors.
>
> **P2 — Hourly profiles will.** An attribute list cannot produce an 8760-value series without compressing it first, and accuracy falls accordingly.
>
> **P3 — Unseen typologies will separate them decisively.** R1 should degrade sharply on held-out building types while structure-aware options degrade gently. **This is where the foundation-model label is earned or is not.**

{: .warning }
**When this analysis would be wrong:** if P3 fails — if a plain attribute list transfers comfortably to unseen typologies — the case for a bespoke building foundation model weakens substantially. Stating the disconfirming condition is what separates a position from advocacy, and it should survive into any publication built on this material.

[^shin2019zoning]: Shin, M., Haberl, J. S. (2019). [Thermal zoning for building HVAC design and energy simulation: A literature review](https://doi.org/10.1016/j.enbuild.2019.109429). *Energy and Buildings*, 203, 109429.

---
[← Previous: 2.2 The Five Design Decisions](2-2-five-design-decisions.html) · [Next: 2.4 Existing FMs Relevant to Energy →](2-4-existing-fms-relevant-to-energy.html)
