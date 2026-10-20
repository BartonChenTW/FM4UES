# Brainstorming Better Diagrams

Private planning file — excluded from the Jekyll site via `_config.yml`.

**The problem, per Barton (2026-09-12):** the chapter-landing diagrams added on 2026-09-11 aren't very helpful. Looking at them again, the issue is specific: every one of them is a **flowchart of the table of contents** — boxes holding a section number and title, connected by arrows that mostly just mean "comes after" or "is a sub-page of." That's the same information the sidebar nav and the "In this chapter" table on the same page already give, in a form that's harder to read, not easier. A diagram earns its place when it shows something a sentence can't — a mechanism, a structure, a comparison, a transformation — not when it re-draws a table of contents as boxes and arrows.

This file goes through each existing diagram, says concretely what's weak about it, and proposes what a genuinely useful diagram in that spot could show instead. Nothing here is committed — it's a menu to pick from, edit, or reject.

---

## Fix already applied

`chapter-4-directions/index.md`'s diagram had wrong section numbers (`4.9 Screening`, `4.10 Candidate sub-fields`, `4.11 Methods`, `4.12 Building it` — the real numbers are §4.5–4.6, §4.6, §4.7, §4.8). Corrected 2026-09-12 as a quick fix, independent of the redesign question below.

---

## Existing diagrams, one by one

### `chapter-1-background/index.md` (TOC flowchart)

**What it shows now:** five section boxes all funnelling into "1.5 Why UES, why now," then into "1.6 Scope." Pure sequence, no content.

**What Chapter 1 is actually about:** why two fields that don't currently talk to each other (UES and FMs) might. The one real idea in this chapter is the **cost-structure contrast** between a bespoke model (built once, thrown away) and a foundation model (built once, reused across many studies) — that's the argument for the whole book.

**Better diagram idea:** a simple before/after or cost-over-time comparison — two lines or bars: "bespoke surrogate: cost per study, N studies → N × cost" vs. "foundation model: one upfront cost, amortised across N studies → cost per study falls with N." This is the same idea developed in prose in §1.2 and formalised in §3.3/§2.1 — a small chart here would preview it, not duplicate it.

### `chapter-2-fm-foundations/index.md` (TOC flowchart)

**What it shows now:** eight section boxes, mostly "feeds into §2.2," which isn't really true structurally — §2.5/§2.6/§2.1 are background the reader needs before §2.2–§2.4 make sense, not tributaries of §2.2 specifically.

**What Chapter 2 is actually about:** the five design decisions (§2.2) that define any FM, and §2.3's criterion for judging whether a domain has a viable "basic element." The chapter's actual shape is **prerequisite knowledge (§2.5–2.1) → the five decisions (§2.2) → the hardest decision in depth (§2.3) → survey of who's solved it so far (§2.4) → who hasn't (§2.4)**.

**Better diagram idea:** the five design decisions themselves, as a small pipeline (Unit of observation → Tokenisation → Architecture → Pretraining objective → Evaluation), since that's the chapter's actual organising idea and recurs at every tier in Chapters 4–5. A reader who internalises this one diagram has the chapter's real content, not just its section order.

### `chapter-3-sim-opt/index.md` (TOC flowchart)

**What it shows now:** eight boxes with genuine dependency arrows (this one is slightly better than the others — A→B, A→C etc. reflect real prerequisite structure). Still just architecture-of-the-chapter, not architecture-of-the-domain.

**What Chapter 3 is actually about:** what gets modelled in a UES and at what computational cost — the "where does the cost live" question that motivates using a learned model at all.

**Better diagram idea:** the actual UES modelling stack — building-level simulation → energy hub / multi-carrier coupling → dispatch optimisation → design/sizing optimisation — labelled with which one is expensive and why (e.g. MILP solve time growing combinatorially with device count, or simulation runs needed per design iteration). This is a domain diagram, not a book-structure diagram, and it's the one picture that would let a UES reader instantly place where their own work sits.

### `chapter-4-directions/index.md` (TOC flowchart)

**What it shows now:** eleven boxes funnelling toward "building it," now number-corrected but still just sequence.

**What Chapter 4 is actually about:** a *screening decision* — which sub-fields of UES pass a test for being FM-ready, and which don't yet. That's a genuinely visual idea: a 2×2 or funnel, not a flowchart.

