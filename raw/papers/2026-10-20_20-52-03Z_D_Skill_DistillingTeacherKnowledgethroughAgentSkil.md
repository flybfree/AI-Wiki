---
title: D-Skill: Distilling Teacher Knowledge through Agent Skills
published: 2026-10-20T20:52:03Z
authors: Shuo Yuan, Dacheng Li, Joseph E. Gonzalez
url: http://arxiv.org/abs/2610.28914v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# D-Skill: Distilling Teacher Knowledge through Agent Skills

## Abstract
Frontier language-model agents excel at complex tasks, but high inference costs make transferring their capabilities to smaller models essential. Traditional knowledge distillation achieves this through parameter updates, requiring access to the student's weights and additional training compute while encoding the transferred knowledge implicitly in the parameters. We introduce D-Skill, a framework that treats the teacher as a black box and distills its behavioral advantage into an interpretable natural-language skill by analyzing paired rollouts and identifying behavioral divergences and agreements. The resulting lessons are consolidated offline, with any compatible skill-update backend, into a skill document that is provided to the student at inference time. D-Skill constructs the skill entirely offline from fixed trajectories, without labels, further environment interaction, or weight updates after rollout collection. Across SpreadsheetBench-Verified, ALFWorld, and chess puzzles spanning multiple teacher-student pairs, D-Skill closes 75%-95% of the teacher-student gap without touching model weights. After a single offline pass over the paired traces, D-Skill outperforms one-epoch SFT baselines and remains competitive with multi-epoch SFT. Under the same model family, the resulting student also incurs 5.7x-8.3x lower inference cost per task than the teacher. Our results demonstrate that natural-language skill distillation offers a performant, interpretable, and efficient alternative to weight-based capability transfer.

## Metadata
- **Published**: 2026-10-20T20:52:03Z
- **Authors**: Shuo Yuan, Dacheng Li, Joseph E. Gonzalez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28914v1)