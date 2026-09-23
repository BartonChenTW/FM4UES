# TODO

Private working list — excluded from the Jekyll site via `_config.yml`. Key changes are recorded in [log.md](log.md).

Items tagged **[Claude]** are suggestions from Claude (2026-09-11), not yet agreed. Untagged items are Barton's.

## Aim of the repo

- A living knowledge base that helps people in the urban energy systems (UES) domain learn about foundation models (FMs).
- Long-term goal: build an FM for UES.

## In progress

- [ ] 

## Next

- [ ] **Fill in the four stub sections in Chapter 4.** [§4.1](chapter-4-directions/4-1-off-the-shelf-fms.md) (off-the-shelf FMs), [§4.2](chapter-4-directions/4-2-fms-for-building-stocks.md) (FMs for building stocks), [§4.3](chapter-4-directions/4-3-llm-agents-for-simulation.md) (LLM agents for simulation), [§4.4](chapter-4-directions/4-4-generative-design.md) (generative design) are each marked `{: .note }` "Stub — needs expansion" — they state the direction and cross-reference the rest of the book but don't yet contain a worked example, benchmark numbers, or a literature survey specific to that sub-topic. **Progressed 2026-09-19:** each now has at least one verified citation tied to the direction — §4.1 a worked zero-shot district-heating evaluation with reported numbers, §4.2 the nearest empirical result (and a dated search confirming no stock-level FM exists yet), §4.3 one grounded LLM-agent example for the occupant-behaviour assumption category, §4.4 an adjacent-domain precedent validated on power-system test cases plus an in-domain example clarifying the input-vs-design distinction. None has this book's own benchmark run — see log.md for what's still open per section.
- [ ] **Add remaining diagrams.** Every Part landing page (1–5), the Tier progression page (§4.9), the roadmap (§5.1), and the token schema/temporal hierarchy (§5.5) now have Mermaid diagrams (enabled via `mermaid:` in `_config.yml`, 2026-09-11). Not yet illustrated: individual section pages within each Part (e.g. the four-requirements table in §2.3, the bipartite graph worked example in §5.4) — the phasing note below still applies to these.
- [ ] **The existing chapter-landing diagrams aren't very helpful (Barton, 2026-09-12).** All six started as flowcharts of the table of contents. See [diagram-ideas.md](diagram-ideas.md) for a page-by-page critique and concrete replacement ideas. **Chapter 4's landing is done (2026-09-13):** replaced the TOC flowchart with a screening 2×2 (public-data availability × basic-element clarity) placing the five sub-fields from §4.5/§4.8. Remaining TOC landings: Chapters 1, 2, 3, 5. (§4.9 tier progression and §5.1 roadmap are keep/touch-up, not replacements.)
- [ ] **Verify the just-the-docs Mermaid version pin (`11.4.1` in `_config.yml`) still resolves** once this is actually built via GitHub Pages/`bundle exec jekyll serve` — set from current documented just-the-docs convention but not yet build-verified in this repo. The Chapter 4 landing uses `quadrantChart`, which requires Mermaid ≥10.2.0, so the 11.4.1 pin is fine and a `flowchart` fallback is **not** needed. (The "Syntax error in text" seen on 2026-09-13 was unquoted semicolons in two quadrant labels, not the version — fixed by quoting, and the fixed block verified against a real Mermaid 11.4.1 parser. See log.md.)

## Restructure (done 2026-09-11)

