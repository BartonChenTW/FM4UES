# References to add

Private working list, excluded from the Jekyll site via `_config.yml` (like
`TODO.md`). Each entry is a reference not yet in
[`references/fm-for-ues.bib`](references/fm-for-ues.bib), with where it would go.
Compiled 2026-09-23 against `main` plus the unmerged
`docs/4-1-through-4-4-stub-citations` branch, so nothing already cited on
either branch is listed.

**Verified** means the metadata was checked against Crossref, arXiv or the
publisher's page. It does *not* mean the paper has been read: per
[`CONTRIBUTING.md`](CONTRIBUTING.md), each citation still needs its claim
written up as what the work demonstrated, what limitation remains, and why
that matters for UES, from the source itself.

---

## A. Suggested by Barton

### A1. Lédée, Crawford & Evins (2025): surrogates for multi-energy system design ★ high value

> **Partly done 2026-09-24; completed 2026-11-19:** added to the `.bib` as `ledee2025messurrogate` and cited in §2.1 (the surrogate-literature paragraph), §4.7.3, §3.3 (amortisation argument), and §6.1 (G9).

- **Ref:** Lédée, F., Crawford, C. and Evins, R. (2025). Improved surrogate modeling for multi-energy system design: Model architecture, sampling and scaling choices. *Applied Energy*, 390, 125812. <https://doi.org/10.1016/j.apenergy.2025.125812>. Verified via Crossref; abstract read via OpenAlex.
- **Suggested key:** `ledee2025messurrogate`
- **What the abstract says:** ML surrogates that directly predict the *optimal design* of a multi-energy system. The authors say few prior works predict the design itself, as opposed to cost or other objectives, and those that do perform poorly. Design variables show "irregularities and sudden changes" that reduce learnability. Four things improve performance on small datasets: objective-oriented sample selection, upsampling to balance the data, non-linear rescaling of outputs, and a Mixture-of-Experts network. Tested across climates, building types and decarbonisation targets.
- **Where it fits.** Each of these sentences is currently uncited:
  - [§2.1](chapter-2-fm-foundations/2-1-what-defines-an-fm.md#surrogates-vs-fms) line 24: "Surrogates are already routine in this domain: a neural network trained to predict energy hub operating cost as a function of design…" The paper is direct evidence, and also notes that predicting cost is the common case and predicting design is rare.
  - [§3.3](chapter-3-sim-opt/3-3-energy-hub-formalism.md#design-and-sizing) line 37, on why existing multi-energy surrogates rarely repay their training cost for one system in one study.
  - [§4.7.3](chapter-4-directions/4-7-3-methods-tier3.md) line 34 ("simple, proven. *Weakness:* one surrogate per system"). The paper qualifies "simple": direct design prediction needed a tailored pipeline to work at all. It also bears on Tier 3's feasibility discussion, since irregular design variables are what break learnability.
- **Caution:** "scaling choices" in the title means rescaling of the output data, not scaling laws. Don't cite it in [§2.5](chapter-2-fm-foundations/2-5-scaling-laws.md).

### A2. *Forecasting: Principles and Practice, the Pythonic Way*, ch. 15 "Foundation forecasting models"

> **Done 2026-11-24:** verified online edition (`https://otexts.com/fpppy/`, last updated 20 November 2026), added to `.bib` as `hyndman2026fpppy`, and cited in [§4.1](chapter-4-directions/4-1-off-the-shelf-fms.md) (Nord Pool electricity-price forecasting example with TimeGPT and Moirai using load and wind forecasts as known-future covariates).

- **Ref:** Hyndman, R. J., Athanasopoulos, G., Garza, A., Challu, C., Mergenthaler Canseco, M. and Olivares, K. G. (2026). *Forecasting: Principles and Practice, the Pythonic Way*. OTexts. Chapter 15, <https://otexts.com/fpppy/15-foundation-models.html>.
- **Barton's note:** "not the fan really, but we should not disregard it completely."
- **Where it fits:** [§4.1](chapter-4-directions/4-1-off-the-shelf-fms.md) ("Why try existing models before building your own"), cited neutrally for how mainstream textbooks introduce zero-shot and covariate-conditioned foundation forecasters.

### A3. bnlearn: Bayesian networks in R

> **Done 2026-11-24:** added to `.bib` as `scutari2010bnlearn` and cited in [§2.8](chapter-2-fm-foundations/2-8-ues-fm-evaluation-criteria.md) under Dimension 6 (uncertainty awareness) as a classical probabilistic graphical-model baseline noting super-exponential worst-case structure learning.

- **Ref:** Scutari, M. (2010). Learning Bayesian Networks with the bnlearn R Package. *Journal of Statistical Software*, 35(3), 1–22. <https://doi.org/10.18637/jss.v035.i03>. Verified via Crossref. Examples page: <https://www.bnlearn.com/examples/>.
- **Suggested key:** `scutari2010bnlearn`
- **Barton's note:** used in practice. Worked, but slow, probably because it's R (although much of it is written in C).

### A4. Bayes Server documentation (further reading only, not a citation)

- <https://www.bayesserver.com/docs/introduction/getting-started>. Link checked (200 OK).
- Vendor documentation for a commercial product. Fine as a "further reading" link beside A3, but it can't carry a claim under CONTRIBUTING's rules. If Bayesian-network basics need a citable source, use a textbook instead, e.g. Koller & Friedman, *Probabilistic Graphical Models* (MIT Press, 2009). Not yet verified.

### A5. ChatGPT summary: not citable

- <https://chatgpt.com/share/6aad3def-6554-83eb-9e07-fbc3206398dc>
- AI-generated and not a checkable source, so it can't go in the `.bib` or a footnote. Use it only to find primary sources, then verify and cite those instead.

---

## B. Tools and models named in the notes without any citation

Found by a sweep for named tools, models and datasets in body text that no footnote anywhere in the notes mentions. All DOIs below were verified via Crossref on 2026-09-23. **Done 2026-11-19** for EnergyPlus (`crawley2001energyplus`), OSeMOSYS (`howells2011osemosys`), SpineOpt (`ihlemann2022spineopt`), OpenModelica (`fritzson2020openmodelica`), PowerModels (`coffrin2018powermodels`), and Sentinel-2 (`drusch2012sentinel2`), added to `.bib` and cited in §3.2, §3.4 and §4.5 (DLinear, XGBoost and LightGBM were already cited in §4.7.1 and `.bib`). **Done 2026-11-24** for **PyCity** (`schiefelbein2019pycity`, confirmed via RWTH-EBC `pyCity` README citation list), added to `.bib` and cited in §3.4. This table is now complete.

| Named in | Where | Candidate reference | DOI / link |
| :--- | :--- | :--- | :--- |
| **EnergyPlus** (3 pages) | [§3.2](chapter-3-sim-opt/3-2-building-simulation-data.md) l.29, [§3.4](chapter-3-sim-opt/3-4-tools-and-standards.md#tool-landscape), [§4.3](chapter-4-directions/4-3-llm-agents-for-simulation.md) | Crawley, D. B. et al. (2001). EnergyPlus: creating a new-generation building energy simulation program. *Energy and Buildings*, 33(4) | `10.1016/S0378-7788(00)00114-6` |
| OSeMOSYS | [§3.4](chapter-3-sim-opt/3-4-tools-and-standards.md#tool-landscape) l.27 | Howells, M. et al. (2011). OSeMOSYS: The Open Source Energy Modeling System. *Energy Policy*, 39(10) | `10.1016/j.enpol.2011.06.033` |
| SpineOpt | §3.4 l.27 | Ihlemann, M. et al. (2022). SpineOpt: A flexible open-source energy system modelling framework. *Energy Strategy Reviews*, 43, 100902 | `10.1016/j.esr.2022.100902` |
| OpenModelica | §3.4 l.25 | Fritzson, P. et al. (2020). The OpenModelica integrated environment for modeling, simulation, and model-based development. *Modeling, Identification and Control*, 41(4) | `10.4173/mic.2020.4.1` |
| PowerModels | §3.4 l.29 | Coffrin, C. et al. (2018). PowerModels.jl: An open-source framework for exploring power flow formulations. *PSCC 2018* | `10.23919/PSCC.2018.8442948` |
| PyCity | §3.4 l.26 | Schiefelbein, J. et al. (2019). Automated urban energy system modeling and thermal building simulation based on OpenStreetMap data sets. *Building and Environment*, 149. **Confirm** this is the pyCity paper the text means before citing | `10.1016/j.buildenv.2018.12.025` |
| DLinear | [§4.7.1](chapter-4-directions/4-7-1-methods-tier1.md) l.70 | Zeng, A. et al. (2023). Are Transformers Effective for Time Series Forecasting? *AAAI 2023*. Also arXiv:2205.13504 | `10.1609/aaai.v37i9.26317` |
| XGBoost | §4.7.1 l.71 | Chen, T. and Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD '16* | `10.1145/2939672.2939785` |
| LightGBM | §4.7.1 l.71 | Ke, G. et al. (2017). LightGBM: A highly efficient gradient boosting decision tree. *NeurIPS 30*. No DOI; **proceedings URL to confirm** | — |
| Sentinel-2 | [§4.5](chapter-4-directions/4-5-screening-fields.md) l.44 | Drusch, M. et al. (2012). Sentinel-2: ESA's optical high-resolution mission for GMES operational services. *Remote Sensing of Environment*, 120 | `10.1016/j.rse.2011.11.026` |

Note: 10.1145 (ACM) and 10.1609 (AAAI) DOIs are already excluded in
`.github/lychee.toml` as bot-blocked, so these won't fail link-check CI.

## C. Uncited tools still needing a primary source identified

> **Done 2026-11-24:** verified and added canonical references for all four tools below to `.bib` and §3.2 / §3.4 (`robinson2009citysim`, `nouvel2015simstadt`, `chen2017citybes`, `ait2026disheatlib`).

- **CitySim** ([§3.2](chapter-3-sim-opt/3-2-building-simulation-data.md) l.29, [§3.4](chapter-3-sim-opt/3-4-tools-and-standards.md#tool-landscape)): Robinson et al. (2009), *CITYSIM: Comprehensive Micro-Simulation of Resource Flows for Sustainable Urban Planning*, Building Simulation 2009 (IBPSA), `10.26868/25222708.2009.1083-1090`.
- **SimStadt** (§3.4 l.30): Nouvel et al. (2015), *SimStadt, a new workflow-driven urban energy simulation platform for CityGML city models*, CISBAT 2015, `10.5075/epfl-cisbat2015-889-894`.
- **CityBES** (§3.4 l.30): Chen, Hong & Piette (2017), *Automatic generation and simulation of urban building energy models based on city datasets for city-scale building retrofit analysis*, *Applied Energy*, 205, 323–335, `10.1016/j.apenergy.2017.07.128`.
- **DisHeatLib** (§3.4 l.31): AIT Austrian Institute of Technology, `https://github.com/AIT-IES/DisHeatLib` (open-source Modelica library repository; no canonical paper found).

## D. Existing citation to double-check

- **Granite-GFM**, [§1.3](chapter-1-background/1-3-fm-landscape-by-domain.md) l.32. The sentence about Granite-GFM estimating land surface temperature (30 m, hourly, built on Prithvi-SWIN-L) is cited to `szwarcman2024prithvieo2`, the Prithvi-EO-2.0 paper. Check that this paper actually describes the Granite LST model. If not, find Granite-GFM's own source. Granite-GFM is also named uncited in the §1.3 table (l.27).
  - **Resolved (2026-10-01).** The paper does not describe it, since Prithvi-EO-2.0 is a ViT released after the Granite model. Both §1.3 mentions now cite the IBM Hugging Face model card (`bhamjee2024granitelst`). Prithvi-SWIN-L cites `jakubik2023prithvi`, the paper that model card gives for its base model. [§2.4.3](chapter-2-fm-foundations/2-4-3-clean-energy-forecasting-fms.md#weather-and-geospatial) l.24 had the same error ("Prithvi-EO-2.0 … underlies Granite-GFM") and is corrected the same way.

## E. Previously logged, still open

- ~~**[G9](chapter-6-outlook/6-1-open-gaps.md#g9)** is uncited on its own page ([log.md](log.md), 2026-09-19 entry).~~ **Done 2026-11-19:** G9 now cites `ledee2025messurrogate`, `sharif2021renovationvae` and `gasse2019learn2branch` as nearest-miss work on multi-energy design surrogates, renovation scenario generation and MILP variable–constraint graphs.
