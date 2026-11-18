---
layout: page
title: Facility
permalink: /facility/
description: 연구실과 공동 연구 공간 및 장비를 소개합니다.
nav: false
nav_order: 5
---

{% assign facility_projects = site.projects | where: "kind", "facility" | sort: "order" %}
<div class="collection-landing projects facility-projects">
  <div class="grid">
    {% for project in facility_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
