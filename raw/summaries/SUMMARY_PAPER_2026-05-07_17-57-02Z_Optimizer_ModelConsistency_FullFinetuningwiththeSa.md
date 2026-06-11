---
title: Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less
url: http://arxiv.org/abs/2605.06654v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-07_17-57-02Z_Optimizer_ModelConsistency_FullFinetuningwiththeSa.md
generated_at: 2026-06-11 10:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates optimizer‑model consistency and demonstrates that using the same optimizer throughout pretraining and fine‑tuning reduces forgetting while preserving or improving performance compared to other optimizers such as AdamW and LoRA.

## Key Takeaways
- Optimizers shape model landscapes by imposing regularization on activations, which influences how weights are updated during supervised fine‑tuning.  
- The optimal weight updates align with the optimizer’s behavior, leading to less forgetting when the same optimizer is employed from pretraining to SFT.  
- Muon underperforms in reasoning tasks because its strong tendency toward rote memorization can hinder pattern acquisition with limited data.

## Context
Large language models depend heavily on optimizers for both pretraining and fine‑tuning stages, yet mismatched optimizers can degrade adaptation efficiency. Understanding this relationship is essential for scalable model deployment and effective knowledge transfer.

## Implications
Practitioners should adopt optimizer consistency to improve transfer learning outcomes and minimize catastrophic forgetting, providing a straightforward strategy for efficient supervised fine‑tuning in industry settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.06654v1)
