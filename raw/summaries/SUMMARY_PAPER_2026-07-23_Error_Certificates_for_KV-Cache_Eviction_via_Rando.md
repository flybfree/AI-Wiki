---
title: Error Certificates for KV-Cache Eviction via Randomized Design
url: http://arxiv.org/abs/2607.21475v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_16-16-59Z_ErrorCertificatesforKV_CacheEvictionviaRandomizedD.md
generated_at: 2026-07-23 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses a fundamental flaw in deterministic key-value cache eviction where the top‑k tokens are kept based on importance scores while the rest are deleted. It shows that this approach cannot guarantee that the retained model output is unchanged when the evicted cache entries are altered, leading to an arbitrarily large attention‑output error that no serving estimator can detect consistently. Randomized eviction restores identifiability and enables a reliable error certificate.

## Key Takeaways
- Deterministic top‑k eviction cannot prevent the true attention output from changing when evicted cache entries are modified, breaking consistency of any service‑time estimator.
- A Poisson‑sampled tail with known inclusion probabilities allows a single logit offset inside the softmax to apply the Hájek correction, producing an error certificate with 0.97 empirical coverage at no loss in prediction accuracy.
- Survey‑sampling variance over the retained set yields a per‑step error certificate that is useful for attribution without affecting model output.

## Context
Current AI systems rely heavily on KV caches to reduce computational cost during inference. Deterministic eviction strategies are common but often sacrifice reliability because they cannot distinguish between cache‑induced errors and genuine model failures. This work introduces a randomized framework that preserves the ability to estimate true error sources, aligning with best practices in robust system design.

## Implications
Practitioners can use the certificate to schedule recomputation only when necessary, improving efficiency without sacrificing user experience. The method also provides clear attribution between cache‑related and inherent failures, guiding better resource allocation in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21475v1)
