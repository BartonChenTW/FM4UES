# Change Log

Key changes to the knowledge base, oldest first (new entries go at the bottom). Private file — excluded from the Jekyll site via `_config.yml`.

Record structural changes, content merges, renamed or moved pages, and decisions. Small typo fixes don't need an entry.

---

## Before 2026-09-11

- `2a3938b` Published the v1.1 textbook as a Jekyll site (just-the-docs theme): Parts I–VII plus Appendices A–C.

## 2026-09-11

- Added private planning files, excluded from the site: `TODO.md` (task list), `outline.md` (proposed new textbook structure, for review), `log.md` (this file).
- `_config.yml`: added an `exclude:` list (`TODO.md`, `outline.md`, `log.md`, `Gemfile`, `Gemfile.lock`, `vendor/`).
- Added `add/FM_for_UES.md` and `add/reference.md`: working notes and references from an earlier conversation, to be merged into the textbook.
- Recorded the repo aim in `TODO.md`: a living knowledge base for UES people to learn about FMs; long-term goal to build an FM for UES.
- Added `LICENSE` (CC BY 4.0 for the written content).
- `_config.yml`: enabled `jekyll-redirect-from` (ready for use once the outline restructure renames pages); excluded `add/` from the build so the working notes and personal-communication references aren't reachable on the published site before merging.
- Added `CONTRIBUTING.md` and `.github/ISSUE_TEMPLATE/` (error report, reference suggestion, section proposal) to support outside contributions.
- Added `references/fm-for-ues.bib`: starter BibTeX bibliography (~16 entries) for Zotero import, seeded from confirmed-metadata entries in `add/reference.md` §1–4 and `11-references.md`. Citation keys follow `firstauthorYEARshortname`, matching the planned footnote-citation convention. Added `references/README.md` explaining import and how to contribute entries; excluded the `.bib` itself from the site build but kept the README as a page.
- Claude's setup suggestions from the prior session (LICENSE, redirects, CONTRIBUTING, `add/` exclusion, references folder) are now implemented; marked done in `TODO.md`. Still open: references workflow decision (hand-written footnotes vs. `jekyll-scholar` via GitHub Actions), and the outline restructure itself (blocked on Barton's review of `outline.md`).
- Added `_includes/page-status.html`: renders a "Status / Last reviewed" badge from page front matter. Added `status: draft` + `last_reviewed: 2026-09-10` (the v1.1 publish date) and the include call to all 14 chapter/appendix pages (skipped `index.md`, which already has a version/date label).
- Added `.github/workflows/link-check.yml` (lychee, on push/PR to main + weekly) and `.github/lychee.toml`. Internal `chapter-name.html` cross-links are excluded (Jekyll-rendered paths, not real files against raw `.md` source).
- **Found while setting up the link checker:** `add/reference.md` links to `inbox.md` (~20 times) and once to `FM_for_UES.md`, but `inbox.md` doesn't exist in the repo. Logged in `TODO.md`; not fixed yet since it's tied to the still-open `add/` merge decision.

## 2026-09-11 (restructure)

**Full restructure into six Parts, one page per section**, implementing `outline.md` with the amendments agreed in `TODO.md`: split the outline's draft Part 4 into Part 4 (neutral survey of directions) / Part 5 (case study: multi-carrier energy hub FM) / Part 6 (outlook), broadened Part 4 with four new stub directions, and added ML-basics content to Part 2.

**New file layout** (just-the-docs nesting via `parent:` / `has_children:` / `grand_parent:`):

- `part-1-background/` (index + 6 sections, 1.1–1.6) — was `01-the-domain.md` plus new intro material.
- `part-2-fm-foundations/` (index + 12 sections, 2.1–2.8 with 2.4 having 5 sub-children 2.4.1–2.4.5) — was `02-fm-fundamentals.md`, `03-basic-elements.md`, `04-fm-landscape.md`, plus new ML-basics sections 2.6–2.8.
- `part-3-sim-opt/` (index + 8 sections, 3.1–3.8) — was `01-the-domain.md` §2–4, plus new material (3.2 building-simulation data, 3.3 energy-hub formalism, 3.4/3.5 dispatch and design framing, 3.7 schemas) drawn from `add/reference.md` §4–7.
- `part-4-directions/` (index + 13 sections, 4.1–4.10 with 4.9 having 3 sub-children 4.9.1–4.9.3) — was `05-screening.md`, `06/07/08-methods-tierN.md`, `09-building-it.md`, plus four new stub sections (4.1–4.4) and `add/FM_for_UES.md` §3–4 (screening/candidate sub-fields).
- `part-5-case-study/` (index + 8 sections, 5.1–5.8) — entirely new pages built from `add/FM_for_UES.md` §5, §6, §8.2–8.4, §9, §10 (roadmap, representation problem, concrete representation, token schema, physics loss, module decomposition, risks).
- `part-6-outlook/` (index + 2 sections, 6.1–6.2) — was `10-open-gaps.md`, plus a new "how to contribute" page.
- `appendices/` (index + A, B) — was `appendix-a-glossary.md`, `appendix-b-checklist.md`, internal links renumbered throughout.

**Deleted** (fully migrated, verified via a link/content audit before removal): `01-the-domain.md` through `10-open-gaps.md`, `11-references.md` (folded into per-page footnotes + `references/fm-for-ues.bib`; see decision below), `appendix-a-glossary.md`, `appendix-b-checklist.md`, `appendix-c-buildfm-bs2027.md` (moved to private notes, see below), and the entire `add/` directory (`add/FM_for_UES.md`, `add/reference.md`).

**Private notes file added**: `notes-concept-paper.md` (excluded from the site build via `_config.yml`), merging the former public `appendix-c-buildfm-bs2027.md` (the BS2027 applied example) with `add/FM_for_UES.md` §7 (concept-paper structure notes) — per the decision that project-specific submission strategy (venue choice, author-list-as-argument, double-blind handling) isn't public-textbook material, even though the reasoning is a useful internal reference.

**Dropped entirely**: `add/reference.md` §8 "Project resources & personal communication" (NEST facility entry and personal-communication citation) and §9 "Notes on using this list in a manuscript" (meta-content about citation practice, judged not worth carrying into the public book — the substance, e.g. arXiv-vs-venue-of-record citation practice, is already reflected in how footnotes were written).

**11-references.md decision**: folded entirely into per-page footnotes plus `references/fm-for-ues.bib`, then deleted, rather than kept as a slimmed "further reading" page. Rationale: with every claim now footnoted at point of use, a separate reference-pointers page would only duplicate the `.bib` (already the machine-readable source of truth) without adding reader value. Added `redirect_from: /11-references.html` on `references/README.md` as the closest surviving destination.

**References**: extended `references/fm-for-ues.bib` from ~16 to ~22 entries, adding confirmed-metadata entries from `add/reference.md` §5–6 (Geidl & Andersson energy-hub papers ×3, MATPOWER, PyPSA, PGLib-OPF, CESAR-P). Entries marked `[to confirm]` in the original source notes (e.g. TimeGPT, Granite TSPulse/FlowState, several `[to confirm]` author/institution fields) were not added, per the no-fabrication rule. Converted all inline claims across every new page to Markdown footnotes keyed to match `.bib` entries, per `CONTRIBUTING.md`'s convention; verified programmatically that every footnote key used in the text has a corresponding `[^key]:` definition, and that `.bib`/footnote key names agree (one mismatch found and fixed: `cesarp2022` → `orehounig2022cesarp`).

**Redirects**: added `redirect_from:` front matter for all 13 old public URLs (`01-the-domain.html` through `10-open-gaps.html`, `11-references.html`, `appendix-a-glossary.html`, `appendix-b-checklist.html`) pointing to wherever the bulk of that page's content landed. `appendix-c-buildfm-bs2027.html` has no redirect, since its content is now private (a redirect would point to a 404 on the built site).

**Diagrams**: enabled Mermaid via `mermaid: { version: "11.4.1" }` in `_config.yml`. Added diagrams to every Part landing page (1–6 minus 6, appendices — landing pages without a natural "flow" to show were left as lists), the Tier 1→2→3 progression page (§4.9), the roadmap Phase 0→5 flow (§5.1), and the token-schema temporal hierarchy (§5.5) — the two sections flagged in an earlier review as most needing a picture. Per-section illustration for the remaining ~45 pages is logged as open in `TODO.md`.

**`_config.yml`**: removed `add/` from `exclude:` (directory deleted); added `notes-concept-paper.md` to `exclude:`; added the `mermaid:` block.

**`index.md`** and **`README.md`**: rewritten tables of contents/structure tables to match the six-Part layout; version label bumped to "2.0" to mark the structural break from v1.1.

**`CONTRIBUTING.md`**: updated the glossary link and the front-matter guidance paragraph to describe the new `parent:`/`has_children:`/`status`/`last_reviewed` pattern.

**`.github/lychee.toml`**: broadened the internal-link exclusion regex from a bare-filename pattern (`^[a-zA-Z0-9_-]+\.html(#.*)?$`) to also match relative paths with slashes (`^(?:\.\./)*[a-zA-Z0-9_/-]+\.html(#[^\s)]*)?$`), since cross-Part links now routinely look like `../part-4-directions/4-9-1-methods-tier1.html`.

**Verification performed before considering the restructure complete**: (1) a script-based check that every internal `.html` link in every new page resolves to an actual `.md` file at the linked relative path — zero broken links; (2) a check that every `parent:` front-matter value matches an existing page's `title:` exactly — zero mismatches; (3) a check for duplicate page titles and duplicate `nav_order` values within the same parent group — zero collisions; (4) a check that every footnote key used in text has a matching `[^key]:` definition — zero missing; (5) manual cross-check of the outline's source-mapping table against the new file layout to confirm every old section landed somewhere.

## 2026-09-11 (rename: Part → Chapter)

Renamed the top-level structure from "Part" to "Chapter" at Barton's request: directories `part-1-background/` … `part-6-outlook/` → `chapter-1-background/` … `chapter-6-outlook/`; every `title:`/`parent:`/`grand_parent:` front-matter value and every in-text "Part N" reference (breadcrumbs, cross-links, prose) updated to "Chapter N" across all 55 site pages, `index.md`, `README.md`, `CONTRIBUTING.md`, and `TODO.md`. `_config.yml` and `.github/lychee.toml` comments updated to match.

`notes-concept-paper.md`'s own internal "Part 1"/"Part 2" section labels were deliberately left alone — those are that private document's own structure, unrelated to the book's chapters. `log.md` and `outline.md` entries from before today were left as a historical record rather than rewritten.

Verified before committing: no remaining `part-N-`/`Part N` references outside the two intentionally-untouched files; every `parent:`/`grand_parent:` value matches its target index page's `title:` exactly; no broken internal `.html` links (re-ran the same link-resolution check used after the original restructure).

## 2026-09-11 (attribution + leftover "Part" wording)

Added author/founder attribution at Barton's request, framed as an open, community-editable textbook rather than sole-authored: a credit line on `index.md` ("Started by Barton Chen — open for anyone to contribute", linking to the how-to-contribute page), a paragraph on `README.md`, and an opening-line credit on `CONTRIBUTING.md`. `LICENSE` already said "Barton Chen and contributors" — no change needed there.

