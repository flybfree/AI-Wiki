---
title: ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models
url: http://arxiv.org/abs/2608.21100v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_13-47-21Z_ReFrame_Evidence_GuidedTest_TimeSafetyAlignmentinM.md
generated_at: 2026-08-23 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ReFrame, a training‑free framework that reframes multimodal inputs to improve safety alignment in deployed MLLMs. Experiments show that ReFrame reduces jailbreak success, enhances safety awareness, and lessens oversensitivity while keeping model utility intact.

## Key Takeaways
- Utility dominance causes models to prioritize task performance over latent risks, leading to unsafe outputs.  
- Reasoning inertia makes models follow malicious reasoning trajectories without detecting hidden dangers.  
- ReFrame mitigates these issues by using a lightweight local MLLM to generate evidence and rewrite prompts, preserving the original model’s functionality.

## Context
Multimodal safety alignment is essential as MLLMs become ubiquitous in real‑world applications where user interactions are multimodal. Existing methods often require retraining or internal inspection, which is impractical for closed‑source systems, highlighting a need for test‑time solutions that do not alter the model.

## Implications
This work provides practitioners with a practical way to enhance safety without compromising performance or requiring access to proprietary models. By integrating lightweight reframing agents, organizations can deploy safer multimodal services while maintaining existing utility and compliance standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21100v1)
