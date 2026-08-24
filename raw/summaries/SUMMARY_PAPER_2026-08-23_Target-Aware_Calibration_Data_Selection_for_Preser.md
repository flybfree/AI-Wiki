---
title: Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models
url: http://arxiv.org/abs/2608.21019v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_12-07-49Z_Target_AwareCalibrationDataSelectionforPreservingU.md
generated_at: 2026-08-23 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of selecting calibration data for quantized language models while preserving uncertainty measures such as confidence, margin, and abstention. The authors introduce Doubt-Preserving Quantization (DPQ), a family of recipes that use full‑precision predictions to build target‑aligned mixtures of high‑doubt examples and generic anchors. Experiments across eight models, nine benchmarks, and twenty comparison methods show that the optimal recipe varies with the preservation goal.

## Key Takeaways
- DPQ-r75 outperforms other methods on SQuAD2 answerability-boundary preservation tasks, indicating a strong focus on preserving decision boundaries rather than overall confidence.  
- Milder variants like DPQ-r50 and confidence‑only preserve broad multiple‑choice QA behavior better, showing that prioritizing confidence can improve general applicability.  
- Entropy‑only approaches excel when the goal is to maintain uncertainty entropy across diverse inputs, highlighting a trade‑off between specific risk mitigation.

## Context
Quantization reduces model size for deployment but often degrades uncertainty signals that are crucial for safe and reliable inference. Prior work has focused on accuracy or post‑quantization score adjustment without explicitly modeling how calibration data influences these signals. This paper bridges that gap by treating uncertainty preservation as a core objective of calibration selection.

## Implications
For practitioners, the findings suggest that one size does not fit all; calibration strategies must be tailored to the specific uncertainty behavior required in each application. Industry teams can therefore allocate resources more efficiently, avoiding unnecessary complexity while ensuring safety‑critical models retain necessary confidence signals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21019v1)