While in these files, fixed leftover "Part" wording the previous rename pass missed (its regex only matched `Part <number>`, not bare/plural/lowercase uses): the `## In this part` heading on all six chapter `index.md` files, "this part surveys"/"this part is a case study" in the Chapter 4/5 landing pages, "the operational core of this part" in §4.9's landing page, the Contents table header on `index.md`, and "nested by Part"/"the Part's title" in `README.md`/`CONTRIBUTING.md`. Re-ran the case-insensitive sweep afterward — clean (remaining "part"/"parts" hits are all ordinary English, e.g. "part-load", "network of parts").

**AI-assistance disclosure added**, same three files: `index.md` (a small-print line under the founder credit), `README.md` (a short paragraph), `CONTRIBUTING.md` (a note after the founder-credit paragraph, plus a line that the sourcing standard applies equally to human- and AI-drafted contributions). Names both models actually used in this session, Claude Opus 5 and Claude Sonnet 5 (Anthropic) — the session switched from Opus to Sonnet partway via `/model sonnet`.

## 2026-09-11 (branch protection docs + site link)

Barton turned on branch protection for `main` (require PR before merging, require the `lychee` link-check status check, block force-push/deletion, no bypass even for the owner) via the GitHub UI — I don't have `gh` CLI access in this environment, so this was applied by Barton directly, not by me.

Updated docs to match the new workflow:
- `CONTRIBUTING.md`: new "How changes get in" section explaining the fork → branch → PR flow and that the link-check must pass; added a "Read the book" link at the top.
- `README.md`: added a prominent site link at the top and in the founder-attribution paragraph ("Contributions go through a pull request"); replaced the old placeholder ("once GitHub Pages is enabled... `https://<your-username>.github.io/...`") with the real live URL now that Pages is confirmed working; removed a redundant second copy of the site link; fixed the "Building locally" closing line, which still described Pages as not-yet-enabled.

Site URL used throughout: `https://bartonchentw.github.io/FM-for-Urban-Energy-Systems/` — superseded later the same day when the repo was renamed to `FM4UES`; the current URL is `https://bartonchentw.github.io/FM4UES/`.

## 2026-09-12 (diagram critique + a quick correctness fix)

Barton flagged that the six chapter-landing Mermaid diagrams (added 2026-09-11) aren't very helpful. Added `diagram-ideas.md` (private, excluded from the build): a page-by-page critique — every one of the six is a flowchart of the table of contents (section-number boxes, "comes after" arrows), which duplicates the sidebar nav and the "In this chapter" table rather than showing anything the reader couldn't already see. Proposes concrete replacements per chapter (e.g. Chapter 4's landing diagram → the actual screening funnel/2×2 instead of a TOC; Chapter 5's → promote the bipartite-graph worked example already in §5.4). Flags §5.5's temporal-hierarchy diagram and §5.1's roadmap as the two that already work, as a model for what "good" looks like here.

While reviewing, found and fixed a real bug independent of the redesign question: `chapter-4-directions/index.md`'s diagram used wrong section numbers (`4.9 Screening`, `4.10 Candidate sub-fields`, `4.11 Methods`, `4.12 Building it`) — the actual numbering (confirmed against the page's own "In this chapter" table, right below the diagram) is §4.5–4.7 (screening), §4.8 (candidate sub-fields), §4.9/4.9.1–3 (methods/tiers), §4.10 (building it). Corrected.

Added a TODO item pointing at `diagram-ideas.md`, and excluded that file from the site build.

## 2026-09-13 (light/dark mode toggle)

Barton asked to enable light/dark mode. just-the-docs already ships both color schemes (`assets/css/just-the-docs-light.css`/`-dark.css`, `color_scheme: light|dark` in `_config.yml`) and a `jtd.setTheme(name)` runtime function, but no user-facing toggle button, no click handler, and no persistence across page loads.

Researched the theme's actual mechanism directly rather than assuming (this session had already gotten one Sass convention wrong earlier by assuming instead of checking): fetched the theme's own `assets/js/just-the-docs.js` source and confirmed `jtd.setTheme`/`jtd.getTheme` work by reading/rewriting the `href` of the page's first `[rel="stylesheet"]` link — there's no `data-theme` attribute or CSS custom-property switch involved. Also confirmed, by fetching `_includes/components/sidebar.html` and `components/footer.html` directly, that `nav_footer_custom.html` (the documented include point for this kind of control) renders **twice** on every page — once in the desktop sidebar, once in a `d-md-none` mobile-only footer copy present in the DOM even on desktop. Using `id="..."` there would have caused duplicate-ID bugs; built the toggle with classes and DOM-scoped `querySelector` instead, and guarded the click-listener registration with a `window` flag so the listener (whose script tag also renders twice) doesn't attach twice and double-toggle on click.

Added:
- `_includes/nav_footer_custom.html`: the toggle button (sun/moon SVG icons, inline, no external asset) plus its script — reads/writes `localStorage.theme`, calls `jtd.setTheme`, syncs both DOM copies of the button.
- `_includes/head_custom.html`: a new script block (added before the existing external-links-in-new-tab script already there) that re-applies a saved `localStorage.theme` preference by rewriting the stylesheet `href`, as early as this include runs, so a returning visitor's preference applies before paint rather than flashing the site's default light scheme first. Not perfectly flicker-free without forking the theme's own `head.html` (this include runs after the theme's stylesheet `<link>` tags, confirmed by fetching `head.html`) -- judged not worth it for this.

`_config.yml`'s `color_scheme: light` is unchanged and correct to leave as-is: it sets the build-time default for a first-time visitor; dark is a client-side, opt-in preference on top of that.

**Not verified in this environment** -- no Ruby/Jekyll/browser here, so this could not be built and clicked. What was verified: Liquid/JS bracket balance in both new files, and that the full existing site (footnotes, bib, lychee link check) still passes untouched. The real test is the next Pages build plus Barton clicking the button.

## 2026-09-13 (new §2.9: UES-FM evaluation criteria)

Barton shared a draft (originally from ChatGPT) proposing seven evaluation dimensions for judging UES-specific foundation-model claims — generality, transferability, task generality, physical consistency, data efficiency, uncertainty awareness, computational benefit — plus a benchmark table and a proposed alternative FM definition, and asked whether/where it fits.

Assessment: the seven-dimension framework fills a real gap (§2.1 defines what an FM *is* generically; nothing previously said how to judge whether a *UES* FM proposal is good specifically), but the draft as supplied couldn't go in directly:
- Two of its five references ([2], [4]) were cited with no author list, which this book's own sourcing standard treats as unverified.
- It restated the §2.1 definition and proposed a second, competing "working definition" — redundant with, and in tension with, the one already in the book.
- It assumed a direct line to "the case study in Chapter 5" that didn't exist yet.

Verified all five references before using any of them (Crossref API for the four DOI-based ones, arXiv/search for the specific claims attributed to each):
- Reference [2] ("Foundation models for the electric power grid", Joule 8(12):3245-3258) is exactly the paper already in this book's bib as `hamann2024foundation` -- reused that key rather than adding a duplicate.
- [1] Bommasani et al. 2021 -- already cited in this book (§1.3, §2.1).
- [3] Karniadakis et al. 2021, "Physics-informed machine learning", *Nature Reviews Physics* 3(6):422-440 -- real, confirmed via Crossref.
- [4] Ma, Jiang, Hu & Chen (2025), "A review of physics-informed machine learning for building energy modeling", *Applied Energy* 381:125169 -- real, confirmed via Crossref; also independently verified the specific "physics-informed inputs/loss functions/architectural design/ensemble models" fourfold taxonomy is genuinely this paper's own categorisation (not [3]'s), via a direct search of its abstract, and attributed it correctly to [4] alone rather than to both papers jointly as the draft implied.
- [5] Xu, Hu, Atamturktur, Chen & Wang (2025), "Systematic review on uncertainty quantification in machine learning-based building energy modeling", *Renewable and Sustainable Energy Reviews* 218:115817 -- real, confirmed via Crossref; the "aleatoric and epistemic uncertainty" claim and the "three primary sources: building operations, simulation tools, ML model" detail both independently confirmed via search of the paper's actual findings.

Added, on branch `docs/ues-fm-evaluation-criteria`:
- `chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.md`: the seven dimensions, trimmed from the original draft -- no restated FM definition (already in §2.1), no duplicate surrogate/FM contrast (already in §2.8, cross-referenced instead), framed as sharpening the existing definition rather than replacing it. Cross-links out to where this book already touches each dimension (§5.6 physics loss, §3.2 data scarcity, §2.8/§3.4/§3.5 amortisation, Chapter 6 G4 benchmarks gap).
- `chapter-5-case-study/5-8-risks.md` §5.8.3: a new sub-section applying the seven dimensions honestly to this book's own case study -- a table stating plainly which dimensions are demonstrated (none), designed-for-but-undemonstrated (generality, task generality), concretely addressed as a design target (physical consistency, computational benefit), or genuinely unaddressed (data efficiency, uncertainty awareness). This is the "bridge to Chapter 5" the original draft claimed but didn't yet have, since Chapter 5 didn't reference the framework before this change.
- 3 new `.bib` entries (`karniadakis2021piml`, `ma2025piml_bem`, `xu2025uq_bem`); reused `hamann2024foundation` and `bommasani2021opportunities` rather than duplicating.
- Updated `chapter-2-fm-foundations/index.md` (TOC table + diagram) and `2-8-surrogates-vs-fms.md`'s footer nav link for the new §2.9.

Dropped from the original draft: the restated Bommasani definition, the proposed second "working definition" blockquote, and the generic benchmark table (replaced with one specific to this book's actual case study rather than a hypothetical generic one).

Verified locally: footnote ref/def integrity clean site-wide, 77 bib entries (74 -> 77), no duplicate keys, brace-balanced. 0 link-check errors, 127 OK.

## 2026-09-13 (switched log.md to append-at-bottom, oldest-first)

Barton asked why merge conflicts kept recurring across the several parallel branches in flight. Root cause: `log.md` was newest-first, so every branch inserted its new entry at the same "top of file" location. Two branches doing that from the same starting version is a guaranteed textual conflict — Git cannot tell which entry should come first — even though the entries never actually overlap in content. It was not caused by starting a new task before the previous branch merged; it was this file's ordering colliding with working on several branches at once.

Reordered to oldest-first, with new entries appended at the bottom. Two branches appending at the end of a file merge cleanly far more often, since Git only conflicts where both sides touch the same lines, and an append touches only the tail. Updated the file's own intro line to state the convention, so future entries (mine or a contributor's) go to the right place.

Pure reordering — no entry content removed or altered, verified by diffing old and new content sorted, and by word count.

Note on this branch's own history: the first attempt at this reordering was cut from a `main` that predated the §2.9 entry, so once §2.9 merged the branch conflicted across the whole file (one side had rewritten every line's position, the other had inserted a new section at the top). Rather than resolve that hunk-by-hunk, the branch was reset onto current `main` and the reordering redone against the nine-section content — same end state, no conflict.


