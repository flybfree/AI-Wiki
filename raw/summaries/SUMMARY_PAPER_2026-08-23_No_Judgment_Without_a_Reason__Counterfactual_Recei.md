---
title: No Judgment Without a Reason: Counterfactual Receipts for Versioned AI Evaluators
url: http://arxiv.org/abs/2608.20938v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_10-01-58Z_NoJudgmentWithoutaReason_CounterfactualReceiptsfor.md
generated_at: 2026-08-23 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a framework for analyzing how AI evaluators update their judgments by examining the minimal set of reasoning sources—grounds, norms, and authority—that cause such changes. It demonstrates that standard accuracy metrics mask significant robustness issues, showing that only 54.8 % of valid receipts can be recovered when source permutations are applied, while a counterfactual cube prediction score drops to 96.99 %. The authors also show that frozen models like Qwen3-1.7B achieve high standard accuracy but low receipt accuracy, highlighting the need for separate certification and prediction evaluation.

## Key Takeaways
- The eight‑cell judgment cube reveals that most model updates are driven by a single source change, yet complex multi‑source updates recover only 7.16 % of receipts under current training regimes.  
- Standard accuracy masks severe robustness flaws: permutation retraining improves consistency to 96.6 % but worsens cube prediction deficits, indicating a decoupling problem between prediction and certification.  
- Reason‑aware evaluation must report transformation consistency alongside standard accuracy to provide trustworthy auditing of AI evaluators.

## Context
Current AI systems rely on black‑box evaluators that generate correct labels without transparent reasoning, posing risks in high‑stakes applications such as autonomous agents or regulatory compliance. Existing benchmarks focus solely on final label correctness, ignoring the underlying logical steps that produce those judgments. This work addresses the gap by formalizing accountability through receipts and a counterfactual cube.

## Implications
For practitioners, separating prediction from certification enables targeted fixes that improve both accuracy and explainability without sacrificing performance. For researchers, the framework offers a benchmark (ReasonBench) to evaluate robustness across source variations, guiding safer deployment of AI evaluators in critical domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20938v1)
