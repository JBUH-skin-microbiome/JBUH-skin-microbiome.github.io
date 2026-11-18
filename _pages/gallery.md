---
layout: page
title: 갤러리
permalink: /gallery/
description: 연구실의 학술 활동과 구성원들의 기록입니다.
nav: true
nav_order: 4
---

## 2026

- 대한피부연구학회(KSID × ISID APAC) — 2026.04.11
- 세계모발학회(WCHR) — 2026.05.28
- IHMC — 2026.06.03
- 대한피부진균및감염학회 — 2026.06.27
- 김병지·박윤환 학생 졸업 — 2026.08.21
- 개교 55주년 우수연구상 — 2026.09.18

## 2025

- JBNU Research Fair — 2025.02.19
- Welcome party for Trang — 2025.04.04
- 박하은 선생님 송별회 — 2025.07.01
- Start-up Program Workshop — 2025.07.03
- 마이크로바이옴 R&D 사업 중간 성과 교류회 — 2025.08.26
- 대한피부진균및감염학회 — 2025.11.01

## 2024

- 최가영 선생님 송별회 — 2024.02.22
- 대한피부연구학회(KSID) — 2024.03.23
- Joint Meeting(약학대학) — 2024.04.02
- 최태림 학생 송별회 — 2024.07.23
- 김소연 학생 석사 졸업 — 2024.08.26
- 대한피부진균및감염학회 — 2024.11.02
- APSMM(Kyoto) — 2024.11.06

## 2023

- 단체 사진 촬영
- ISID 학회 참석 — 2023.05.10–13

<div class="photo-grid">
{% assign gallery_files = site.static_files | where_exp: "file", "file.path contains '/assets/img/jbsm/gallery-asset-'" | sort: "path" %}
{% for file in gallery_files %}
  <figure class="photo-card"><img src="{{ file.path | relative_url }}" alt="피부마이크로바이옴연구실 갤러리 사진 {{ forloop.index }}" loading="lazy"></figure>
{% endfor %}
</div>
