---
title: Appendix D — Model Index
parent: Appendices
nav_order: 4
status: draft
last_reviewed: 2026-10-01
---

# Appendix D — Model Index
{: .no_toc }

{% include page-status.html %}

Every named model the notes discuss, with who built it, what it is, and where to find it. Hover over a model's name anywhere in the notes to see the same card. Each fact is taken from the model's paper or its official page; the page that discusses a model carries the full citation in its footnotes.

1. TOC
{:toc}

{% assign families = "General time series|Energy|Weather and geospatial|Vision and multimodal|Language" | split: "|" %}
{% for family in families %}
## {{ family }}

<table>
  <thead>
    <tr><th>Model</th><th>Developer</th><th>What it is</th><th>Links</th></tr>
  </thead>
  <tbody>
  {%- for m in site.data.models -%}{%- if m.family == family %}
    <tr id="{{ m.id }}">
      <td><strong>{{ m.name }}</strong>{% if m.full_name and m.full_name != m.name %}<br>{{ m.full_name }}{% endif %}</td>
      <td>{{ m.developer }}{% if m.year %}, {{ m.year }}{% endif %}</td>
      <td>{{ m.description }}</td>
      <td>{% if m.url %}<a href="{{ m.url }}">Model</a>{% endif %}{% if m.url and m.paper %} · {% endif %}{% if m.paper %}<a href="{{ m.paper }}">Paper</a>{% endif %}</td>
    </tr>
  {%- endif -%}{%- endfor %}
  </tbody>
</table>
{% endfor %}

---
[← Previous: Appendix C — Version History](c-version-history.html) · [Back to Appendices](index.html) · [Back to Home](../index.html)
