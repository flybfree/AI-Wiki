---
title: Code Owns the Simulation, Jev Owns the Evaluation
url: http://arxiv.org/abs/2610.01834v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_15-06-40Z_CodeOwnstheSimulation_JevOwnstheEvaluation.md
generated_at: 2026-10-01 22:07
model: qwen3.6-35b-a3b
---

## Summary
This paper examines "Jev" judgment models that output action probabilities in a single call without reasoning text, revealing a sharp performance boundary between evaluation and simulation capabilities. While Jev excels at selecting options based solely on input descriptions, it fails when decisions require predicting unseen variables like opponent actions or prerequisite subgoals. The authors demonstrate that integrating code-based simulation with Jev's evaluation strengths yields expert-level agent control, whereas relying on the model for both tasks leads to systematic errors despite intact underlying knowledge.

## Key Takeaways
- Jev models succeed in "evaluation" mode when the optimal choice is directly inferable from the input, achieving 99% accuracy on counterintuitive cognitive reflection tests, but fail significantly in "simulation" modes where actions depend on predicting external factors not present in the context, such as opponent moves in matrix games or necessary subgoals in ALFWorld tasks.
- Failures are attributed to architectural constraints rather than knowledge deficits; Jev often answers simulation queries correctly when asked separately and performs well given simulated inputs, indicating that the bottleneck is the requirement to perform both prediction and evaluation within a single non-reasoning inference call.
- The study advocates for a hybrid architecture where code handles simulation tasks

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01834v1)
