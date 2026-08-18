---
title: SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry
published: 2026-08-17T08:58:55Z
authors: Jiaming Hu, Yan Zheng, Tian Wang
url: http://arxiv.org/abs/2608.16287v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry

## Abstract
Joint-embedding predictive world models plan by scoring predicted terminal embeddings against a goal embedding using a cost defined on the representation itself. Two prominent strategies for obtaining non-collapsed representations are to inherit a pretrained feature space, as in DINO-WM, and to learn an embedding end to end with anti-collapse regularization, as in LeWorldModel (LeWM) with SIGReg. These strategies show complementary strengths across tasks. Although task-relevant state is decodable from the full embeddings of both models, DINO-WM's leading principal components usually retain substantially more state information than LeWM's. Because Euclidean planning costs are dominated by high-variance directions, this difference affects how strongly state can influence candidate selection. We propose SCALE (State-CAlibrated Latent Embeddings) to give the end-to-end LeWM representation the favorable geometric property observed in DINO-WM. SCALE induces this property by correlating sampled pairwise latent distances with distances in a standardized task-relevant state space, without replacing LeWM's learned encoder. Across five tasks, three planning solvers, and five compute budgets, SCALE improves every task--solver average over LeWM. A latent-to-state regression control matches or exceeds SCALE's full-embedding decodability yet leaves latent--state distance alignment essentially unchanged and yields less consistent planning gains. SCALE adds a single lightweight training-time regularizer and no planning-time overhead. These results show that planning depends not only on whether task-relevant information is present, but also on whether it shapes the geometry consumed by the planner.

## Metadata
- **Published**: 2026-08-17T08:58:55Z
- **Authors**: Jiaming Hu, Yan Zheng, Tian Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16287v1)