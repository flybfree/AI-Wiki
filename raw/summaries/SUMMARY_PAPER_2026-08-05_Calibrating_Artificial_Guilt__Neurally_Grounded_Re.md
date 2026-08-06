---
title: Calibrating Artificial Guilt: Neurally Grounded Reward Shaping for Prosocial Multi-Agent Reinforcement Learning
url: http://arxiv.org/abs/2608.04663v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_10-21-11Z_CalibratingArtificialGuilt_NeurallyGroundedRewardS.md
generated_at: 2026-08-05 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a method to calibrate artificial guilt signals for multi‑agent reinforcement learning using human neurobehavioral data. It fits a regression of momentary happiness changes to outcome counts and extracts a guilt weight that is embedded in a two‑agent Social Lottery task. The calibrated agents reproduce the human safe‑choice rate with minimal divergence.

## Key Takeaways
- A subject‑fixed‑effects regression on fMRI data yields a guilt weight of 1.118 (Cohen's d=0.214) that quantifies how negative social outcomes reduce happiness relative to non‑social negatives.
- Embedding this calibrated weight in the reward shaping leads to agents whose behavior closely matches human safe‑choice rates, achieving a KL divergence of only 0.0012 compared with other shaping regimes.
- The study demonstrates that neural and behavioral priors can serve as quantitative constraints for prosocial reinforcement learning.

## Context
Current multi‑agent RL systems often rely on manually tuned social terms to encourage cooperation, which may not align with human preferences or neurobiological limits. This work shifts the calibration responsibility from designers to empirical neuroscience, offering a principled way to ground artificial morality in real data.

## Implications
For researchers, this approach provides a scalable framework for aligning agent incentives with human prosocial norms without extensive trial‑and‑error tuning. For industry and practitioners, it suggests that ethical AI design can benefit from neurocognitive insights, reducing the risk of overly punitive or indifferent agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04663v1)
