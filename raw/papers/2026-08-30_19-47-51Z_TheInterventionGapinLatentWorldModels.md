---
title: The Intervention Gap in Latent World Models
published: 2026-08-30T19:47:51Z
authors: Donna Vakalis
url: http://arxiv.org/abs/2608.29998v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Intervention Gap in Latent World Models

## Abstract
Planning-time intervention fidelity is a distinct, measurable property of a learned world model: whether the model's own open-loop transitions move task variables the way matched environment interventions do. In the settings we test, it is neither revealed by reward fit nor ensured by task-anchored training. Across released TD-MPC2 checkpoint sizes, episode return falls as an operator-error diagnostic on task observables grows, while reward-prediction error stays small and nearly flat, and a self-supervised world model trained without task signal preserves the same operator substantially better than a task-anchored model on the shared task. A capture-gated matched-intervention audit then localizes what fails. On Cheetah, three LeWorldModel checkpoints capture the current task query and support decodable real intervention effects; however, their imagined five-step effects are worse than predicting no effect and worse than an environment-endpoint oracle. The failure is task-direction rotation with excess gain, not feature collapse. This severe pattern is conditional: five PreJEPA seeds retain an oracle-relative deficit without it, Finger Spin experiments extend the deficit beyond locomotion with heterogeneous severity across seeds, and shared-bank effect geometry is both candidate- and support-dependent. We also test practice-side questions. In DreamerV3 the posterior distribution, not its sample, carries the current query; ensemble disagreement ranks error only near training support; and a frozen support-aware score degrades held-out error ranking in both tested transfer directions while native disagreement remains informative in both. We conclude that intervention fidelity must be audited directly, capture-first, on the model's native interface.

## Metadata
- **Published**: 2026-08-30T19:47:51Z
- **Authors**: Donna Vakalis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29998v1)