---
title: Faithful Dual-constrained Erasure for Robust LLM Safety Alignment
url: http://arxiv.org/abs/2609.39279v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_08-29-43Z_FaithfulDual_constrainedErasureforRobustLLMSafetyA.md
generated_at: 2026-09-30 22:12
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the vulnerability of machine unlearning in Large Language Models to retraining attacks, where suppressed malicious behaviors resurface after benign fine-tuning due to shallow alignment mechanisms. The authors identify that models often rely on spurious suppressors rather than truly erasing knowledge, leading to fragile safety shells that can be easily bypassed. To solve this, they propose FDCU, a dual-constrained subspace projection framework that enforces authentic memory deletion by preserving general knowledge via Fisher Information while blocking spurious parameter activation through the Principle of Minimal Functional Intervention, achieving robust safety against retraining without compromising model utility.

## Key Takeaways
- Current unlearning methods suffer from shallow alignment where models fail to erase malicious representations, instead activating dormant parameters as spurious suppressors that create a fragile inhibitory shell; this allows retraining attacks to easily bypass safety measures and restore suppressed behaviors.
- FDCU introduces a scalable element-wise dual-masking rule that enforces authentic knowledge dismantling by simultaneously preserving general knowledge manifolds using Fisher Information and strictly prohibiting the abnormal activation of spurious suppressors via the Principle of Minimal Functional Intervention.
- Extensive experiments demonstrate that FDCU achieves state-of-the-art robustness against retraining attacks across specific knowledge erasure and

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39279v1)
