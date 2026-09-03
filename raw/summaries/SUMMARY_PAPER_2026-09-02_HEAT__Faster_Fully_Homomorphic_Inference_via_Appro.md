---
title: HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation
url: http://arxiv.org/abs/2609.01730v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_18-02-02Z_HEAT_FasterFullyHomomorphicInferenceviaApproximati.md
generated_at: 2026-09-02 20:57
model: nvidia/nemotron-3-nano-4b
---

## Summary
HEAT introduces a fine‑tuning method that makes the per‑nonlinearity iteration counts learnable, allowing them to co‑adapt with model weights during training. On encrypted GPT‑2 decoding it reduces iterations by 3.1×, bootstraps by 1.6× and end‑to‑end latency by 1.4× while improving decode agreement over the calibrated baseline. The method demonstrates that iterative approximation errors can be managed by learning per‑site iteration budgets, which directly translates into faster encrypted inference.

## Key Takeaways
- The per‑nonlinearity iteration counts are made learnable during training, enabling co‑adaptation with weights.
- Iterations are optimized relative to the task objective, allowing the model to adapt to approximation errors without architectural changes or retraining from scratch.
- This leads to a 3.1× reduction in iterations, a 1.6× reduction in bootstraps and a 1.4× reduction in end‑to‑end latency while improving decode agreement.

## Context
Fully homomorphic encryption (FHE) enables encrypted computation but is limited by depth constraints that trigger costly bootstrapping operations. Existing solutions treat iteration budgets uniformly, ignoring per‑site error tolerances, which hampers practical deployment of large language models on encrypted data.

## Implications
For the field and industry, HEAT shows that iterative approximation can be tailored to each model site, reducing computational overhead and latency without sacrificing performance. Practitioners can adopt this approach to make homomorphic encryption viable for real‑world AI services such as secure inference pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01730v1)
