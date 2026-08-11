---
title: Mismatch Matters: On-Policy Distillation Beyond Token Agreement
url: http://arxiv.org/abs/2608.09836v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_16-53-14Z_MismatchMatters_On_PolicyDistillationBeyondTokenAg.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
On-policy distillation suffers from degenerate agreement where students mimic teacher outputs without learning. The paper introduces TIDE to address token-level mismatches and improves reasoning performance on Qwen3 benchmarks.

## Key Takeaways
- Student-excess tokens are produced by the student but given near-zero probability by the teacher, causing unbounded log‑ratio corrections that destabilize updates.
- Student-deficit tokens represent preferences of the teacher that are rarely sampled by the student, preventing transfer of reasoning patterns when absent.
- TIDE applies bounded Hellinger shaping to suppress severe excesses and injects a top‑K teacher probability mass analytically, restoring missing probabilities without requiring deficit sampling.

## Context
Current LLM fine‑tuning relies heavily on token agreement metrics that can mask deeper failures in model behavior. Recent works focus on improving alignment but often ignore the impact of mismatched tokens on downstream reasoning tasks.

## Implications
Practitioners will benefit from more robust distillation methods that correct both excess and deficit tokens, leading to shorter, cleaner responses and higher accuracy on complex prompts. This shift could reduce reliance on token‑level metrics in evaluating model quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09836v1)
