---
title: A Model Merging Approach for Continual MLLM Unlearning
url: http://arxiv.org/abs/2608.04548v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_07-37-23Z_AModelMergingApproachforContinualMLLMUnlearning.md
generated_at: 2026-08-05 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces Merging for Continual Unlearning (MCU), a method that combines multiple one‑shot unlearning adapters into a single unified adapter when new sensitive data must be removed from multimodal large language models. Experiments on ICU‑Bench and MLLMU‑Bench show that MCU outperforms prior approaches, maintaining high unlearning effectiveness while preserving both retained knowledge and general multimodal performance.

## Key Takeaways  
- The cross‑task dependencies among adapters can cause interference, leading to cumulative utility degradation and retention drift.  
- Projecting adapters into a shared representation space allows the method to preserve dominant directions of each adapter while suppressing over‑concentrated coordinates that amplify interference.  
- Reconfiguring these dependencies improves unlearning transferability without sacrificing the model’s overall multimodal capability.

## Context  
Continual unlearning is essential for models that must retain useful knowledge while removing private or proprietary information across multiple tasks. Existing one‑shot approaches often fail in repeated scenarios, highlighting a need for methods that handle dynamic merging of adapters effectively.

## Implications  
MCU offers practitioners a scalable solution to maintain model utility when continuously updating sensitive data, reducing the risk of performance collapse. This can lead to more reliable deployment of AI systems in regulated environments where privacy and accuracy must coexist.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04548v1)
