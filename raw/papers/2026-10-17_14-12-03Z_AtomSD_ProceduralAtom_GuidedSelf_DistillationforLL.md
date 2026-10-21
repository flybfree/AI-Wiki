---
title: AtomSD: Procedural Atom-Guided Self-Distillation for LLM Agents
published: 2026-10-17T14:12:03Z
authors: Bohan Yu, Pengfei Cao, Kai Tian, Chen Han, Shi-Yang Li, Chenxi Zhou, Junlin Liu, Cao Liu, Ke Zeng, Jun Zhao, Kang Liu
url: http://arxiv.org/abs/2610.26926v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AtomSD: Procedural Atom-Guided Self-Distillation for LLM Agents

## Abstract
Large language models (LLMs) possess broad factual knowledge and strong reasoning capabilities, but solving complex tasks also requires procedural knowledge about how to act. Existing approaches often represent procedural knowledge through trajectories or bundled skills, limiting flexible reuse across interaction histories. This paper introduces Procedural Atoms, fine-grained and independently applicable units that represent Intent, When, Do, and Avoid guidance. Building on this representation, we propose AtomSD, an Atom-guided Self-Distillation framework in which the learner continually extracts Procedural Atoms from its own successful trajectories and distills them into the evolving policy through Atom-conditioned supervision and task-reward optimization. Comprehensive experiments show that AtomSD consistently outperforms strong reward-based and distillation methods, exceeding the state-of-the-art baseline by up to 9.31 points in average performance. Further analyses demonstrate that the proposed Procedural Atoms provide effective guidance, highlighting the value of atom-level procedural knowledge for policy learning.

## Metadata
- **Published**: 2026-10-17T14:12:03Z
- **Authors**: Bohan Yu, Pengfei Cao, Kai Tian, Chen Han, Shi-Yang Li, Chenxi Zhou, Junlin Liu, Cao Liu, Ke Zeng, Jun Zhao, Kang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26926v1)