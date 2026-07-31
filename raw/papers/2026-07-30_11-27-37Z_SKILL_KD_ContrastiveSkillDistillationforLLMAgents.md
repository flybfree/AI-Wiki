---
title: SKILL-KD: Contrastive Skill Distillation for LLM Agents
published: 2026-07-30T11:27:37Z
authors: Qiming Shi, Yibo Dou, Jiawen Zhu, Yulong Tao, Linbo Jin, Zhaolu Kang, Yunfan Zhou, Di Weng
url: http://arxiv.org/abs/2607.28048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SKILL-KD: Contrastive Skill Distillation for LLM Agents

## Abstract
Skill-based prompting has become a practical mechanism for improving large language model (LLM) agents, yet existing skill acquisition methods often treat skills as experience summaries, memory entries, or direct summaries of successful demonstrations. This creates a mismatch for weaker student agents: when a student fails because it lacks task knowledge or operational strategy, its failed trajectory may not contain enough evidence to infer the missing behavior, while the teacher trajectory may be too implicit to be internalized as reusable guidance. We propose SKILL-KD, a contrastive skill distillation framework that treats skills as an explicit distillation medium between agents of different capabilities. Given a student failure and the teacher trajectory on the same task, SKILL-KD distills their actionable discrepancy into a textual skill patch, evaluates the patch by re-running the student, and iteratively refines the patch when the student still fails. To prevent repeated local updates from causing skill drift, SKILL-KD further maintains trace-linked edit histories and performs Drift-Aware Skill Consolidation, deciding whether each patch should add a new rule, delete or modify an existing rule, or be skipped. Across five agent benchmarks and two student settings, SKILL-KD consistently improves frozen student agents over fixed-model adaptation baselines.

## Metadata
- **Published**: 2026-07-30T11:27:37Z
- **Authors**: Qiming Shi, Yibo Dou, Jiawen Zhu, Yulong Tao, Linbo Jin, Zhaolu Kang, Yunfan Zhou, Di Weng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28048v1)