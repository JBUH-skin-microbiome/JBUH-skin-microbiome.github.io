---
layout: page
title: Facility
permalink: /facility/
description: 연구실과 공동 연구 공간 및 장비를 소개합니다.
nav: true
nav_order: 5
---

<div class="facility-list">
{% for facility in site.data.facility %}
  <section class="facility-card">
    <header><p>Research Space {{ forloop.index | prepend: '0' }}</p><h2>{{ facility.title }}</h2><span>{{ facility.title_en }}</span></header>
    <div class="facility-images">
    {% for image in facility.images %}<img src="{{ '/assets/img/jbsm/' | append: image | relative_url }}" alt="{{ facility.title }} 사진 {{ forloop.index }}" loading="lazy">{% endfor %}
    </div>
  </section>
{% endfor %}
</div>

<section class="equipment-note"><h2>Equipment List</h2><p>각 연구 공간의 시설 및 장비 사진을 공간 이름과 함께 확인할 수 있습니다.</p></section>
