# Private Notes: Concept Paper and Applied Example

Private working file — excluded from the Jekyll site via `_config.yml`. This
merges two things that were previously public but are project-specific and
identifying enough that they shouldn't be on the published site:

1. The former public Appendix C (`appendix-c-buildfm-bs2027.md`) — an applied
   example of using this book's framework for a real paper submission.
2. `add/FM_for_UES.md` §7 "Concept paper structure" — working notes on
   structuring a specific concept paper (positioning, section skeleton,
   figures, venue/coalition/sequencing notes).

Kept privately because the reasoning is a useful internal reference, but the
submission specifics (venue strategy, author-list-as-argument comments,
double-blind handling) are not meant for the public textbook.

---

## Part 1 — Applied Example: BS2027 Submission (formerly public Appendix C)

This section is a **redacted** version of internal working notes for a
specific paper submission. Author names, internal sign-off status, and
details of an unannounced position at the originating lab have been removed
in this version (they were already redacted in the version that was public).

### Context

The example below concerns a paper submission to an academic venue in
building simulation, in the "Simulation Methods & Emerging Tools" category.
Two-stage process: a short abstract first, then a full paper of limited
length under double-blind review.

**Double-blind handling used throughout:** no institution names; a named
experimental demonstrator building described generically; simulation and
optimisation tools may be named since they are public software, but
combinations of named tools can still be identifying, so this is decided
case by case; self-citations in third person; acknowledgments and funding
stripped from the review version.

### Paper scope as agreed

Framed as a **review and position paper**, not an empirical results paper,
for three reasons that generalise beyond this specific submission:

1. **Budget and timeline honesty.** Per the book's §4.10.4 and §4.10.4.1
   (realistic budget expectations, publication format), a trained and
   validated foundation model was not going to exist by the paper deadline.
   Promising one in the abstract and under-delivering in the paper is worse
   than scoping correctly from the start.
2. **Where the actual contribution lives.** The representation argument —
   the book's §2.3 (Choosing a Basic Element) — is finished thinking,
   independent of any training run. It does not depend on compute that
   hadn't happened yet.
3. **Graceful degradation.** An anchored position paper (argument-led, with
   one demonstrative empirical result) stands on its own if further
   experiments slip, and gets stronger without restructuring if they don't.

Scope, concretely: (1) why a foundation model for this sub-domain is needed,
(2) a review of existing modelling approaches and foundation models
organised **by basic element** rather than by tool family or publication
date, so the representation gap is visible before the reader reaches the
proposal, (3) candidate directions and open questions.

### What was reused from prior internal material, and what was new

A short internal concept note existed before this paper was scoped,
describing a proposed system by name, its motivation, and its planned use of
existing simulation and optimisation tools. Reusable from it: the motivation
chain (why a foundation model for this domain is timely), the framing of the
domain as spanning multiple coupled scales, and the description of how
physics-based simulation and optimisation tools would generate training
data.

Not reusable, and rewritten: institutional-capability language became method
justification; a "rapid decision support" framing became an
amortised-inference claim requiring a stated speedup and accuracy trade-off;
a budget table, team roster, and month-numbered work-package schedule were
dropped entirely, since none of these belong in a paper.

New, and the actual contribution of the paper: the representation argument
in full — the four-requirement criterion, the building-level analysis, the
representation strategies, and the falsifiable predictions (now the book's
§2.3).

**A framing shift worth naming explicitly in any similar situation:** an
internal proposal document typically frames a system as something to be
*built*. A paper reframes it as an investigation of whether the
representation makes it *possible*. Same underlying project, same data, same
tools — a materially different claim. Anyone who signed off on the original
proposal framing should see the paper framing before submission, since it is
not simply a shorter version of the same argument.

### Language and audience translation

