---
title: Chapter 5 — Case Study
nav_order: 6
has_children: true
status: draft
last_reviewed: 2026-11-19
---

# Chapter 5 — Case Study: A Foundation Model for Multi-Carrier Energy Hubs
{: .no_toc }

{% include page-status.html %}

One specific, opinionated proposal, worked through in full technical depth: representation, token schema, module decomposition, a phased roadmap, and the risks that could kill it.
{: .fs-6 .fw-300 }

{: .note }
**This chapter is a case study, not a survey.** It commits to one representation and one roadmap, where [Chapter 4](../chapter-4-directions/index.html) deliberately stayed neutral across many directions. Treat everything here as one group's specific bet, argued in full — not as "what the field has established."

```mermaid
flowchart LR
    subgraph BUS["Carrier-bus tokens (carrier + quality level)"]
        B2["B2: Electricity · MV<br/>Grid import"]
        B1["B1: Electricity · 0.4 kV<br/>Internal LV"]
        B5["B5: Natural gas<br/>Import"]
        B3["B3: Heat · 75 °C<br/>DH supply"]
        B4["B4: Heat · 45 °C<br/>DH return / LT loop"]
        B6["B6: Ambient · ~12 °C<br/>Ground source"]
    end
    subgraph DEV["Device tokens (multi-port conversion & storage)"]
        D8["D8: Transformer"]
        D4["D4: Rooftop PV"]
        D5["D5: Battery (state)"]
        D1["D1: CHP unit"]
        D3["D3: Gas boiler"]
        D6["D6: Hot water tank (state)"]
        D2["D2: Heat pump"]
        D7["D7: Borehole seasonal storage (state)"]
    end
    B2 <-->|"in / out"| D8
    D8 <-->|"in / out"| B1
    D4 -->|"out"| B1
    B1 <-->|"charge / discharge"| D5
    B5 -->|"gas in"| D1
    D1 -->|"elec out"| B1
    D1 -->|"75 °C heat out"| B3
    B5 -->|"gas in"| D3
    D3 -->|"75 °C heat out"| B3
    B3 <-->|"charge / discharge"| D6
    B1 -->|"elec in"| D2
    B6 -->|"source in"| D2
    D2 -->|"45 °C heat out"| B4
    B4 <-->|"seasonal state"| D7
    D7 <-->|"ground coupling"| B6
    B3 -.->|"quality downgrade permitted (upgrade forbidden)"| B4
```

*Bipartite representation of the 50-building district worked example in [§5.3.3](5-3-concrete-representation.html#533-worked-example--a-50-building-district).* Devices are first-class nodes with typed ports rather than edges, because multi-input/multi-output converters (CHP, heat pumps) connect three carrier-buses at once; the one-way quality edge (`B3 → B4`) forbids free upgrading of heat temperature without a device and has no analogue in power-grid models.

## In this chapter

| § | Page | Covers |
| :--- | :--- | :--- |
| 5.1 | [A roadmap for a multi-carrier energy hub FM](5-1-roadmap.html) | Phases 0–5, from representation to multi-scale coupling |
| 5.2 | [The representation problem](5-2-representation-problem.html) | Why representation is four decisions, and the causal chain from representation to capability |
| 5.3 | [A concrete representation and token schema](5-3-concrete-representation.html) | Bipartite graph of carrier-bus and device tokens with a worked 50-building example; the full token schema, temporal hierarchy, masking tasks, invariances and minimum viable v0 |
| 5.4 | [Data, modules and training tasks](5-4-data-modules-and-tasks.html) | Sampling design for the case study; encoders, pretraining tasks and benchmark suite; the physics-loss inventory |
| 5.5 | [Risks and unsettled design questions](5-5-risks.html) | Five risks most likely to kill the programme; three unsettled questions |

---
[← Previous: 4.9 A Future Ecosystem of UES FMs](../chapter-4-directions/4-9-ecosystem.html) · [Next: 5.1 A Roadmap for a Multi-Carrier Energy Hub FM →](5-1-roadmap.html)
