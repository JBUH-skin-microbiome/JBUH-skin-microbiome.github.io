---
layout: page
title: 구성원
permalink: /members/
description: 피부마이크로바이옴연구실의 교수진, 연구진과 졸업생을 소개합니다.
nav: true
nav_order: 1
---

## 교수진

<div class="member-grid">
  <article class="member-card"><img src="{{ '/assets/img/jbsm/members_1-01.png' | relative_url }}" alt="박진 교수"><div class="member-body"><h3>박진 <small>Jin Park, MD, PhD</small></h3><p class="member-role">전북대학교병원 피부과 · 피부과 전문의</p><p><a href="mailto:airmd@jbnu.ac.kr">airmd@jbnu.ac.kr</a> · <a href="https://scholar.google.co.kr/citations?user=qc6CJjYAAAAJ">Google Scholar</a></p><details><summary>경력</summary><ul><li>원광대학교 의학과 의학사</li><li>전북대학교 대학원 의학과 의학석사</li><li>전남대학교 대학원 의학과 의학박사</li><li>미국국립보건원(NIH/NIAMS) 피부과 방문연구원</li><li>대한피부과학회 평의원</li><li>대한피부과학회 대외협력위원회 및 보험위원회 위원</li><li>대한피부과학회 전북지부회 총무이사</li><li>대한모발학회 간행정보이사</li><li>대한피부진균및감염학회 기획이사</li><li>대한의진균학회 및 아시아태평양의진균학회 평의원</li><li>건강보험심사평가원 비상근심사위원</li></ul></details></div></article>
  <article class="member-card"><img src="{{ '/assets/img/jbsm/members_1-02.png' | relative_url }}" alt="남경화 교수"><div class="member-body"><h3>남경화 <small>Kyung-Haw Nam, MD, PhD</small></h3><p class="member-role">전북대학교병원 피부과 · 피부과 전문의</p><p><a href="mailto:kyung1212@hanmail.net">kyung1212@hanmail.net</a> · <a href="https://scholar.google.co.kr/">Google Scholar</a></p><details><summary>경력</summary><ul><li>전북대학교 의학과 의학사</li><li>전북대학교 대학원 의학과 의학석사·의학박사</li><li>전북대학교병원 피부과 전임의사</li><li>전주예수병원 피부과 과장(2014.7–2021.2)</li><li>현 전북대학교 의과대학 피부과 부교수</li><li>대한건선학회 간행 이사</li><li>대한백반증색소학회 평의원</li><li>대한피부과학회 신의료기술위원회 위원</li><li>대한피부과학회 의약품 및 의료기기위원회 위원</li></ul></details></div></article>
</div>

## 연구진

<div class="member-grid">
{% assign members = "이건종|Gun Jong Lee|MD Student|gjderma@gmail.com|members_1-03.jpg;강태종|Tae Jong Gang|MD Student|tjderma@gmail.com|members_1-04.jpg;Trang Tran|Trang Tran|MD, PhD Integrated Student|ttqtrang.dl@huemed-univ.edu.vn|members_1-05.jpg;오유림|YuRim Oh|CRC|971213ok@gmail.com|members_1-06.jpg;정주은|JooEun Jeong|CRC|jooeun2@kakao.com|members_1-07.png;김병지|ByeongJi Kim|Lab Technician|qudwl07@naver.com|members_1-08.jpg;박윤환|YunHwan Park|Researcher|dbsghks5226@gmail.com|members_1-09.png;김광일|Gwang-il Kim|PhD Integrated Student|rhkd97750@gmail.com|members_1-10.jpg" | split: ";" %}
{% for item in members %}{% assign member = item | split: "|" %}
  <article class="member-card"><img src="{{ '/assets/img/jbsm/' | append: member[4] | relative_url }}" alt="{{ member[0] }}"><div class="member-body"><h3>{{ member[0] }} <small>{{ member[1] }}</small></h3><p class="member-role">{{ member[2] }}</p><a href="mailto:{{ member[3] }}">{{ member[3] }}</a></div></article>
{% endfor %}
</div>

<div class="member-grid mt-4">
  <article class="lab-card"><h3>유현지 <small>HyunJi Ryu</small></h3><p class="member-role">MD Student</p></article>
  <article class="lab-card"><h3>성기재 <small>KiJae Sung</small></h3><p class="member-role">MD Student</p><a href="mailto:kijae.sung.med@gmail.com">kijae.sung.med@gmail.com</a></article>
  <article class="lab-card"><h3>김소연 <small>Soyeon Kim</small></h3><p class="member-role">PhD Student</p><a href="https://github.com/KitHubb">GitHub</a></article>
</div>

## 졸업생

<div class="member-grid">
  <article class="member-card"><img src="{{ '/assets/img/jbsm/members_1-11.jpg' | relative_url }}" alt="최가영"><div class="member-body"><h3>최가영 <small>Gayong Choi</small></h3><p class="member-role">CRC</p><a href="mailto:rkdud6662@naver.com">rkdud6662@naver.com</a></div></article>
  <article class="member-card"><img src="{{ '/assets/img/jbsm/members_1-12.jpg' | relative_url }}" alt="박하은"><div class="member-body"><h3>박하은 <small>Haeun Park</small></h3><p class="member-role">CRC</p><a href="mailto:gkdms6132@naver.com">gkdms6132@naver.com</a></div></article>
</div>
