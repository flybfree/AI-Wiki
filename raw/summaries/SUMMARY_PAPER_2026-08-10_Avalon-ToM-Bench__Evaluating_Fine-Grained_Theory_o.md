---
title: Avalon-ToM-Bench: Evaluating Fine-Grained Theory of Mind via Asymmetric Game Mechanics
url: http://arxiv.org/abs/2608.09638v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_14-19-08Z_Avalon_ToM_Bench_EvaluatingFine_GrainedTheoryofMin.md
generated_at: 2026-08-10 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Avalon-ToM-Bench, a benchmark that uses The Resistance: Avalon's asymmetric game mechanics to evaluate Theory of Mind reasoning in large language models. It decomposes ToM into epistemic versus motivational reasoning crossed with inference versus action using human‑crafted queries. Results show that while models understand the game rules well, their social reasoning is weak.

## Key Takeaways
- Reasoning, not knowledge: Models demonstrate strong rule comprehension but poor mental‑state inference, indicating failures are in social reasoning rather than missing factual data.
- Expression, not representation: Linear probing reveals high accuracy of correct inferences in hidden states (77‑82%) while generated outputs have lower accuracy (62‑70%), showing a gap between internal representation and output.
- Policy, not deliberation: Dedicated reasoning training improves performance significantly (+11.0 points) compared to test‑time chain‑of‑thought which yields only marginal gains (+1.1 points), indicating that robust ToM relies on learned policies rather than extra inference time.

## Context
Theory of Mind remains a challenge for AI, and most benchmarks either lack fine‑grained decomposition or provide only holistic performance metrics. This work contributes a granular evaluation framework that isolates epistemic versus motivational reasoning and inference versus action, offering clearer diagnostic signals for model improvement.

## Implications
For researchers, the findings suggest focusing on training policies rather than simply increasing chain‑of‑thought length could yield better ToM capabilities. For industry practitioners, Avalon-ToM-Bench provides a concrete tool to assess and target specific aspects of social reasoning in deployed models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09638v1)
