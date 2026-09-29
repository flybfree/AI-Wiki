---
title: K-OPSD: Verifiable On-Policy Self-Distillation for Post-Training Vision-Language Models on AEC Drawings
url: http://arxiv.org/abs/2609.34082v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_01-19-57Z_K_OPSD_VerifiableOn_PolicySelf_DistillationforPost.md
generated_at: 2026-09-28 22:56
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces K-OPSD, a novel post-training methodology designed to enhance the ability of vision-language models to interpret architecture, engineering, and construction (AEC) drawings. By leveraging verifiable on-policy self-distillation, the approach constructs a reliable teacher model from verified best-of-N generations and updates student weights using a cross-entropy inner-loss instead of traditional divergence metrics. The resulting fine-tuned Qwen3-VL models achieve state-of-the-art performance on AECV-Bench and demonstrate strong generalization to out-of-domain architectural datasets.

## Key Takeaways
- K-OPSD employs a process-level verifier to certify model generations, creating a high-quality teacher from the model’s own best outputs while rescuing failed prompts through hint-guided resampling that exposes verified answers.
- The training pipeline replaces the bounded token-wise generalized Jensen-Shannon divergence with a more efficient cross-entropy inner-loss for on-policy updates, significantly improving convergence and reducing computational overhead during distillation.
- Empirical evaluations show that fine-tuned Qwen3-VL models reach a top average judge score of 0.819 and combined accuracy of 0.738 on AECV-Bench, with the 8B variant showing substantial performance gains when transferred to the ArchCAD dataset.

## Context
Special

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34082v1)
