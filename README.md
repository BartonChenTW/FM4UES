# Foundation Models for Urban Energy Systems — Working Notes

**📖 Read online: https://bartonchentw.github.io/FM4UES/**

Working notes on what gets simulated in urban energy systems, what could plausibly be
learned by a foundation model, and how to build it. Written for someone who knows urban
energy systems well and machine learning less well.

These are notes from a learning process: written while working out what foundation models could do for urban energy systems, and shared in case they help others doing the same. Every claim cites a checkable source and is open to correction, but nothing here is peer-reviewed.

**Open, community-editable notes.** Started by [Barton Chen](https://github.com/BartonChenTW)
as their initiator and current maintainer, but the intent is that anyone in the UES or FM
communities can contribute — corrections, references, new sections. Contributions go
through a pull request (fork → branch → PR); see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
the full guide.

**AI assistance.** Much of the text has been drafted and edited with Claude (Opus 5 and
Sonnet 5, Anthropic) under Barton Chen's direction and review — prompting, fact-checking
against source material, and final sign-off are his. Citations are meant to trace to real,
checkable sources (see the references workflow in `CONTRIBUTING.md`); if you spot a claim
that doesn't, please flag it via issue.

**Page views** are counted with [GoatCounter](https://fm4ues.goatcounter.com), which uses no cookies and does not track individual visitors.

**Read them as Markdown instead:** every page is a plain `.md` file in this repo, starting at
[`index.md`](index.md).

## Structure

One page per section, nested by chapter using just-the-docs' `parent:` /
`has_children:` front matter. Each chapter is a folder; each folder has an
`index.md` landing page plus one file per numbered section.

| Folder / file | Contents |
| :--- | :--- |
| `index.md` | Landing page and table of contents |
| `chapter-1-background/` | §1.1–1.4 — what a UES contains, FMs in one page, the FM landscape, why UES/why now, scope of the notes |
| `chapter-2-fm-foundations/` | §2.1–2.8 — what defines an FM, the five design decisions, **Choosing a Basic Element** (the core argument), surrogates vs FMs, existing FMs relevant to energy, ML basics (self-supervision, transformers, GNNs, neural operators), **multimodal models**, evaluation criteria for UES FMs |
| `chapter-3-sim-opt/` | §3.1–3.7 — modelling tasks and their mathematical structure, building simulation data, the energy hub formalism, dispatch and design/sizing optimisation as ML problems, the tool landscape, schemas, where cost lives, building retrofit and whole-life carbon, social dimensions (behaviour, adoption, energy poverty and justice), flexible loads (EV charging, data centres) |
| `chapter-4-directions/` | §4.1–4.9 — a neutral survey: off-the-shelf FMs, building-stock FMs, LLM agents for simulation, generative design, screening, candidate sub-fields, a proposed three-tier development path (§4.7, the one non-survey section), building it, and how the pieces could fit together as an ecosystem |
| `chapter-5-case-study/` | §5.1–5.5 — one concrete proposal: roadmap (Phases 0–5), the representation problem, data generation, a concrete representation, token schema, physics loss, module decomposition, risks |
| `chapter-6-outlook/` | §6.1–6.2 — eleven open gaps (G1–G11), how to contribute |
| `appendices/` | Glossary (A), pre-project checklist (B), version history (C), model index (D, generated from `_data/models.yml`) |
| `references/` | `fm-for-ues.bib` (Zotero import) and its README |

## Status

Version 3.3 (21 October 2026) — actively revised. Each version is a tagged
[GitHub Release](https://github.com/BartonChenTW/FM4UES/releases), summarised in
[Appendix C](appendices/c-version-history.md). Each page on the site links to its own
change history. Corrections and additions welcome via issue or pull request.

## Building locally (optional)

```bash
bundle install
bundle exec jekyll serve
```

Requires Ruby and Bundler. Not needed to publish — GitHub Pages builds and deploys the
site automatically from the `main` branch on every push.
