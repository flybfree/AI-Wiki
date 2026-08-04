---
title: ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching
published: 2026-08-03T08:59:22Z
authors: Zihan Liu, Yuzhe Zhuang, Yuanzu Li, Wanshuang Gou, Jiahong Liu, Min Zhou, Menglin Yang
url: http://arxiv.org/abs/2608.01926v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching

## Abstract
JEPA-style visual world models offer an effective paradigm for visual goal planning by predicting future latent representations. Existing methods typically learn local transition consistency through next-step representation prediction. However, in long-horizon tasks, accurate local prediction alone need not ensure sustained progress toward the goal. First, multi-step rollouts can remain locally plausible while drifting away from goal-relevant trajectories. Second, locally similar future states can correspond to substantially different long-term progress, making them difficult to distinguish in a latent space optimized mainly for local consistency. To address these challenges, we introduce goal-conditioned progress order, a relative ordering of states according to how they advance toward a given goal. This order exhibits an asymmetric, coarse-to-fine structure: early states retain broader future possibilities, while later states concentrate on more specific goal-relevant regions. Such a structure is well suited to hyperbolic geometry. Motivated by this observation, we propose ProWorld, a progress-aware hyperbolic visual world model. ProWorld leverages goal-conditioned progress order to organize visual latent-space dynamics, maintains directional progress within trajectories via hyperbolic entailment learning, and mitigates progress ambiguity among locally similar future states via hyperbolic future discrimination. Furthermore, we design a progress-aware planning objective that scores candidate rollouts by jointly considering proximity to the goal and sustained progress across intermediate states. Experiments on four visual goal-reaching tasks demonstrate that ProWorld achieves an average absolute success-rate gain of 9.67 over LeWM. The code will be released after the paper is accepted.

## Metadata
- **Published**: 2026-08-03T08:59:22Z
- **Authors**: Zihan Liu, Yuzhe Zhuang, Yuanzu Li, Wanshuang Gou, Jiahong Liu, Min Zhou, Menglin Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01926v1)