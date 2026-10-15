---
title: Measuring and Reducing Unusable Replies of LLM Agents
published: 2026-10-14T06:35:49Z
authors: Yilin Jiang, Fei Tan, Xuanyu Yin, Guanchu Wang, Xia Hu, Yutao Yue
url: http://arxiv.org/abs/2610.19659v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring and Reducing Unusable Replies of LLM Agents

## Abstract
People delegate multi-step work to LLM agents and read only the reply that the agent hands back. Current evaluation scores task completion and the faithfulness of reports, and it leaves open whether the requester can understand and use the reply. We call this property reply usability and measure it with a reader model that takes the requester's position and tests whether the reply can be interpreted from what the requester has seen, is in the requester's language and answers the request. Its agreement with the majority of five annotators lies within the range of the individual annotators. Across eight models from seven families, 54% of 480 replies fail, and the best model still fails on 30%. Failed replies mostly point to material the requester has not seen or use labels that the agent coined during its work. Stating explicit requirements for the reply reduces the failure rate from 0.52 to 0.43 together with errors and omissions, and a secondary model that rewrites the reply reduces it to 0.36, which human annotators confirm in a blind comparison. Reply usability can thus be scored alongside task success and improved with one appended message or one call to a secondary model.

## Metadata
- **Published**: 2026-10-14T06:35:49Z
- **Authors**: Yilin Jiang, Fei Tan, Xuanyu Yin, Guanchu Wang, Xia Hu, Yutao Yue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19659v1)