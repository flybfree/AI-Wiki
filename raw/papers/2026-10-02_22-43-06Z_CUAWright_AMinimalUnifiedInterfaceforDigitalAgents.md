---
title: CUAWright: A Minimal Unified Interface for Digital Agents
published: 2026-10-02T22:43:06Z
authors: Yadong Lu, Theodore Lee, Yifei Li, Lawrence Keunho Jang, Tianci Xue, Yu Su, Huan Sun, Ahmed Hassan Awadallah
url: http://arxiv.org/abs/2610.04116v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CUAWright: A Minimal Unified Interface for Digital Agents

## Abstract
The prevailing approach to computer-use agents couples a model with a domain-specific harness: a browser or desktop environment equipped with human engineered tools that are fixed before task execution. As models' coding capabilities improve, the GUI native and static harness prevents them from direct programmatic operation on system state, as well as flexible construction of tools. To this end, we introduce CUAWright, a minimal terminal harness of roughly 3K lines of code that uses bash commands as its sole action interface, and a file system as its evolvable space for dynamically creating tools and managing the context. We conduct comprehensive experiments across a wide range of digital tasks, and demonstrate that by giving the agent a minimal, programmable interface, it achieves substantially stronger results compared to their GUI or hybrid CLI interface across a wide range of tasks. On OSWorld 2.0, CUAWright delivers a 33.2% relative improvement in partial reward while reducing estimated cost by 37.5% compared with the published GPT-5.5 baseline. On Online-Mind2Web and the long horizon Odysseys benchmark, CUAWright substantially outperforms GUI native harness by 4.7% and 44.0% in success rate, respectively. Furthermore, we found the gains extend to CAD applications that require accurate visual understanding and CLI interaction: on CADGenBench and BenchCAD, our unified harness yields 8.1%-41.6% relative improvements over other CLI based harnesses with GPT-5.5. Together, these results suggest digital environments are far more programmable than their GUI interfaces imply, and a minimal terminal-focused harness is the key for better performance and efficiency.

## Metadata
- **Published**: 2026-10-02T22:43:06Z
- **Authors**: Yadong Lu, Theodore Lee, Yifei Li, Lawrence Keunho Jang, Tianci Xue, Yu Su, Huan Sun, Ahmed Hassan Awadallah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04116v1)