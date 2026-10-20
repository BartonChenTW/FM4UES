---
title: "3.4 Tools and Data Standards"
parent: "Chapter 3 — Simulation and Optimisation in UES"
nav_order: 4
status: draft
last_reviewed: 2026-09-11
redirect_from:
  - /chapter-3-sim-opt/3-6-tool-landscape.html
  - /chapter-3-sim-opt/3-7-schemas-and-standards.html
---

# 3.4 Tools and Data Standards
{: .no_toc }

{% include page-status.html %}

1. TOC
{:toc}

---

## The tool landscape
{: #tool-landscape}

Not exhaustive, but covering the families you will meet. The point of this table is that **each family produces a different data structure**, which determines what a [foundation model](../appendices/a-glossary.html#foundation-model) could consume.

| Family | Representative tools | Task coverage | Output structure |
| :--- | :--- | :--- | :--- |
| **Building simulation** | EnergyPlus, TRNSYS, IDA-ICE, ESP-r | T1, T7 | time series per zone/building |
| **UBEM** | CitySim, UMI, SimStadt, TEASER, CityBES, City Energy Analyst, CESAR-P | T1, T2 | building-resolved time series + geometry |
| **Equation-based dynamic** | Modelica (Buildings, IBPSA, DisHeatLib), Dymola, OpenModelica | T1, T6, T7 | [DAE](../appendices/a-glossary.html#dae) trajectories, high resolution |
| **District/urban platforms** | PyCity, City Energy Analyst, eNeuron | T1, T4, T6 | multi-building energy flows |
| **Energy-system optimisation** | oemof, Calliope, PyPSA, SpineOpt, TIMES/MARKAL, EnergyPLAN, OSeMOSYS | T4, T5, T8 | dispatch + capacity decisions |
| **Energy-hub / multi-carrier** | ehubX, eNeuron, hub formulations in Calliope/oemof | T4, T5 | carrier-resolved dispatch |
| **Power system** | pandapower, PowerModels, MATPOWER,[^zimmerman2011matpower] PyPSA[^brown2018pypsa] | T4, T6 | bus/line-resolved states |
| **[Co-simulation](../appendices/a-glossary.html#co-simulation)** | FMI/FMU, mosaik, HELICS | cross-task | coupled trajectories |

A taxonomic review of co-simulation practice for buildings and smart energy systems surveys exactly this landscape of coupled, tool-spanning approaches.[^alfalouji2023cosimulation] The distinction that matters for foundation models: **integrated** approaches (one solver, one formulation) produce coherent single-object outputs, while **co-simulation** approaches (separate sub-models exchanging data at a coupling interface) produce multiple loosely-coupled streams.

{: .note }
A second and more consequential way to read this table is **by the [basic element](../appendices/a-glossary.html#basic-element) each family commits to** — whole building, thermal zone, component, node/bus, or time series. That grouping, not the tool family, determines what a foundation model trained on the output can transfer. See [§2.3 Choosing a Basic Element](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html).

### MATPOWER as the reference point

MATPOWER — steady-state operations, planning and analysis tools for power systems research and education — is repeatedly invoked in these notes as "the tool that made the bus a shared, learnable object."[^zimmerman2011matpower] No equivalent tool exists yet for multi-carrier hubs; this is the "MATPOWER moment" gap named in [§5.1](../chapter-5-case-study/5-1-roadmap.html)'s roadmap.

## Schemas and data standards
{: #schemas-and-standards}

Two interoperability schemas already exist in this space, and both are relevant to a foundation model's data pipeline without being sufficient for it.

**ESDL (Energy System Description Language)**, maintained by TNO and Netbeheer Nederland, is a schema for describing multi-carrier energy systems — assets, networks, carriers — designed for interoperability between planning and simulation tools.[^tno2026esdl]

**CIM (Common Information Model)**, IEC 61970/61968, is the power-systems industry's interoperability standard for grid asset and topology data.[^iec61970]

### Why neither is ML-ready as-is

Both schemas were designed for **interoperability between software tools**, not for **learning**. Concretely:

- Neither defines a basic element in the sense of [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion) — they specify what fields an asset record has, not what a model should treat as its atomic, poolable unit of training data.
- Neither carries a canonical [tokenisation](../appendices/a-glossary.html#tokenisation) or normalisation convention — two ESDL files describing equivalent systems are not guaranteed to be numerically comparable without additional processing.
- Neither preserves the *assumptions* behind a value alongside the value itself (see [gap G6](../chapter-6-outlook/6-1-open-gaps.html#g6)) — a schema can record a device's rated capacity, but not why that capacity was chosen or what scenario it was studied under.

This is the schema-level version of the "MATPOWER moment" gap: power systems had MATPOWER and the bus abstraction decades before [GridFM](../appendices/d-model-index.html#gridfm); multi-carrier urban energy systems have ESDL and CIM, but neither plays the equivalent role for a learned model. Closing this gap — a schema, a canonical benchmark set, and a data-generation library analogous to `gridfm-datakit` — is Phase 0 of the roadmap in [§5.1](../chapter-5-case-study/5-1-roadmap.html).

[^zimmerman2011matpower]: Zimmerman, R. D., Murillo-Sánchez, C. E., Thomas, R. J. (2011). [MATPOWER: Steady-state operations, planning, and analysis tools for power systems research and education](https://doi.org/10.1109/TPWRS.2010.2051168). *IEEE Transactions on Power Systems*, 26(1), 12–19.
[^brown2018pypsa]: Brown, T., Hörsch, J., Schlachtberger, D. (2018). [PyPSA: Python for power system analysis](https://doi.org/10.5334/jors.188). *Journal of Open Research Software*, 6(1), 4.
[^alfalouji2023cosimulation]: Alfalouji, Q., Schranz, T., Falay, B. et al. (2023). [Co-simulation for buildings and smart energy systems — A taxonomic review](https://doi.org/10.1016/j.simpat.2023.102770). *Simulation Modelling Practice and Theory*, 126, 102770.
[^tno2026esdl]: TNO. [ESDL — Energy System Description Language](https://www.esdl.nl/en/).
[^iec61970]: International Electrotechnical Commission. [IEC 61970 — Energy management system application program interface (EMS-API)](https://webstore.iec.ch/en/publication/6208).

---
[← Previous: 3.3 The Energy Hub: Formalism, Dispatch, Design](3-3-energy-hub-formalism.html) · [Back to Chapter 3](index.html) · [Next: 3.5 Building Retrofit and Whole-Life Carbon →](3-5-retrofit-and-whole-life-carbon.html)
