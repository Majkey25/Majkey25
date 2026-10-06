# GitHub README showcase

30 options you can choose by ID, for example **A08 + A13 + A18**. Each section shows the rendered result and a copyable example. This file is a separate gallery, not your profile.

Examples are demonstrations, not measurements or promises about your projects. Existing profile graphics and project links are real.

Native syntax follows [GitHub's formatting guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) and the [GitHub Flavored Markdown specification](https://github.github.com/gfm/).

## Pick an option

| ID | Option | Uses |
| --- | --- | --- |
| [A01](#a01-headings) | Heading hierarchy | Native Markdown |
| [A02](#a02-text-styling) | Emphasis, inline code, small text | Markdown + HTML |
| [A03](#a03-links-and-navigation) | Section navigation, relative links, anchors | Native Markdown |
| [A04](#a04-lists-and-checklists) | Lists, nested lists, checklists | Native Markdown |
| [A05](#a05-quotes-and-separators) | Quotes and section separators | Native Markdown |
| [A06](#a06-tables) | Comparison tables and alignment | Native Markdown |
| [A07](#a07-code-and-diffs) | Highlighted code and colored diffs | Native Markdown |
| [A08](#a08-collapsible-sections) | Expandable project notes | Native HTML |
| [A09](#a09-colored-alerts) | Note, tip, important, warning, caution | GitHub extension |
| [A10](#a10-inline-html) | Keyboard keys, superscripts, definitions | Native HTML |
| [A11](#a11-footnotes) | References without long inline text | GitHub extension |
| [A12](#a12-math) | Equations for ML or research | GitHub math renderer |
| [A13](#a13-workflow-diagram) | Architecture or verification flow | Mermaid |
| [A14](#a14-sequence-diagram) | API and RAG request flow | Mermaid |
| [A15](#a15-roadmap) | A timeline with task dependencies | Mermaid |
| [A16](#a16-mind-map) | Areas of work or project structure | Mermaid |
| [A17](#a17-charts) | Pie charts and other diagram types | Mermaid |
| [A18](#a18-clickable-images) | Image links and screenshot previews | Images + Markdown |
| [A19](#a19-two-column-layout) | Compact project tiles | Native HTML table |
| [A20](#a20-light-and-dark-images) | Images that follow system theme | Native picture element |
| [A21](#a21-custom-svg-branding) | Gradient text, banners, illustrations | Repository SVG |
| [A22](#a22-animations) | Animated SVGs and GIFs | Image assets |
| [A23](#a23-badges-and-link-buttons) | Status labels and prominent links | Generated images |
| [A24](#a24-icon-row) | Small language or tool icons | External image service |
| [A25](#a25-music-and-activity-cards) | Spotify and contribution graphics | Services + Actions |
| [A26](#a26-maps) | Interactive geographic data | GeoJSON / TopoJSON |
| [A27](#a27-three-dimensional-models) | Rotatable 3D geometry | ASCII STL |
| [A28](#a28-video-and-downloads) | Video attachments and downloadable files | Uploaded assets + links |
| [A29](#a29-automated-content) | Blog feeds, releases, generated cards | GitHub Actions or services |
| [A30](#a30-source-only-features) | Comments, escapes, emoji, references | Markdown + GitHub behavior |

For your profile, the strongest additions to try first are **A08** for project detail, **A13** for your engineering workflow, and **A18** for real product screenshots.

## A01 Headings

### Section heading
#### Subsection heading
##### Small heading
###### Fine-grained heading

Use hierarchy for structure, not merely to shrink a font.

<details>
<summary>Copy Markdown</summary>

~~~markdown
# Page title
## Section
### Subsection
#### Detail
##### Small heading
###### Fine-grained heading
~~~

</details>

## A02 Text styling

**Bold** · *Italic* · ***Bold + italic*** · ~~Removed text~~ · `inline code`

<sub>Small secondary text</sub> · <sup>Superscript</sup> · <ins>Underlined text</ins>

<details>
<summary>Copy Markdown</summary>

~~~markdown
**Bold** · *Italic* · ***Bold + italic*** · ~~Removed text~~ · `inline code`
<sub>Small secondary text</sub>
<sup>Superscript</sup>
<ins>Underlined text</ins>
~~~

</details>

## A03 Links and navigation

[Profile](https://github.com/Majkey25) · [Projects](https://github.com/Majkey25?tab=repositories) · [Skip to diagrams](#a13-workflow-diagram) · [Profile README](../README.md)

<a name="custom-example"></a>
This paragraph has its own [custom anchor](#custom-example).

GitHub also supplies an Outline menu for files with headings. Section and relative-link behavior is documented in [GitHub's navigation syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links).

<details>
<summary>Copy Markdown</summary>

~~~markdown
[Projects](https://github.com/Majkey25?tab=repositories)
[Section](#selected-work)
[Another file](../README.md)

<a name="custom-example"></a>
[Jump to that location](#custom-example)
~~~

</details>

## A04 Lists and checklists

- AI applications
  - Retrieval
  - Evaluation
- Backend services

1. Define constraints.
2. Implement.
3. Verify.

Demo checklist:

- [x] Define the contract
- [x] Check the happy path
- [ ] Explore another failure case

README checkboxes describe state; changing that state requires editing the source.

<details>
<summary>Copy Markdown</summary>

~~~markdown
- AI applications
  - Retrieval
  - Evaluation

1. Define constraints.
2. Implement.
3. Verify.

- [x] Completed example
- [ ] Planned example
~~~

</details>

## A05 Quotes and separators

> Context → constraints → implementation → verification.

A horizontal rule can separate two larger parts:

---

<details>
<summary>Copy Markdown</summary>

~~~markdown
> Context → constraints → implementation → verification.

---
~~~

</details>

## A06 Tables

| Project | Focus | Example number |
| :--- | :---: | ---: |
| ScanIt | Documents | 1 |
| TuneItAll | Audio | 2 |
| Selia-Weather | Weather | 3 |

The numbers here demonstrate right alignment; they are not project metrics.

<details>
<summary>Copy Markdown</summary>

~~~markdown
| Project | Focus | Example number |
| :--- | :---: | ---: |
| ScanIt | Documents | 1 |
| TuneItAll | Audio | 2 |
~~~

</details>

## A07 Code and diffs

~~~python
from pathlib import Path

readme = Path("README.md")
print(readme.read_text(encoding="utf-8"))
~~~

~~~diff
- Scope: build the feature
+ Scope: build the feature and verify its behavior
~~~

Language names enable syntax highlighting. [GitHub documents code fences and highlighting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~python
from pathlib import Path
print(Path("README.md").read_text(encoding="utf-8"))
~~~

~~~diff
- Old description
+ New description
~~~
~~~~

</details>

## A08 Collapsible sections

<details>
<summary><b>Open a project deep dive</b></summary>

### Example: document scanning

- On-device recognition.
- PDF and image export.
- Small capture → review → share workflow.

[Open ScanIt](https://github.com/Majkey25/ScanIt)

</details>

This keeps the overview short while exposing detail on demand. [Native collapsed-section syntax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections).

<details>
<summary>Copy Markdown</summary>

~~~markdown
<details>
<summary><b>Project details</b></summary>

Content goes here. Keep blank lines around Markdown.

</details>
~~~

</details>

## A09 Colored alerts

These five blocks demonstrate styles. They are not warnings about your repository.

> [!NOTE]
> Demo of the blue information style.

> [!TIP]
> Demo of the green suggestion style.

> [!IMPORTANT]
> Demo of the purple emphasis style.

> [!WARNING]
> Demo of the yellow warning style.

> [!CAUTION]
> Demo of the red caution style.

Choose one when the content warrants it. [GitHub's alert syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts) supports these five types.

<details>
<summary>Copy Markdown</summary>

~~~markdown
> [!NOTE]
> Useful context.

> [!TIP]
> A practical suggestion.

> [!IMPORTANT]
> Something the reader needs to know.

> [!WARNING]
> A specific operational warning.

> [!CAUTION]
> A specific risk.
~~~

</details>

## A10 Inline HTML

Press <kbd>Ctrl</kbd> + <kbd>K</kbd> to illustrate a keyboard shortcut.

H<sub>2</sub>O · x<sup>2</sup> · <ins>underlined text</ins>

<dl>
<dt><b>RAG</b></dt>
<dd>Retrieval-augmented generation.</dd>
<dt><b>Evaluation</b></dt>
<dd>Checking behavior against defined cases.</dd>
</dl>

<p align="center"><b>Centered text using a supported HTML attribute</b><br>Second line</p>

<details>
<summary>Copy Markdown</summary>

~~~html
<kbd>Ctrl</kbd> + <kbd>K</kbd>
H<sub>2</sub>O · x<sup>2</sup>
<ins>Underlined text</ins>

<dl>
<dt>Term</dt>
<dd>Definition</dd>
</dl>

<p align="center">Centered text<br>Second line</p>
~~~

</details>

## A11 Footnotes

A short description can link to longer evidence without interrupting the paragraph.[^evidence]

<details>
<summary>Copy Markdown</summary>

~~~markdown
A short description can link to evidence.[^evidence]

[^evidence]: A source link or a longer explanatory note.
~~~

</details>

## A12 Math

Inline equation: $F_\beta = (1+\beta^2)\frac{PR}{\beta^2 P+R}$.

Display equation:

~~~math
\mathrm{cost\ per\ verified\ task} = \frac{\mathrm{total\ execution\ cost}}{\mathrm{verified\ completed\ tasks}}
~~~

These are equations, not claimed measurements. [GitHub math rendering](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) accepts LaTeX-style expressions.

<details>
<summary>Copy Markdown</summary>

~~~markdown
Inline: $x^2 + y^2 = z^2$.

$$
\mathrm{precision} = \frac{TP}{TP+FP}
$$
~~~

</details>

## A13 Workflow diagram

A small diagram fits your engineering post without adding another live widget.

~~~mermaid
flowchart LR
    C[Context] --> K[Constraints]
    K --> A[Coding agent]
    A --> V{Verification}
    V -- Pass --> M[Merge]
    V -- Fail --> A
~~~

[GitHub's diagram renderer](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) turns a Mermaid code fence into a diagram.

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~mermaid
flowchart LR
    C[Context] --> K[Constraints]
    K --> A[Coding agent]
    A --> V{Verification}
    V -- Pass --> M[Merge]
    V -- Fail --> A
~~~
~~~~

</details>

## A14 Sequence diagram

Demo of a request moving through an AI application:

~~~mermaid
sequenceDiagram
    actor User
    participant API
    participant Search
    participant LLM
    User->>API: Question
    API->>Search: Retrieve context
    Search-->>API: Relevant passages
    API->>LLM: Question and context
    LLM-->>API: Draft response
    API->>API: Validate response and sources
    API-->>User: Response
~~~

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~mermaid
sequenceDiagram
    actor User
    participant API
    participant Search
    participant LLM
    User->>API: Question
    API->>Search: Retrieve context
    Search-->>API: Relevant passages
    API->>LLM: Question and context
    LLM-->>API: Draft response
    API->>API: Validate response and sources
    API-->>User: Response
~~~
~~~~

</details>

## A15 Roadmap

Illustrative timeline, not a plan for your projects:

~~~mermaid
gantt
    title Demo roadmap
    dateFormat YYYY-MM-DD
    section Scope
    Define the contract :scope, 2026-10-06, 2d
    section Implementation
    Build a first slice :build, after scope, 3d
    section Verification
    Check the changed flow :check, after build, 2d
~~~

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~mermaid
gantt
    title Demo roadmap
    dateFormat YYYY-MM-DD
    section Scope
    Define the contract :scope, 2026-10-06, 2d
    section Implementation
    Build a first slice :build, after scope, 3d
    section Verification
    Check the changed flow :check, after build, 2d
~~~
~~~~

</details>

## A16 Mind map

~~~mermaid
mindmap
  root((AI engineering))
    Context
      Sources
      Constraints
    Applications
      APIs
      Interfaces
    Verification
      Tests
      Evals
      Runtime behavior
~~~

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~mermaid
mindmap
  root((AI engineering))
    Context
      Sources
      Constraints
    Applications
      APIs
      Interfaces
    Verification
      Tests
      Evals
      Runtime behavior
~~~
~~~~

</details>

## A17 Charts

Fictional values used only to demonstrate a chart:

~~~mermaid
pie showData
    title Demo distribution
    "Context" : 25
    "Implementation" : 35
    "Verification" : 40
~~~

Mermaid also offers class, state, entity-relationship, and Git diagrams. Available types depend on the version GitHub runs; this gallery demonstrates the types rendered here. [Mermaid diagram types](https://mermaid.js.org/intro/).

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~mermaid
pie showData
    title Demo distribution
    "Context" : 25
    "Implementation" : 35
    "Verification" : 40
~~~
~~~~

</details>

## A18 Clickable images

This real profile banner opens your engineering post:

<a href="https://lnkd.in/p/duaqwHh9"><img src="../assets/header.svg" width="600" alt="Read Matěj's post on modern software engineering"></a>

The same pattern works for product screenshots, release links, and demo thumbnails.

<details>
<summary>Copy Markdown</summary>

~~~markdown
[![Banner](../assets/header.svg)](https://lnkd.in/p/duaqwHh9)

<a href="https://github.com/Majkey25/ScanIt">
  <img src="../assets/header.svg" width="400" alt="Open the project">
</a>
~~~

</details>

## A19 Two-column layout

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/Majkey25/ScanIt">ScanIt</a></h3>
<p>Document scanning, on-device OCR, and PDF/image export.</p>
<a href="https://github.com/Majkey25/ScanIt">Open project →</a>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/Majkey25/TuneItAll">TuneItAll</a></h3>
<p>Offline tuning for guitar, bass, ukulele, and chromatic use.</p>
<a href="https://github.com/Majkey25/TuneItAll">Open project →</a>
</td>
</tr>
</table>

HTML tables provide columns within GitHub's formatting limits. Small phone screens make dense columns less comfortable.

<details>
<summary>Copy HTML</summary>

~~~html
<table>
<tr>
<td width="50%" valign="top">
<h3>Project one</h3>
<p>A short description.</p>
</td>
<td width="50%" valign="top">
<h3>Project two</h3>
<p>A short description.</p>
</td>
</tr>
</table>
~~~

</details>

## A20 Light and dark images

This selects the existing Pac-Man image using the system color preference:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Majkey25/Majkey25/output/pacman-contribution-graph-dark.svg">
  <img src="https://raw.githubusercontent.com/Majkey25/Majkey25/output/pacman-contribution-graph.svg" alt="Theme-aware Pac-Man contribution graph">
</picture>

[GitHub supports the picture element](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#the-picture-element). A custom SVG can also switch its own colors, as your header does.

<details>
<summary>Copy HTML</summary>

~~~html
<picture>
  <source media="(prefers-color-scheme: dark)"
    srcset="https://raw.githubusercontent.com/Majkey25/Majkey25/output/pacman-contribution-graph-dark.svg">
  <img
    src="https://raw.githubusercontent.com/Majkey25/Majkey25/output/pacman-contribution-graph.svg"
    alt="Pac-Man contribution graph">
</picture>
~~~

</details>

## A21 Custom SVG branding

<img src="../assets/header.svg" width="800" alt="Gradient profile header">

SVG images can contain custom typography, gradients, decorative dividers, diagrams, and illustrations. Your header is a real repository asset, not a live widget service.

<details>
<summary>Copy Markdown</summary>

~~~markdown
![Profile header](../assets/header.svg)
~~~

</details>

[Inspect the SVG source](../assets/header.svg).

## A22 Animations

<img src="../assets/typing.svg" width="800" alt="Colorful typing animation">

Animated SVG or GIF assets use the same image embedding pattern. GIFs need an actual GIF file; this working demo uses your SVG. This animation includes a reduced-motion fallback.

<details>
<summary>Copy Markdown</summary>

~~~markdown
![Typing animation](../assets/typing.svg)
~~~

</details>

## A23 Badges and link buttons

Demo badges, not repository status claims:

![Demo version badge](https://img.shields.io/badge/demo-v0.1.0-8250df)
![Demo label badge](https://img.shields.io/badge/example-verified-1a7f37)

[![Open projects](https://img.shields.io/badge/Open_projects-0969da?logo=github&logoColor=white&style=for-the-badge)](https://github.com/Majkey25?tab=repositories)

Badges are images. A surrounding link makes a badge behave like a navigation button.

<details>
<summary>Copy Markdown</summary>

~~~markdown
![Demo label](https://img.shields.io/badge/example-verified-1a7f37)

[![Open projects](https://img.shields.io/badge/Open_projects-0969da?logo=github&logoColor=white&style=for-the-badge)](https://github.com/Majkey25?tab=repositories)
~~~

</details>

## A24 Icon row

<img src="https://skillicons.dev/icons?i=py,ts,kotlin,react&theme=dark" height="48" alt="Python, TypeScript, Kotlin, and React icons">

This is an external image service, not native text formatting. A repository copy of the SVG can remove the viewing-time dependency.

<details>
<summary>Copy HTML</summary>

~~~html
<img src="https://skillicons.dev/icons?i=py,ts,kotlin,react&theme=dark"
     height="48" alt="Python, TypeScript, Kotlin, and React icons">
~~~

</details>

## A25 Music and activity cards

Your restored Spotify snapshot:

<a href="https://open.spotify.com/user/an3l6poe03o6g6htrdrs0hgjy">
  <img src="https://raw.githubusercontent.com/Majkey25/Majkey25/output/spotify.svg"
       width="300" alt="Recently played Spotify tracks">
</a>

Music cards, contribution animations, coding-time cards, and statistics are generated assets. They need a service, data access, or a workflow; Markdown itself does not fetch the underlying data. Your card is refreshed by the repository workflow and retains its last valid snapshot during provider failures.

<details>
<summary>Copy HTML</summary>

~~~html
<a href="https://open.spotify.com/user/an3l6poe03o6g6htrdrs0hgjy">
  <img src="https://raw.githubusercontent.com/Majkey25/Majkey25/output/spotify.svg"
       width="300" alt="Recently played Spotify tracks">
</a>
~~~

</details>

## A26 Maps

Demo geography; this is not a personal location.

~~~geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {"name": "Demo city marker"},
      "geometry": {"type": "Point", "coordinates": [14.42, 50.08]}
    }
  ]
}
~~~

GitHub can render GeoJSON and TopoJSON maps from their respective code fences. [Native map syntax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-geojson-and-topojson-maps).

<details>
<summary>Copy Markdown</summary>

~~~~markdown
~~~geojson
{
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "properties": {"name": "Demo city marker"},
    "geometry": {"type": "Point", "coordinates": [14.42, 50.08]}
  }]
}
~~~
~~~~

</details>

## A27 Three-dimensional models

A small demo tetrahedron:

~~~stl
solid demo
  facet normal 0 0 -1
    outer loop
      vertex 0 0 0
      vertex 0 1 0
      vertex 1 0 0
    endloop
  endfacet
  facet normal 0 -1 0
    outer loop
      vertex 0 0 0
      vertex 1 0 0
      vertex 0 0 1
    endloop
  endfacet
  facet normal -1 0 0
    outer loop
      vertex 0 0 0
      vertex 0 0 1
      vertex 0 1 0
    endloop
  endfacet
  facet normal 0.57735 0.57735 0.57735
    outer loop
      vertex 1 0 0
      vertex 0 1 0
      vertex 0 0 1
    endloop
  endfacet
endsolid demo
~~~

GitHub supports [ASCII STL in fenced blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-stl-3d-models). Copy this section's block from source view to reuse it.

## A28 Video and downloads

[Open or save this showcase as Markdown](https://raw.githubusercontent.com/Majkey25/Majkey25/main/docs/README-showcase.md)

Video needs an uploaded media asset. GitHub supports [video attachment formats](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files); paste its generated attachment URL into the document after upload. There is no demo clip in this repository.

For YouTube or a hosted demo, use a clickable thumbnail or a normal link. A README cannot host an arbitrary iframe player.

<details>
<summary>Copy the Markdown source link</summary>

~~~markdown
[Markdown source](https://raw.githubusercontent.com/Majkey25/Majkey25/main/docs/README-showcase.md)
~~~

</details>

## A29 Automated content

A README can display generated or regularly updated content:

| Idea | Needed |
| --- | --- |
| Latest blog posts | A public feed and a job that updates Markdown |
| Latest releases | Release data and an update job |
| Contribution animation | A generator, already present in this repo |
| Music history | Spotify data and a generated card, already present here |
| Real CI/version badges | A badge URL tied to a real workflow or release |

Automation lives outside Markdown. [Your actual workflow](../.github/workflows/animations.yml) generates the cards; the README embeds them.

<details>
<summary>See the existing schedule syntax</summary>

~~~yaml
on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:
~~~

</details>

## A30 Source-only features

Escaped symbols: \*literal asterisks\* · \#literal hash

Emoji aliases: :wrench: :musical_note: :sparkles:

<!-- This example note is visible only in the Markdown source. -->

Explicit repository links are reliable in a README: [profile](https://github.com/Majkey25) and [example PR](https://github.com/Majkey25/Majkey25/pull/10). Mentions, issue references, color chips, and rich previews have context-dependent behavior; color chips are documented for issues, PRs, and discussions, not README text.

<details>
<summary>Copy Markdown</summary>

~~~markdown
\*literal asterisks\*
<!-- Maintainer note hidden from readers. -->
:wrench: :musical_note: :sparkles:
[Profile](https://github.com/Majkey25)
~~~

</details>

## Where GitHub stops

GitHub sanitizes rendered HTML. Arbitrary scripts, inline styles, and custom classes do not turn a README into a web app. [GitHub's rendering pipeline](https://github.com/github/markup#github-markup) documents this limitation.

- For custom colors or graphics, use an SVG or image asset.
- For real interactive controls, embeds, or dashboards, link to a website.
- External cards may need accounts or services. Static badges do not prove a build passed.
- Upload a real image, GIF, or video before referencing that asset. A placeholder filename cannot produce a preview.

[^evidence]: Footnote demo. In real project documentation, put the relevant source, benchmark, or validation link here.
