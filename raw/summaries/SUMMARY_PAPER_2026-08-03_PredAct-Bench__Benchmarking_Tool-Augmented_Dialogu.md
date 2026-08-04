---
title: PredAct-Bench: Benchmarking Tool-Augmented Dialogue under Controlled Tool Noise
url: http://arxiv.org/abs/2608.02372v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_15-15-55Z_PredAct_Bench_BenchmarkingTool_AugmentedDialogueun.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
PREDACTBENCH is a benchmark designed to evaluate dialogue agents that rely on noisy tool outputs in high‑stakes educational settings. The study demonstrates that state‑of‑the‑art language models often fail to give teachers clear visibility when the tools are unreliable, resulting in excessive over‑reliance and potential errors.

## Key Takeaways
- PREDACTBENCH creates a framework for AI‑assisted human decision‑making where noisy predictors guide users, allowing systematic study of trust dynamics.  
- The paper introduces two new metrics—Relative AI‑Reliance (RAIR) and Relative self‑reliance (RSR)—that capture episode‑level trust calibration beyond single‑turn measures.  
- Evaluation on OULAD and PREDACT‑CS datasets with a human study shows that current models do not prevent teachers from over‑trusting incorrect tool suggestions, highlighting a critical gap.

## Context
The rapid integration of LLMs into decision‑support tools assumes perfect accuracy, yet real‑world deployments face inherent noise. This work addresses the mismatch between idealized benchmark assumptions and practical system behavior by introducing realistic tool imperfection and human trust dynamics in education.

## Implications
For educators and AI developers, PREDACTBENCH signals a need to build models that explicitly surface uncertainty rather than mask it, improving safety and trust in educational AI. The findings also guide industry practice toward transparent, accountable decision‑support systems where users can evaluate tool reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02372v1)