## 2026-09-13 (Chapter 4 landing: screening 2×2)

Replaced the Chapter 4 landing-page Mermaid diagram. It was a table-of-contents flowchart (section boxes and "comes after" arrows), which duplicates the sidebar nav and the "In this chapter" table on the same page. `diagram-ideas.md` already named this page as the first replacement: the chapter's actual argument is a *screening decision*, which is a 2×2, not a reading-order flowchart.

The new diagram is a Mermaid `quadrantChart` with axes "public-data availability" × "basic-element clarity", placing the five sub-fields already assessed in §4.5 / §4.8:

- Load FM and Grid FM in the mature quadrant (clean basic element + public or physically-simulated data).
- UBEM in the "element exists; generate the data" quadrant (simulator-grounded, privately generable).
- Weather / microclimate in the "data exists; fusion missing" quadrant (HLS / Sentinel / ERA5 abundant, not yet fused with load or grid).
- Multi-carrier hub in the immature quadrant (no clean basic element, essentially no public data) — the reason it is the Chapter 5 case study.

No new claims; a short caption under the chart points at §4.5–4.8 and at the T1–T9 task screen in §4.6/§4.7. `last_reviewed` on the landing page bumped to 2026-09-13.

Uses `quadrantChart`, which needs Mermaid 11 (already pinned as `11.4.1` in `_config.yml`). If GitHub Pages fails to render it, fall back to a labelled 2×2 flowchart — noted in TODO.md.

## 2026-09-13 (fix: Chapter 4 quadrantChart syntax error)

Barton reported a large "Syntax error in text — mermaid version 11.4.1" box on the Chapter 4 landing page, in place of the screening 2×2 added by PR #19.

