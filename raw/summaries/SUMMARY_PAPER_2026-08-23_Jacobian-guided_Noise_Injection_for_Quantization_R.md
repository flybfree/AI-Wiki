---
title: Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models
url: http://arxiv.org/abs/2608.20988v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_11-16-40Z_Jacobian_guidedNoiseInjectionforQuantizationRobust.md
generated_at: 2026-08-23 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the instability of self‑attention in quantized large language models by identifying the softmax operator as a bottleneck that is sensitive to outliers and has a state‑dependent Jacobian. By suppressing the norm of this Jacobian, the authors propose Jacobian‑Guided Noise Injection, which injects zero‑mean Gaussian noise into pre‑attention logits with variance derived from the local Jacobian Frobenius norm. Empirically, the method yields up to +37 % relative gain in Top‑1 accuracy on ImageNet‑1K for SigLIP and a 40 % relative reduction in perplexity on WikiText under low‑bit quantisation.

## Key Takeaways
- The softmax operator’s sensitivity to outliers and its state‑dependent Jacobian is the primary source of quantization instability.  
- Suppressing the norm of this Jacobian provides a theoretical bound for how much performance can degrade due to discretization errors.  
- The proposed method computes optimal noise variance directly from the local Jacobian Frobenius norm, ensuring that injected Gaussian noise matches the model’s sensitivity profile.

## Context
Quantizing large language models is essential for efficient deployment but often sacrifices accuracy because of nonlinearities like softmax. Prior approaches either apply generic penalties or heuristics to control quantization error, which can be suboptimal and computationally heavy. This work offers a principled way to tailor noise injection to the local behavior of attention mechanisms.

## Implications
For researchers, this technique demonstrates that robustness can be engineered through data‑driven noise rather than static regularization. For industry practitioners, it enables reliable low‑bit quantized LLMs with minimal loss in performance, reducing hardware costs and accelerating model rollout.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20988v1)
