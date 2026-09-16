---
title: Test-Time Unlearning via Sparse Autoencoder
url: http://arxiv.org/abs/2609.16229v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_18-58-09Z_Test_TimeUnlearningviaSparseAutoencoder.md
generated_at: 2026-09-15 20:08
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces ARIA, a novel test-time unlearning framework that removes specific knowledge from large language models without altering their underlying weights. By leveraging sparse autoencoder latents to detect forget-related states and applying lightweight gating interventions during inference, ARIA effectively mitigates the traditional forget-utility trade-off while maintaining robustness against post-unlearning adversarial recovery attacks.

## Key Takeaways
- ARIA operates entirely at inference time by training a lightweight linear detector on sparse autoencoder features to identify when generation enters a forget-related state, allowing it to gate access to unwanted knowledge without any weight modification or retraining overhead.
- Empirical evaluations across multiple benchmarks (TOFU, R-TOFU, WMDP) and model architectures demonstrate that ARIA significantly reduces target knowledge retention while preserving general utility, keeping MMLU scores within one percent of the original pre-unlearning performance.
- The authors introduce three novel post-unlearning adversarial attacks targeting weight-space and decoding-space recovery, demonstrating that ARIA maintains its unlearning effectiveness with less than one percent degradation in forgetting capability under attack, alongside revealing that some retained knowledge loss may stem from response style shifts rather than actual data leakage.

## Context
Machine unlearning has emerged as a critical requirement for aligning large language models with regulatory standards and ethical guidelines, yet existing weight-modification techniques struggle to balance knowledge removal with model utility. This research addresses a fundamental bottleneck in the field by shifting the unlearning paradigm from static parameter updates to dynamic, feature-level inference control, offering a more flexible and interpretable alternative to traditional fine-tuning approaches.

## Implications
By decoupling unlearning from weight updates, ARIA enables practitioners to deploy safety interventions that can be toggled or updated without costly retraining cycles, significantly reducing computational overhead and deployment friction. The framework’s resilience against adversarial recovery also provides a more reliable safeguard for high-stakes applications, while its interpretability features offer valuable insights into how model biases and response patterns interact with unlearning objectives.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.16229v1)
