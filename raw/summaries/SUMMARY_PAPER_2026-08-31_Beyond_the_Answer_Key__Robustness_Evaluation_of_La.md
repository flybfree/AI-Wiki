---
title: Beyond the Answer Key: Robustness Evaluation of Large Language Models for Step-Level Mathematical Verification
url: http://arxiv.org/abs/2608.28725v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_16-17-11Z_BeyondtheAnswerKey_RobustnessEvaluationofLargeLang.md
generated_at: 2026-08-31 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a benchmark for evaluating large language models as evaluators of mathematical reasoning by measuring both final‑answer correctness and step‑level trace accuracy. The study shows that state‑of‑the‑art LLMs are robust to canonical solutions but fail on perturbed yet logically equivalent traces, especially when localizing errors. Supervised fine‑tuning and test‑time compute can improve robustness but often at the cost of canonical performance.

## Key Takeaways
- Models that correctly grade canonical solution traces often reject valid perturbed traces with false‑rejection rates up to 85.3%, indicating strong dependence on a specific solution form.
- The gap in error localization is pronounced: base models degrade substantially when the trace deviates from the expected canonical pattern, even though the underlying answer remains correct.
- Improvements through supervised fine‑tuning or test‑time compute are model dependent and may trade off accuracy on canonical traces for better robustness.

## Context
The paper addresses a longstanding issue in AI research where evaluation focuses solely on final outputs while ignoring the internal reasoning process. As LLMs become used as automated graders, ensuring they can handle variations of valid solutions is crucial for reliable deployment in education and research settings.

## Implications
For developers and educators, this work highlights that evaluator robustness must be measured independently from solver accuracy to avoid hidden biases. Companies relying on LLM‑based grading systems should consider additional validation steps or fine‑tuning strategies to mitigate false rejections of valid solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28725v1)
