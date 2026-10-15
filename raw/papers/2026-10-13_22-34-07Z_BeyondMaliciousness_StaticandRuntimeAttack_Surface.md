---
title: Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills
published: 2026-10-13T22:34:07Z
authors: Ratnesh Pandey, Japneet Singh, Harsh Akshit, Sonali Tyagi, Cassie Crossley
url: http://arxiv.org/abs/2610.19264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills

## Abstract
Agent skills are Markdown documents that a tool-using agent reads as instructions and then acts on with the privileges of the session that loaded them. Installing one grants authority (the standing to direct the agent, not new privilege), and the size of that grant is what we measure. We present a two-phase attack-surface profiling methodology that combines whole-bundle static analysis and dependency provenance checking with instrumented sandbox execution and separate model-based assessment of the resulting traces. We apply the methodology to 6,309 listings from two marketplaces, selecting listings for execution without conditioning that decision on a prior threat or risk signal. Half the corpus carries evidence of shell-execution capability; the corresponding shares are 35% for filesystem read, 31% each for filesystem write and network egress, and 13% for credential access; seven listings in ten carry at least one elevated capability. That is the surface a user accepts at install time, and almost none of it is visible then. A permission model exists but is close to inert. Authors may list the tools a skill pre-approves in its own frontmatter, which removes confirmation prompts rather than restricting what the skill can reach; of the 6,061 listings whose frontmatter parses, 770 declare anything at all, the vocabulary cannot express credential or environment access, and nothing checks what it does express against the bundle. Declaring is also not declaring accurately: 59% of declaring listings understate what their bundle can do. ClawHub declares roughly twice as often as skillsmp, yet under-declares on 88% of its declarations against 31%. Triage at the marketplace boundary therefore cannot rest on what a listing declares. It must rest on what the bundle can do. These results position capability-oriented attack-surface profiling as a necessary complement to maliciousness detection.

## Metadata
- **Published**: 2026-10-13T22:34:07Z
- **Authors**: Ratnesh Pandey, Japneet Singh, Harsh Akshit, Sonali Tyagi, Cassie Crossley
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19264v1)