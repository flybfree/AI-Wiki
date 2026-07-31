---
title: Good Rankers, Bad Objectives: Bilinear Contrastive Critics under Expressive Policy Search
published: 2026-07-29T19:43:40Z
authors: Ayushman Singh, Siddharth Aphale
url: http://arxiv.org/abs/2607.27422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Good Rankers, Bad Objectives: Bilinear Contrastive Critics under Expressive Policy Search

## Abstract
Good action rankings do not make a contrastive critic safe to maximize. These critics increasingly act as value-like objectives for best-of-$K$ selection, planning, and critic-guided generation. Unbounded bilinear scores can let large embedding norms inflate off-support values, but cosine bounding does not remove the failure. A controlled support decomposition attributes most raw bilinear regret to norm drift. Cosine and hybrid critics nevertheless select off-support actions from most pools and incur comparable regret. Contrastive scores are weakly calibrated or inverted in the top score decile across four OGBench navigation tasks, and they fail to order fixed-query actions by value. Bellman-trained TD-Q succeeds, including in a parameter-matched function-class control. Realized costs depend on the task: simulator rollouts reveal single-step selection costs on PointMaze and the exact-$Q^*$ toy but well-powered nulls on AntMaze and HumanoidMaze, where the controller can self-correct. A training/readout decomposition traces the lost ordering to the cosine training objective; raw-trained embeddings retain weak ordering after inference-time normalization. Candidate maximization can therefore exploit false positives caused by norm drift, score saturation, or in-support misranking. Contrastive critics remain useful compatibility rankers on navigation and manipulation tasks, but action selection requires a value-calibrated scalar.

## Metadata
- **Published**: 2026-07-29T19:43:40Z
- **Authors**: Ayushman Singh, Siddharth Aphale
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27422v1)