**Better diagram idea:** the screening funnel itself — start with "all UES sub-fields," apply the five-criterion screen (§4.5), end with a short list of survivors (§4.6's candidates) plotted against "not yet FM-ready." Or: a 2×2 grid (data availability × basic-element clarity) with the actual candidate sub-fields placed as points — this is literally what §4.5–4.6 argue in prose and would make the chapter's verdict visible at a glance.

### `chapter-5-case-study/index.md` (TOC flowchart)

**What it shows now:** eight boxes with some real dependency structure (representation → data generation / concrete representation → token schema → physics loss / module decomposition → roadmap → risks).

**What Chapter 5 is actually about:** one worked example of applying a representation to a real system. The single most concrete, most visual idea in the whole book is the **50-building district worked example in §5.3** — 30 carrier-buses, ~40 devices, bipartite graph structure.

**Better diagram idea:** promote the bipartite graph example itself to the chapter-landing page (even a simplified version — a handful of building nodes, a handful of carrier-bus nodes, edges between them) instead of a TOC flowchart. That one picture *is* the chapter's argument: "here is what a multi-carrier energy hub looks like as a graph a model could learn from." Currently this exists only deep in §5.3's prose.

### `chapter-4-directions/4-9-methods-landing.md` (Tier 1→2→3 progression)

**What it shows now:** three boxes in a line — "Tier 1 → Tier 2 → Tier 3" with one-line labels. This is honestly fine as far as it goes, but it says only "these get harder," which the reader already knows from the section titles.

**Better diagram idea:** the same three-box shape, but each box annotated with *what actually changes* between tiers — the dimension that increases (e.g. Tier 1: single hub / fixed topology → Tier 2: N hubs / graph topology → Tier 3: continuous dispatch → discrete design decisions). That's the real content of §4.7's three sub-pages, compressed into one picture instead of three separate reads.

### `chapter-5-case-study/5-1-roadmap.md` (Phase 0→5 timeline)

**What it shows now:** six boxes, Phase 0 through Phase 5, each with a year range and a one-line label. This is a genuinely reasonable use of a diagram — it's a timeline, timelines are diagrams, and the labels are specific rather than generic ("Phase 3: Amortised optimisation" is real content, not a section title).

**Verdict: keep, probably improve rather than replace.** Possible upgrade: add a second row showing what's *validated* vs. *aspirational* at each phase (per the risks in §5.5), so the diagram also communicates confidence, not just sequence.

### `chapter-5-case-study/5-5-token-schema.md` (L0/L1/L2 temporal hierarchy)

**What it shows now:** three nested levels (hourly → sparse day tokens → annual token), with real structural content — attention density, sparsity pattern. This is the best diagram in the book so far: it shows a genuine architectural idea (a temporal hierarchy that avoids the 8760-timestep-per-year problem) that would take several sentences to convey otherwise.

**Verdict: keep as-is.** This is the model for what the others should aim for — it shows *how something works*, not *what order to read things in*.

---

## The general pattern

Diagrams that work in this book so far (§5.3, arguably §5.1) share a trait: they show a **mechanism or structure specific to this book's argument** — something that would take a paragraph to explain in prose and is genuinely clearer as a picture. Diagrams that don't work (all six chapter-landing pages) share the opposite trait: they could be regenerated automatically from the front-matter `parent:`/`nav_order:` fields, because that's all the information they actually encode.

**Proposed rule going forward:** before adding a diagram, ask "does the sidebar nav plus the 'In this chapter' table already tell the reader this?" If yes, don't add a flowchart — add nothing, or replace it with a diagram of the chapter's actual central idea instead.

## Candidate replacement priority (if picking a few to redo first)

1. **Chapter 4 landing** — the screening funnel/2×2, since this is the chapter whose entire point is a decision, and a decision diagram is the most natural fit of anywhere in the book.
2. **Chapter 5 landing** — promote the bipartite graph worked example; this is sitting right there in §5.3 already, just needs pulling forward and simplifying.
3. **Chapter 3 landing** — the UES modelling-stack-with-cost diagram, since "where does the cost live" is the chapter's actual thesis and currently has no picture anywhere.
4. **Chapter 2 landing** — the five-design-decisions pipeline, since it recurs as a framework throughout Chapters 4–5 and deserves to be memorable.
5. **Chapter 1 landing** — the amortisation cost-over-time comparison, lowest priority since it's a fairly simple idea that prose already conveys reasonably well.

Tier-progression (§4.7 landing) is a smaller touch-up (add the "what changes" annotation) rather than a full redo.
