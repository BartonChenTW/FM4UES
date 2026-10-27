---
title: Appendix E — Research Institutes
parent: Appendices
nav_order: 5
status: draft
last_reviewed: 2026-10-27
---

# Appendix E — Research Institutes
{: .no_toc }

{% include page-status.html %}

The universities, research institutes and companies behind the foundation-model work these notes cite. The list starts from the authors of each publication, not from a survey of the field. An institution is here because at least one of its researchers co-authored a cited paper that builds, pretrains, adapts or evaluates a [foundation model](a-glossary.html#foundation-model), LLMs and LLM agents included. An institution that works on foundation models but has no paper cited in the notes is not listed.

{% assign uni = site.data.institutes | where: "sector", "University" %}
{% assign ri = site.data.institutes | where: "sector", "Research institute" %}
{% assign co = site.data.institutes | where: "sector", "Company" %}
**{{ site.data.institutes | size }} institutions** from 137 publications: {{ uni | size }} universities, {{ ri | size }} research institutes and public bodies, and {{ co | size }} companies. Most are in the United States (74 institutions), China (30), Germany (16) and the United Kingdom (12).

How the list was compiled:

- **Affiliations** come from each paper's [OpenAlex](https://openalex.org/) record, checked against the affiliation printed in the paper. Where OpenAlex had none, mostly for arXiv preprints, they were read from the paper's title page. For a model card or README with no author list, the institution is the developer it names.
- **Institutions are counted at organisation level.** Departments, campuses and national branches are merged, so IBM Research in Zurich, Dublin, Bangalore and Yorktown Heights is one row, with each country listed.
- **Three papers are left out** because no affiliation could be verified from the paper itself: Shirzadi et al. (2026) and Ball et al. (2026), whose publisher pages could not be read and which have no preprint, and Wang (2026), which states no affiliation.
- **Each paper links to the page that cites it.** Hover over a link to see the paper's title. Model names link the same way; the model itself is described in [Appendix D](d-model-index.html).

Within each table, institutions are sorted by the number of cited papers. The count measures how much of an institution's work these notes happen to cite, not how much foundation-model work it does.

1. TOC
{:toc}

{% assign sectors = "University|Research institute|Company" | split: "|" %}
{% assign headings = "Universities|Research institutes and public bodies|Companies and industry labs" | split: "|" %}
{% for sector in sectors %}
## {{ headings[forloop.index0] }}

<table>
  <thead>
    <tr><th>Institution</th><th>Country</th><th>Papers</th><th>Cited work</th></tr>
  </thead>
  <tbody>
  {%- for i in site.data.institutes -%}{%- if i.sector == sector %}
    <tr>
      <td><strong>{{ i.name }}</strong></td>
      <td>{{ i.countries }}</td>
      <td>{{ i.papers | size }}</td>
      <td>{% for p in i.papers %}<a href="../{{ p.page }}#fn:{{ p.key }}" title="{{ p.title | escape }}">{{ p.label }}</a>{% unless forloop.last %} · {% endunless %}{% endfor %}</td>
    </tr>
  {%- endif -%}{%- endfor %}
  </tbody>
</table>
{% endfor %}

---
[← Previous: Appendix D — Model Index](d-model-index.html) · [Back to Appendices](index.html) · [Back to Home](../index.html)
