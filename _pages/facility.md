---
layout: page
title: 연구시설
permalink: /facility/
description: 연구실과 공동 연구 공간 및 장비를 소개합니다.
nav: true
nav_order: 5
---

## 연구 공간

- 지하 1층 서버 스토리지실(Server Storage Room)
- 1층 공동연구실(First-Floor Shared Lab)
- 2층 공동연구실(Second-Floor Shared Lab)
- 피부과 검체 채취실(Dermatology Specimen Collection Room)
- 분석실(Analysis Room)

## 시설 및 장비

<div class="photo-grid">
{% assign facility_files = site.static_files | where_exp: "file", "file.path contains '/assets/img/jbsm/facility-'" | sort: "path" %}
{% for file in facility_files %}
  <figure class="photo-card"><img src="{{ file.path | relative_url }}" alt="피부마이크로바이옴연구실 시설 및 장비 {{ forloop.index }}" loading="lazy"></figure>
{% endfor %}
</div>
