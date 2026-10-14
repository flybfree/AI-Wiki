---
title: Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills
published: 2026-10-13T07:23:34Z
authors: Letian Zhu, Han Li, Yifan Yao, Xinping Lei, Xinyu Che, Jiahao Wang, Dianyi Wang, Yucheng Fu, Jiakai Wang, Zhiqi Bai, Wenbo Su, Jiaheng Liu
url: http://arxiv.org/abs/2610.17860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills

## Abstract
Agent Skills improve LLM agents by making task knowledge reusable across sessions. Learning transferable Skills requires evidence about a procedure and its conditions of use, which a successful task attempt can leave untested. We introduce Socratic Skill Learning (SSL), which interleaves expert teaching with Student practice. An Educator guides investigation while the Student remains the sole environment operator and Skill author, able to question, test, and adapt advice. To test reuse beyond the learning task, we construct SkillTransferBench, with 35 task families and 408 executable cases, pairing public variation specifications with held-out evaluation in fresh solver sessions. On the main 22-family, 155-case cohort, Fixed-Window SSL reaches 0.801 utility, versus 0.723 without a Skill, 0.761 for adapted Trace2Skill (trajectory distillation), and 0.751 for adapted SKILL-KD (contrastive distillation). Across three model pairs on shared families, interleaved guidance outperforms expert authoring and post-hoc teaching. Process analysis links guidance to Student writing and package revision; a case study shows the Student testing and refining a proposed procedure for later reuse. As demand for new lessons falls, the cost of fixed-window review grows. Issue-Guided SSL tracks unresolved questions across Skill revisions to select and focus review, reaching 0.805 utility with 61.7% fewer Educator tokens and 16.9% fewer total acquisition tokens than Fixed-Window SSL on the main cohort.

## Metadata
- **Published**: 2026-10-13T07:23:34Z
- **Authors**: Letian Zhu, Han Li, Yifan Yao, Xinping Lei, Xinyu Che, Jiahao Wang, Dianyi Wang, Yucheng Fu, Jiakai Wang, Zhiqi Bai, Wenbo Su, Jiaheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17860v1)