---
title: SPARED: Reasoning-Based AI-Generated Image Detection via Adversarially Edited Data
published: 2026-08-13T06:40:20Z
authors: Yicheng Bao, Xiahui Guo, Xuhong Wang, Xin Tan
url: http://arxiv.org/abs/2608.12876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPARED: Reasoning-Based AI-Generated Image Detection via Adversarially Edited Data

## Abstract
Detecting AI-generated images is only half the task: a deployed detector must also justify its verdict, yet existing detectors inherit three failure modes from their training data: real and fake images collected from different sources invite provenance shortcuts, supervised explanation corpora teach templated rationales, and a static forgery corpus leaves the decision boundary standing still while generators keep moving. We introduce \methodname{}, an adversarial reinforcement learning framework that pits two heterogeneous models against each other. A diffusion image editor learns to edit real photographs into fake counterparts of those same photographs that fool the current detector, while a reasoning MLLM learns to expose them with a verdict grounded in free-form reasoning. Both rewards are shortcut-proof by design: the attacker is credited only when its edit is faithfully executed, and the defender only when its verdict is correct. As the two models alternate, each round's attacker regenerates a harder training pool aimed at the current detector's blind spots, so the detector must generalize rather than memorize any fixed artifact distribution. Although the explanation is never rewarded, its quality rises round over round as a side effect of accuracy-only training. A detector trained within this loop improves monotonically across rounds on each of three external benchmarks.

## Metadata
- **Published**: 2026-08-13T06:40:20Z
- **Authors**: Yicheng Bao, Xiahui Guo, Xuhong Wang, Xin Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12876v1)