---
title: Gated Q-learning: Add Off-Policy Bias to Taste
published: 2026-07-31T00:32:46Z
authors: Brett Daley
url: http://arxiv.org/abs/2607.28916v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gated Q-learning: Add Off-Policy Bias to Taste

## Abstract
Multistep credit assignment is critical for sample-efficient reinforcement learning, yet managing off-policy bias in Q-learning remains a fundamental challenge. For 30 years, practitioners have been limited to a binary choice: eliminate the bias at the cost of severely truncated eligibility traces (Watkins' Q($λ$)), or ignore the bias to learn faster while injecting detrimental errors into the value estimates (Peng's Q($λ$)). Modern off-policy estimators fail to resolve this tension, as importance-sampling ratios collapse under Q-learning's greedy target policy. We introduce Gated Q-learning, a novel algorithmic framework that ends this dilemma by smoothly interpolating between the two historical extremes. Rather than relying on importance sampling, our approach employs a continuous, state-action-dependent gating mechanism to selectively attenuate eligibility traces in an exploration-aware manner. We provide a rigorous theoretical foundation for this mechanism, proving that the expected operator remains a contraction mapping and deriving its exact fixed point. Empirical evaluations verify that intermediate gating safely enables longer credit-assignment horizons, yielding faster initial learning than either extreme. Gated Q-learning offers a simple alternative to importance sampling while enabling customization of the effective multistep horizon and the amount of off-policy bias in Q-learning agents.

## Metadata
- **Published**: 2026-07-31T00:32:46Z
- **Authors**: Brett Daley
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28916v1)