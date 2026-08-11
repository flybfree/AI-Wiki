---
title: Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation
published: 2026-08-10T07:51:45Z
authors: Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama
url: http://arxiv.org/abs/2608.09228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation

## Abstract
On-Policy Self-Distillation (OPSD) is commonly interpreted as the transfer of privileged information: a teacher observes the verified solution to the target problem and supervises the student's trajectory. However, this interpretation conflates two effects. The reference solution not only reveals the answer to the current instance but also changes the context under which the teacher provides token-level supervision. We investigate the role of target-specific privilege with $\mathrm{OP}^{2}\mathrm{SD}$ (On-Policy Self-Distillation from Other Problems), which replaces the paired reference with a problem and solution from a different example, while preserving the student rollout, teacher, and distillation objective. Across three models and three mathematics benchmarks, $\mathrm{OP}^{2}\mathrm{SD}$ improves over the base model, remains competitive with OPSD. The success of $\mathrm{OP}^{2}\mathrm{SD}$ implies that OPSD gains do not necessarily come from access to the reference solution, and that the teacher's context-induced behavior is an important factor.

## Metadata
- **Published**: 2026-08-10T07:51:45Z
- **Authors**: Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09228v1)