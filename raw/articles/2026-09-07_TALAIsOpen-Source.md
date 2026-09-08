---
title: TALA Is Open-Source
date: 2026-09-07
url: https://d2lang.com/blog/tala-is-open-source/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://d2lang.com/blog/tala-is-open-source/
source_feed: Hacker News
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-07 20:16
---

# TALA Is Open-Source

## Full Article

Following up on the announcement
here
, TALA (Terrastruct's AutoLayout Algorithm) is now open-source under the same license as D2 (MPL-2.0).
TALA is a novel autolayout algorithm designed with software architecture diagrams in mind. This means it's primarily an orthogonal layout engine, which more closely matches what you might find on whiteboards, rather than the DAG-based ones that grow in one direction. It blends ideas from different graph-drawing research papers (cited in source code) along with original techniques to achieve aesthetic diagrams. It considers multiple objectives of "aesthetic", including symmetry, median distance, flow, clustering of like nodes, and much more.
I'll keep the text short and lead with examples.
The first batch compares diagrams rendered with TALA with the other two layout algorithms D2 comes with -- Dagre and ELK. These are not hand-selected, I just found public d2 files from around GitHub. So for some, you may very well prefer the not-TALA layout.
The second batch demonstrates a unique property of TALA, which is that node positions and sizes can be customized, e.g. locking in the coordinates. This lends itself especially well to agentic use cases, where models can draw in 2D space well, but TALA still takes care of routing, which models still struggle with. I had AI generate these.
The third batch demonstrates TALA's capability to support a hybrid of some nodes specifying coordinates and some left to the layout engine. You might have a specific shape of a collection of nodes in mind, which you can specify with coordinates, and TALA can take care of the rest. Again, AI generated.
Please also note that TALA is not without tradeoffs.
It has randomness in the algorithm. It finds the best layout by using a default of 3 seeds and choosing the one scored the best. Given the same seeds and same input, it'll produce the same diagram. But let's say you just add one more node. The diagram could look completely different. In Dagre and ELK, it looks mostly the same as prior, with the extra node accommodated for. This is sometimes desirable.
It doesn't do DAGs as well. I often find myself preferring Dagre or ELK when I want a long flowing graph.
It can take longer to run for larger diagrams -- scaling nonlinearly. For a benchmark of TALA's runtime performance compared to others, see
https://github.com/d2lang/d2-benchmarks
.
TALA comes bundled into D2 v0.9.0, so just install and specify with
--layout=tala
to try it out! Or head on over to
https://play.d2lang.com
, which runs 100% client-side. I especially look forward to the improvements that being open-source brings, and can't wait to see what improvements and ideas are submitted by the community.
Special thanks to Gavin Nishizawa for substantial broad contributions across TALA, and JÃºlio CÃ©sar Batista for his work on hierarchy algorithms and more. It was so fun getting to work on such interesting stuff with you guys.
Batch 1: Comparisons
â
Fulcro RAD architecture
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[Fulcro RAD architecture rendered with TALA]
Dagre
Open SVG â
[Fulcro RAD architecture rendered with Dagre]
ELK
Open SVG â
[Fulcro RAD architecture rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
Mocha secure-enclave SoC
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[Mocha secure-enclave SoC rendered with TALA]
Dagre
Open SVG â
[Mocha secure-enclave SoC rendered with Dagre]
ELK
Open SVG â
[Mocha secure-enclave SoC rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
Jupyter on AWS EKS
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[Jupyter on AWS EKS rendered with TALA]
Dagre
Open SVG â
[Jupyter on AWS EKS rendered with Dagre]
ELK
Open SVG â
[Jupyter on AWS EKS rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
Lion Reader frontend data flow
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[Lion Reader frontend data flow rendered with TALA]
Dagre
Open SVG â
[Lion Reader frontend data flow rendered with Dagre]
ELK
Open SVG â
[Lion Reader frontend data flow rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
ROSS rotor-dynamics workflow
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[ROSS rotor-dynamics workflow rendered with TALA]
Dagre
Open SVG â
[ROSS rotor-dynamics workflow rendered with Dagre]
ELK
Open SVG â
[ROSS rotor-dynamics workflow rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
Go Queue worker architecture
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[Go Queue worker architecture rendered with TALA]
Dagre
Open SVG â
[Go Queue worker architecture rendered with Dagre]
ELK
Open SVG â
[Go Queue worker architecture rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
Ouroboros Leios simulator
â
Side by side
TALA
Dagre
ELK
D2 source â
TALA
Open SVG â
[Ouroboros Leios simulator rendered with TALA]
Dagre
Open SVG â
[Ouroboros Leios simulator rendered with Dagre]
ELK
Open SVG â
[Ouroboros Leios simulator rendered with ELK]
Select a diagram to enlarge it. Each layout is scaled to fit its panel.
Batch 2: Custom positioning
â
Signal House
â
TALA Â· positioned with top / left
D2 source â
Open SVG â
[Signal House]
View D2 source
Atlas / Data platform
â
TALA Â· positioned with top / left
D2 source â
Open SVG â
[Atlas / Data platform]
View D2 source
Night shift / Mission control
â
TALA Â· positioned with top / left
D2 source â
Open SVG â
[Night shift / Mission control]
View D2 source
Friday deploy: the escape room
â
TALA Â· positioned with top / left
D2 source â
Open SVG â
[Friday deploy: the escape room]
View D2 source
The Internet is a jellyfish
â
TALA Â· positioned with top / left
D2 source â
Open SVG â
[The Internet is a jellyfish]
View D2 source
Orbital coffee logistics
â
TALA Â· positioned with top / left
D2 source â
Open SVG â
[Orbital coffee logistics]
View D2 source
Cloud Conservatory
â
TALA Â· positioned with top / left
D2 + icons â
Open SVG â
[Cloud Conservatory]
View D2 source
Velvet Rope
â
TALA Â· positioned with top / left
D2 + icons â
Open SVG â
[Velvet Rope]
View D2 source
Synthwave City
â
TALA Â· positioned with top / left
D2 + icons â
Open SVG â
[Synthwave City]
View D2 source
Batch 3: Partial positioning
â
The Printing Room
â
TALA Â· 4 pinned nodes / 10 automatic nodes
D2 + icons â
Open SVG â
[The Printing Room]
Pinned:
The four CMYK stations share a fixed top coordinate and equally spaced left coordinates so the print sequence retains its mechanical alignment.
Automatic:
TALA positions the feeder, camera, registration controller, dryer, prepress and finishing steps; none has top or left.
See the positioning declarations
View D2 source
MULE / Utility Rover
â
TALA Â· 4 pinned nodes / 11 automatic nodes
D2 + icons â
Open SVG â
[MULE / Utility Rover]
Pinned:
The four motor assemblies are fixed at the front and rear corners of the chassis rectangle.
Automatic:
TALA places every controller, sensor, power and safety node between or around those corners and arranges the unpositioned fleet container.
See the positioning declarations
View D2 source
Sources and rendering details
The seven layout comparisons use public project diagrams from D2's
real-world fixtures
.
Each comparison uses the same D2 source and the same compiler build, changing
only the layout engine. Source styles, themes, and explicit grid constraints
are preserved. Some fixture icons were already replaced with built-in shapes.
SVGs are scaled independently to fit each panel. Use
Open SVG
to inspect
labels and connections at a larger size.
Source provenance and licenses
Â·
Render settings and revisions
The eleven positioning examples are original, fictional compositions rendered with
TALA using the same public D2 build. Icon downloads include the full source and local
vector assets. The two partial-positioning examples apply top/left only to their
listed pinned nodes; all other nodes and every container are automatically placed.
Positioning render settings
.

## Metadata
- **Source**: [Original Article](https://d2lang.com/blog/tala-is-open-source/)
