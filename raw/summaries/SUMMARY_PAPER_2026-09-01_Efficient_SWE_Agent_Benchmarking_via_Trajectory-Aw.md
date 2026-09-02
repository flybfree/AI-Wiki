---
title: Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation
url: http://arxiv.org/abs/2609.01603v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-59-46Z_EfficientSWEAgentBenchmarkingviaTrajectory_AwareEv.md
generated_at: 2026-09-01 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PTA‑IRT, a Privileged Trajectory‑Aware Item Response Theory framework that evaluates software engineering agents by leveraging both their outcomes and the detailed execution trajectories they generate. By using process‑level evidence such as explored context and attempted edits, PTA‑IRT improves calibration subset selection and ability estimation compared with traditional IRT baselines on four SWE benchmarks.

## Key Takeaways
- PTA‑IRT fuses outcome scores with rich trajectory data to create a calibrated assessment that reflects how agents actually solve tasks.  
- The framework enables efficient evaluation using small calibration budgets while maintaining high accuracy in score and ranking recovery.  
- Historical execution trajectories provide privileged information that enhances the representativeness of selected test items.

## Context
Efficient benchmarking is essential for advancing AI research in software engineering because full‑scale evaluations are computationally expensive. Existing methods rely on static pass/fail matrices, which ignore the nuanced problem‑solving processes and limit their ability to detect subtle improvements or regressions.

## Implications
For practitioners, PTA‑IRT offers a practical way to obtain reliable agent performance metrics without exhaustive testing, supporting rapid iteration cycles. In industry, this approach can inform model selection and training strategies while reducing resource costs, fostering trustworthy AI deployment in code generation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01603v1)
