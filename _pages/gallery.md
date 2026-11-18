---
layout: page
title: Gallery
permalink: /gallery/
description: 연구실의 학술 활동과 구성원들의 기록입니다.
nav: true
nav_order: 4
---

<nav class="year-jump" aria-label="갤러리 연도 목차">
  {% assign gallery_years = "2026,2025,2024,2023" | split: "," %}
  {% for year in gallery_years %}<a href="#year-{{ year }}">{{ year }}</a>{% endfor %}
</nav>

{% assign gallery_projects = site.projects | where: "kind", "gallery" | sort: "order" %}
<div class="collection-landing projects">
  {% for year in gallery_years %}
    <section class="collection-year" id="year-{{ year }}">
      <h2>{{ year }}</h2>
      <div class="grid">
        {% for project in gallery_projects %}
          {% assign project_year = project.year | append: "" %}
          {% if project_year == year %}{% include projects.liquid %}{% endif %}
        {% endfor %}
      </div>
    </section>
  {% endfor %}
</div>
