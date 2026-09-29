---
title: ExpVoyager: Direct Experience Navigation for Dynamic Agent Skill Synthesis
published: 2026-09-26T13:48:10Z
authors: Kwangwook Seo, Dongha Lee
url: http://arxiv.org/abs/2609.32630v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ExpVoyager: Direct Experience Navigation for Dynamic Agent Skill Synthesis

## Abstract
Learning from experience in LLM agents has become a key paradigm for developing self-evolving agents that continuously learn and expand their capabilities. Within this paradigm, synthesizing the agent skill has emerged as a promising solution for transforming accumulated experience into reusable procedural knowledge, serving as an important layer for the harness system that supplies agents at runtime. Despite its potential, existing approaches largely abstract past experience into fixed procedural knowledge before downstream demands are known, which risks discarding knowledge that later becomes critical while retaining instance-specific details irrelevant to future tasks. In this paper, we reframe agent skill synthesis as a dynamic navigation problem over past experience, where agents actively explore accumulated trajectories on demand for the current task with targeted and fine-grained access to experience knowledge. To this end, we propose ExpVoyager, a novel framework in which a skill curator navigates raw experience across different views and resolutions, continually identifying reusable procedural knowledge from what it observes while tracking remaining knowledge needs that guide where to navigate next. Extensive experiments demonstrate both the effectiveness and versatility of ExpVoyager, showing consistent improvements in downstream task performance, continual gains as the experience space scales, and practical compatibility with existing skills under efficient experience access.

## Metadata
- **Published**: 2026-09-26T13:48:10Z
- **Authors**: Kwangwook Seo, Dongha Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32630v1)