The target reviewer pool has building simulation expertise and little or no
machine learning background. Every ML concept in the paper is introduced
through its domain counterpart — tokenisation as a discretisation choice
(the book's §2.3.1 does this directly) — with a short glossary for anything
unavoidable. Vocabulary discipline applied throughout: "basic element"
rather than "token," "carries over" rather than "transfers," "fitted" rather
than "trained," wherever the substitution didn't cost precision.

The single most effective persuasive device available for this audience was
the thermal-zone example in §2.3.2(b): zoning ambiguity is a debate the
building simulation community has already lived, rather than an abstraction
imported from machine learning. Leading with material the audience already
believes, rather than material they must take on trust, did more work than
any amount of careful definition.

### A related open question worth flagging generally

At the time of writing, the originating lab was also hiring for a position
on **tabular foundation models** for building and district energy systems —
a specific and different answer to the same representation question this
paper addresses (see the book's §2.4.4). Where a project and a new hire's
brief overlap this closely, the generalisable lesson is to define the
division of labour *before* the position is filled rather than after: for
instance, one thread taking tabular/structured representation and another
taking sequence/profile-level representation, compared later on a shared
benchmark rather than either duplicating the other's work or working around
it informally.

### Open decisions carried forward

- Whether to release a benchmark (tasks, held-out splits, baseline results)
  alongside the paper. Per gap G4 (book's §6.1), this is the cheapest
  available upgrade to a position paper — it converts an argument into
  infrastructure the field can reuse, and it is the artifact most likely to
  outlive the paper itself.
- Whether specific named tools, in combination, are identifying enough under
  double-blind review to require genericising rather than naming — a
  judgment call that has to be made per venue and per co-author group, not
  answered generically here.

---

## Part 2 — Concept Paper Structure (formerly `add/FM_for_UES.md` §7)

### 2.1 The positioning problem

The Joule GridFM perspective (Hamann, Gjorgiev, Brunschwiler et al., 2024)
already argues: energy transition creates a computational gap → FMs have
properties that close gaps → roadmap for GridFM-v0 → downstream uses → call
to action. Reviewers in this community have read it. A paper that is "the
same argument for urban energy systems" reads as derivative regardless of
how new the sentences are.

**Recommended central claim:**

> The obstacle to a foundation model for urban energy systems is not
> compute, data volume, or architecture. It is that the domain has no
> tokenization. This paper proposes one, and shows what becomes possible
> once it exists.

The GridFM paper structurally could not make this claim, because power
systems already had MATPOWER and the bus abstraction. The claim is
genuinely unsolved and positions the work as complementary rather than an
echo.

### 2.2 Section skeleton

| Section | Length | Function |
|---|---|---|
| Title + Summary | ~150 w | Name the model class and commit to it |
| Context & Scale | ~200 w | Editor-facing: why this matters beyond specialists |
| 1. Introduction | 1–1.5 pp | Thesis, contributions, roadmap of the paper |
| 2. The urban energy system and its computational limits | 2–3 pp | The gap, framed by *what questions cannot be asked today* |
| 3. Why FMs, and why not | 2–3 pp | Honest capability assessment including failure modes |
| 4. **The representation problem** | 3–4 pp | Core contribution |
| 5. Pretraining tasks and module decomposition | 2–3 pp | The self-supervision suite |
| 6. Downstream tasks and a benchmark proposal | 2 pp | What the model is evaluated on |
| 7. Roadmap | 2–3 pp | Phased, with kill criteria |
| 8. Coupling to adjacent FMs | 1–2 pp | GridFM handshake, load FMs, geospatial FMs |
| 9. Barriers | 1.5 pp | Data, privacy, trust, validation, misuse |
| 10. Call to action | 0.5 pp | Concrete asks, not vague enthusiasm |

Total 20–30 pages, typical for this genre.

### 2.3 Notes on the load-bearing sections

**Section 2 — frame the gap as unanswerable questions, not slowness.**
"MILP is slow" invites "buy a better solver." Instead: design a district
under 500 climate-and-price scenarios; evaluate reliability criteria at
city scale; co-optimise a hundred hubs against a distribution grid; explore
policy-lever space rather than capacity space. Each is a question, not a
speedup, and each maps to a roadmap phase.

**Section 3 — put limitations in the middle, not the end.** Say plainly
that FMs cannot replace the optimisation problem: objective degeneracy,
dual variables needed for regulation, inter-temporal coupling, and discrete
decisions all remain. Then argue FMs can *amortise* the solve and *enable*
uncertainty and reliability work. A concept paper that admits its
boundaries is read as serious.

**Section 4 — this is the paper.** Most space, best figure. Bipartite
structure, typed multi-port devices, carrier-quality dimension,
hierarchical temporal tokenization, physics-loss inventory, and an explicit
worked example. (This content now lives publicly in the book's Part 5.)

**Section 6 — propose the benchmark and name it.** Communities coalesce
around benchmarks more reliably than around models (PGLIB-OPF,
EnergyBench). It also gives other groups something to do that is not
competing with you.

**Section 7 — include failure criteria.** State that if Phase 1 surrogates
do not beat a tuned reduced-order model on held-out topologies by year two,
the premise is wrong. Almost no concept paper does this; it costs nothing
and buys credibility.

### 2.4 Figures

Budget five or six — in this genre figures carry more argumentative weight
than text.

1. The computational gap: questions against tractable scale
2. The representation: a district as bipartite graph, annotated with token
   feature vectors
3. Carrier quality levels and permitted conversions
4. Pretraining task suite, masking illustrated on the graph
5. Roadmap phases with deliverables and go/no-go gates
6. FM ecosystem: hub FM relative to GridFM, load FMs, geospatial FMs

### 2.5 Practical notes

- **Venue.** Joule Perspective is the obvious target given precedent, but
  it is the same venue as the paper being differentiated from. Applied
  Energy, Advances in Applied Energy, or Nature Energy Perspective are
  alternatives. A preprint early is worth more than perfect placement —
  concept papers work by being cited into existence.
- **Coalition.** The GridFM paper carries roughly forty authors across IBM,
  ETH, Argonne, NREL, Hydro-Québec, and INESC TEC. That author list *is*
  part of the argument. Decide early whether this is a single-institution
  position paper or a coalition paper; the second is slower and much
  stronger.
- **Sequencing.** The commonest failure of concept papers is being all
  promise. Even a small empirical result — a hub tokenization pretrained on
  a few thousand synthetic scenarios with a zero-shot transfer number —
  turns a manifesto into a manifesto with evidence.

---

*Compiled from working conversations. Nothing here is peer-reviewed; the
numbered risks, unresolved questions, and venue/coalition notes are the
parts most likely to change or go stale.*

---

## Publication format (moved from §4.10.4, 2026-10-03)

Moved here from the public §4.10 because it is paper-writing strategy rather than a survey of how to build a model.

### Publication format follows from the budget (original text)

The same logic applies to papers. For a novel concept with limited empirical results, three formats are available:

- **Pure empirical** — a benchmark, a baseline, a measurement. Safe with reviewers; low ceiling. Competent and rarely cited.
- **Pure concept / position** — argument only. High ceiling, but at an engineering venue it reads as a proposal unless it does real analytical work: a criterion others can apply, a taxonomy with consequences, falsifiable predictions, a benchmark specification.
- **Anchored concept paper (recommended)** — argument-led, with one demonstrative empirical result. Roughly three-quarters argument, one-quarter evidence. The argument carries the paper; a single result converts the central claim from assertion to demonstration.

The anchored format matches the budget reality above: it does not depend on a trained model existing by the deadline, and it fails gracefully — if training slips, the paper still stands; if it succeeds, a results subsection is added without restructuring.

**Audience translation is part of the format choice.** Writing FM concepts for a domain audience means introducing every ML idea through its domain counterpart ([§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion) does this with discretisation), avoiding unexplained vocabulary, and including a short glossary. The test: if a paragraph requires ML background to parse, rewrite it.
