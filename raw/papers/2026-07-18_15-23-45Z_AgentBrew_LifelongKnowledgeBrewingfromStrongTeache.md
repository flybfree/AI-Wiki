---
title: AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents
published: 2026-07-18T15:23:45Z
authors: Yangqin Jiang, Chao Huang
url: http://arxiv.org/abs/2607.16851v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentBrew: Lifelong Knowledge Brewing from Strong Teachers to Weak LLM Agents

## Abstract
Deploying LLM agents typically requires a compact test-time student, even if a stronger teacher is available during training. We study knowledge brewing: distilling a teacher's interactive experience into a persistent external memory for the student. Crucially, this requires no weight updates, expert demonstrations, ground-truth labels, or test-time teacher access. This setting poses two challenges: environments provide only sparse, binary feedback, and teacher-authored notes must be inherently tailored to be concretely executable by a substantially weaker student. To address these hurdles, we propose AgentBrew, comprising two coupled components. First, a failure-triggered teacher--Ralph Loop mitigates sparse feedback by transforming student failures into environment-validated notes. Second, student-aware synthesis calibrates teacher knowledge to the weak executor's operational granularity, yielding model-specific, actionable guidance. Extensive evaluations and comprehensive ablations across coding, math, and tool-use tasks demonstrate that this asymmetric, training-free brewing paradigm produces highly capable yet deployable LLM agents.

## Metadata
- **Published**: 2026-07-18T15:23:45Z
- **Authors**: Yangqin Jiang, Chao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16851v1)