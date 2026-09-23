# Foundation Models for Urban Energy Systems — A Working Textbook

**📖 Read it here: https://bartonchentw.github.io/FM4UES/**

A working textbook on what gets simulated in urban energy systems, what could plausibly be
learned by a foundation model, and how to build it. Written for someone who knows urban
energy systems well and machine learning less well.

**An open, community-editable textbook.** Started by [Barton Chen](https://github.com/BartonChenTW)
as its initiator and current maintainer, but the intent is that anyone in the UES or FM
communities can contribute — corrections, references, new sections. Contributions go
through a pull request (fork → branch → PR); see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
the full guide.

**AI assistance.** Much of the text has been drafted and edited with Claude (Opus 5 and
Sonnet 5, Anthropic) under Barton Chen's direction and review — prompting, fact-checking
against source material, and final sign-off are his. Citations are meant to trace to real,
checkable sources (see the references workflow in `CONTRIBUTING.md`); if you spot a claim
that doesn't, please flag it via issue.

**Read it as Markdown instead:** every page is a plain `.md` file in this repo, starting at
[`index.md`](index.md).

## Structure

One page per section, nested by chapter using just-the-docs' `parent:` /
`has_children:` front matter. Each chapter is a folder; each folder has an
`index.md` landing page plus one file per numbered section.

| Folder / file | Contents |
| :--- | :--- |
| `index.md` | Landing page and table of contents |
| `chapter-1-background/` | §1.1–1.6 — what a UES contains, FMs in one page, the FM landscape, why UES/why now, scope of the book |
| `chapter-2-fm-foundations/` | §2.1–2.9 — what defines an FM, the five design decisions, **Choosing a Basic Element** (the core argument), existing FMs relevant to energy, ML basics (self-supervision, transformers, GNNs, neural operators), surrogates vs FMs, evaluation criteria for UES FMs |
| `chapter-3-sim-opt/` | §3.1–3.8 — task taxonomy, building simulation data, the energy hub formalism, dispatch and design/sizing optimisation as ML problems, the tool landscape, schemas, where cost lives |
| `chapter-4-directions/` | §4.1–4.10 — a neutral survey: off-the-shelf FMs, building-stock FMs, LLM agents for simulation, generative design, screening, candidate sub-fields, methods by problem tier (Tier 1–3), building it |
| `chapter-5-case-study/` | §5.1–5.8 — one concrete proposal: roadmap (Phases 0–5), the representation problem, data generation, a concrete representation, token schema, physics loss, module decomposition, risks |
| `chapter-6-outlook/` | §6.1–6.2 — nine open gaps (G1–G9), how to contribute |
| `appendices/` | Glossary (A), pre-project checklist (B) |
| `references/` | `fm-for-ues.bib` (Zotero import) and its README |

## Status

Version 2.0 — actively revised. Corrections and additions welcome via issue or pull request.

## Building locally (optional)

```bash
bundle install
bundle exec jekyll serve
```

Requires Ruby and Bundler. Not needed to publish — GitHub Pages builds and deploys the
site automatically from the `main` branch on every push.
