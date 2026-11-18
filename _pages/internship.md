---
layout: page
title: Internship
permalink: /internship/
description: JBSM 인턴십의 교육 과정과 프로젝트를 안내합니다.
nav: true
nav_order: 6
toc:
  sidebar: right
---

<div class="internship-page">
  <section class="content-section">
    <h2 id="training-plan">3-Month Training Plan</h2>
    <div class="internship-feature-grid">
      <div class="internship-copy">
        <p>신규 인원도 기초부터 단계적으로 학습할 수 있도록, 연구실 합류 후 3개월 동안 R과 Linux를 비롯한 생물정보학 기초 교육부터 실제 마이크로바이옴 데이터 분석 및 결과 해석까지 체계적인 교육과 실습을 지원합니다.</p>
        <ul>
          <li><strong>1 month</strong> [마이크로바이옴 분석을 위한 프로그램 학습 과정]: R &amp; Linux &amp; 생물정보학 기초</li>
          <li><strong>2 month</strong> [마이크로바이옴 분석을 위한 프로그램 숙달 과정]: Microbiome &amp; QIIME2 &amp; DADA2</li>
          <li><strong>3 month</strong> [실제 예제 데이터를 사용한 실습 과정]: 예제 데이터 분석 &amp; 마이크로바이옴 결과 토의 및 해석</li>
        </ul>
      </div>
      <figure><img src="{{ '/assets/img/jbsm/jbsm-internship-01.png' | relative_url }}" alt="JBSM 인턴십 3개월 교육 과정" loading="lazy"></figure>
    </div>
  </section>

  <section class="content-section">
    <h2 id="research-areas">Our Research Areas</h2>
    <div class="internship-topic-grid">
      <article class="internship-topic">
        <h3 data-toc-skip>피부 마이크로바이옴이란?</h3>
        <ul>
          <li>피부 마이크로바이옴은 피부에 서식하는 세균, 진균, 바이러스 등 다양한 미생물과 이들의 유전정보 및 주변 환경을 포괄하는 개념입니다. 이러한 미생물은 숙주의 면역 반응 조절, 미생물 간 상호작용 및 미생물 유래 대사물질의 작용 등을 통해 피부 기능과 항상성 유지에 중요한 역할을 합니다.</li>
          <li>피부 미생물 군집은 숙주의 상태, 신체 부위, 연령, 생활환경 등 다양한 요인에 따라 그 구성과 특성이 달라지는 것으로 알려져 있습니다.</li>
        </ul>
      </article>
      <article class="internship-topic">
        <h3 data-toc-skip>우리 연구실에서는 어떤 연구를 수행할까요?</h3>
        <ul>
          <li>우리 연구실에서는 다양한 피부 질환에서 나타나는 미생물 군집의 특성과 변화를 중점적으로 연구하고 있으며, 피부 마이크로바이옴과 피부 질환 사이의 연관성을 이해하고자 합니다.</li>
          <li>또한 피부 유래 세균과 진균의 분리·배양 및 동정 연구를 수행하며, 다양한 오믹스 분석을 추가적으로 활용하여 숙주–미생물 간 상호작용을 다각도로 연구하고 있습니다.</li>
        </ul>
      </article>
      <article class="internship-topic">
        <h3 data-toc-skip>우리 연구실에서는 어떤 방법으로 연구할까요?</h3>
        <ul>
          <li>주로 피부 면봉을 이용하여 피부 표면의 미생물을 채취하고 있으며, 이를 통해 피부 마이크로바이옴의 구성과 특성을 연구하고 있습니다.</li>
          <li>또한 연구 목적에 따라 모발, 피부 조직 등의 검체와 각질층 테이프 스트리핑 등 다양한 채취 방법을 활용하고 있습니다.</li>
        </ul>
      </article>
      <article class="internship-topic">
        <h3 data-toc-skip>채취한 검체는 어떻게 분석할까요?</h3>
        <ul>
          <li>차세대 염기서열 분석 기술을 활용하여 미생물 군집의 구성과 다양성을 분석하고, 통계적 방법을 통해 연구 결과를 해석합니다.</li>
          <li>또한 세균과 진균의 분리·배양 및 동정을 수행하며, 연구 목적에 따라 전사체·단백질체·대사체 등 다양한 오믹스 분석을 활용하고 있습니다.</li>
        </ul>
      </article>
    </div>
    <div class="internship-research-images">
      <img src="{{ '/assets/img/jbsm/jbsm-internship-02.png' | relative_url }}" alt="피부 마이크로바이옴 개념도" loading="lazy">
      <img src="{{ '/assets/img/jbsm/jbsm-internship-03.png' | relative_url }}" alt="피부 마이크로바이옴 분석 과정" loading="lazy">
    </div>
  </section>

  <section class="content-section">
    <h2 id="microbiome-analysis">Microbiome Analysis</h2>
    <div class="internship-analysis-grid">
      <article class="internship-topic">
        <h3 data-toc-skip>R이란?</h3>
        <ul><li>통계 분석과 데이터 시각화에 널리 사용되는 프로그래밍 언어입니다.</li><li>데이터 전처리와 통계 분석을 수행할 수 있습니다.</li><li>분석 결과를 그래프와 그림으로 시각화할 수 있습니다.</li></ul>
      </article>
      <article class="internship-topic">
        <h3 data-toc-skip>우리 연구실에서 R을 사용하는 이유는?</h3>
        <ul><li>마이크로바이옴 데이터를 통계적으로 분석하고 시각적으로 확인하기 위해 사용합니다.</li><li>데이터를 그래프로 표현해 결과를 직관적으로 이해할 수 있습니다.</li></ul>
      </article>
      <article class="internship-topic">
        <h3 data-toc-skip>Linux란?</h3>
        <ul><li>다양한 분석 프로그램을 실행하고 데이터를 처리하는 데 널리 사용되는 운영체제입니다.</li><li>대용량 데이터 처리와 반복적인 분석 작업을 효율적으로 수행하는 데 적합합니다.</li></ul>
      </article>
      <article class="internship-topic">
        <h3 data-toc-skip>우리 연구실에서 Linux를 사용하는 이유는?</h3>
        <ul><li>마이크로바이옴 raw data를 분석 가능한 형태로 가공하고 전처리하기 위해 사용합니다.</li><li>우리 실험실 서버 환경을 활용하여 대용량 데이터를 보다 빠르고 효율적으로 처리할 수 있습니다.</li></ul>
      </article>
    </div>
    <div class="internship-tools-row">
      <img class="internship-r-logo" src="{{ '/assets/img/jbsm/jbsm-internship-04.png' | relative_url }}" alt="R 로고" loading="lazy">
      <img class="internship-linux-logo" src="{{ '/assets/img/jbsm/jbsm-internship-05.png' | relative_url }}" alt="Linux Tux" loading="lazy">
      <img class="internship-result-image" src="{{ '/assets/img/jbsm/jbsm-internship-06.png' | relative_url }}" alt="마이크로바이옴 분석 결과 예시" loading="lazy">
    </div>
    <article class="internship-topic internship-topic-wide">
      <h3 data-toc-skip>R, Linux로 만들어진 결과는 어떻게 나올까요?</h3>
      <ul><li>Linux를 이용해 마이크로바이옴 raw sequencing data를 전처리하고 분석 가능한 형태로 정리합니다.</li><li>R을 이용해 통계 분석을 수행하고 결과를 그래프와 그림으로 시각화합니다.</li><li>최종적으로 균의 구성, 다양성, 그룹 간 차이, 특정 균의 증감 등을 확인할 수 있습니다.</li></ul>
    </article>
    <article class="internship-topic internship-topic-wide">
      <h3 data-toc-skip>피부 마이크로바이옴 분석 결과는 어떻게 해석할까요?</h3>
      <ul><li>매주 진행되는 Journal Club을 통해 피부 마이크로바이옴 및 피부 질환에 관련한 연구를 교수님, 연구원들과 함께 공유하며 학습하는 시간을 가질 수 있습니다.</li><li>또한 Project Meeting을 통해 연구원들이 발표하는 주제나 교수님의 피드백을 접하며, 마이크로바이옴 데이터를 연구 주제와 연관 지어 해석하는 관점을 배울 수 있습니다.</li><li>충분한 데이터 검토와 토의를 거친 연구 결과는 학회 포스터, 구연 발표 및 논문 출판으로 이어질 수 있습니다.</li></ul>
    </article>
  </section>

  <section class="content-section">
    <h2 id="qna">Q&amp;A</h2>
    <div class="internship-qna">
      <details open><summary>R이나 Linux 같은 운영체제를 배우지 않았더라도 괜찮을까요?</summary><p>네, 관련 경험이 없거나 부족하셔도 괜찮습니다. 실제로 연구실 구성원 중에는 사전 프로그램 경험 없이 입학 후 교육을 받으며 연구를 수행하고 있는 경우도 있습니다. 다만 주 업무가 Excel, R, Linux 등으로 이루어지기 때문에, 사전에 관련 지식을 접해본다면 연구에 도움이 될 수 있습니다.</p></details>
      <details><summary>실제 입학 후 주로 어떤 업무를 하게 되나요?</summary><p>기초적인 프로그램 학습이 완료된 후에는 연구실 진행 상황과 관심 분야에 따라 연구 주제 또는 과제를 배정받아 수행합니다. 연구를 수행하기 위해 환자 및 연구 대상자의 정보와 샘플 정보를 정리하고, 시퀀싱 데이터를 분석하게 됩니다. 최종적으로 시각화된 데이터를 바탕으로 마이크로바이옴 특성과 해당 연구 주제의 연관성을 확인하고 해석합니다.</p></details>
    </div>
  </section>

  <footer class="internship-credits">
    <p><strong>JBSM Internship — Image Credits:</strong> R logo © R Foundation (CC BY-SA 4.0, modified). Tux © Larry Ewing, created using GIMP.</p>
    <p><strong>JBSM Internship — Contributors:</strong> Soyeon Kim and YunHwan Park.</p>
  </footer>
</div>
