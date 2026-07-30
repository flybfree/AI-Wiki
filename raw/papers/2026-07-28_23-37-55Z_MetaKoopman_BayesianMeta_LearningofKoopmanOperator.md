---
title: MetaKoopman: Bayesian Meta-Learning of Koopman Operators for Modeling Structured Dynamics under Distribution Shifts
published: 2026-07-28T23:37:55Z
authors: Mahmoud Selim, Sriharsha Bhat, Karl H. Johansson
url: http://arxiv.org/abs/2607.26345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MetaKoopman: Bayesian Meta-Learning of Koopman Operators for Modeling Structured Dynamics under Distribution Shifts

## Abstract
Modeling and forecasting nonlinear dynamics under distribution shifts is essential for robust decision-making in real-world systems. In this work, we propose MetaKoopman, a Bayesian meta-learning framework for modeling nonlinear dynamics through linear latent representations. MetaKoopman learns a Matrix Normal-Inverse Wishart (MNIW) prior over the Koopman operator, enabling closed-form Bayesian updates conditioned on recent trajectory segments. Moreover, it provides a closed-form posterior predictive distribution over future state trajectories, capturing both epistemic and aleatoric uncertainty in the learned dynamics. We evaluate MetaKoopman on a full-scale autonomous truck and trailer system across a wide range of adverse winter scenarios, including snow, ice, and mixed-friction conditions, as well as in simulated control tasks with diverse distribution shifts. MetaKoopman consistently outperforms prior approaches in multi-step prediction accuracy, uncertainty calibration, and robustness to distributional shifts. Field experiments further demonstrate its effectiveness in dynamically feasible motion planning, particularly during evasive maneuvers and operation at the limits of traction. Project website: https://mahmoud-selim.github.io/MetaKoopman/

## Metadata
- **Published**: 2026-07-28T23:37:55Z
- **Authors**: Mahmoud Selim, Sriharsha Bhat, Karl H. Johansson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26345v1)