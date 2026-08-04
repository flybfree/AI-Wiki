---
title: Is More Privileged Information Better? From Solution Traces to Problem-Solving Structure in Self-Distilled Reasoning
published: 2026-08-03T01:47:25Z
authors: Xuyang Zhao, Liting Zhang, Zichen Xu, Zhihu Wang, Xu Caiyue, Shiwan Zhao, Qicheng Li
url: http://arxiv.org/abs/2608.01589v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is More Privileged Information Better? From Solution Traces to Problem-Solving Structure in Self-Distilled Reasoning

## Abstract
On-policy self-distillation (OPSD) improves reasoning by using a privileged view of a model conditioned on reference solutions to supervise a student view that observes only the question. However, the teacher-provided token-level targets may depend on reference-specific information unavailable at inference time. We propose Problem-Space-Guided OPSD (PS-OPSD), which replaces the complete solution with trajectory-grounded guidance describing the initial state, goal conditions, constraints, and a selected state-transition path. The student rollout and OPSD objective remain unchanged. Across three mathematical reasoning benchmarks and model scales ranging from 1.7B to 8B, PS-OPSD achieves the highest aggregate question-only accuracy among the compared methods. Controlled experiments further indicate that guidance relevance and path coherence contribute to these gains, highlighting the representation of privileged information as an important design choice in OPSD.

## Metadata
- **Published**: 2026-08-03T01:47:25Z
- **Authors**: Xuyang Zhao, Liting Zhang, Zichen Xu, Zhihu Wang, Xu Caiyue, Shiwan Zhao, Qicheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01589v1)