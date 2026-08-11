---
title: Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models
published: 2026-08-10T00:57:48Z
authors: Yu Ma, Hongli Shi, Xinran Xu
url: http://arxiv.org/abs/2608.08982v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Twin Rollouts: Noise-Coupled Counterfactual Branching in Interactive Video World Models

## Abstract
Interactive video world models generate rollouts autoregressively under an action stream, yet they are trained and evaluated almost exclusively on factual prediction. We study counterfactual generation inside the rollout: given a trajectory the model has itself generated, what would have happened had the actions differed from step t* onward? We formalize noise-coupled twin rollouts --- a factual and a counterfactual branch sharing the generated prefix and the future exogenous noise sequence, diverging only in the action stream at an intervention point. Because the factual branch is self-generated, its exogenous noise is known exactly: the abduction step of Pearl's counterfactual procedure is exact by construction, sidestepping the approximate-inversion problem faced by editing-based pipelines. Noise coupling further turns the minimal-change principle into a per-sample verifiable property: we define a spatiotemporal locality metric that penalizes divergence outside the causal descendants of the intervention, computable against simulator ground truth without a learned judge. Forking the simulator state at t* yields ground-truth counterfactual re-renders, which we use as verifiable rewards for post-training. This note establishes the formal framework, metric definitions, and positioning; experiments are forthcoming.

## Metadata
- **Published**: 2026-08-10T00:57:48Z
- **Authors**: Yu Ma, Hongli Shi, Xinran Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08982v1)