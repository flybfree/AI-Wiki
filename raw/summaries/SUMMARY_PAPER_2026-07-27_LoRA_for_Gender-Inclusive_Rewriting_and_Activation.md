---
title: LoRA for Gender-Inclusive Rewriting and Activation Steering for Counter-Narrative Generation
url: http://arxiv.org/abs/2607.23083v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_07-11-22Z_LoRAforGender_InclusiveRewritingandActivationSteer.md
generated_at: 2026-07-27 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces IHLC, a system that performs gender‑inclusive rewriting and counter‑narrative generation for the LT‑EDI 2026 task. It uses LoRA fine‑tuning to achieve an official score of 80 % on rewriting and a compute‑efficient activation steering method that yields 78.12 % on counter‑narratives.

## Key Takeaways
- The system leverages parameter‑efficient LoRA fine‑tuning to produce gender‑inclusive rewrites while keeping the original model weights unchanged.
- Counter‑narrative generation is steered by extracting a principal direction from contrastive hidden‑state activations via PCA and injecting it into intermediate representations at inference time.
- Manual analysis reveals failure modes such as semantic drift, residual bias leakage, layer sensitivity, over‑steering, and text degeneration.

## Context
Gender‑inclusive language models are a growing concern in AI ethics, where biased outputs can reinforce stereotypes. This work demonstrates that lightweight techniques like LoRA and activation steering can improve fairness without large retraining costs.

## Implications
These findings suggest that inference‑time representation engineering offers a practical path for deploying socially aligned models in production pipelines. Practitioners can adopt such methods to fine‑tune behavior on the fly, reducing both computational expense and model drift risk.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23083v1)
