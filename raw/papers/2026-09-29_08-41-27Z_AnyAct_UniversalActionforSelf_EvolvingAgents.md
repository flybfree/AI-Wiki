---
title: AnyAct: Universal Action for Self-Evolving Agents
published: 2026-09-29T08:41:27Z
authors: Lingrui Xu, Yangqin Jiang, Jiachang Zhang, Xubin Ren, Chao Huang
url: http://arxiv.org/abs/2609.37025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AnyAct: Universal Action for Self-Evolving Agents

## Abstract
As large language models (LLMs) advance, AI agents are increasingly deployed in open-world environments to tackle complex sequential tasks (e.g., document processing, cross-application collaboration), relying heavily on actions ranging from GUI operations to semantic APIs. However, three core challenges persist: the "scale dilemma" of massive tool ecosystems exceeding LLM context windows, the "non-stationarity" of tool quality due to updates or outages, and the "heterogeneity" of feedback formats (pixels, text, structured data) creating information silos. To address these, we propose AnyAct, a universal action layer that unifies available capabilities into a self-evolving action space, enabling agents to operate efficiently and reliably in large-scale, dynamic tool ecosystems. AnyAct's core design focuses on two objectives: constructing this action space via hierarchical progressive retrieval (filtering task-relevant actions) and test-time reliability evolution (pruning unreliable actions), and enabling reliability-aware action orchestration through a heterogeneous observation grounding module that unifies multi-modal feedback. Additionally, it defines a hybrid action space (primitive + semantic actions) and optimizes for a balance between task success rate and execution cost. Evaluations on LiveMCPBench and OSMCP (a new benchmark we developed for multi-granularity action collaboration) demonstrate state-of-the-art performance. AnyAct delivers substantial performance gains over baseline methods across various LLM base models on LiveMCPBench and improvements are particularly notable for models with constrained native capabilities. On OSMCP, it achieves 77.27% overall success with only 50 steps, which is half the steps required by most competitors.

## Metadata
- **Published**: 2026-09-29T08:41:27Z
- **Authors**: Lingrui Xu, Yangqin Jiang, Jiachang Zhang, Xubin Ren, Chao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37025v1)