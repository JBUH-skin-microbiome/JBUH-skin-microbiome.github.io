---
layout: page
title: Gallery
permalink: /gallery/
description: 연구실의 학술 활동과 구성원들의 기록입니다.
nav: true
nav_order: 4
---

<nav class="year-jump" aria-label="갤러리 연도 목차">
  {% for year_group in site.data.gallery %}<a href="#year-{{ year_group.year }}">{{ year_group.year }}</a>{% endfor %}
</nav>

<div class="gallery-portfolio">
{% for year_group in site.data.gallery %}
  <section class="gallery-year" id="year-{{ year_group.year }}">
    <h2>{{ year_group.year }}</h2>
    <div class="event-grid">
    {% for event in year_group.events %}
      <article class="event-card">
        <header><p>{{ event.date }}</p><h3>{{ event.title }}</h3></header>
        <div class="event-images event-images-{{ event.images.size }}">
        {% for image in event.images %}
          <img src="{{ '/assets/img/jbsm/' | append: image | relative_url }}" alt="{{ event.title }} 사진 {{ forloop.index }}" loading="lazy">
        {% endfor %}
        </div>
      </article>
    {% endfor %}
    </div>
  </section>
{% endfor %}
</div>
