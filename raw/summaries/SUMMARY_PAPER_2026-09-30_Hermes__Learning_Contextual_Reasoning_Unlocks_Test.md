---
title: Hermes: Learning Contextual Reasoning Unlocks Test-Time Scaling
url: http://arxiv.org/abs/2609.38332v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_18-01-13Z_Hermes_LearningContextualReasoningUnlocksTest_Time.md
generated_at: 2026-09-30 20:55
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Hermes, a family of configurable harnesses designed to enhance test-time scaling by shifting decisions regarding context allocation and reuse from fixed strategies to the model itself through learned contextual reasoning. The authors propose Hermes-Learn, a two-stage training framework that enables models to adaptively manage inference-time compute based on problem complexity and reasoning progress. Results demonstrate that while capable models naturally exploit this flexibility, smaller open-source models benefit significantly from training with Hermes-Learn, closing performance gaps and achieving gains that generalize across benchmarks and extrapolate beyond training compute limits.

## Key Takeaways
- The core innovation is "contextual reasoning," where models learn to decide how to allocate fresh contexts and carry information between windows during inference, moving away from prescribed decisions made by external harnesses toward adaptive model-controlled strategies that vary with problem type and reasoning progress.
- The Hermes-Learn framework employs a two-stage training process to induce these adaptive capabilities, effectively closing the performance gap between large capable models and smaller open-source models that initially struggle to utilize flexible context management without explicit instruction.
- The benefits of this approach are robust and versatile; performance improvements generalize across diverse benchmarks and models, extrapolate effectively to inference-time compute levels exceeding those encountered during training, and successfully transfer to complementary test-time scaling techniques beyond the Hermes harnesses themselves.

## Context
Test-time scaling has emerged as a critical paradigm for boosting large language model performance by dynamically allocating computational resources during inference rather than relying solely on static training parameters. However, realizing the full potential of this approach requires sophisticated mechanisms to manage information flow across multiple context windows,

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38332v1)
