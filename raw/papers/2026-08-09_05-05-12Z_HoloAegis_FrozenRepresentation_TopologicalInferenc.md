---
title: HoloAegis: Frozen Representation, Topological Inference: Minimally Parametric Safety Manifolds for Zero-Shot LLM Guardrails
published: 2026-08-09T05:05:12Z
authors: Tak Ho Alex Li, Kaijie Liu, Lik-Hang Lee, Kin Chung Ho, Ping Shum, Michael K. Ng
url: http://arxiv.org/abs/2608.08485v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HoloAegis: Frozen Representation, Topological Inference: Minimally Parametric Safety Manifolds for Zero-Shot LLM Guardrails

## Abstract
Current LLM safety guardrails face a fundamental tension: fine-tuning distorts pre-trained representations while generative judges incur prohibitive inference costs. We challenge the prevailing paradigm by asking: can safety be achieved through pure geometric reasoning over frozen semantic representations? We present HoloAegis, a minimally parametric topological inference framework that decouples representation from reasoning. We term our approach minimally parametric because the only free parameters are the anchor count K and the temperature tau, both fixed after construction and requiring no gradient-based training. An un-fine-tuned encoder maps text to a unit sphere, after which all decisions are purely geometric. We formalize safety evaluation as a Gibbs-Boltzmann Free Energy computation over a pre-computed System Topology Anchor Bank, and we introduce Dual Time-Scale Exponential Moving Averages to detect progressive multi-turn semantic drift. Our key theoretical insight is a Topological Boundary Stability Conjecture: we provide theoretical motivation and strong empirical evidence that sparse anchor centroids stabilize the decision boundary against high-frequency lexical perturbations far better than full vector space methods. Evaluated across 8 benchmarks, HoloAegis achieves state-of-the-art accuracy (1.0000 AUC on AuthenHallu, 0.9802 on HarmBench) with sub-millisecond latency, zero cold-start data, and cross-lingual transfer (0.9758 AUC on Chinese CHIFRAUD).

## Metadata
- **Published**: 2026-08-09T05:05:12Z
- **Authors**: Tak Ho Alex Li, Kaijie Liu, Lik-Hang Lee, Kin Chung Ho, Ping Shum, Michael K. Ng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08485v1)