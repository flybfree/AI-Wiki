---
title: GROM: Gradient-Free Rapid One-Shot Machine Unlearning
url: http://arxiv.org/abs/2608.05783v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_09-16-53Z_GROM_Gradient_FreeRapidOne_ShotMachineUnlearning.md
generated_at: 2026-08-06 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GROM, a gradient‑free one‑shot unlearning method that removes targeted knowledge from large language models without iterative optimization or backpropagation. By formulating the forgetting problem as a ridge‑regularized least‑squares task and providing an exact additive weight update, GROM achieves state‑of‑the‑art forgetting‑utility trade‑offs while updating in seconds, far faster than conventional fine‑tuning.

## Key Takeaways
- GROM replaces iterative gradient‑based fine‑tuning with a direct analytical solution that computes the exact weight edit from forward passes alone.  
- The method preserves the model’s behavior on retained data and suppresses only the unwanted content, preventing the hidden‑knowledge issue common to other approaches.  
- Because the update is applied directly to the weights rather than masking them, GROM remains effective under low‑bit quantization attacks that typically recover unlearned information.

## Context
Machine unlearning is essential for safely removing sensitive data from large language models, yet existing solutions depend on costly iterative fine‑tuning and often fail to truly erase targeted knowledge. This limitation hampers real‑world deployment where rapid, reliable forgetting is required without degrading overall performance.

## Implications
GROM offers a practical alternative that reduces computational overhead dramatically, enabling frequent model updates in production environments. Its robustness to quantization attacks makes it suitable for resource‑constrained settings where preserving privacy and security is paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05783v1)
