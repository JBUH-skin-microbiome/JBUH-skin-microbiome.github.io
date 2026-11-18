---
layout: page
title: Members
permalink: /members/
description: 피부마이크로바이옴연구실의 교수진, 연구진과 졸업생을 소개합니다.
nav: true
nav_order: 1
---

{% assign groups = "faculty|Faculty,researcher|Researchers,alumni|Alumni" | split: "," %}
{% assign sorted_members = site.members | sort: "order" %}
{% for group_item in groups %}
  {% assign group_data = group_item | split: "|" %}
  <section class="member-section member-section-{{ group_data[0] }}">
    <h2>{{ group_data[1] }}</h2>
    <div class="member-grid member-grid-{{ group_data[0] }}">
      {% for member in sorted_members %}
        {% if member.group == group_data[0] %}
          <article class="member-card">
            <a class="member-image-link" href="{{ member.url | relative_url }}"><img src="{{ member.image | relative_url }}" alt="{{ member.name }} 프로필 사진" loading="lazy"></a>
            <div class="member-body">
              <h3><a href="{{ member.url | relative_url }}">{{ member.name }}</a> <small>{{ member.name_en }}</small></h3>
              <p class="member-role">{{ member.role }}</p>
              <a class="profile-link" href="{{ member.url | relative_url }}">View profile →</a>
            </div>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>
{% endfor %}
