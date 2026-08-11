---
title: Rethinking Factor Sharing in Federated LoRA: A Rank-Aware Adaptive Approach
url: http://arxiv.org/abs/2608.09742v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_15-38-45Z_RethinkingFactorSharinginFederatedLoRA_ARank_Aware.md
generated_at: 2026-08-10 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how to share the two LoRA update matrices in federated learning, proposing a rank‑aware strategy that chooses whether the input or output side is shared. Using a least‑squares residual metric, it shows that one sharing pattern yields smaller aggregate residuals and thus better fine‑tuning performance. The authors introduce FedAS‑LoRA, which selects the optimal sharing side before training.

## Key Takeaways
- Share‑A/Local‑B requires a common rank‑r input subspace, and its preference is determined by whether this shared space produces small projection residuals across clients.
- Share‑B/Local‑A uses a common rank‑r output subspace, with residual magnitude guiding the choice of which side to share.
- The Rank‑Aware Shared‑Subspace Sufficiency (RSS) metric evaluates how well a shared subspace captures local data distributions from a frozen LLM backbone.

## Context
Federated learning demands lightweight parameter updates that respect client privacy while maintaining model performance. Low‑rank adaptation (LoRA) reduces the number of trainable parameters, but deciding which LoRA factor to share remains an open challenge in distributed settings. This work addresses that gap by providing a principled, rank‑aware selection mechanism.

## Implications
For practitioners, FedAS‑LoRA offers a practical way to improve federated fine‑tuning without additional communication overhead. The method can be integrated into existing LoRA pipelines, enabling better adaptation across diverse tasks and data distributions while keeping the system efficient.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09742v1)
