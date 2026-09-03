---
title: When Decodability Is Not Enough: Logical Validity Representations, Behavioral Dissociation, and Causal Tests in Language Models
url: http://arxiv.org/abs/2609.02438v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_11-01-09Z_WhenDecodabilityIsNotEnough_LogicalValidityReprese.md
generated_at: 2026-09-02 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how logical validity is represented in transformer language models using five open-weight models and matched valid-invalid premise-claim pairs across various inference families. Despite near-chance behavioral performance, the models show strong decoding of validity from hidden states and under held-out conditions. Validity remains decodable even when behaviorally incorrect.

## Key Takeaways
- Logical validity is almost perfectly decodable from hidden states despite low behavioral accuracy.
- Decoding holds up across different template domains and inference families, indicating robust internal representation.
- Interventions along probe-derived validity directions have only weak effects compared to random controls, showing limited causal influence.

## Context
Understanding how models encode logical reasoning beyond surface behavior is crucial for trustworthy AI. This work highlights a gap between representational fidelity and observable performance in language models.

## Implications
For practitioners, the findings suggest that improving model outputs may require deeper probing of internal representations rather than surface-level adjustments. It also underscores the need for causal evaluation methods to assess true logical reasoning capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02438v1)
