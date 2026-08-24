---
title: No Judgment Without a Reason: Counterfactual Receipts for Versioned AI Evaluators
published: 2026-08-21T10:01:58Z
authors: Ye Chen, Weining Zhang
url: http://arxiv.org/abs/2608.20938v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# No Judgment Without a Reason: Counterfactual Receipts for Versioned AI Evaluators

## Abstract
Evaluators often produce correct labels via flawed reasoning, a critical failure for agentic systems gating actions, routing reviews, or supplying training feedback. Standard evaluation only verifies final label correctness, ignoring whether judgment changes stem from valid evidence, consistent rules, or proper rule applicability. We formalize evaluator reasoning accountability via three core sources: grounds, norms, and authority. Varying these sources yields an eight-cell counterfactual judgment cube to characterize judgment updates. We define judgment receipts as minimal source replacement sets that reproduce revised verdicts to explain judgment transitions. We derive certification cost bounds for black-box evaluators and present ReasonBench, a policy and logical reasoning benchmark with verifiable receipts covering 19,520 cases and 7,200 controls. In frozen evaluations, Qwen3-1.7B reaches 98.41% receipt accuracy, while cube prediction scores 96.99%, a consistent 1.42-point drop validated by Qwen3-0.6B replication. Strong standard accuracy masks severe robustness flaws. Meaning-preserving source permutations reduce valid receipt recovery to 54.8% and 49.2% for direct and cube prediction. Models trained on simple single-source changes retain 93.75% verdict accuracy but recover only 7.16% of receipts for complex multi-source updates. Permutation retraining boosts consistency to 96.6% yet worsens cube prediction deficits. Structured counterfactual supervision fails to guarantee robust reasoning. We show reason-aware evaluation must decouple prediction and certification, reporting transformation consistency alongside standard accuracy for trustworthy evaluator auditing.

## Metadata
- **Published**: 2026-08-21T10:01:58Z
- **Authors**: Ye Chen, Weining Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20938v1)