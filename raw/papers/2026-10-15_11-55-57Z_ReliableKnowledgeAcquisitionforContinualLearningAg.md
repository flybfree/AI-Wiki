---
title: Reliable Knowledge Acquisition for Continual Learning Agents
published: 2026-10-15T11:55:57Z
authors: Yixu Huang, Jiaqi W. Ma
url: http://arxiv.org/abs/2610.21739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reliable Knowledge Acquisition for Continual Learning Agents

## Abstract
As agents powered by foundation models move into open-ended environments, continual learning from experience becomes essential. For agents built on models with fixed parameters, this learning requires reusing prior task experience in context to improve performance and efficiency on future tasks. Existing memory and experience-learning systems typically focus on either retained facts or procedures, and lack a mechanism for establishing the reliability of claims extracted from the ongoing task stream. Indeed, we find that approximately 12--33\% of entries produced by representative systems harm future task performance when reused. To address these limitations, we propose \textbf{RIKA} (Reliable Knowledge Acquisition), which combines hierarchical extraction of factual, conceptual, procedural, and metacognitive knowledge with Evidence-based Knowledge Admission, which uses source evidence and subsequent experience to govern which claims enter the task agent's context, without additional validation tasks. Across six task streams from Continual Learning Bench and four model backbones, RIKA achieves the highest aggregate score on every backbone.

## Metadata
- **Published**: 2026-10-15T11:55:57Z
- **Authors**: Yixu Huang, Jiaqi W. Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21739v1)