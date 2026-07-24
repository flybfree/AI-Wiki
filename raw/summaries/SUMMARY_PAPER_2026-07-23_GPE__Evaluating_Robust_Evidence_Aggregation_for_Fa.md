---
title: GPE: Evaluating Robust Evidence Aggregation for Fact Verification under Controllable GEO-Style Poisoning
url: http://arxiv.org/abs/2607.20730v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_21-04-51Z_GPE_EvaluatingRobustEvidenceAggregationforFactVeri.md
generated_at: 2026-07-23 22:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GPE, a multi-domain fact-verification benchmark and an evaluation framework designed to test robustness against GEO-style poisoning attacks. Experiments across various verification methods show that GPE reveals degradation in performance when evidence sources are manipulated, highlighting efficiency trade‑offs beyond clean evaluations. The findings confirm the necessity of adversarial evidence environments for reliable model assessment.

## Key Takeaways
- GPE creates a controlled setting where evidence can be poisoned at defined ratios, allowing systematic testing of robustness.
- The benchmark exposes that verification accuracy drops when selected documents are favored or altered, revealing hidden weaknesses in current models.
- Efficiency considerations emerge as poisoning may increase retrieval costs while reducing factual correctness, indicating a trade‑off between speed and reliability.

## Context
Fact verification relies on large language models that pull information from external sources, making them vulnerable to manipulation. Existing benchmarks assume clean data, which can mask security risks. GPE addresses this gap by providing a structured way to simulate adversarial evidence injection.

## Implications
For practitioners, GPE offers a practical tool to stress‑test verification pipelines before deployment. Industry adoption could improve trust in AI outputs and reduce false confidence stemming from poisoned information. Future research may extend GPE’s framework to other knowledge domains beyond fact checking.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20730v1)
