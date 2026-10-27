---
title: WebViSE: Scaling Visual Design Intelligence from the Open Web for LLM Website Generation
published: 2026-10-24T21:43:29Z
authors: Yifei Sun, Peng Zhao, Le Zhang, Bingjin Chen, Zhengfan Wu
url: http://arxiv.org/abs/2610.33929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WebViSE: Scaling Visual Design Intelligence from the Open Web for LLM Website Generation

## Abstract
Large language models have made remarkable strides in website development, enabling complete and interactive web experiences to be built from natural-language instructions with far less effort. Yet, non-expert users often struggle to articulate sophisticated visual and interaction designs in natural language. Meanwhile, the open web already contains a vast reservoir of such design knowledge, embodied in mature website implementations. To this end, we introduce Website-derived Visual Skill Extraction (WebViSE), a framework that automatically abstracts these implementations into reusable Visual Skills and builds a structured Skill library. To scale the library, WebViSE organizes its Skills in a multi-parent DAG and jointly evolves Skill descriptions and DAG structure using Skill-conditioned Potential Queries, enabling efficient matching between diverse user instructions and relevant Skills. The auto-evolved structure outperforms non-hierarchical LLM retrieval baselines at only 39.09% of the estimated retrieval cost with Qwen3.8-Max. For any models, WebViSE can be directly injected as plug-and-play guidance, enabling diverse models to produce more visually compelling and aesthetically refined web pages. For open-source models, WebViSE can be used to build a data-synthesis pipeline that internalizes visual design intelligence into model weights. Experiments across multiple web development benchmarks and human evaluation consistently show that WebViSE improves the visual quality and interaction fidelity of artifacts. Overall, our work establishes an automated path for extracting, organizing, and transferring design intelligence from the open web to website-building models. We release all extracted Visual Skills, the associated Skill DAG, and our code at https://github.com/YifeiSun-0710/WebViSE.

## Metadata
- **Published**: 2026-10-24T21:43:29Z
- **Authors**: Yifei Sun, Peng Zhao, Le Zhang, Bingjin Chen, Zhengfan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33929v1)