<h1 align="center">
  <img src="assets/header.svg" width="800" alt="Matěj &quot;Majkey&quot; Teplý" />
</h1>
<p align="center"><b>Full-Stack AI/ML Engineer &amp; Backend Developer</b></p>

<div align="center">
  <a href="https://www.linkedin.com/in/matejteply/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&style=for-the-badge" height="25" alt="LinkedIn" />
  </a>
  <a href="https://www.instagram.com/_majkey_/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white&style=for-the-badge" height="25" alt="Instagram" />
  </a>
  <a href="https://discordapp.com/users/529408301193101352" target="_blank">
    <img src="https://img.shields.io/badge/Discord-7289DA?logo=discord&logoColor=white&style=for-the-badge" height="25" alt="Discord" />
  </a>
</div>

<table>
<tr>
<td width="60%" valign="top">

I'm a **Full-Stack AI/ML Engineer & Backend Developer**. I build LLM applications, Python services, automation, and interfaces that connect them into usable products.

At **[OKsystem a.s.](https://www.oksystem.com/en)**, I develop and evaluate AI chatbots and RAG pipelines. My work spans retrieval, context and prompt design, model integration, REST APIs, databases, and frontend implementation.

Outside work, I build **developer tools, Android applications, and websites**. My projects cover project and release tracking, prompt and agent instructions, document scanning, offline music tools, weather data, and the WeTheGods website.

In my own projects, I research and prototype AI tools, testing their practical fit and integration trade-offs. I'm interested in how these systems find relevant information, handle missing context, and behave when a model or service fails.

I'm **eager to learn new things**, deepen my understanding of AI/ML, and test new tools through practical projects. I like comparing approaches and understanding why they succeed or fail.

Alongside development, I study **Software Engineering at Tomas Bata University in Zlín**, combining the degree with professional work and independent projects.

</td>
<td width="40%" align="center">

<img src="https://github.com/user-attachments/assets/f9c5e42b-e334-4915-b855-0cbe27709a14" width="300" alt="" />

</td>
</tr>
</table>

<div align="center">
  <img src="assets/typing.svg" width="800" alt="LLM applications and agent workflows; Python backends and APIs; retrieval and evaluation; React, TypeScript, Kotlin, and Android" />
</div>

## What I build

> [!NOTE]
> I build AI applications, backend services, and the interfaces that bring them together. My work includes chatbots, RAG pipelines, retrieval, model integration, and evaluation.

- **Knowledge-backed chatbots:** Build retrieval and context flows that connect language models to relevant information from their knowledge bases.
- **Full-stack integration:** Connect LLM services to Python backends, REST APIs, databases, automation, and user-facing interfaces.
- **Evaluation and debugging:** Test answers and retrieval behavior, investigate failures, and improve prompts, context, performance, and code quality.

## Selected work

| Project | What it does |
| --- | --- |
| **[project-board-showcase](https://github.com/Majkey25/project-board-showcase)** | Project and release board separating workflow phases from deployed versions. Public showcase; application source is private. |
| **[ScanIt](https://github.com/Majkey25/ScanIt)** | Android document scanner with on-device OCR, local document operations, and PDF/image export. |
| **[TuneItAll](https://github.com/Majkey25/TuneItAll)** | Offline Android tuner for guitar, bass, ukulele, and chromatic tuning. |
| **[prompt-engineering-skill](https://github.com/Majkey25/prompt-engineering-skill)** | Reusable prompt and agent instructions with explicit constraints, verification, and evaluation criteria. |
| **[Selia-Weather](https://github.com/Majkey25/Selia-Weather)** | Czech weather app with provider forecasts, ČHMÚ radar, and configurable Android widgets. |
| **[WeTheGods](https://github.com/Majkey25/WeTheGods)** | Band website built with Astro and published through GitHub Pages. |

<p align="right"><a href="https://github.com/Majkey25?tab=repositories"><b>And much more...</b></a></p>

## How I build

> AI does not remove the engineer. It changes where engineering effort goes.
>
> From [my post on modern software engineering with AI agents](https://lnkd.in/p/duaqwHh9).

~~~diff
- Scope: implementation
+ Scope: implementation + verification
~~~

> [!TIP]
> I start with the problem, constraints, and failure cases.
>
> I prefer small, understandable systems and verify behavior with tests, type checks, evals, and real app or device testing.

## Career so far

~~~mermaid
gantt
    dateFormat YYYY-MM-DD
    axisFormat %Y
    todayMarker off
    Mechanical studies (SPŠ Zlín) :done, school, 2021-01-01, 2025-01-01
    Azure Programming (STC) :done, azure, 2023-01-01, 2025-07-01
    AI / full-stack development :active, work, 2025-06-01, 2026-10-06
    Software Engineering (UTB) :active, university, 2025-01-01, 2026-10-06
    AI safety evaluations :done, safety, 2026-05-01, 2026-10-01
~~~

<sub>As of October 2026. Study dates are shown by year; work dates by month.</sub>

---

## Outside software

I play drums, guitar, bass, and saxophone, and I sing. I currently play with **[WETHEGODS](https://www.facebook.com/wethegodsband/)**, previously with **[Exhalace](https://exhalace.cz)**, and collect vinyl records.

[WETHEGODS on Spotify](https://open.spotify.com/artist/0t37G5AusfBBeHTv85jxj9)

<a href="https://open.spotify.com/user/an3l6poe03o6g6htrdrs0hgjy">
  <img src="https://raw.githubusercontent.com/Majkey25/Majkey25/output/spotify.svg" width="300" alt="Recently played Spotify tracks" />
</a>

<details>
<summary><b>Explore a 3D guitar-pick sketch</b></summary>

A small music-inspired 3D sketch, connecting my mechanical-engineering foundation with the instruments I play.

~~~stl
solid guitar_pick
  facet normal 0 -0 -1
    outer loop
      vertex -11 10 0
      vertex 0 -17 0
      vertex -14 6 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -11 10 1.2
      vertex -14 6 1.2
      vertex 0 -17 1.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -11 10 0
      vertex 14 6 0
      vertex 0 -17 0
    endloop
  endfacet
  facet normal 0 0 1
    outer loop
      vertex -11 10 1.2
      vertex 0 -17 1.2
      vertex 14 6 1.2
    endloop
  endfacet
  facet normal 0 0 -1
    outer loop
      vertex -11 10 0
      vertex 11 10 0
      vertex 14 6 0
    endloop
  endfacet
  facet normal -0 0 1
    outer loop
      vertex -11 10 1.2
      vertex 14 6 1.2
      vertex 11 10 1.2
    endloop
  endfacet
  facet normal -0.8 0.6 0
    outer loop
      vertex -11 10 0
      vertex -14 6 0
      vertex -14 6 1.2
    endloop
  endfacet
  facet normal -0.8 0.6 0
    outer loop
      vertex -11 10 0
      vertex -14 6 1.2
      vertex -11 10 1.2
    endloop
  endfacet
  facet normal -0.85419856 -0.51994695 0
    outer loop
      vertex -14 6 0
      vertex 0 -17 0
      vertex 0 -17 1.2
    endloop
  endfacet
  facet normal -0.85419856 -0.51994695 0
    outer loop
      vertex -14 6 0
      vertex 0 -17 1.2
      vertex -14 6 1.2
    endloop
  endfacet
  facet normal 0.85419856 -0.51994695 0
    outer loop
      vertex 0 -17 0
      vertex 14 6 0
      vertex 14 6 1.2
    endloop
  endfacet
  facet normal 0.85419856 -0.51994695 0
    outer loop
      vertex 0 -17 0
      vertex 14 6 1.2
      vertex 0 -17 1.2
    endloop
  endfacet
  facet normal 0.8 0.6 0
    outer loop
      vertex 14 6 0
      vertex 11 10 0
      vertex 11 10 1.2
    endloop
  endfacet
  facet normal 0.8 0.6 -0
    outer loop
      vertex 14 6 0
      vertex 11 10 1.2
      vertex 14 6 1.2
    endloop
  endfacet
  facet normal 0 1 0
    outer loop
      vertex 11 10 0
      vertex -11 10 0
      vertex -11 10 1.2
    endloop
  endfacet
  facet normal 0 1 -0
    outer loop
      vertex 11 10 0
      vertex -11 10 1.2
      vertex 11 10 1.2
    endloop
  endfacet
endsolid guitar_pick
~~~

[Open or save the STL model](assets/guitar-pick.stl)

</details>

## GitHub activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Majkey25/Majkey25/output/pacman-contribution-graph-dark.svg">
  <img src="https://raw.githubusercontent.com/Majkey25/Majkey25/output/pacman-contribution-graph.svg" alt="GitHub contribution activity for Majkey25" />
</picture>

[Portfolio](https://majkey25.github.io/init/) · [Support my work](https://www.buymeacoffee.com/majkey)
