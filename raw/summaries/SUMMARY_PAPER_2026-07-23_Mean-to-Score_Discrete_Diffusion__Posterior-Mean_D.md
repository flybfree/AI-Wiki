---
title: Mean-to-Score Discrete Diffusion: Posterior-Mean Denoisers for Score Entropy
url: http://arxiv.org/abs/2607.21372v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_14-37-30Z_Mean_to_ScoreDiscreteDiffusion_Posterior_MeanDenoi.md
generated_at: 2026-07-23 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses a limitation in Score Entropy Discrete Diffusion (SEDD) where the score-entropy loss, while optimal on average, can generate scores that violate the bridge polytope, leading to negative pre‑normalization weights and poor external generative performance. The authors propose mean-to-score (M2S), which predicts a clean‑token posterior mean and maps it exactly onto the bridge polytope using a kernel‑dependent linear transform. Experiments show M2S reduces test BPD from 3.173 to 3.129, improves FID‑50k, and outperforms several strong checkpoints across sampling budgets.

## Key Takeaways
- SEDD’s score‑entropy loss does not guarantee that generated scores can be induced by any valid posterior, allowing violations of the coordinate box and negative weights in finite‑step sampling.  
- M2S resolves this by converting a clean‑token posterior mean to a score via an exact kernel mapping, ensuring all scores lie within the bridge polytope.  
- The method improves external generative PPL from 183.6 to 143.3 at 128 steps and achieves lower BPD (3.129) than pure‑uniform SEDD.

## Context
In diffusion models, generating realistic samples often hinges on the internal consistency of score vectors with respect to known forward processes. The bridge polytope captures this consistency by restricting scores to a convex set that reflects valid posterior probabilities. Prior work has focused on loss functions and checkpoints, but few have systematically addressed the mapping between posterior means and permissible scores across diverse corruption schemes.

## Implications
M2S offers a principled way to align score generation with theoretical constraints, which can be directly integrated into existing diffusion pipelines without retraining large models. For practitioners, this reduces sample quality degradation and enables more reliable sampling budgets, potentially lowering computational costs for high‑resolution image synthesis. The approach also provides a template for extending mean‑to‑score ideas to other continuous‑time Markov chains in generative AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21372v1)
