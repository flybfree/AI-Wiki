---
title: Variance-reduced Domain Adaptation using Paired Sampling
url: http://arxiv.org/abs/2607.20367v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_16-58-45Z_Variance_reducedDomainAdaptationusingPairedSamplin.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Paired Sampling for Domain Adaptation (PSDA), a variance‑reduced stochastic variance reduction method that pairs observations within and across domains to form quadruplets sampled together during training. By minimizing expected gradient variance through linear assignment problems, PSDA reduces variance compared to correlation alignment or maximum mean discrepancy losses. Experiments on three domain shift datasets show improved target accuracy.

## Key Takeaways
- The proposed PSDA technique creates quadruplet pairs that are always sampled together, forming a fixed‑size batch that stabilizes training and lowers gradient variance.
- The pairing design is equivalent to solving linear assignment problems, which ensures the loss has finite‑sum structure suitable for classical stochastic variance reduction methods.
- Simulations show reduced variance relative to existing UDA losses, leading to higher target domain accuracy on three benchmark datasets.

## Context
Unsupervised domain adaptation seeks to transfer knowledge from a source domain to a target domain without labeled examples. Traditional alignment losses such as correlation and maximum mean discrepancy suffer from high variance in minibatch settings, limiting their practical use. This work addresses that limitation by introducing a structured sampling strategy that preserves finite‑sum properties.

## Implications
PSDA offers practitioners a more stable training procedure for UDA tasks, potentially improving real‑world deployment where data scarcity is common. The method’s reliance on linear assignment problems may also inspire further research into combinatorial optimization in machine learning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20367v1)
