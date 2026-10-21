---
title: Can Native Safety Travel? Reusing Safety Pretraining Across Models via On-Policy Distillation
url: http://arxiv.org/abs/2610.27555v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_03-13-04Z_CanNativeSafetyTravel_ReusingSafetyPretrainingAcro.md
generated_at: 2026-10-20 22:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the "native safety reuse" problem and demonstrates that safety acquired during model pretraining can be transferred to other models through on-policy distillation. By having a small safety-pretrained teacher supervise a standard-pretrained student's token-level predictions along the student's own generated trajectories, the student inherits the teacher's robust safety behavior while preserving its own higher general utility, effectively decoupling native safety from the model in which it was originally pretrained.

## Key Takeaways
- Native safety, defined as safety embedded during pretraining, provides substantially greater robustness to subsequent fine-tuning than conventional safety post-training. The paper shows that a 1.7B student distilled from a safety-pretrained teacher experiences only a 5.00% increase in average attack success rate (ASR) after fine-tuning, compared to 11.58% for models that relied on safety post-training, demonstrating a more than twofold improvement in safety robustness.
- The on-policy distillation framework enables selective, small-to-large safety transfer: a smaller safety-pretrained teacher supervises a larger standard-pretrained student, allowing the student to inherit safety expertise without inheriting the teacher's lower general utility. The distilled student achieves an average utility of 48.20%, far exceeding the aligned teacher's 27.42%, showing that safety and utility can be effectively decoupled across model sizes.
- Cross-tokenizer alignment techniques enable native safety transfer across different model families, meaning the safety knowledge is not locked to a specific architecture or tokenizer. This establishes native safety as a reusable, transferable model property rather than an artifact permanently tied to the originally pretrained model, opening a new pathway for safety engineering in model development pipelines.

## Context
Safety alignment in large language models has traditionally relied on post-training techniques such as RLHF or supervised fine-tuning, which are vulnerable to degradation when models are subsequently fine-tuned for downstream tasks. Safety pretraining emerged as a more robust alternative, but its practical adoption has been limited by the high cost of training safety-specialized models from scratch and the utility trade-offs they introduce. This paper addresses a critical gap in the safety alignment literature by asking whether the robustness benefits of safety pretraining can be harvested and transferred, rather than requiring every deployed model to undergo expensive safety pretraining independently.

## Implications
For practitioners and industry, this work suggests a practical and cost-efficient safety pipeline: organizations could train a single small safety-pretrained model and distill its safety knowledge into many larger, general-purpose students, avoiding the prohibitive cost of safety pretraining at scale. For the broader AI safety field, establishing native safety as a transferable property challenges the assumption that safety must be baked into every model from scratch and points toward modular, composable safety architectures. This could accelerate the deployment of safety-robust models across diverse domains while reducing the compute and data overhead currently required for safety alignment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27555v1)
