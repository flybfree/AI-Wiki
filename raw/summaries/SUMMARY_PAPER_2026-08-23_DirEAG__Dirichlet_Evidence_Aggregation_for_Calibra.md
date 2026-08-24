---
title: DirEAG: Dirichlet Evidence Aggregation for Calibrating Verbalized Confidence in Mathematical Reasoning
url: http://arxiv.org/abs/2608.20717v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_03-48-25Z_DirEAG_DirichletEvidenceAggregationforCalibratingV.md
generated_at: 2026-08-23 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DirEAG, a method for calibrating verbalized confidence in mathematical reasoning by converting each answer-confidence observation into calibrated soft evidence over candidate answers and an additional null state. Experiments on GSM8K, SVAMP, and GSM-Hard with Qwen, Mistral, and Gemma models show that DirEAG improves calibration compared to direct averaging or heuristic methods while keeping answer selection competitive.

## Key Takeaways
- The method treats confidence as calibrated soft evidence over generated candidate answers plus a null state, allowing representation of cases where none is correct. 
- Evidence aggregation addresses prompt‑dependent bias and model‑specific shifts that affect confidence scales across steering levels. 
- Ablations show that both the aggregation step and final binary calibration target different aspects of the calibration problem.

## Context
Large language models often output verbalized confidence that is not well calibrated, making it hard to trust their reasoning outputs in high‑stakes settings such as automated tutoring or research assistance. Existing uncertainty measures focus on answer agreement or entropy without linking them to the numerical self‑reported confidence, limiting practical calibration.

## Implications
This work provides a principled framework for improving model reliability by aligning reported confidence with actual correctness across diverse prompts and datasets. Practitioners can adopt DirEAG to reduce overconfidence errors and improve decision making in automated reasoning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20717v1)