- [x] **Merged `add/` notes into the textbook.** `add/FM_for_UES.md` and `add/reference.md` fully folded into the new section pages (see [log.md](log.md) for the detailed mapping) and deleted, along with `add/`.
- [x] **Added detailed references with footnotes** throughout the new section pages, using the citation keys in `references/fm-for-ues.bib` (extended from ~16 to ~22 entries during the merge).
- [x] **Restructured the textbook into six Parts**, one page per numbered section, per [outline.md](outline.md) as amended (6-part split: Chapter 4 neutral survey vs. Chapter 5 case study vs. Chapter 6 outlook, instead of the outline's original 5-part draft). See [log.md](log.md) for the full before/after mapping.
- [x] **Broadened Chapter 4** with off-the-shelf FMs, building-stock FMs, LLM/agent-built simulation models, and generative design (stubs, see Next above).
- [x] **Added ML-basics content to Chapter 2**: self-supervised pretraining, fine-tuning, scaling laws (§2.6), transformer/GNN/neural-operator architectures (§2.7), and a surrogates-vs-FMs section (§2.8).
- [x] **Added illustrations to the highest-value spots**: every Part landing page, the tier-progression page, the roadmap, and the token schema/temporal hierarchy. Per-section illustration (previously flagged as ~40 diagrams of work) intentionally deferred — see Next above.
- [x] **Moved Appendix C and the concept-paper notes to a private file** (`notes-concept-paper.md`, excluded from the site build) rather than keeping them as a public appendix.
- [x] **Added `redirect_from:` front matter** for all 13 old public URLs (`01-the-domain.html` through `11-references.html`, plus both old appendices) so existing links don't 404.

## Suggestions from Claude (2026-09-11) — to review

### Setup

- [x] **[Claude] Exclude `add/` from the site now.** Done 2026-09-11: added `add/` to `exclude:` in `_config.yml`.
- [ ] **[Claude] Decide the references workflow before writing footnotes.** `jekyll-scholar` (auto-build citations from a `.bib`) is not supported by the standard GitHub Pages build. Choose one:
  - (a) hand-written footnotes whose names match `.bib` citation keys — simple, but two copies to keep in sync;
  - (b) build the site with a GitHub Actions workflow so `jekyll-scholar` can run — more setup, single source of truth.
  - Either way: manage references in Zotero with the Better BibTeX plugin, which gives stable citation keys and auto-exports the `.bib`. Key convention `firstauthorYEARshortname` (e.g. `raissi2019physics`) already used in `references/fm-for-ues.bib` — confirm or change.
- [x] **[Claude] Add `jekyll-redirect-from` before renaming files.** Done 2026-09-11: added to `plugins:` in `_config.yml` (bundled via the `github-pages` gem already in the Gemfile, no Gemfile change needed). Not yet *used* — add `redirect_from:` front matter when pages are actually renamed in the restructure.
- [x] **[Claude] Add a LICENSE.** Done 2026-09-11: [`LICENSE`](LICENSE), CC BY 4.0 for the written content.
- [x] **[Claude] Add `CONTRIBUTING.md` and GitHub issue templates.** Done 2026-09-11: [`CONTRIBUTING.md`](CONTRIBUTING.md) plus three templates in `.github/ISSUE_TEMPLATE/` (error report, reference suggestion, section proposal).
- [x] **[Claude] Add a status / last-reviewed line to each page** (e.g. `status: draft | reviewed`, `last_reviewed: 2026-09-11` in front matter, displayed at the top), so readers can tell mature pages from rough ones. Done 2026-09-11: `_includes/page-status.html` renders the badge; added `status: draft` + `last_reviewed: 2026-09-10` (the v1.1 publish date, from git history) to front matter and the include call to all 14 chapter/appendix pages. Skipped `index.md` — it already shows a version/date label. Flip `status` to `reviewed` and bump `last_reviewed` per page as each is actually re-checked.
- [x] **[Claude] Add an automated link checker** (e.g. lychee or html-proofer in GitHub Actions). Reference-heavy pages collect broken links quickly. Done 2026-09-11: `.github/workflows/link-check.yml` (lychee, runs on push/PR to main + weekly cron), config in `.github/lychee.toml`. Chose lychee over html-proofer since it doesn't require building the Jekyll site first (no Ruby/remote-theme build step in CI). Internal `chapter-name.html` cross-links are excluded from the check (see comment in `lychee.toml`) since those are Jekyll-rendered paths that don't exist as literal files against the raw `.md` source — a real check of those would need to run against the *built* site instead.
  - **Found a real pre-existing broken link while setting this up:** `add/reference.md` linked to `inbox.md` (~20 times) and to `FM_for_UES.md` once, but `inbox.md` never existed in the repo. **Resolved 2026-09-11**: `add/reference.md` was deleted as part of the restructure (its content merged into `references/fm-for-ues.bib` and per-page footnotes), which removed the broken links along with it.

### Outline

All items below are now implemented as part of the 2026-09-11 restructure (see "Restructure (done 2026-09-11)" above and [log.md](log.md) for details).

- [x] **[Claude] Separate the neutral survey from the research proposal.** Implemented as the Chapter 4 (neutral survey) / Chapter 5 (case study) / Chapter 6 (outlook) split.
- [x] **[Claude] Broaden Chapter 4 (Directions).** Added as §4.1–4.4 (off-the-shelf FMs, building-stock FMs, LLM/agent-built simulation models, generative design) — currently stubs, see Next above.
- [x] **[Claude] Add ML basics to Chapter 2.** Added as §2.6 (self-supervision, fine-tuning, scaling laws) and §2.7 (transformers, GNNs, neural operators).
- [x] **[Claude] Add a "surrogate models vs FMs" section to Chapter 2.** Added as §2.8.
- [x] **[Claude] Frame Chapter 3 as "UES through an ML lens".** Reframed throughout — see e.g. §3.2 ("Framed for an ML reader"), §3.4, §3.5.
- [x] **[Claude] Add a dedicated data and benchmarks section to Chapter 3.** Added as §3.2 (BuildingsBench, EnergyBench, ResStock/ComStock, CESAR-P).
- [x] **[Claude] Resolve the overlap between basic elements and the representation problem.** §2.3 (Chapter 2) is the general criterion and concept; §5.2 (Chapter 5) is its application to the specific case-study representation — explicitly cross-referenced both ways.
- [x] **[Claude] Phase the illustrations.** Done for Part landing pages, the tier-progression page, the roadmap, and the token schema. Per-section illustration remains open — see Next above.

## Later / ideas

- [ ] 

## Done

- [x] Publish v1.1 textbook as Jekyll site (just-the-docs)
- [x] Create `TODO.md`, `outline.md` and `log.md` as private planning files
