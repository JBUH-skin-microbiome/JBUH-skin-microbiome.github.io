---
layout: page
title: 인턴십
permalink: /internship/
description: JBSM 인턴십의 교육 과정과 프로젝트를 안내합니다.
nav: true
nav_order: 6
---

## 3개월 교육 과정

1. **1개월 차:** R, 기초 통계분석, 생물정보학 기초
2. **2개월 차:** Microbiome, QIIME 2, DADA2
3. **3개월 차:** 데이터 분석, Git·GitHub

### 세부 교육 내용

- R 기초 및 R 통계분석
- 생물정보학과 시퀀싱
- Human microbiome과 skin microbiome
- Microbiome analysis
- Linux 기초 및 quality control
- QIIME 2 tutorial
- BLAST
- DADA2 tutorial
- Git·GitHub

<div class="photo-grid">
{% assign internship_files = site.static_files | where_exp: "file", "file.path contains '/assets/img/jbsm/jbsm-internship-'" | sort: "path" %}
{% for file in internship_files %}<figure class="photo-card"><img src="{{ file.path | relative_url }}" alt="JBSM 인턴십 교육 자료 {{ forloop.index }}" loading="lazy"></figure>{% endfor %}
</div>

## 인턴 프로젝트

1. R 환경에서 피부 마이크로바이옴 데이터 기초 분석 수행(DADA2)
2. Linux 환경에서 마이크로바이옴 분석 수행(QIIME)
3. BLAST 도구 결과와 QIIME 분석 결과 비교
4. R 환경에서 alpha·beta 다양성, 계통 조성 분석 및 시각화
5. PICRUSt2를 활용한 기능 예측 및 군 간 비교
6. ALDEx2 및 ANCOM-BC2를 이용한 differential abundance analysis
7. 네트워크 분석을 통한 통합적 이해

## 수행 과제

- Alpha diversity의 군 간 평균과 95% 신뢰구간을 R로 정리
- Beta diversity에서 PERMANOVA를 이용한 통계분석
- Taxonomy 결과에서 평균 relative abundance 1% 이상인 genus 정리
- ALDEx2와 ANCOM-BC2를 이용해 군 간 marker microbiome 확인
- 네트워크 분석에서 군 간 hub(keystone) 확인
