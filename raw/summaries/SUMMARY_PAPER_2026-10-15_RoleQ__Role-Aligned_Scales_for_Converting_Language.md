---
title: RoleQ: Role-Aligned Scales for Converting Language Models to Ternary
url: http://arxiv.org/abs/2610.21808v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_12-56-57Z_RoleQ_Role_AlignedScalesforConvertingLanguageModel.md
generated_at: 2026-10-15 23:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
RoleQ introduces a novel quantization framework that assigns scales to Transformer weight matrices based on the functional roles of units (reading from or writing to the residual stream) rather than the conventional layout-based approach. The method enables post-training conversion of existing language model checkpoints to ternary (1.59 bits per weight) in a few GPU-hours, outperforming all other post-training ternary methods on perplexity, zero-shot accuracy, and MMLU benchmarks across model sizes from 0.6B to 14B.

## Key Takeaways
- RoleQ uses a structural, search-free rule for placing quantization scales: vectors that read from the residual stream receive one scale per output unit, while those that write to it receive one per input unit. This rule requires no calibration, no stored state, and holds on integer and ternary grids, yet in a rotated basis it matches per-layer axis search at half the solver computational work.
- At ternary precision, RoleQ cuts perplexity by up to half compared to layout-based scale placement across two model families at every size from 0.6B to 14B. Critically, conventional per-row scales leave MMLU at chance level, whereas RoleQ preserves factual knowledge and task accuracy far more effectively.
- A sparse second ternary plane placed by per-unit Fisher saliency keeps matrix multiplication multiplication-free and recovers what ternary quantization loses first. At 8B parameters, adding a fraction of a bit returns approximately half the MMLU performance lost during conversion, significantly outperforming random or Hessian-based placement at equivalent bit budgets.

## Context
Weight quantization below four bits is a critical technique for deploying large language models on constrained hardware, but existing ternary approaches either require training from scratch or extensive fine-tuning, making them impractical for practitioners who need to convert existing checkpoints. The broader field has struggled with the tradeoff between aggressive compression and preservation of factual knowledge, with layout-based quantization formats consistently degrading knowledge-intensive benchmarks. RoleQ addresses this gap by exploiting the structural asymmetry in Transformer architectures—specifically how units interact with the residual stream—to derive quantization scales from architecture semantics rather than numerical optimization.

## Implications
For industry practitioners deploying large language models on edge devices or memory-constrained servers, RoleQ offers a practical post-training pipeline that converts existing checkpoints to 1.59 bits per weight in a few GPU-hours, a fraction of the cost of learned ternarization methods. This makes aggressive ternary compression accessible without retraining, potentially enabling deployment of 8B–14B models on hardware previously limited to 4-bit quantization. The finding that functional-role-based scale placement dramatically outperforms layout-based approaches suggests that future quantization research should prioritize architectural semantics over numerical search, which could reshape how compression techniques are designed for transformer-based systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21808v1)
