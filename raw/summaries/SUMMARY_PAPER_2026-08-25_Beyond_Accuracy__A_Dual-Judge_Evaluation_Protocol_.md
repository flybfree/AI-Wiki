---
title: Beyond Accuracy: A Dual-Judge Evaluation Protocol for Vision-Language Models in Legally Grounded Tasks
url: http://arxiv.org/abs/2608.24258v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_08-49-46Z_BeyondAccuracy_ADual_JudgeEvaluationProtocolforVis.md
generated_at: 2026-08-25 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a dual-judge evaluation protocol for vision-language models in legally grounded tasks, using a standard 0‑10 quality judge and a strict binary semantic‑equivalence judge against a human reference. On 4,680 evaluations of UK traffic‑sign interpretation under varying visibility and occlusion, the judges show moderate association (point‑biserial r = 0.644) but an asymmetric Type II error pattern that peaks at high occlusion.

## Key Takeaways
- The dual‑judge protocol reveals a non‑zero rate of semantic mismatches even when quality scores are high, indicating that a good answer can still be legally incorrect under certain conditions.
- High visibility reduces the mismatch rate, while heavy occlusion increases it to 54–63 % for answers scoring above 7, showing that degraded inputs make the reference judge less trustworthy.
- The standard 0‑10 judge aligns closely with human judgments (Pearson r = 0.81) and with LLM accuracy sub‑scores, whereas the equivalence judge is more stringent in one direction.

## Context
Legal AI systems must not only be accurate but also produce outputs that can be justified against established legal standards. Existing benchmarks often rely on single‑judge metrics, which may overlook subtle mismatches between model output and human expectations under adverse conditions.

## Implications
Practitioners should adopt dual‑judge protocols to detect when a high‑scoring response is legally invalid, especially in safety‑critical domains like traffic sign interpretation. This approach can improve trustworthiness assessments beyond simple accuracy scores.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24258v1)
