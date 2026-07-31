---
title: VeriSkill: A Self-Evolution Framework for Program Verification Skills
published: 2026-07-30T06:15:29Z
authors: Changguo Jia, Tianqi Zhao, Zhiyou Xiao, Weiming Zhang, Minghui Zhou
url: http://arxiv.org/abs/2607.27733v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VeriSkill: A Self-Evolution Framework for Program Verification Skills

## Abstract
Automating program verification with LLM agents requires generating specifications, annotations, auxiliary lemmas, and tool invocations, all of which depend on reusable skills. A natural remedy is skill self-evolution: distilling skills from trajectories and refining them through feedback. However, existing evolution methods struggle with program verification tasks because they cannot reliably identify skill-specific failures or extract actionable signals from opaque verifier feedback. In this paper, we propose VeriSkill, a self-evolution framework built for program verification. It attributes verification failures to skill deficiencies, distills diagnostic signatures into reusable lessons, and iteratively refines candidate skills, admitting only revisions that improve verification performance while preserving program semantics. Experiments show that VeriSkill consistently outperforms all baselines across multiple verification tools, agent frameworks, and LLM backends.

## Metadata
- **Published**: 2026-07-30T06:15:29Z
- **Authors**: Changguo Jia, Tianqi Zhao, Zhiyou Xiao, Weiming Zhang, Minghui Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27733v1)