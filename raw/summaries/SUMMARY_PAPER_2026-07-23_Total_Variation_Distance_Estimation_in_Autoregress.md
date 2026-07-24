---
title: Total Variation Distance Estimation in Autoregressive Models
url: http://arxiv.org/abs/2607.19510v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_18-49-45Z_TotalVariationDistanceEstimationinAutoregressiveMo.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of estimating the total variation distance between two length‑n autoregressive distributions to an additive error ε under different access models. The authors present algorithms that require fewer queries than previous methods and demonstrate practical utility by comparing SGLang and vLLM serving identical weights.

## Key Takeaways
- Under sample access, the TV estimator needs only O(n²K/ε²) queries, which is a significant improvement over Meel et al.’s O(n³m/ε⁵) approach where m is the total token alphabet size.  
- Logit access provides a tight bound of O(n/ε²) queries and cannot be improved asymptotically.  
- Noisy logit access yields an interpolated guarantee of O((n+n²σ²)/ε²) queries, balancing accuracy with query cost.

## Context
The paper contributes to the field by tackling distribution estimation in large language models where inference optimizations can alter output probabilities without changing model weights. Accurate total variation distance is crucial for assessing fairness and performance differences across serving engines despite identical underlying models.

## Implications
For industry practitioners, this work offers scalable methods to quantify subtle distributional shifts that may affect user experience or downstream tasks. The ability to estimate TV distance even when KL divergence diverges opens new avenues for robust model monitoring in production LLM systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19510v1)
