---
title: "4.3 LLMs and Agents That Build or Run Simulation Models"
parent: Chapter 4 — Directions for FMs in UES
nav_order: 3
status: draft
last_reviewed: 2026-10-20
---

# 4.3 LLMs and Agents That Build or Run Simulation Models
{: .no_toc }

{% include page-status.html %}

{: .note }
**Partial.** This page now covers published tools that let agents set envelope and HVAC inputs, studies that measure how far agent-built models fall from expert ones, a proposed checklist for verifying agent-built models, and energy-specific tests of language models standing in for survey respondents. Two things are still missing: any tool that chooses a building's thermal zoning, and any published case that lists the specific defaults an agent got wrong.

1. TOC
{:toc}

---

## The direction

Everything elsewhere in these notes treats a [foundation model](../appendices/a-glossary.html#foundation-model) as something that predicts a *quantity* — a trajectory, a cost, a decision. A structurally different direction uses a large language model, generally used agentically (able to call tools, write and run code, inspect results, and iterate), to **produce or operate the simulation itself**: setting up an EnergyPlus or Modelica model from a natural-language description of a building, configuring an energy-hub optimisation from a project brief, or driving an existing tool's API to explore a design space without a human writing the configuration by hand.

This is not the same claim as the rest of these notes. Elsewhere, an FM is trained to approximate what a simulator or solver would output. Here, the model is generating the *inputs* to a conventional simulator or solver — assumptions, geometry, topology, parameter choices — which then runs unchanged. The two are complementary: an agent could plausibly configure a model whose dispatch is then evaluated by one of these notes' Tier 1–3 approaches ([§4.7](4-7-methods-landing.html)).

## Why this matters, and the problem it creates

As natural-language model setup commoditises, the interesting question shifts from *generation* to *verification*: were the assumptions an agent silently chose — occupancy schedules, default U-values, a discretisation, a technology default — actually defensible for the case at hand? This is exactly **[gap G7](../chapter-6-outlook/6-1-open-gaps.html#g7)**, verification of agent-built models, logged in [Chapter 6](../chapter-6-outlook/index.html). Work on AI agents has moved the same way, towards measuring reliability rather than single successes: one framework splits agent reliability into consistency, robustness, predictability and safety, and across 15 models finds that recent gains in capability have brought only small gains in reliability.[^rabanser2026agentreliability] That is the right frame for judging this direction rather than treating it as a solved convenience.

**How the literature was searched.** A search on 19 September 2026, on arXiv only, found no tool for envelope, discretisation or technology defaults. That result was wrong because of where it looked: most of this literature is published in building-simulation journals and conference proceedings and never appears on arXiv. A second search on 20 October 2026 added OpenAlex (which indexes journals), with queries on EnergyPlus, Modelica, OpenStudio and urban building energy modelling combined with language-model terms, and on thermal zoning, archetypes, verification and synthetic survey respondents. The sections below come from that second search.

## Envelope, HVAC and model-setup tools

The question was whether any tool lets an agent set the inputs that usually carry the most silent assumptions: envelope properties (such as a wall or window U-value), the choice of HVAC and other technology, and the model's discretisation into thermal zones.

**Envelope and HVAC, under a building code.** One study compared two designs of LLM agent that edit EnergyPlus models of seven reference buildings from the Canadian national energy code (NECB 2020), with access to the code text.[^shirzadi2026necbagents] For a simple task, changing the window U-value, both designs succeeded every time and gave identical energy results. For a complex one, converting each building's HVAC system to a variable-refrigerant-flow system, the tool-augmented agent succeeded in all seven buildings with no severe simulation errors, while the autonomous agent failed in every case. The authors conclude that reliability "degrades sharply when tasks require many coordinated changes". Note what the agent was asked to do: change a reference model to an instructed value, not choose a default it was not given.

**Tool layers that carry the domain knowledge.** EnergyPlus-MCP exposes 35 tools to an agent, including inspection of HVAC configuration and automated model validation.[^li2025energyplusmcp] Its successor for the OpenStudio toolkit exposes 197 tools covering model creation, HVAC system synthesis, simulation and results analysis, and is tested on a benchmark across six language models.[^ball2026openstudiomcp] In both, the agent works through validated tools, so the know-how for assembling an HVAC system or validating a model sits in the tools rather than in the language model.

**Whole models from a description.** A fine-tuned language model translates a natural-language description of a building into an EnergyPlus model, which its authors report cuts modelling effort by over 95% and "achieves 100% accuracy in establishing BEMs".[^jiang2024eplusllm] A four-agent workflow generates and debugs EnergyPlus models from a description, producing "error-free" models that its authors report beat manual modelling on accuracy, reliability and time.[^zhang2025bemagentic] Both claims need reading carefully. "Accuracy" is measured against the description, and "error-free" means the simulation runs without errors. Neither says whether the defaults that filled the gaps in the description were right for the building.

**Parameter values checked against measurements.** The one case found where an LLM sets parameter values that are then tested against measured data is a calibration study. The LLM proposes prior distributions for a building model's calibration parameters, and the model is then calibrated against three years of a campus building's monthly utility bills. Compared with priors taken from the literature, the LLM's priors improved accuracy by 22% and made calibration converge 2.4 times faster, mostly because they started closer to the right values.[^bai2026llmpriors] The abstract does not say which parameters the priors were for.

**District and urban scale.** Language models have been used to turn a textual description of requirements into Modelica models of building and district energy systems, constrained so that the output is a valid model, which is then calibrated with weather and operational data.[^mostafavi2024modelicallm] At city scale, an LLM drew scenario settings from the literature and drove a toolchain that reconfigured and simulated an existing urban building energy model of Shanghai, with 113 archetypes standing for 311,612 buildings.[^zhou2026ubemresilience] There the LLM set the *scenarios*; the archetype defaults were inherited from the existing model. Further upstream, a multi-agent pipeline that maps building-age groups from census, map and monument data reached 90.69% overall accuracy but a macro-F1 of 67.25%, and flags low-confidence cases for manual review.[^thota2026buildingage] Building age is what urban models use to assign envelope values, so this is an assumption with its own stated confidence.

**Thermal zoning: nothing found.** No tool was found in which an LLM or agent *chooses* how a building is divided into thermal zones. An arXiv search combining language-model terms with thermal zoning returned no results, and two journal papers from 2026 whose titles suggest automated geometry or zoning could not be read beyond their titles.

**The pattern across these.** Where agents succeeded at anything complex, the domain knowledge sat in validated tools, a code-compliant reference model or measured data, and the language model chose among or edited what those provided. That is the same arrangement as the policy agent below: let the learned model propose, and let something that knows the constraints decide.

## Where agent-built models diverge from experts

No published case was found that lists a specific default an agent chose, such as a U-value or a zoning choice, against what an expert chose for the same building. Several studies measure the gap in aggregate, and they point the same way: a model that runs is often still wrong.

| Study | Domain | What was compared | Result |
| :--- | :--- | :--- | :--- |
| Sur & Jain (2025)[^sur2025promptbem] | Building energy models | LLM-built model against an industry-standard calibrated model | Up to 93.6% overall match; the abstract does not say which inputs differ in the rest |
| Wu et al. (2027)[^wu2027powercodebench] | Power-system analysis code (pandapower) | Engineering review of outputs that had already passed numerical checks | Review confirmed the requested analysis in 88% with the full workflow and 66% with simple repair, so 12–34% of outputs that passed the checks were still wrong |
| Song et al. (2026, preprint)[^song2026intentfidelity] | Multiphysics simulation code | Whether runnable code solved the intended equations | 39–40% of 220 cases ran but solved the wrong physics |
| Wan et al. (2025, preprint)[^wan2025cdlmodelica] | Modelica control modules for building plant | Success rate of generated control modules | Up to 83% success; failures needed an estimated one to eight hours of human repair, and human evaluation beat AI evaluation because the models "cannot assess simulation results or validate behavioral correctness" |
| Jia et al. (2026)[^jia2026bemeval] | Extracting model inputs from building documents | Extracted inputs against ground truth | The first task of a community benchmark; accuracy depends on the target data format |
| Jiang et al. (2025)[^jiang2025buildingscibench] | Building-science questions | 15 language models on 1,487 questions | About 50% accuracy on average and about 13% on calculations; median 20–40% on physics fundamentals and HVAC, against about 80% on standards and codes |

The last row matters most for silent defaults. Unassisted language models are weakest exactly on the physics that envelope and HVAC defaults depend on, and strongest on looking up codes, which is the part the tool layers above already supply.

## What a verification protocol should check

The checklist below is these notes' own proposal, put together from the sources cited in each item. It is meant for a model an agent has built or changed, before any result from that model is used.

1. **Assumption log.** List every input not stated in the brief, including the simulator's own defaults that nobody chose. A study of agent-built reservoir simulations found that choices "resolved tacitly through simulator defaults are invisible to the assumption log", and that rebuilding the same model several times shows how much these choices vary.[^lie2026jutulgpt]
2. **The four classic validity checks.** Is the conceptual model right; is it implemented correctly (verification); does it behave well enough for its purpose (operational validity); and are its data right?[^sargent2013vv]
3. **Comparative test cases.** Run standard comparative tests, of the kind the BESTEST procedure defines for whole-building simulation programs, on the envelope and HVAC behaviour.[^judkoff1995bestest]
4. **Physical invariants.** Check energy balance and that no energy is created. In one study of agent-built Modelica models, an invariant check exposed a model that created energy, at a level indistinguishable from noise in its fit.[^frochte2026modelicaacceptance]
5. **Acceptance by tolerance.** Accept a model if it falls within a stated set of tolerances, rather than requiring it to match one reference model. Stating the threshold explicitly made more of the agents' deliveries pass in the same study.[^frochte2026modelicaacceptance]
6. **An evaluator outside the agent.** Score the model with checks the agent cannot change; a Modelica benchmark of 232 tasks does exactly this.[^wang2026pufibara]
7. **Repeatability.** Build the same model several times and report how often all attempts succeed, not just whether one did. The measure pass^k counts a task as solved only if all k attempts succeed; GPT-4o scored below 25% on pass^8 in one benchmark's retail tasks.[^yao2024taubench] [^rabanser2026agentreliability]
8. **Calibration against measurements**, where measured data exist.[^coakley2014calibration] [^ruiz2017calibration]
9. **Sensitivity of the decision to resolution.** Check whether a coarser discretisation changes the decision the model supports, not only its error. In one study of EnergyPlus models generated from operator descriptions (without an LLM), a low-resolution model underestimated heating energy by 21%, outside ASHRAE Guideline 14, while a medium-resolution model's projected savings from energy-conservation measures closely matched the high-resolution baseline.[^fadel2026operatorbem]

Items 4 and 5 correspond to the feasibility measure of the evaluation protocol in [§4.8.3](4-8-building-it.html#483-evaluation-protocol), and item 7 to its transfer measure. Applied to an agent-built hub model, this checklist would show whether the agent's choices can be trusted. No published study has applied it, or anything like it, to a building or energy-hub model.

## One category, addressed: occupant-behaviour assumptions

Of the assumption categories listed above, occupant behaviour has a recent, concrete treatment. A platform grounds LLM agents playing simulated building occupants in the American Time Use Survey — each agent is instantiated with a demographic persona and an activity scheduler drawn from real population statistics, rather than a generic default schedule, and maintains a memory stream across timesteps so its choices can depend on its own history.[^jung2026buildocc]

**What this does and does not do, precisely.** It replaces one specific default (an arbitrary or generic occupancy schedule) with one grounded in a real, checkable dataset — genuine progress on that one assumption. It does **not** address the other assumptions listed above (U-values, discretisation or technology defaults), and the platform generates a behavioural *input* to a conventional simulator rather than configuring the simulator itself, which keeps it inside the "agent supplies inputs, simulator runs unchanged" framing above rather than the fuller "agent builds the model" case this section is named for.

**And grounding is not the same as verification.** A schedule sampled from ATUS population statistics is defensible in aggregate; whether it is the right schedule for *this* building's actual occupants is the verification question again, one level down — swapping an arbitrary default for a population-representative one narrows the range of silently wrong assumptions without eliminating the need to check the one actually in play.

## Beyond occupancy: simulated respondents, adopters and policy agents

The occupant agent above is one instance of a wider idea from social science: conditioning a language model on a demographic persona so that it answers as a member of that group would. Conditioned on thousands of sociodemographic backstories from real participants in large US surveys, GPT-3 was shown to emulate the response distributions of a wide variety of subgroups — a property its authors call *algorithmic fidelity*, with the resulting synthetic respondents called "silicon samples".[^argyle2023silicon] A later test of the same idea is more cautious. ChatGPT, prompted to adopt personas, reproduced the *average* feeling-thermometer scores of the American National Election Study closely, but with less variation than real respondents, regression coefficients that often differed significantly from the survey's, sensitivity to minor changes in prompt wording, and different results from the same prompt over three months.[^bisbee2024synthetic] Both are US political-opinion surveys, not energy decisions. What carries over is the pattern: **averages can look right while variance, relationships between variables and reproducibility do not** — and variance across households is exactly what the distributional questions in [§3.6](../chapter-3-sim-opt/3-6-social-dimensions.html) depend on.

### Tests against real energy and climate surveys

A few studies now test [silicon samples](../appendices/a-glossary.html#silicon-sample) on energy or climate questions against real respondents:

- **Heating and retrofit choices.** Four language models were asked to reproduce the answers of real respondents in a stated-preference experiment on heating systems and retrofit options, at both individual and aggregate level. The best reached 77% average accuracy. All showed systematic bias against the gas boiler and against not retrofitting, preferring more efficient options than the respondents did, and the most useful input was each respondent's own earlier choices.[^wang2025llmstatedpref] The abstract does not report variance or subgroup results.
- **Tenants and energy renovation.** Agents built from survey data on 1,068 Dutch citizens, about 40,548 question-and-answer pairs on energy-efficient renovation, predicted responses better when their personas included transaction costs (the effort and hassle of renovating). The abstract gives no figures for the improvement.[^xia2026tenantllm]
- **A reporting standard.** One framework asks every validity claim for synthetic respondents to say which of four properties it checks (the average, the spread, how answers are reached, and the relationships between variables) and to report validity for subgroups, not only overall. It is applied to electric-vehicle charging tariffs.[^kutzner2026syntheticvalidity]
- **Climate opinion, with a subgroup failure.** On two nationally representative US climate surveys, GPT-4, conditioned on demographics and other respondent characteristics, reached accuracies from 53% to 91%, and it systematically underestimated the global-warming concern of Black Americans.[^lee2024climateopinion]

The heating study is the energy test this page asked for, and it shows the same pattern as the general literature: a respectable average with a systematic bias in one direction. No test was found for heat-pump willingness to pay specifically; an arXiv search combining language-model terms with willingness to pay and energy returned nothing.

### Language models inside energy models

Two recent energy preprints use a language model in a deliberately bounded role rather than as a free-standing decision-maker:

- **Behavioural assumptions inside a calibrated [agent-based model](../appendices/a-glossary.html#agent-based-model-abm).** For PV adoption by Irish dairy farms, LLM-assisted specifications add interpretable behavioural rubrics (conservative, balanced, optimistic) and rule-validated scenario specifications, while keeping the calibrated techno-economic adoption mechanism. Adoption stays bounded and monotonic across behavioural regimes, with up to about 13% more adoption than the corresponding logistic case.[^faiud2026llmabm] The language model augments a validated model rather than replacing it — the authors' own answer to the interpretability, reproducibility and behavioural-validity concerns of replacing adoption models with LLM reasoning.
- **A policy agent scored on energy-poverty metrics.** In a simulated peer-to-peer market on an IEEE 33-bus distribution grid, an open-weight LLM sets price and carbon bounds and targeted subsidies for a community of household personas whose load curves are checked against real smart-meter data. Scored on [energy burden](../appendices/a-glossary.html#energy-burden), its Gini coefficient and a low-income-high-cost indicator, it lowered the Gini of energy burden from 0.351 to 0.305 and mean burden by 28% while cutting cost. With the LLM only setting bounds and a validate-and-project gate executing them, grid-constraint violations were zero, against 55 under direct LLM control.[^jadhav2026eqgrid] One simulated community on one test grid: the equity figures are a demonstration, not evidence about real households. The architectural point is the one that transfers, and it is the same as the retrofit corollary in [§4.7.3](4-7-3-methods-tier3.html): **let the learned model propose, and let something that knows the constraints decide.**

Both keep the language model where its output can be checked. That is the verification question of [gap G7](../chapter-6-outlook/6-1-open-gaps.html#g7) (verification of agent-built models) applied to social assumptions: a behavioural rubric or a persona is an assumption, and grounding it in a survey narrows the range of silently wrong choices without showing it is right for the population actually in question.

## What would still need to be added here

- A tool in which an agent chooses a building's thermal zoning or discretisation, and a test of it; none was found on 20 October 2026.
- A published case that lists the specific defaults an agent chose against an expert's for the same building. The studies above measure only the overall gap.
- The verification checklist above, applied to an agent-built building or energy-hub model.
- A silicon-sample test on heat-pump willingness to pay, reporting spread and subgroup results rather than only averages.

[^jung2026buildocc]: Jung, W. (2026). [BuildOcc: A large language model occupant agent platform for building energy research](https://doi.org/10.1016/j.softx.2026.103068). *SoftwareX*, 36, 103068. arXiv:2609.02729.
[^argyle2023silicon]: Argyle, L. P., Busby, E. C., Fulda, N. et al. (2023). [Out of one, many: Using language models to simulate human samples](https://doi.org/10.1017/pan.2023.2). *Political Analysis*, 31(3), 337–351.
[^bisbee2024synthetic]: Bisbee, J., Clinton, J. D., Dorff, C. et al. (2024). [Synthetic replacements for human survey data? The perils of large language models](https://doi.org/10.1017/pan.2024.5). *Political Analysis*, 32(4), 401–416.
[^faiud2026llmabm]: Faiud, I., Khaleghy, H., Schukat, M., Mason, K. (2026). [LLM-assisted behavioural and scenario augmentation for agent-based energy adoption models](https://doi.org/10.1007/978-3-032-39395-1_34). In *Multi-Agent Systems*, Lecture Notes in Computer Science, 607–623. arXiv:2609.04866.
[^jadhav2026eqgrid]: Jadhav, K., More, S. (2026). [Grounded, compute-efficient LLM policy agents for energy-poverty equity in physically-constrained peer-to-peer energy markets](https://arxiv.org/abs/2609.01918). arXiv:2609.01918.
[^rabanser2026agentreliability]: Rabanser, S., Kapoor, S., Kirgis, P. et al. (2026). [Towards a science of AI agent reliability](https://arxiv.org/abs/2602.16666). arXiv:2602.16666. Accepted at ICML 2026.
[^shirzadi2026necbagents]: Shirzadi, N., Lopez, P., Stylianou, M. (2026). [Tool-augmented vs. autonomous LLM agents for building energy model modifications: A comparative study using NECB compliance models](https://doi.org/10.1016/j.egyai.2026.100896). *Energy and AI*, 26, 100896.
[^li2025energyplusmcp]: Li, H., Xu, Y., Hong, T. (2025). [EnergyPlus-MCP: A model-context-protocol server for AI-driven building energy modeling](https://doi.org/10.1016/j.softx.2025.102367). *SoftwareX*, 32, 102367.
[^ball2026openstudiomcp]: Ball, B. L., Long, N., Fleming, K. et al. (2026). [OpenStudio-MCP: A model context protocol (MCP) server for AI agent-driven building energy modeling with the OpenStudio SDK](https://doi.org/10.1016/j.softx.2026.103020). *SoftwareX*, 36, 103020.
[^jiang2024eplusllm]: Jiang, G., Ma, Z., Zhang, L. et al. (2024). [EPlus-LLM: A large language model-based computing platform for automated building energy modeling](https://doi.org/10.1016/j.apenergy.2024.123431). *Applied Energy*, 367, 123431.
[^zhang2025bemagentic]: Zhang, L., Ford, V., Chen, Z. et al. (2025). [Automatic building energy model development and debugging using large language models agentic workflow](https://doi.org/10.1016/j.enbuild.2024.115116). *Energy and Buildings*, 327, 115116.
[^bai2026llmpriors]: Bai, Y., Wang, E. (2026). [LLM-informed efficient Bayesian calibration of building energy simulation models under limited data](https://doi.org/10.26868/30680611.2026.1308). *Proceedings of SimBuild Conference 2026*, 12.
[^mostafavi2024modelicallm]: Mostafavi, S., Maxwell, J. T., Zhenirovskyy, M. et al. (2024). [Simplifying modeling for building and district energy systems with large language models](https://doi.org/10.26868/30680611.2024.2256). *Proceedings of SimBuild Conference 2024*, 11.
[^zhou2026ubemresilience]: Zhou, J., Chen, J., Wang, M. et al. (2026). [Large language model orchestrated workflow integrating retrieval-augmented generation and model context protocol tools for urban-scale simulation-based resilience assessment](https://doi.org/10.1016/j.buildenv.2026.114553). *Building and Environment*, 297, 114553.
[^thota2026buildingage]: Thota, K., Schlachter, T., Hagenmeyer, V. (2026). [A multi-agent system for building-age cohort mapping to support urban energy planning](https://arxiv.org/abs/2603.17626). arXiv:2603.17626.
[^sur2025promptbem]: Sur, D. A., Jain, R. K. (2025). [Demonstrating the feasibility of prompt engineering to develop complex building energy models](https://doi.org/10.26868/25222708.2025.1230). *Proceedings of Building Simulation 2025: 19th Conference of IBPSA*, 19.
[^wu2027powercodebench]: Wu, H., Wang, X., Fan, Z. (2027). [Knowledge boundary probing and demand-guided intervention for LLM-based power system code generation](https://doi.org/10.1016/j.aei.2026.105328). *Advanced Engineering Informatics*, 77, 105328. arXiv:2605.31478. Published online 2026.
[^song2026intentfidelity]: Song, Z., Liu, Y., Wan, C. et al. (2026). [Your simulation runs but solves the wrong physics: PDE-grounded intent verification for LLM-generated multiphysics simulation code](https://arxiv.org/abs/2605.09360). arXiv:2605.09360.
[^wan2025cdlmodelica]: Wan, H., Lu, X., Chen, Y. et al. (2025). [Automating Modelica module generation using large language models: A case study on building control description language](https://arxiv.org/abs/2509.14623). arXiv:2509.14623. Pre-peer-review version of a journal paper.
[^jia2026bemeval]: Jia, Y., Fu, X., Zhang, L. (2026). [BEMEval-Doc2Schema: Benchmarking large language models for structured data extraction in building energy modeling](https://doi.org/10.26868/30680611.2026.1360). *Proceedings of SimBuild Conference 2026*, 12. arXiv:2602.16926.
[^jiang2025buildingscibench]: Jiang, G., Chen, K., Liu, J. et al. (2025). [Benchmarking knowledge and capability of large language models in building science domain](https://doi.org/10.59717/ipj.energy-use.2025.100026). *Energy Use*, 1(2), 100026.
[^lie2026jutulgpt]: Lie, K.-A., Møyner, O., Svee, E. et al. (2026). [Agentic scientific simulation: Execution-grounded model construction and reconstruction](https://arxiv.org/abs/2603.00214). arXiv:2603.00214.
[^sargent2013vv]: Sargent, R. G. (2013). [Verification and validation of simulation models](https://doi.org/10.1057/jos.2012.20). *Journal of Simulation*, 7(1), 12–24.
[^judkoff1995bestest]: Judkoff, R., Neymark, J. (1995). [International Energy Agency building energy simulation test (BESTEST) and diagnostic method](https://doi.org/10.2172/90674). NREL/TP-472-6231, National Renewable Energy Laboratory.
[^frochte2026modelicaacceptance]: Frochte, J., Schmidt, H. (2026). [LLM agents as suppliers of physical system models: Calibration and acceptance in Modelica](https://arxiv.org/abs/2610.25019). arXiv:2610.25019.
[^wang2026pufibara]: Wang, Z. (2026). [Beyond executable models: The Pufibara agent harness and the Modelica agent workflow benchmark for physical system modeling](https://arxiv.org/abs/2608.23653). arXiv:2608.23653.
[^yao2024taubench]: Yao, S., Shinn, N., Razavi, P. et al. (2024). [τ-bench: A benchmark for tool-agent-user interaction in real-world domains](https://arxiv.org/abs/2406.12045). arXiv:2406.12045.
[^coakley2014calibration]: Coakley, D., Raftery, P., Keane, M. (2014). [A review of methods to match building energy simulation models to measured data](https://doi.org/10.1016/j.rser.2014.05.007). *Renewable and Sustainable Energy Reviews*, 37, 123–141.
[^ruiz2017calibration]: Ruiz, G., Bandera, C. (2017). [Validation of calibrated energy models: Common errors](https://doi.org/10.3390/en10101587). *Energies*, 10(10), 1587.
[^fadel2026operatorbem]: Fadel, M., Günay, B., O'Brien, L. et al. (2026). [Toward automated generation of EnergyPlus models for existing buildings through operator descriptions](https://doi.org/10.26868/31114504.2026.90). *Proceedings of eSim 2026: 14th Conference of IBPSA-Canada*.
[^wang2025llmstatedpref]: Wang, H., Pawlak, J., Sivakumar, A. (2025). [Can large language models simulate human responses? A case study of stated preference experiments in the context of heating-related choices](https://arxiv.org/abs/2503.10652). arXiv:2503.10652.
[^xia2026tenantllm]: Xia, W., Horian, S., Huang, H. et al. (2026). [Simulating tenant responses to energy policy interventions with transaction-cost-aware LLM agent](https://arxiv.org/abs/2607.24341). arXiv:2607.24341.
[^kutzner2026syntheticvalidity]: Kutzner, F., Kacperski, C., de Molière, L. et al. (2026). [Consequential behaviour and representational fairness in the validation of synthetic research](https://arxiv.org/abs/2609.27690). arXiv:2609.27690.
[^lee2024climateopinion]: Lee, S., Peng, T.-Q., Goldberg, M. H. et al. (2024). [Can large language models estimate public opinion about global warming? An empirical assessment of algorithmic fidelity and bias](https://doi.org/10.1371/journal.pclm.0000429). *PLOS Climate*, 3(8), e0000429.

---
[← Previous: 4.2 FMs for Whole Building Stocks](4-2-fms-for-building-stocks.html) · [Back to Chapter 4](index.html) · [Next: 4.4 Generative Design →](4-4-generative-design.html)
