---
title: The Wording Effect: Quantifying Two-Way Drift in LLM Benchmark Performance
url: http://arxiv.org/abs/2608.11694v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_06-05-47Z_TheWordingEffect_QuantifyingTwo_WayDriftinLLMBench.md
generated_at: 2026-08-12 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how small changes in the wording of benchmark questions can cause large and opposite shifts in model performance, a phenomenon termed drift. By generating meaning‑preserving variations across linguistic, referential, pragmatic, and structural axes, the authors demonstrate that some failures become successes and vice versa. Their experiments on GSM8K, MMLU, and MATH‑Hard reveal significant bidirectional drift for eight models.

## Key Takeaways
- Rephrasing a problem while keeping its meaning fixed can flip a model’s answer in both directions, indicating large bidirectional drift.
- Weak models gain more correct answers from rephrasing than they lose, whereas strong models lose far more correct answers than they gain, showing that sensitivity to wording does not fade with model strength and instead changes sign.
- The observed fragility lies primarily in the rephrased problem rather than in the model itself.

## Context
Benchmark evaluation traditionally treats a single phrasing as representative of all possible ways a question could be asked. This study shows that such an assumption is misleading, because meaning‑preserving variations can dramatically alter performance metrics across models and tasks.

## Implications
Practitioners must recognize that benchmark scores are sensitive to wording and may not reflect true underlying ability. This calls for more robust evaluation frameworks that account for drift rather than relying on static phrasing alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11694v1)
