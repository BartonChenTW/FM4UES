# Contributing

📖 Read the book: **https://bartonchentw.github.io/FM4UES/**

This is a living, open-contribution knowledge base — started by
[Barton Chen](https://github.com/BartonChenTW), but corrections, references,
and new sections are welcome from anyone in the urban energy systems (UES)
or foundation model (FM) communities.

Much of the existing text was drafted and edited with Claude (Opus 5 and
Sonnet 5, Anthropic) under Barton's direction and review. That doesn't
change what's expected of new contributions: claims should trace to a real,
checkable source (see the references workflow below), whether written by a
person, drafted with AI assistance, or both.

## How changes get in

`main` is protected — nobody, including the maintainer, pushes to it
directly. Every change goes through a pull request:

1. **Fork** this repo (or, if you've been added as a collaborator, create a
   branch directly).
2. Make your change on a branch.
3. Open a **pull request** against `main`. The `lychee` link-check workflow
   runs automatically; it needs to pass before the PR can merge.
4. The maintainer (or another reviewer, once there are some) reviews and
   merges.

For small fixes (typos, a broken link) this whole cycle can be quick —
GitHub's web editor can create the fork, branch, and PR for you in one go
from the file's "Edit" (pencil) button.

## Ways to contribute

- **Report an error or an outdated claim** — open an issue.
- **Suggest a reference** — open an issue with the citation (a DOI or URL is
  enough) and a one-line note on which section it belongs to. See
  [references/](references/) for how the bibliography is organised.
- **Propose a new section or restructuring** — open an issue first to
  discuss scope before writing, since this book has an explicit outline
  (chapters are numbered and cross-referenced).
- **Fix a typo or small wording issue** — a pull request directly is fine,
  no need to open an issue first.
- **Larger additions** (a new chapter, a reworked argument) — open an issue
  to discuss before investing time in a draft.

## Style notes

- Written for a reader who knows urban energy systems well and machine
  learning less well (or vice versa) — define jargon on first use, or link
  to [`appendices/a-glossary.md`](appendices/a-glossary.md).
- Cite claims. See the references workflow below.
- British English spelling, matching the existing text (e.g. "optimisation",
  "modelling").
- Each page has Jekyll front matter (`title`, `parent`, `nav_order`, and for
  section pages also `status` and `last_reviewed`, rendered via
  `{% include page-status.html %}`). Match the existing pattern when adding
  a page — see any section file for the format. Chapters are folders with
  an `index.md` (`has_children: true`) and one file per numbered section
  (`parent:` pointing back to the chapter's title).

## References workflow

References are tracked in Zotero and exported as BibTeX to
[`references/`](references/) for import by others. In the text, cite using
Markdown footnotes:

```markdown
Pretrained time-series models can forecast zero-shot.[^ansari2024chronos]

[^ansari2024chronos]: Ansari, A. F., Stella, L., Turkmen, C. et al. (2024).
  [Chronos: Learning the language of time series](https://arxiv.org/abs/2403.07815).
  *Transactions on Machine Learning Research*. arXiv:2403.07815.
```

Use the same citation key as the `.bib` entry (e.g. `ansari2024chronos`,
following the `firstauthorYEARshortname` pattern in
[`references/README.md`](references/README.md)) as the
footnote name, so the two stay traceable to each other.

**Do not add a reference to the bibliography alone.** A `.bib` entry with
no corresponding claim in the text adds nothing a reader can use. Every
reference should be attached to a specific statement that makes three
things explicit:

1. **What the work demonstrated** — the concrete result, not just the topic.
2. **What limitation remains** — the boundary of what it establishes.
3. **How that limitation bears on urban energy systems** — why the gap
   matters here, ideally cross-linked to the section that takes it up.

The second and third points are the ones most often skipped, and they are
what make a citation load-bearing rather than decorative. A reference that
only supports "work exists in this area" is usually better merged into an
existing sentence than given one of its own.

### Every identifier must resolve

Look each source up before citing it. Do not reconstruct a citation from
memory, and do not infer a DOI or arXiv ID from a pattern — a plausible
identifier that points at the wrong paper is worse than no identifier,
because it survives a skim. Both failures have reached this repo already:
a citation with a real author but an invented title and venue, and an
arXiv ID belonging to an entirely unrelated paper.

- Check the DOI resolves (`https://api.crossref.org/works/<DOI>` returns
  the paper you mean) or the arXiv abstract page shows the title and
  authors you are citing.
- If you cannot verify a source, write `[citation needed — could not
  verify]` in the text and say so in the pull request. That is an
  acceptable contribution; a fabricated identifier is not.
- Prefer the primary source over a survey. Surveys are right for
  landscape claims, not for specific results.
- One citation per claim. Stacking references does not add rigour.

### Small and verified beats large and plausible

A short, well-sourced improvement is more useful here than a broad
rewrite. If you are editing an existing section, prefer one kind of change
per pull request — repair something broken, add a citation to an unsourced
claim, sharpen an imprecise statement, or fill one visible gap — and keep
existing cross-references intact.

Saying what you considered and **rejected**, and why, is welcome in the
pull request description. It shows restraint and gives the maintainer a
backlog.

## Local build

```bash
bundle install
bundle exec jekyll serve
```

Requires Ruby and Bundler. Not required just to read or edit the Markdown —
only for previewing how a change renders on the site.

## Questions

Open an issue, or see [`TODO.md`](TODO.md) if you're wondering what's
already planned.
