---
title: HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants
published: 2026-11-25T16:11:53Z
authors: Yifei Xu, Li Yu, Zhaoyang Liu, Ce Wang, Sen Huang, Yanyan Shen, Yun Lin, Linpeng Huang, Hong Mei
url: http://arxiv.org/abs/2611.34624v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HoMe: Toward Practical Harness Optimization of Memory Systems for AI Assistants

## Abstract
The behavior of memory systems for long-running AI assistants is governed by a harness, which consists of the code, prompts, and configurations for memory construction, maintenance, retrieval, and answer generation. However, optimizing the harness of a memory system remains largely manual, and unrestricted editing alone does not ensure structural improvements. In this paper, we introduce HoMe, an evaluation-driven framework that iteratively evaluates candidate harnesses and derives each new candidate from any previously evaluated harness by editing any part of it. HoMe combines session-level memory versioning with execution traces to identify shared failure mechanisms across cases and localize them to the responsible sessions and harness components. It encourages early structural exploration through candidate gating and reduces evaluation cost through smoke tests, adaptive sampling, and the reuse of constructed memory. We validate HoMe with the open-source memory system ReMe on two large-scale long-horizon memory benchmarks, LongMemEval-S and BEAM. With six formal candidate evaluations per benchmark, after a full initial evaluation, HoMe discovers harnesses that improve end-task performance over the originally strong harness while consuming far fewer query-time tokens. The code is available at https://github.com/agentscope-ai/ReMe.

## Metadata
- **Published**: 2026-11-25T16:11:53Z
- **Authors**: Yifei Xu, Li Yu, Zhaoyang Liu, Ce Wang, Sen Huang, Yanyan Shen, Yun Lin, Linpeng Huang, Hong Mei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.34624v1)