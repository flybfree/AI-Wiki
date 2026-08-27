---
title: PhaseShift: Topology-Aware Data Harmonization and Model Consolidation Across Signalized Intersections
published: 2026-08-26T01:22:49Z
authors: Yash Ranjan, Artur Kumik, Rahul Sengupta, Anand Rangarajan, Sanjay Ranka
url: http://arxiv.org/abs/2608.25275v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PhaseShift: Topology-Aware Data Harmonization and Model Consolidation Across Signalized Intersections

## Abstract
Learned traffic-behavior models are commonly trained separately for each intersection, creating model portfolios that cannot share evidence across sites. We present PhaseShift, a topology-aware framework that harmonizes heterogeneous roadside trajectories into a shared actor-centric representation and trains one reusable backbone. Ego-relative coordinates, trajectory-induced movement paths, normalized signal context, and variable-cardinality interaction tokens remove site conventions while preserving behaviorally relevant topology. The backbone supports pooled operation, zero-shot at a held-out intersection, and low-data adaptation. We evaluate five intersections in two Florida regions on balanced field data, 100k training windows and equal-sized test sets per site under a replay-conditioned, best-of-sampled-trajectory protocol. At 10s, one pooled model lowers both minADE and minFDE relative to trained local models at all five sites, with median reductions of 36.8% and 22.0%. Leave-one-intersection-out deployment, including one cross-region fold, beats local training on both 10-s metrics at four of five sites, although short-horizon performance is less uniform. Fine-tuning with 1,000 target update windows improves on zero-shot at three sites and is the strongest regime at one. At site 7, every cross-site mixture sharply lowers long-horizon error under a fixed 100k-window budget; test-likelihood gains argue against a best-of-sample dispersion-only explanation. Local models fall behind calibrated IDM at the two highest-flow sites after long autoregressive rollouts; pretrained-backbone regimes do not. Within this five-site evaluation, PhaseShift demonstrates consolidation across heterogeneous physical control settings while identifying sites that still require adaptation. The protocol measures conditional single-vehicle generation under replayed context, not closed-loop traffic simulation.

## Metadata
- **Published**: 2026-08-26T01:22:49Z
- **Authors**: Yash Ranjan, Artur Kumik, Rahul Sengupta, Anand Rangarajan, Sanjay Ranka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25275v1)