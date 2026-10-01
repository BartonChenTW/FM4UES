---
title: Appendix B — Pre-Project Checklist
parent: Appendices
nav_order: 2
status: draft
last_reviewed: 2026-09-11
redirect_from: /appendix-b-checklist.html
---

# Appendix B — Questions to Ask Before Starting Any Project in This Space
{: .no_toc }

{% include page-status.html %}

1. What is one training example? (D1, [§2.2](../chapter-2-fm-foundations/2-2-five-design-decisions.html))
2. **What is the [basic element](a-glossary.html#basic-element), and does it satisfy all four requirements of [§2.3.1](../chapter-2-fm-foundations/2-3-choosing-a-basic-element.html#231-the-criterion)?** If not, which one does it break, and what does that cost?
3. Where does ground truth come from, and how much can I generate?
4. What is the loop where the existing method is actually too slow?
5. What am I claiming to generalise over — and does my held-out split test exactly that?
6. **What does a representation-free baseline score, and did I run it before committing to an architecture?**
7. What physical constraints must hold, and by which mechanism ([§4.10.2](../chapter-4-directions/4-10-building-it.html#4102-enforcing-physics))?
8. What is the honest speedup, including data generation and correction?
9. What are the baselines, and have I included a domain heuristic?
10. Which rare regimes matter, and how am I guaranteeing coverage?
11. **Is this genuinely multi-task, or is it a transferable [surrogate](a-glossary.html#surrogate) being called a [foundation model](a-glossary.html#foundation-model)?** ([§2.8](../chapter-2-fm-foundations/2-8-surrogates-vs-fms.html))
12. What survives if the trained model is thrown away? (Usually: the dataset, the benchmark, the representation.)
13. Has someone already done this in power systems? *(Frequently, yes — check [§2.4.2](../chapter-2-fm-foundations/2-4-2-power-grid-fms.html) first.)*

---
[← Previous: Appendix A — Glossary](a-glossary.html) · [Next: Appendix C — Version History →](c-version-history.html) · [Back to Appendices](index.html) · [Back to Home](../index.html)
