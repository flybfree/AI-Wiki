---
title: Marginal Matching Does Not License Factorized Sampling: Auditing Conditional Style Leakage in Factorized Generative Models
url: http://arxiv.org/abs/2608.05243v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_14-56-53Z_MarginalMatchingDoesNotLicenseFactorizedSampling_A.md
generated_at: 2026-08-06 21:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper challenges the common assumption that factorized generative models achieve independent style and class representations by showing that matching only the marginal distribution of a latent style variable does not guarantee independence from class labels. The authors demonstrate that this mismatch allows linear probes to recover class information with high accuracy while the model’s global MMD remains low. Empirically, their case‑study model reaches 99.15% clustering accuracy yet external generation succeeds only 16% of the time.

## Key Takeaways
- Matching only the marginal distribution of z_s provides no constraint on class‑conditional distributions, so style can remain predictive despite appearing Gaussian overall.
- The exact decomposition reveals that eliminating one condition is necessary but not sufficient for proper factorization; other conditions still allow leakage.
- Linear probes achieve 74%–100% accuracy (10% chance level) indicating strong class‑style coupling hidden in the model.

## Context
Factorized generative models are widely used to disentangle latent factors such as style and content, but their claimed independence is often unverified. This work highlights a gap between statistical regularization and real‑world performance, prompting researchers to reconsider how marginal statistics are reported.

## Implications
For practitioners, relying solely on marginal MMD can mislead confidence in model disentanglement. Industry adoption of factorized models must incorporate additional checks beyond marginal matching to ensure true independence, otherwise generated data may retain hidden class information that degrades downstream applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05243v1)