I had reviewed that PR and said the diagram would render, on the strength of having confirmed `quadrantChart` shipped in Mermaid v10.2.0 (so the repo's 11.4.1 pin covers it). That was the wrong check: the version was never the problem, and I asserted it would render without ever running the block through a parser.

**Root cause: two unquoted semicolons.** In the quadrant grammar (`quadrant.jison`), `";"` returns a `SEMI` token and `eol` is defined as `NEWLINE | SEMI | EOF` — a semicolon terminates a statement. So `quadrant-2 Element exists; generate the data` parsed as `quadrant-2 Element exists`, then failed trying to read `generate the data` as a fresh statement. Same for `quadrant-4 Data exists; fusion missing`.

Verified empirically rather than by inference this time — installed Mermaid 11.4.1 locally and parsed the exact block plus isolated single-character variants:

| Case | Result |
| :--- | :--- |
| Exact block from `main` | FAIL — `Parse error on line 6: ...s; generate the data` |
| Semicolon in a quadrant label, isolated | FAIL — same error |
| Colon in `title`, isolated | PASS (lexer rule `<title>(?!\n\|;\|#)*[^\n]*` does not exclude `:`) |
| Slash in a point name, isolated | PASS (`/` is in the grammar's `PUNCTUATION` class) |
| Fix A — semicolons replaced with dashes | PASS |
| Fix B — quadrant labels wrapped in double quotes | PASS |

So the title colon and the `Weather / microclimate` slash were both innocent; only the semicolons broke it.

Applied **Fix B** (quoting) rather than Fix A (rewording), to preserve the PR author's exact wording. Re-extracted the block from the file on disk after the edit and re-parsed it: PASS.

Also scanned every other Mermaid block in the book for the same bug class — no other block contains a semicolon, and `quadrantChart` is the only non-`flowchart` diagram in use, so this is contained to this one page.

Updated the `TODO.md` note that had said to fall back to a `flowchart` if Pages failed to render the quadrant chart; that advice was based on the wrong diagnosis and is now corrected.

## 2026-09-13 (four energy-domain FM references)

Applied Barton's 14-point editing guideline: add four references, each **tied to a specific claim in the main text** rather than parked in the bibliography. Placement was chosen by topic (Barton's call) rather than by the chapter numbers the guideline listed, so each citation sits where the book already makes the relevant argument.

| Reference | Placed in | Claim it supports |
| :--- | :--- | :--- |
| Arjunan et al. 2026, *EnergyFM* (e-Energy '26) | §2.4.2, new subsection | Domain-specific energy FMs already exist on the demand side; their basic element is a single-carrier meter series, which is exactly what the multi-carrier layer lacks |
| Park et al. 2025, *Energy and Buildings* 348:116446 | §2.9, dimensions 2 and 6 | Zero-shot transfer can fall short off-distribution while fine-tuning recovers much of it — so transferability is measured, not assumed; also that probabilistic forecasting is achievable with FMs |
| Bose et al. 2024, arXiv:2411.14421 | §2.6, scaling laws | Dataset heterogeneity and architecture outweighed parameter count — reframes the planning question as sampling design, not model budget |
| Lin et al. 2024, arXiv:2411.08888 | §6.1, G4 — Benchmarks | Building-scale TSFM benchmarks exist but score only single-modality metered data, so a UES benchmark cannot be assembled by pointing generic FM benchmarks at energy data |

**Fixed a fabricated author field.** The pre-existing `energyfm2026` entry credited the institutions (`{Empa and IBM Research and IISc Bangalore}`) as the author — a placeholder, not real metadata. Crossref gives the actual authors: Arjunan, Srivastava, Kumar, Jati, Ekambaram, Dayama, pages 556–568. Entry corrected and rekeyed to `arjunan2026energyfm` to match the `firstauthorYEARshortname` convention; the old key was uncited anywhere, so nothing dangled. It is now cited for the first time.

**Date discrepancy recorded rather than smoothed over.** Barton's guideline dates Park et al. to 2026; Crossref returns 2025 (online-first, in a 2026-dated issue). The `.bib` entry uses 2025 with a `note` field stating both, so the next person doesn't silently "correct" it in either direction.

Added the guideline's item 13 to `CONTRIBUTING.md`'s references workflow as a standing rule: a reference must be attached to a statement making explicit (1) what the work demonstrated, (2) what limitation remains, (3) how that limitation bears on urban energy systems. The second and third are the ones usually skipped, and are what make a citation load-bearing rather than decorative.

All four references verified against Crossref/arXiv before use. Checked after editing: footnote ref/def integrity on all four edited pages, bib key uniqueness, brace balance (596/596), and DOI/arXiv identifiers matching between `.bib` and footnotes.
## 2026-09-13 (optimisation-learning citations, from a rejected contribution)

Gemini proposed a new §3.6 "Integrating FMs into Dispatch Optimisation". **Not merged**, for three reasons:

1. **Slot collision.** It claimed `nav_order: 6` in Chapter 3, already held by §3.6 The Tool Landscape, which §3.5 and §3.7 both link by filename in their footer nav.
2. **Duplication.** Its three paradigms (end-to-end surrogate / warm-start / differentiable layers) are §4.9.3's existing three families, but without the recommendation, the Big-M MILP pattern, or the retrofit deployment-risk corollary. It also asserted dispatch is a *real-time* bottleneck, which contradicts §3.8 — single runs are affordable, loops are not.
3. **Two bad citations out of six.** Verified every reference: Raissi, Kotary, Amos & Kolter, and Donti et al. all check out exactly. The other two did not.

| Cited as | Reality |
| :--- | :--- |
| Baker (2019), "Learning to Optimize: Accelerating OPF via Data-driven Initialization", *PESGM 2019* | Title and venue invented. Real paper: Baker, "Learning Warm-Start Points for AC Optimal Power Flow", **IEEE MLSP 2019**, `10.1109/mlsp.2019.8918690` — right author, right year, right topic |
| Chatzos et al. (2020), arXiv:2006.11893 | **That ID is "The societal impact of ion beam therapy"** — an unrelated physics paper. Dropped entirely; the real Chatzos work exists but its identifier was not established |

Neither reference list entry carried a DOI, which is where both defects hid. Worth noting the Baker failure mode: plausible title, correct author, true underlying claim — it passes a skim.

**What was harvested.** §4.9.3 recommended warm-starting as the default with *no citation for warm-starting*, and Family 2's "no feasibility guarantees" claim was likewise uncited. Added, each tied to a claim per the CONTRIBUTING rule:

- `kotary2021survey` → Family 2, for the general fast-but-unconstrained trade across combinatorial domains.
- `baker2019warmstart` → Family 3, for the established continuous-AC-OPF warm-start result — **plus what it does not settle**: it warm-starts a continuous problem, while hub design binds on discrete technology/commitment decisions, where a bad predicted binary can send branch-and-bound down a worse tree. Flagged as a tractable open experiment, linked to D4 in §5.7.
- `amos2017optnet` + `donti2017taskbased` → a new "fourth option" paragraph on differentiable optimisation layers, with two caveats the source draft omitted: the formulations are **convex** (so G9's integer decisions remain open) and each forward pass contains a solve (partly giving back the amortisation speedup that motivates surrogates at all).

Contributor guidance this suggests: footnotes not `(Author, Year)` parentheticals, a resolvable DOI/arXiv ID on every reference, and check `nav_order` against the chapter before claiming a slot.

## 2026-09-13 (UES scope reviews in §1.1)

Barton supplied five review papers to ground §1.1's definition of what an urban energy system contains. **All five verified exactly against Crossref** — titles, authors, journals, volumes and pages all matched as supplied, a clean sweep (worth noting against the previous contribution, where two of six citations were defective).

§1.1 previously ran to about twenty lines: a scales table, the multi-carrier definition, and the energy-hub abstraction. It said nothing about distributed resources, autonomy, climate exposure, or the control layer — and a repo-wide search confirmed *none* of "decentralis", "microgrid", "resilien", "smart city" or "sector coupling" appeared anywhere in the book. So this was a genuine gap in the opening definition, not duplication.

Added a new subsection, **"What the boundary contains beyond the hub"**, with four claims rather than a transcription of the source paragraphs:

| Reference | Claim it carries |
| :--- | :--- |
| `sola2020multidomain` | Demand, generation and networks are modelled jointly because isolating them loses the interactions that make the system urban |
| `bishop2024multidomaindata` | The data spans building stock, transport and geography; assembling it is a recognised obstacle, not a preliminary |
| `weinand2020decentralized` | DERs and microgrids give districts varying degrees of energy autonomy — the supply side is no longer just a transmission connection |
| `nik2021climateresilient` | The local climate is a resilience question under extreme events, not merely a weather input |
| `martins2021smartcitytools` | Multi-carrier balancing depends on metering, DSM and automated control |

Per the CONTRIBUTING rule, the subsection closes by stating what each widening **costs**, rather than leaving the references as scope decoration: multi-domain scope means a corpus spanning sources never collected together (§3.2, §3.7); decentralisation means configuration varies between instances, so transfer must cross system designs and not only time (§2.9 dim. 2); climate exposure puts the boundary conditions themselves under uncertainty (§2.9 dim. 6). The closing line ties the breadth back to why the grid bus works as a basic element and a UES equivalent does not (§2.3).

Two date discrepancies recorded rather than silently picked, same as the earlier Park case:

- **Nik et al.** — published online 2020, print issue 2021 (vol. 8, no. 3). Cited as 2021, `note` field records both.
- **Bishop et al.** — supplied as 2023; Crossref gives published-print 2024. Cited as 2024, `note` field records both.

Deliberately did *not* import the "smart city" framing as a section theme — the book otherwise avoids that vocabulary — but kept the Martins reference for the control/DSM layer it actually supports.

`lychee.toml`: excluded the OUP DOI prefix (`10.1093`). `academic.oup.com` returns 403 to automated checkers, the same bot-blocking already handled for Wiley, Science, MDPI, OSTI and ACM; the Nik et al. DOI was verified against Crossref before excluding.

## 2026-09-13 (§2.2 D3/D5 citations, from a mostly-rejected rewrite)

Mistral proposed a full rewrite of §2.2 plus a contribution guideline. **The rewrite was largely rejected; two of its findings were acted on, and its guideline was adopted.**

**The premise was false.** It reported that §2.2 was "truncated (marked with [...])" and "fragmented". A repo-wide search finds no `[...]` anywhere in the book, and §2.2 is 84 lines / ~900 words with 12 working footnotes. The truncation was in its own web scrape of the rendered page, not in the source.

What the rewrite would have cost, had it been merged wholesale:

- **D1** — replaced the four abstract candidates (one timestep / one (configuration, boundary conditions, trajectory) triple / one whole model instance / one modelling decision) with four scale tiers (building / hub / grid segment / district). Shallower, and the scale tiers duplicate the table already in §1.1. The existing four are about *what kind of object* an example is, which is precisely the question §2.3 then adjudicates with a criterion.
- **D2** — dropped four **cited** bullets (GridFM float tokenisation, UniStruct medical codes, Earth-coupling aliasing, Moirai multi-resolution) in favour of an uncited "four dimensions" table. Net loss of four citations.
- **D3/D4** — added plausible but entirely uncited tables, partly duplicating §2.7, which already covers transformers, GNNs and neural operators with primary sources.
- Also: American spelling throughout against the repo's British convention, and the submission itself ended mid-sentence at "Self-supervised".

**Two findings were real, and are what this commit acts on:**

1. **D5 was one sentence** — correctly identified as the thinnest subsection. It is now four sentences with two primary sources. Deliberately *not* a restatement of §4.10.3's six-metric protocol or §2.9 dimension 4: D5's job is the principle (low average error and physical validity are different properties), with the protocol and the criterion cross-linked rather than copied.
2. **D3's "state-space model" was an unreferenced passing mention**, and §2.7 — which D3 points at for detail — does not cover state-space models at all. That cross-reference silently under-delivered on one of the five families D3 names. Now cited, with the 8760-hour seasonal-storage motivation and an explicit statement of what it does *not* solve (multi-carrier coupling is a separate decision from sequence length).

| Reference | Placement | Claim |
| :--- | :--- | :--- |
| `gu2022s4` | D3 | Linear-time sequence processing via a recurrent state rather than pairwise attention |
| `gu2023mamba` | D3 | Selective state spaces make that state input-dependent, recovering much of attention's modelling power |
| `fioretto2020acopf` | D5 | Learned AC-OPF proxies report constraint violations alongside error, and train against the Lagrangian dual so violations are penalised not merely measured |
| `donti2021dc3` | D5 | Completion-and-correction enforces equality constraints by construction and corrects remaining inequality violations through the network |

Both D5 sources are single-carrier power flow with a fixed constraint set, so the text says plainly that they relocate the evaluation burden rather than remove it — a multi-carrier hub adds conversion, storage continuity and discrete on/off decisions, some of them combinatorial.

**One citation honestly incomplete.** Mamba's arXiv comments field is empty, so the venue could not be confirmed from metadata. Cited as a preprint, with a `note` field recording that the venue is unconfirmed, rather than asserting COLM 2024 from memory.

**Guideline adopted.** Mistral's contribution guideline was the strongest part of the submission — better than what `CONTRIBUTING.md` had. Added in condensed form: every identifier must resolve before being cited (with both of this repo's actual fabrication incidents named as the reason), `[citation needed — could not verify]` as an acceptable output, primary sources over surveys, one citation per claim, one kind of change per PR, and a rejected-list in the PR description as a welcome habit.

## 2026-09-14 (merge "what an energy-system model does" into §3.1)

Barton had drafted a "What does an energy-system model actually do?" section on the Chapter 3 **landing page** (uncommitted working-tree change). Reviewed it, and moved it into [§3.1](chapter-3-sim-opt/3-1-taxonomy-of-tasks.md) instead of keeping it on the landing page. Three reasons:

1. **Landing-page uniformity.** Every other chapter landing is one-line intro + diagram + "In this chapter" table, with no body prose. The draft added ~55 lines, making Chapter 3 structurally unlike Chapters 1, 2, 4, 5, 6.
2. **Duplication with Chapter 1.** Checked each claim against Chapter 1. The component list, the building→district→urban scale ladder, and the energy-hub paragraph all restate [§1.1](chapter-1-background/1-1-what-is-ues.md) (which is richer — it has the scale table with typical extents, the coupling matrix, and the four "beyond the hub" items with five review citations). The "learned models are cheaper over loops" point restates [§1.2](chapter-1-background/1-2-fms-in-one-page.md) consequence 2 and [§1.5](chapter-1-background/1-5-why-ues-why-now.md). These were cut and replaced with a one-sentence back-link to §1.1.
3. **It was doing §3.1's assigned job.** [§1.6](chapter-1-background/1-6-scope-and-how-to-use.md) job #1 assigns "what actually gets modelled… what mathematical object each task is" to Chapter 3. §3.1 previously opened cold on "Each row is a distinct *task*…" with no statement of what a task *is* — the draft's input→output framing is exactly that missing preamble.

**Kept** (genuinely new, not anywhere else in the book): the `system description + external conditions → model → outcomes` mapping; the simulation-vs-optimisation distinction; the "why this framing matters for FMs" argument. Grepped the whole book for the sim/opt distinction — it appears only in §3.4's opening line and §3.5's "structurally different from dispatch", both of which assume the reader already has it. Nothing introduced it, in a chapter titled "Simulation and Optimisation in UES".

**Numbering left alone.** Considered a new §3.1 pushing the others down. Rejected: §3.1 is cross-referenced by number from §3.2, §3.4, §3.6, §4.6, and the T1–T9 task IDs are cited as "T1 in §3.1" across chapters, plus TODO.md and outline.md. Renumbering touches all of that for no reader benefit.

**Two Mermaid diagrams dropped**, and one bug avoided. The draft added a second diagram above the existing TOC flowchart, contradicting [diagram-ideas.md](diagram-ideas.md)'s rule (don't add a diagram the nav + table already conveys) and TODO.md, which lists the Chapter 3 landing flowchart as still-to-be-*replaced*, not added to. The draft diagram also used `C{Simulation\nOR\nOptimisation}`, which renders the literal characters `\n` in Mermaid 11 — traced through an actual 11.4.1 install rather than inferred, since this log records that inferring Mermaid behaviour already produced one wrong call here (the quadrantChart semicolons). Flowchart nodes route `labelHelper` → `createText` → `markdownToHTML`, which converts only real newlines (`/\n */g`); the `replace(/\n|\n/g, "<br />")` that would have handled it lives in `createLabel`, which no flowchart shape calls in v11. Matches the independently reported v11 regression. Correct form is `C{"Simulation<br/>OR<br/>Optimisation"}` if the diagram is ever wanted. Not verified in a browser: jsdom cannot complete a Mermaid render (`getBBox`), so this rests on source-path tracing plus the external report.

**References.** Two new citations, both verified against Crossref: `crawley2008simulation` (Building and Environment 43(4):661–673, DOI 10.1016/j.buildenv.2006.10.027) and `conejo2010decision` (Springer US, ISOR&MS 153, DOI 10.1007/978-1-4419-7421-1). Added to `references/fm-for-ues.bib` (93 → 95 entries; `conejo2010decision` is the file's first `@book`) and written as hyperlinked footnotes in house style — the draft's versions were plain text with `&` in the author lists, against the convention in 120 of the book's 124 footnote definitions. The draft also redefined `ferrando2020ubem` and `geidl2007opf`, already defined in §1.1/§3.1/§3.3; those duplicates are gone with the landing-page revert.

`last_reviewed` on §3.1 bumped to 2026-09-14. Chapter 3 landing page left untouched (the draft was never committed).

## 2026-09-16 (fill in §2.4.3, clean-energy forecasting FMs)

§2.4.3 was a stub: one sentence on multi-modal fusion and patch tokenisation, one citation, nothing else — despite being labelled "(Mature)" and sitting between two substantive siblings. Considered deleting it as irrelevant. Rejected: renewable generation forecasting is the one energy sub-domain besides the grid where domain-pretrained FMs demonstrably work, and [§2.4](chapter-2-fm-foundations/2-4-existing-fms-relevant-to-energy.md) promises the reader a survey "organised by family". Removing it would leave the promise unmet and drop the clearest worked example of [§2.3.1](chapter-2-fm-foundations/2-3-choosing-a-basic-element.md)'s criterion succeeding.

**An error found in the one citation that was there.** `ferdaus2025cleanenergy` was recorded as *Renewable Energy*. Crossref gives *Renewable and Sustainable Energy Reviews* — a different journal. The review has since been published (vol. 226, art. 116452, DOI `10.1016/j.rser.2025.116452`); the arXiv record carries no `journal_ref`, so the venue could not have come from there. Corrected, DOI added, author list expanded from `and others` to all five. Like the fabricated `energyfm2026` author field caught on 2026-09-13, this one surfaced by running an *existing* entry past Crossref rather than while adding a new one — worth doing periodically across the whole `.bib`, not only at insertion time.

**Four primary sources added**, each verified by fetching the arXiv record and matching the title before citing:

| Key | What it demonstrates |
| :--- | :--- |
| `fan2025windfm` | WindFM — 8.1M params, WIND Toolkit (~150B timesteps, 126k sites), SOTA zero-shot, holds on another continent, weights public |
| `huang2026tyanwp` | Tyan-WP — same corpus, static site embedding + power–meteorology fusion, U.S. → U.K. transfer |
| `mishra2025spirit` | SPIRIT — solar cold start, ~70% over prior zero-shot SOTA where the conventional route needs 5+ years of site data |
| `longarini2026coldstart` | 440 PV sites; general covariate-aware TSFMs on *synthetic* histories beat baselines 1.7–2×, insensitive to the generator |

Surveys were kept for the landscape claim only, per CONTRIBUTING; the specific results are all primary.

**The argument the section now carries**, rather than a list of models. Renewable forecasting matured early because a generation site passes all four requirements of §2.3.1 with no convention to argue about — the positive case that §2.3.2's building analysis is the negative of. Three limits then keep it from being read as encouragement for a UES FM: (1) WindFM and Tyan-WP both sit on the same public WIND Toolkit corpus, and the multi-carrier case has neither an agreed element nor a corpus; (2) these models forecast an *exogenous, weather-driven input* — a boundary condition upstream of the hub, not the system, so nothing about conversion, storage state, topology or discrete decisions ([§3.3](chapter-3-sim-opt/3-3-energy-hub-formalism.md)); (3) single-carrier, single-task, short-horizon, which is narrower than the multi-task transfer that separates an FM from a surrogate ([§2.8](chapter-2-fm-foundations/2-8-surrogates-vs-fms.md)).

The `longarini2026coldstart` finding is the one flagged as most useful here: accuracy tracked *the availability of plausible temporal context*, not the fidelity of whatever generated it — which bears on how much a UES corpus would have to be real versus merely plausible.

**Scope held deliberately.** No claim that a hub FM follows from any of this; §2.4.3 ends by routing the reader to [§4.1](chapter-4-directions/4-1-off-the-shelf-fms.md) (use the forecast off the shelf) and explicitly says that is not a step toward a UES foundation model. Bibliography 93 → 97 entries. `last_reviewed` bumped to 2026-09-16.

**Not verified in a browser.** Footnote rendering and the two new anchor links checked by grep against the target headings, not by a Jekyll build.

## 2026-09-17 (extend §2.8 with the surrogate → FM migration path)

Barton asked whether Kleinebrahm et al.'s *Joule* paper on European grid defection belonged in the surrogate section, and — the better half of the question — how a reader moves from a surrogate to an FM. [§2.8](chapter-2-fm-foundations/2-8-surrogates-vs-fms.md) said what the *difference* is (the four-row table) but never what to *do* about it. The only route it offered was one clause: "making the same class of model transferable across systems rather than rebuilt for each one" — the destination, not the path.

**New subsection: a four-step path, ordered by when each constraint bites.**

| Step | What changes | Routes to |
| :--- | :--- | :--- |
| 0 | Check the basic element — it can veto everything downstream | §2.3.1, §2.3.2 |
| 1 | Widen training from one system to a population (mostly corpus work) | §2.5, §2.4 |
| 2 | Make the transfer claim and test it on held-out *systems* | §2.9 |
| 3 | Broaden from one task to several | §2.1 |

Step 0 is first on purpose: §2.3.2's negative result for buildings means a surrogate on a failing element cannot be scaled into an FM, so the cheapest check gates the expensive ones. Step 1 is framed as corpus construction rather than modelling, consistent with §2.5 treating the missing corpus as the binding constraint.

**Named the middle ground.** Steps 1–3 are separable, and a model taking only some is not a failed FM. Added *transferable surrogate* (Steps 1–2, not 3) as an honest label, with §2.4.3's renewable models as the worked instance — ~126k sites, genuinely zero-shot, but single-carrier and single-task. This gives the book a word for the category most real work lands in, instead of forcing a binary.

**The Kleinebrahm citation, and what it is *not* used for.** Cited for one claim: work at continental building-stock scale is population-level in the sense Step 1 requires. Deliberately **not** cited as a surrogate, because the method could not be verified — the paper is paywalled and the abstract is absent from Crossref, OpenAlex, Semantic Scholar and Europe PMC. An earlier draft of this passage asserted the study "is not released as a model anyone else can apply" and that "Steps 2 and 3 are simply not attempted"; both were claims about a method the writer had not read, and were cut. The replacement argues the general point instead — *the distinction is the deliverable, not the scale* — which needs no unverifiable detail about this particular paper. Only the title, authors, venue and pagination are asserted, all from Crossref.

**A wrong cross-reference fixed in passing.** §2.8 pointed at [§3.4](chapter-3-sim-opt/3-4-dispatch-optimisation.md) for "the break-even arithmetic". §3.4 itself says the arithmetic is developed in §3.5, and [§3.5](chapter-3-sim-opt/3-5-design-sizing-optimisation.md) is where the `N_train × t_sim < Σ(N_evaluations × t_sim)` inequality actually appears. Repointed.

§2.8 had no footnotes before this; the definitions block is placed in house position, above the closing nav rule. Bibliography 99 → 100. `last_reviewed` bumped to 2026-09-17. All 14 links in the section verified to resolve, both anchors checked against the target headings. Not rendered in a browser.

## 2026-09-17 (repo review: fix 12 dead deep links, source §2.3's zoning claim, spelling drift)

A full-repo content review turned up one real bug, one unsourced load-bearing claim, and minor drift. Fixed those three here; the larger findings are recorded at the bottom for later.

**Twelve dead deep links, invisible to CI.** Every `#gN` link into [§6.1](chapter-6-outlook/6-1-open-gaps.md) was broken: Kramdown derives `g9--representing-a-decision-space-alongside-a-state-space` from `### G9 — …`, so a bare `#g9` never resolved and readers landed at the top of the page instead of the gap. Six links to `#g9`, three to `#g4`, two to `#g6`, one to `#g7`. Fixed by adding explicit IDs (`{#g1}` … `{#g9}`) to the nine headings, which is robust to later rewording — repointing the twelve inbound links instead would have re-broken on the next heading edit.

`lychee` could not have caught these: `.github/lychee.toml` excludes internal `.html` cross-links, because they don't exist as files against the raw Markdown. **A real check needs to run against the built site.** Wrote a standalone anchor checker (Kramdown slug rules + explicit `{#id}` support) and verified it by injecting a deliberate break and confirming it caught it — 70 anchor links across the repo, 0 broken after the fix. Worth wiring into CI; not done here.

**§2.3's zoning claim now has a source.** [§2.3](chapter-2-fm-foundations/2-3-choosing-a-basic-element.md) is the page the home page tells readers to read first, and it carried zero citations across 1,422 words. Most of it is original argument that needs none, but §2.3.2(b) asserts that zoning is a modelling convention rather than a property of the building, qualified as "a reason this field already knows" and "a debate they have lived" — naming a literature without pointing at it.

Added Shin & Haberl's systematic review (*Energy and Buildings* 203:109429, DOI `10.1016/j.enbuild.2019.109429`, verified via Crossref). It is a better fit than expected: the abstract reviews "previous **definitions** of HVAC thermal zoning" — competing definitions are exactly the ambiguity §2.3.1 requires an element not to have — and concludes future research is still needed to produce a well-documented zoning method. That second half independently supports §2.3.3's R3 claim ("blocked by an unsolved problem belonging to the building simulation community rather than the ML one") and [G8](chapter-6-outlook/6-1-open-gaps.md), which made the same claim uncited. Cited in all three places. Bibliography 100 → 101.

**Spelling drift**, four instances, all in body prose rather than citation titles: `tokenization` → `tokenisation` (§5.2, §5.8), `artifact` → `artefact` (§5.8, §6.1). Everything else flagged by the sweep was inside a citation title, where the original spelling is correct and was left alone.

### Findings not acted on

- **[§2.5](chapter-2-fm-foundations/2-5-what-does-not-exist-yet.md) is the weakest load-bearing page in the book.** 176 words, six negative existence claims, no citations and no dates — and Chapters 4, 5 and 6 all rest on it. Negative claims age silently and cannot be checked without a stated method. §1.3 does this properly (Scopus terms + date + citation); §2.5 has no equivalent. Both core claims were spot-checked against arXiv on 2026-09-17 and still hold — no FM for multi-carrier operation or energy hubs — so the premise is sound and only the support is missing. Needs a search-methodology line and a nearest-miss citation per bullet.
- **The glossary is one-sided.** 28 terms, roughly 23 ML-side to 5 UES-side, in a book whose stated audience is someone who knows UES well and ML less well *or vice versa*. Missing, with body usage counts: UBEM (21 — the most-used acronym in the book), OPF (16), MILP (14), LP (9), ESDL (8), CIM (6), GNN (6), LLM (5), CHP (4), DH (4), MINLP (3). DINO, SAM and ViT are all defined; UBEM is not.
- **Chapter 4 stubs §4.1–4.4 remain uncited.** One directly fillable: "Systematic Evaluation of TabPFN-TS for Zero-Shot Probabilistic Heat Load Forecasting in District Heating Networks" (arXiv, 2026-08-20) is an off-the-shelf FM applied zero-shot to a UES carrier task — precisely §4.1's subject, covering district heating, which the book discusses but has no FM evidence for. TabPFN-TS is already threaded through §2.4.1 and §2.4.4.
- **Not checked:** whether any *positive* claim has gone stale (§2.4.1's model roster is the likeliest casualty), and anything needing a Jekyll build.

## 2026-09-19 (source §2.5's six negative claims)

First item off last week's "findings not acted on" backlog. [§2.5](chapter-2-fm-foundations/2-5-what-does-not-exist-yet.md) asserted six "no FM exists for X" claims — 176 words, zero citations, zero dates — while Chapters 4, 5 and 6 all build on it being true. A negative claim with no stated search method can't be checked or age-verified; [§1.3](chapter-1-background/1-3-fm-landscape-by-domain.md) already does this correctly (dated Scopus search + citation), so the fix is the same pattern applied here.

**Method.** A dated arXiv title/abstract search per claim, run 19 September 2026 — first attempt silently returned zero hits on every query including a known-good control (`"foundation model" AND "power grid"`, which should and does return 16 results); traced to `export.arxiv.org` 301-redirecting plain `curl` to an empty body. Fixed with `-L` before trusting any result.

Two of the six claims turned up a genuine nearest-miss paper, both new to the bibliography:

- **Multi-carrier operation.** The search returns exactly one paper: TabPFN-TS (an existing general time-series FM) evaluated zero-shot on district-heating load forecasting.[^spoek2026tabpfndh] This is the same paper flagged last week as the direct fill for [§4.1](chapter-4-directions/4-1-off-the-shelf-fms.md)'s stub — cited here for what it is *not*: single-carrier, forecasting-only, no conversion/storage/dispatch. The nearest miss confirms the gap.
- **Representation/interchange format.** Beyond [§3.7](chapter-3-sim-opt/3-7-schemas-and-standards.md)'s existing ESDL/CIM treatment, added a June 2026 paper from *within* the multi-energy-systems research community itself — motivated by discussions at ECOS 2025, concluding that standardised case-study description "remains fragmented".[^vallee2026standardizing] Independent confirmation from outside ML that the same gap is felt domain-side.

Two claims were cross-referenced to material the book already has rather than re-cited: the design/planning claim now points at the single-system surrogates in [§4.9.3](chapter-4-directions/4-9-3-methods-tier3.md) (`perera2019mlsurrogate`, `prina2024energyplan` — neither claims cross-system transfer), and the benchmark claim points at [G4](chapter-6-outlook/6-1-open-gaps.md#g4)'s existing `lin2024tsfmbuilding` citation rather than re-running that search.

The basic-element claim needed no citation, only a pointer — [§2.3.2](chapter-2-fm-foundations/2-3-choosing-a-basic-element.md#232-basic-elements-for-buildings)/[§2.3.3](chapter-2-fm-foundations/2-3-choosing-a-basic-element.md#233-representation-strategies-and-testable-predictions) already argue it at length. The decision-space claim is the cleanest of the six: zero results, no near miss to report, cross-referenced to [G9](chapter-6-outlook/6-1-open-gaps.md#g9).

Both new sources verified against arXiv metadata before use (title, full author list, date). Bibliography 101 → 103. `last_reviewed` bumped to 2026-09-19.

[G9](chapter-6-outlook/6-1-open-gaps.md#g9) itself, which §2.5 cross-references, remains uncited on its own page — out of scope for this pass, one section at a time per CONTRIBUTING; flagged, not fixed.

**Not rendered in a browser.** Footnote ref/def integrity and all nine cross-reference targets checked by grep against the file tree and existing anchor precedent elsewhere in the book, not by a Jekyll build. lychee clean (0 errors) — binary re-downloaded this session since the temp path from last week's session no longer existed.

## 2026-09-19 (progress Chapter 4's four stub sections)

Second item off the backlog, following §2.5's sourcing pass earlier the same day. Ran a dated arXiv search per section (all title/abstract, 19 September 2026), each independent of the others.

**§4.1 gets a genuine worked example, with real numbers.** A published evaluation runs TabPFN-TS and Chronos-2 zero-shot on district-heating heat-load forecasting.[^spoek2026tabpfndh] Reported: hourly 24h-ahead forecasting with a 12-week rolling context and ambient temperature as the only covariate is a parsimonious high-performing configuration (longer context does not help); TabPFN-TS reaches CVRMSE 13.06% against Chronos-2's 12.48% but is better calibrated; and — the part most relevant to this book's own concerns — the configuration was validated on a **second, different network**, i.e. transferability actually tested rather than assumed, exactly what [§2.9](chapter-2-fm-foundations/2-9-ues-fm-evaluation-criteria.md) dimension 2 asks for. Flagged the one caveat worth carrying forward: TabPFN-TS pretrains on synthetic data, which side-steps leakage but leaves open whether its prior captures district-heating dynamics specifically.

**§4.2 stays a stub, but a checked one.** The search (ResStock/ComStock + foundation model/pretrained; separately "building stock" + foundation model) returns exactly one relevant result and confirms no stock-level FM has been published. That one result — `bose2024rnnstofm`, already cited elsewhere in this book for its scaling-laws argument — is reused here for a different claim: it isolates dataset heterogeneity as mattering more than parameter count on ComStock-derived data, which bears directly on what a stock-level pretraining corpus would need to contain, even though it is not itself a stock-level model.

**§4.3 gets one category addressed, not the general problem.** A September 2026 platform (BuildOcc) grounds LLM occupant-behaviour agents in the American Time Use Survey rather than a generic default schedule.[^jung2026buildocc] Framed carefully in the text: this replaces *one* of G7's named assumption categories (occupancy schedules) with a checkable one, leaves U-values/discretisation/technology-defaults untouched, and — the point worth stating plainly — grounding an assumption in real population statistics is not the same as verifying it is the right assumption for *this* building. Sharpens G7 one level down rather than resolving it.

**§4.4 finds a closer adjacent-domain precedent than expected, plus an in-domain contrast.** A generative-design framework (graph-learning generator + performance estimator) is validated on **IEEE power-system test cases specifically**, not a generic mechanical benchmark[^wu2022generativeresilience] — closer to this book's subject than "adjacent engineering domain" usually implies, though it optimises for resilience under disruption rather than cost/feasibility, and single-carrier topology is not multi-carrier device selection. Paired with an in-domain example (SolarGAN, synthetic solar-irradiance scenarios for BIPV design)[^zhang2023solargan] that clarifies a distinction worth having explicitly: generating an uncertain *input* to a design process is not the same as generating the *design* itself — the same "agent supplies inputs, tool runs unchanged" line §4.3 already draws for LLM agents, now drawn for generative models too, and used to place both new citations at opposite ends of one spectrum relative to [G9](chapter-6-outlook/6-1-open-gaps.md#g9).

**One near-miss on fabrication, caught before it shipped.** Drafted the Wu & Wang citation with an ASME-typical page/article-number pattern before checking it — the number turned out to match Crossref's actual `article-number` field (031705) once verified, but it was written down before that check, not after. Re-verified from the full Crossref record before leaving it in. The process was wrong even though the guess was right; flagging it here rather than treating a correct guess as equivalent to a checked fact.

**A repeat of the first-search-returns-nothing bug**, same root cause as §2.5's: `export.arxiv.org` 301-redirects plain `curl` to an empty body. Caught immediately this time (a control query was run first) rather than after drafting content on top of false negatives.

New: `jung2026buildocc`, `wu2022generativeresilience`, `zhang2023solargan`. Reused without duplication: `spoek2026tabpfndh` and `bose2024rnnstofm`, both added earlier the same day for §2.5/already in the bibliography respectively. Bibliography 103 → 106.

`lychee.toml`: added an ASME DOI-prefix exclusion (`10.1115`) — `asmedigitalcollection.asme.org` 403s automated checkers same as the six publishers already excluded; the redirect target itself confirms the article (volume/issue/article-number all match). DOI independently verified against Crossref before excluding, not just via the redirect.

`TODO.md`'s stub-sections item updated with a progress note rather than closed — none of the four sections has this book's own benchmark run, which is what "done" would actually require.

Verified: footnote ref/def integrity on all four pages, bib key uniqueness, brace balance (808/808), all cross-reference targets checked to exist (one initial check gave a false "MISSING" for files just confirmed present by direct read — a shell-loop artifact in the verification script itself, not a real error; re-run with a simpler loop and all resolved), lychee clean (0 errors) across all four pages after the ASME exclusion. Not rendered in a browser. lychee binary re-downloaded again this session (the previous session's temp directory no longer exists, as expected for scratch storage).

## 2026-09-23 (PRs #36 and #37 merged: review follow-ups, stub-citations branch)

Recorded here after the fact; neither PR added its own entry, to avoid a `log.md` conflict between the two branches.

**[#36](https://github.com/BartonChenTW/FM4UES/pull/36), review follow-ups.** Two dead `#gN` anchors created by the explicit-ID fix of 2026-09-17 (an explicit `{#g9}` replaces the auto-generated ID, so two links using the long form broke). Doc drift: §2.9 missing from README/index; the homepage's publication-count statistic now names its Scopus source and links to §1.3; §6.2's stub wording; a published page linking to the unbuilt `log.md`. Every footnote name now matches a `.bib` key. Mermaid diagrams follow the reader's light/dark theme (`_includes/mermaid_config.js`). New CI, `site-check.yml`, builds the site with the github-pages gem and checks every internal link and `#anchor` in the built HTML. Nothing checked these before, because `link-check.yml` must exclude internal links. It also fixed a literal `<script>` inside a JS comment, which made lychee's tokenizer skip every link after the sidebar and would have made the new check pass vacuously. Added [`refs-to-add.md`](refs-to-add.md). The new check passed on its first run; one external link (otexts.com, 403 to bots) needed a `lychee.toml` exclusion.

**[#37](https://github.com/BartonChenTW/FM4UES/pull/37), stub citations.** The 2026-09-19 work below (§2.5's six negative claims; §4.1–4.4), merged after updating the branch with #36. Both checks passed.

Branch cleanup the same day: `fix/review-followups`, `docs/2-5-source-negative-claims` and `docs/3-1-what-a-model-computes` deleted. The last had the same change as `f32ba65` on `main` (patch-equivalent, verified line by line), just under a different commit ID.

## 2026-09-24 (source §2.8, §2.3 and §4.10)

The three weakest pages by uncited literature claims per word: §2.8 (1 citation in 1,243 words), §2.3 (1 in 1,272, and the book's "read only one page" page), §4.10 (2 in 947). Chapter 5 (the case-study proposal), §4.5–4.7 (the book's own screening framework) and §6.2 (contributor guidance) also scored low but are not expected to cite heavily, so they were skipped.

**§2.8.** The heading "Why the existing multi-energy surrogate literature is not FM work" characterised that literature without citing it. Now: `ledee2025messurrogate` for the landscape (its related-work review), `aghaeipour2021interactive` as a typical single-system case, and `perera2019mlsurrogate` (reused) as the nearest exception. Its transfer learning adapts a surrogate to new conditions, which is not one model across system configurations. No dedicated review of multi-energy surrogates was found. "Operating cost" became "cost and other objectives" to match Perera's actual objectives (NPV, grid integration).

**§2.3.** Cited the basic element as it exists in current models. Grid buses: `donon2020gns` (bus-level graph solver, robust to topology change on IEEE 9–118-bus cases) and `hamann2024foundation` (reused, labelled as a proposal). Patches: `das2024timesfm` and `nie2023patchtst`, both reused. Cells: `hollmann2025tabpfnv2`, reused. Attribute-list metamodels: `westermann2019surrogate`. The decision-space claim links to §2.5's dated search instead of re-citing.

**§2.4.4, found in passing.** The per-cell design was credited to TabPFN v1; it is v2's. v1's abstract describes samples as a set-valued input, and the Nature paper's architecture text describes the per-cell design. Fixed, and v1 kept for what it did.

**§4.10.** Latin hypercube (`mckay1979lhs`), Sobol sequences (`sobol1967distribution`), deep imbalanced regression for the rare-regime advice (`yang2021dir`), exact MILP encoding of a ReLU network (`fischetti2018milp`), and physics-informed learning under limited data (`karniadakis2021piml`, reused). `lychee.toml` now excludes Taylor & Francis (`10.1080`), which returns 403 to every scripted client.

**Not cited, on purpose.** §4.10's callout that FMs under-represent extremes and so degrade on high-impact events. The closest evidence (Olivetti & Messori 2024, *GMD*) *qualifies* it: data-driven weather models "can also compete" on extremes in most regions, varying by region, event and lead time. Left for the maintainer to judge rather than cited as support. Also unsourced still: §4.10's speedup-before/after-correction pattern, the NRMSE/CV(RMSE) note, and the cross-scale caution.

Method: every new reference's metadata from Crossref (arXiv for `yang2021dir`); every claim written from the abstract (OpenAlex, Semantic Scholar, arXiv, Springer), plus full text where it mattered and was reachable: TabPFN v2 (Nature, open access). Lédée et al. is CC-BY but blocked to scripted access, so it is cited for its abstract only. Bibliography 108 → 116; footnote names 116, all matching. lychee 0 errors on every changed page. Not rendered in a browser.

## 2026-09-29 (new §3.9: building retrofit and whole-life carbon; task T10)

**Why.** Building materials and LCA (embodied carbon) were raised as a possible new section. The book already argued about retrofit — §2.3's decision layer, [G9](chapter-6-outlook/6-1-open-gaps.md#g9), §4.9.3's retrofit corollary, §4.2's "retrofit policy" — but had no page on how retrofit is actually analysed, and embodied carbon appeared only as a field in §5.5's device token and the "LCA" cell of T9. Framed as retrofit analysis with whole-life carbon inside it, rather than a standalone materials/LCA section, so it grounds the existing decision-space argument instead of opening a separate topic. No new chapter: chapters are organised by kind of material, not by sub-domain.

**New page.** [`chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.md`](chapter-3-sim-opt/3-9-retrofit-and-whole-life-carbon.md): the task (discrete measure search with T1 in the loop), how it composes with T1/T5/T8/T9, instance-specific constraints; whole-life carbon via EN 15978 modules, with B6 (operational energy) as the seam between this book and LCA; data shapes (LCI databases, national datasets, EPDs, the missing paired corpus); why it matters for FMs. Added as §3.9 so nothing is renumbered.

**Taxonomy.** Added **T10 Retrofit analysis & planning** to §3.1 ("The nine tasks" → "The ten tasks"), plus notes for T9 and T10. Added rather than widening T9: retrofit has its own structure (discrete measure selection), while T9 is post-processing. Updated T1–T9 → T1–T10 in §4.6 and the Chapter 4 landing page.

**Screening.** §4.5: new sub-field row "Retrofit / whole-life carbon" (basic element not yet defined — must carry a decision space) and a sentence in the assessment. §4.6: T10 row, verdict "Promising, representation-blocked". §4.7: paragraph on T10 as the task where the task screen and the representation screen disagree most. §4.8: candidate 5, listed last because it needs both G8 and G9. Chapter 4 landing: point added to the quadrant chart (label checked against the Mermaid 11.4.1 quadrant grammar — `MINUS` is allowed after the first token) and one sentence.

**Cross-links to §3.9** from §2.3 (decision layer), G9 in §6.1, the §4.9.3 retrofit corollary, and §4.2. Chapter 3 landing (diagram, table, "Ten tasks"), §3.8's next-link, README and `index.md` contents tables. Glossary: embodied emissions, EPD, LCA, LCI database, retrofit measure, whole-life carbon.

**References (bib 116 → 124).** `ma2012retrofit`, `asadi2012retrofit`, `wang2018cesar`, `rock2020embodied`, `galimshina2021renovation`, `wernet2016ecoinvent` (all Crossref-verified: title, full author list, venue, volume, pages), `en15978` (EN 15978:2026, via the CEN-CENELEC announcement; SIS confirms it replaces EN 15978:2011), `kbob2026oekobilanz` (Swiss LCA data platform, version 9.0 of 14 July 2026). Claims written from abstracts (OpenAlex / Semantic Scholar) for Röck, Galimshina and CESAR; from abstract summaries via search for Ma, Asadi and ecoinvent (publisher pages blocked scripted access); from the landing pages for EN 15978 and KBOB. **Considered and dropped:** Ibn-Mohammed et al. 2013 (*Energy and Buildings* 66) — same claim as Röck 2020, which is the stronger source (one citation per claim). ISO 14040/14044 not cited: iso.org serves a bot challenge that lychee would fail on, and EN 15978 is the building-level standard anyway.

Verified: footnote ref/def integrity on every page, all footnote names match `.bib` keys, no duplicate keys, braces balanced (966/966), every internal `.html` link and `#anchor` resolves to an existing page/heading; lychee v0.24.2 (musl build — the gnu build needs a newer glibc than this machine has) 0 errors across §3.1, §3.9, Chapter 4 and the glossary. Not built with Jekyll (no Ruby on this machine) and not rendered in a browser — `site-check.yml` will do the build on the PR.

## 2026-09-29 (new §3.10: social dimensions; task T11; §4.3 simulated people)

**Why.** Social aspects of UES and buildings were raised as a possible addition, split into four kinds: (1) people as model inputs, (2) social outcomes, (3) social properties of the FM itself, (4) social science without AI. The maintainer chose (1) and (2). Before this, occupant behaviour was covered (§3.1 T1 note, §4.3 BuildOcc) and "equity, comfort" appeared once, undeveloped, in T9.

**New page.** [`chapter-3-sim-opt/3-10-social-dimensions.md`](chapter-3-sim-opt/3-10-social-dimensions.md): the two roles (inputs vs the population outcomes fall on), anchored on Krumm et al.'s finding that social aspects enter energy models mainly exogenously and only ABMs represent actor heterogeneity; occupant behaviour (brief, cross-linked); technology adoption via ABMs (Austin PV; AgentHomeID's owner types and income quartiles, which is the stock-level form of §3.9's retrofit question); energy poverty and energy justice, with the point that distributional outcomes depend on a normative equity principle; data shapes (surveys, registers, observed adoption, meter data as a social signal, text); why it screens like T8.

**Taxonomy.** Added **T11 Behaviour & adoption modelling** to §3.1 ("ten" → "eleven"); T9 note extended to equity outcomes. Added as its own task because adoption models have a distinct structure (calibrated stochastic simulation of decision rules) and, uniquely among the tasks, no physics simulator for ground truth.

**Screening.** §4.5 row "Behaviour, adoption and social outcomes" and an assessment sentence; §4.6 T11 row, verdict "Weak as an FM target — LLMs as bounded tools instead"; §4.7 paragraph separating T11's S1 failure from T8's and naming validity, not scale, as the open problem; Chapter 4 landing: quadrant point and sentence, T1–T10 → T1–T11. No §4.8 candidate: the screen does not support a new pretrained model here.

**§4.3 extended** with "Beyond occupancy: simulated respondents, adopters and policy agents": silicon samples (Argyle et al.) against their failure modes (Bisbee et al.: averages right, variance and coefficients wrong, prompt- and time-sensitive), then two energy preprints that keep the LLM bounded — LLM-assisted rubrics inside a calibrated PV-adoption ABM, and an LLM policy agent scored on energy-burden metrics whose decoupled validate-and-project design gave 0 grid violations vs 55 under direct control. Tied to G7 and to §4.9.3's retrofit corollary. Stub note updated; one "still to add" bullet.

**Cross-links / other.** §3.9 → §3.10 (adoption rate of measures); §4.8's metadata-conditioned load FM → §3.10 data shapes; Chapter 3 landing (diagram, table, "Eleven tasks"), §3.9 next-link, README, `index.md`. Glossary: agent-based model, energy burden, energy justice, energy poverty, silicon sample.

**References (bib 124 → 135).** `krumm2022social`, `rai2015abm`, `bouzarovski2015energypoverty`, `jenkins2016energyjustice`, `vagero2023justice`, `beckel2014household`, `argyle2023silicon`, `bisbee2024synthetic` (Crossref-verified, full author lists), `ganal2026agenthomeid`, `faiud2026llmabm`, `jadhav2026eqgrid` (arXiv API-verified). `doma2023occupant` reused. Claims written from abstracts: OpenAlex (Bouzarovski, Argyle, Bisbee), Semantic Scholar (Jenkins, Krumm, Vågerö), RePEc/EconPapers (Beckel), arXiv (the three preprints); Rai & Robinson from a search summary of its abstract only (flagged in TODO). **Considered and dropped:** Rai & Henry 2016 (*Nature Climate Change*, ABMs of consumer energy choices) — a perspective making the same point as Rai & Robinson's primary result. **Dated search** (arXiv, 2026-09-29), reported in §3.10: "foundation model" × {energy poverty, energy justice, energy equity} → 0; LLM × {energy poverty, energy justice, energy burden} → 2, 1 relevant (EqGrid); LLM × agent-based × adoption × energy → 1 (Faiud et al.); "foundation model" × occupant behaviour → 0 (not reported on the page).

Verified: footnote integrity on every page, all footnote names match `.bib` keys, no duplicate keys, braces balanced (1058/1058), every internal link and anchor resolves; lychee 0 errors across Chapters 3–4, glossary, README and `index.md`. Not built with Jekyll and not rendered in a browser — `site-check.yml` covers the build on the PR.

## 2026-09-29 (new §4.11: a future ecosystem of UES FMs)

**Why.** Picked up the key TODO item: Chapter 4 surveyed directions one at a time and never said how they fit together; the coupling idea lived only in Chapter 5 (Phase 5 hub ↔ grid, D5 flexibility envelope), §4.8's grid-load bridge, and the private concept-paper notes (planned section "Coupling to adjacent FMs" and an "FM ecosystem" figure).

**New page** [`chapter-4-directions/4-11-ecosystem.md`](chapter-4-directions/4-11-ecosystem.md), placed last in Chapter 4 as its synthesis (after §4.10, so nothing is renumbered). Argument: basic elements differ by layer (§2.3, §2.4), so expect several FMs connected at interfaces rather than one. Contents: component table by layer with element and status ("the ends exist and the middle does not"); a Mermaid diagram of components and what flows between them; three interface types (physical quantities, shared learned representations, language/tool calls) with their trade-offs, anchored on co-simulation as today's practice; the concrete UES interfaces and what stands behind each; three shapes (one multimodal FM — conditional on a shared element, Aurora as the precedent that shows why; a federation coupled by physical quantities — the near-term default; an orchestrating agent — ChemGraph as precedent, G7 as the obstacle), with the book's reading that they are complementary; ecosystem-level needs (interface schema, uncertainty across interfaces, chain-level evaluation, constraint authority, shared data engines). Labelled as the book's own synthesis.

**Dated search** (arXiv, 2026-09-29), reported on the page: "foundation model" × ecosystem × {energy, grid} → 11 results, none on coupling energy-system FMs; "foundation model(s)" × {coupling, interoperab*, composable} × {power system, energy system} → 1, unrelated; "multiple foundation models" × {energy, grid} → 1, unrelated (not reported).

**Wiring.** Chapter 4 landing (table row; pointer sentence), §4.10 next-link, §4.8 grid-load bridge → §4.11, §5.1 Phase 5 → §4.11, README and `index.md` contents, glossary "Co-simulation".

**References (bib 135 → 136).** New: `pham2025chemgraph` (arXiv API; claim from abstract). Reused: `alfalouji2023cosimulation`, and `bodnar2025aurora` (already in the bib for §1.3/§2.2; re-checked on Crossref, claim written from its OpenAlex abstract — a duplicate entry was added by mistake and caught by the key-uniqueness check). **Considered and dropped:** HuggingGPT (Shen et al. 2023, arXiv:2303.17580) as the general "LLM as controller of specialist models" precedent — ChemGraph makes the same point in a physical-science setting with simulators in the loop, which is closer to UES (one citation per claim). No new open gap added: whether the interface problem deserves its own G10 is left to the maintainer (TODO).

Verification as for §3.9/§3.10: footnote integrity, bib keys, braces, internal links and anchors, lychee on changed pages. Mermaid diagram not rendered.

## 2026-10-01 (Granite-GFM and Prithvi-SWIN-L citations, §1.3 and §2.4.5)

**Why.** Closes `refs-to-add.md` item D. The Granite-GFM sentence (land surface temperature, 30 m, hourly, Swin backbone on Prithvi-SWIN-L) was cited to `szwarcman2024prithvieo2`, the Prithvi-EO-2.0 paper. That paper does not describe the Granite model: Prithvi-EO-2.0 is a ViT released in December 2024, and the Granite LST model (v1, May 2024) builds on Prithvi-SWIN-L. §2.4.5 also said that Prithvi-EO-2.0 "underlies" Granite-GFM, which was wrong.

**Changes.** §1.3: the Granite-GFM table row and sentence now cite `bhamjee2024granitelst`, and Prithvi-SWIN-L cites `jakubik2023prithvi`. The `szwarcman2024prithvieo2` footnote is no longer used there and was removed. §2.4.5: the sentence was split. Prithvi-EO-2.0 keeps `szwarcman2024prithvieo2`, and Granite-GFM is now attributed to Prithvi-SWIN-L with the same two citations as §1.3.

**References (bib 136 → 137).** New: `bhamjee2024granitelst`, the IBM Hugging Face model card (authors, release date and licence taken from the card). No paper was found for the 30 m, hourly model itself, so the model card is the primary source, following the precedent of EnergyBench in §3.2. The card names `jakubik2023prithvi` as the paper for its Prithvi-SWIN-L base model. **Considered and dropped:** Bhamjee et al., IGARSS 2024 ("Detection and characterization of urban heat islands with machine learning"). It covers a different model (1 km, 2 m air temperature, Johannesburg). Kreismann (2025, arXiv:2509.16617) applies the model rather than describing it.

Verified: footnote ref/def integrity on both pages, bib key unique.

## 2026-10-01 (glossary hover definitions; "Multimodality")

**Why.** The §1.4 bullet "Multimodality is becoming the default" used the term without defining it, and the glossary had no entry. Three options were weighed: a plain link to the glossary, kramdown abbreviations (`*[term]: …`, which give only the browser's own title tooltip, don't show on touch devices, and repeat the definition on each page), or a glossary link with a hover box. The hover box was chosen. The definition is written once, in the glossary, and the link still works without the box.

**Changes.**
- Glossary: new row **Multimodality**, linked to Cross-attention, §1.3 and §1.4.
- §1.4: "Multimodality" now links to `a-glossary.html#multimodality`.
- `_includes/footnote-tooltip.html`: the footnote hover box also works for glossary links. On pages with such a link it fetches the glossary once and shows the matching row's definition. Relative links in the definition are made absolute.
- Glossary anchors: every bold term now carries a kramdown span attribute, `**Term**{: #term}`, which renders as `<strong id="term">`. The id is the term in lower case, with every run of other characters turned into `-`. All 41 are unique. The first version made the ids in the script instead, and lychee failed on the PR with "Cannot find fragment", because it checks the built HTML without running JavaScript. Ids in the source fix that and need no script on the glossary page. CSS highlights the row whose term is the `:target`.
- `handleShow` now uses `currentTarget`, and the active-reference highlight works for links as well as `<sup>`.
- `CONTRIBUTING.md`: the anchor rule, with an example.

Not tested in a browser: there is no JavaScript runtime on this machine, so the script was only reviewed by reading. Check on the deployed site: hover "Multimodality" in §1.4, and open `a-glossary.html#multimodality` directly.

## 2026-10-01 (version history and per-page history links; version 2.1)

**Why.** Barton asked how readers can trace changes to the site's content: book versions, or a revision date on each page. Both are now done, since they answer different questions.

**Per page.** `_includes/page-status.html` now ends with a **Page history** link to the GitHub commit list for that page's source file, built from `page.path` and new `gh_edit_repository` / `gh_edit_branch` settings in `_config.yml`.
- It is automatic, so it can't go stale. The usual way to print a "last modified" date is the `jekyll-last-modified-at` plugin, which the standard GitHub Pages build doesn't allow. Using it would mean moving deployment to an Actions workflow.
- `last_reviewed` stays as it was, set by hand, because it records that someone checked the content, which git can't.
- The badge now renders even on a page with no `status` or `last_reviewed`, since the history link is always there.
- Also turned on just-the-docs' built-in "Edit this page on GitHub" footer link (`gh_edit_link`), which suits a community-edited book.

**Book versions.** New public page `appendices/c-version-history.md` (Appendix C). It gives the numbering rule (major = restructure; minor = new sections, substantial rewrites or site features; corrections are not numbered) and an entry for each version: 2.1 (this release), 2.0 and 1.1.
- 2.1 summarises the private log since 11 September: §2.9, §3.9, §3.10 and §4.11 new; §2.4.3, §2.8, §3.1 and §4.1–4.4 extended; references 54 → 137; site features.
- Version line bumped to 2.1 in `index.md` (now linking to Appendix C) and `README.md`. Appendix C added to the Appendices landing page, the home contents table, the README structure table, and Appendix B's next-link.
- `CONTRIBUTING.md`: new "Versions and releases" section with the release steps.

**Tags and releases.** No tags existed before this.
- `v1.1` → `2a3938b`, the first Jekyll site, 2026-09-10.
- `v2.0` → `3126662`, the last merge on 2026-09-11, so the restructure plus that day's rename and attribution fixes, as the book stood when "Version 2.0 — 11 September 2026" was its label.
- `v2.1` goes on this PR's merge commit, once it merges.
- Appendix C links to the Releases list rather than to each tag, so the PR's link check doesn't fail on `v2.1` before it exists.

## 2026-10-01 (book version in the sidebar)

**Released.** Tagged `v2.1` on the PR #42 merge commit (`50f83cd`) and published its GitHub Release, with notes from Appendix C. The repo now has releases v1.1, v2.0 and v2.1.

**Why.** Barton asked to see the book's version at the top left of the site.

**Changes.**
- `_includes/title.html` overrides the theme's sidebar title to add "Version 2.1" under it, styled in `_sass/custom/custom.scss` (small, 70% opacity, so it works in both colour schemes).
- The version now has one source, `book_version` and `book_version_date` in `_config.yml`. Both the sidebar and the home page label read it.
- `README.md` still states the version as literal text, because GitHub shows that file without Jekyll.
- The release steps in `CONTRIBUTING.md` were updated to match.

## 2026-10-01 (§3.1 retitled)

§3.1 "Taxonomy of Modelling Tasks" is renamed. Barton asked for an alternative to "Taxonomy", and the page does more than classify: it says what a model computes, then gives each task's mathematical structure, which Chapter 4 relies on when it screens the tasks.
- Sidebar title: **3.1 Modelling Tasks**.
- Page heading: **3.1 Modelling Tasks and Their Mathematical Structure**, following the short/long pattern of §3.10.
- The file name and URL (`3-1-taxonomy-of-tasks`) are kept, so existing links and bookmarks still work.
- Updated the visible wording in the Chapter 3 landing table and diagram, §3.2's previous-link, §4.6 and the Chapter 4 landing page ("task taxonomy T1–T11" → "modelling tasks T1–T11"), and the README and home contents.
- In §3.1's own text, "the taxonomy below" became "the eleven tasks below".
- Other uses of "taxonomy" in the book (the UBEM scale taxonomy in §1.1, the co-simulation "taxonomic review", the PIML taxonomy in §2.9, §4.10's "a taxonomy with consequences") refer to other works or the general idea, and are unchanged.

## 2026-10-01 (spell out internal labels outside their home section)

**Why.** Barton found "R4 in §2.3.3" in §4.2 and "the assumption categories G7 names" in §4.3 hard to follow: each is a label defined on another page.
- **R labels:** R1–R4 now appear only in §2.3.3, where its table defines them. Elsewhere the text says what each one is:
  - §4.2 (R4, twice): the building as an element of a stock
  - §4.9.2 (R3, twice): the building as a network of connected parts
  - §6.1 (R3): already spelled out; the redundant "(R3)" is dropped
  - §2.4.4 and §4.9.1 (R1): the attribute list, one row per building
- **G7 in §4.3:** later mentions now say "the verification question" or "gap G7 (verification of agent-built models)". "The categories G7 names" was also inaccurate, because the list of assumptions is §4.3's own, not §6.1's.
- The gap labels G1–G9 are used on many other pages and are left as they are. Each first mention on a page links to §6.1.

## 2026-10-01 (§4.9 marked as the book's proposed development path)

**Why.** Barton asked that §4.9 say it is only a proposed path to a foundation model for multi-carrier (multi-vector) energy systems, and stand apart from the rest of Chapter 4. The chapter's own subtitle calls it "a broad, neutral survey… not one specific programme", while §4.9 is exactly that: a programme of three tiers, each with a build plan.

**Changes.**
- §4.9 renamed **"4.9 A Proposed Development Path"** in the sidebar, with the page heading "4.9 A Proposed Development Path: Methods by Problem Class". The URL is unchanged.
- The subtitle now states the goal. A new `.important` callout, "A proposal, not a survey", gives:
  - what the three tiers are
  - what each one provides
  - that the route has not been built or tested as a whole
  - how it relates to Chapter 5
- Each tier page (§4.9.1–4.9.3) opens with a one-line note placing it in the proposed path. Their `parent:` front matter follows the new title.
- Updated how other pages describe §4.9: the Chapter 4 landing table and its "Chapter 4 vs Chapter 5" note (which now names §4.9 as the one marked exception), §4.8's next-link, the home page (two places), §1.6, and the README.

## 2026-10-01 (§4.8: "Already committed" heading corrected)

The §4.8 heading "Already committed and well-justified" was not accurate. The metadata-conditioned load FM has drawn interest but has not been started. The heading is now "Most promising near-term, limited by data licensing", and the entry ends by naming the limitation: licences on meter data paired with building and household attributes restrict pooling it into a training corpus. It also links to §3.2 on why measured data rarely comes paired with attributes. No page linked to the old heading anchor.

## 2026-10-01 (§4.11: empty layer cell filled)

In the §4.11 table "The components, by layer", the renewable-generation row left the Layer cell empty, meaning "same as above". It read as missing, so it now says "Boundary conditions". The same fix went into the §3.9 life-cycle table, where the B6/B7 row's Stage cell is now "B — use".

The Status column of the §4.11 table now uses the theme's coloured labels on a four-step scale:
- **Mature** (green): working models exist and are in use
- **Emerging** (blue): first domain models exist
- **Early** (yellow): only partial or single-case attempts
- **None yet** (red): nothing built

Each label keeps its qualifier, and a small legend sits under the table. The word inside each pill carries the meaning, so the table still reads without colour.

## 2026-10-01 (§2.7: new "Multimodal models" subsection)

**Why.** Barton asked whether the book explains multimodality with an example anywhere. It didn't. The idea appeared in about ten places, each in a line or two:
- the glossary, §1.3, §1.4
- cross-attention in §2.7 and §2.3.3
- §2.4.3, §4.8, §5.1, §5.7, §4.11

None of them explained what a modality is, how models combine several, or worked an example.

**New subsection** in §2.7, before "The common thread":
- what a modality is in UES terms: time series, attributes, fields, graphs, text
- one encoder per modality
- three ways to combine them: a shared space (CLIP), cross-attention, and one token stream (Janus)
- a worked example: forecasting one building's next-day load from meter history, register attributes and the weather forecast, with what each modality contributes
- three practical difficulties: different rates, missing modalities, and paired data
- pointers to every place the book uses the idea

**Wiring.** The §2.7 intro sentence and its Chapter 2 contents row, the glossary "Multimodality" entry (now pointing to §2.7 for the worked example), and §1.4's multimodality bullet.

**References (bib +1).** New: `radford2021clip` (arXiv API, plus the PMLR proceedings page for venue and pages). Reused: `wu2024janus`, with its claim from the arXiv abstract. The worked example is illustrative, not a cited result.
