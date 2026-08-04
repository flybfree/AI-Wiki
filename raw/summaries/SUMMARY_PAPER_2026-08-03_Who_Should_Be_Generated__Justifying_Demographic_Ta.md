---
title: Who Should Be Generated? Justifying Demographic Targets in Open-Ended Generation
url: http://arxiv.org/abs/2608.02551v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_17-35-31Z_WhoShouldBeGenerated_JustifyingDemographicTargetsi.md
generated_at: 2026-08-03 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the gap between fairness evaluation and generative model outputs by formalizing a “missing‑target” problem for demographic‑value‑unspecified generation. It shows that without explicit justification, output demographics can diverge significantly from intended targets, ranging from 0.508 to 0.606 on a normalized scale.

## Key Takeaways
- The geographic prior is justified under a geographic‑membership interpretation, linking the target distribution to public‑world membership rather than arbitrary assumptions.  
- The occupational prior requires an independently defended objective such as workforce‑composition fidelity, making it non‑arbitrary and defensible.  
- Target construction is not a preliminary step but an integral component of fairness evaluation, influencing model‑specific JSD₂ changes when comparators are altered.

## Context
Generative AI systems often produce outputs that reflect societal biases without explicit control over demographic composition. Fairness audits typically rely on predefined target distributions supplied by researchers, which may obscure the underlying rationale and lead to misleading conclusions about model performance.

## Implications
For practitioners, this framework demands transparent justification of each demographic target before evaluating models, preventing arbitrary or biased comparisons. It encourages a more rigorous approach where targets are grounded in real‑world objectives rather than being imposed as mere benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02551v1)
