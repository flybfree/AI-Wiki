---
title: Beyond Correctness: Validity-Oriented Evaluation of Biomedical LLM Judges
url: http://arxiv.org/abs/2608.29127v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_08-09-29Z_BeyondCorrectness_Validity_OrientedEvaluationofBio.md
generated_at: 2026-08-31 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a validity-oriented evaluation pipeline for biomedical LLM judges that works when human labels are scarce. It augments existing benchmarks with deterministic, metric-grounded mutations to create auditable preference pairs. The study evaluates Llama‑3.1‑8B‑Instruct across four regimes and finds that SFT→RL outperforms the others on correctness, compliance, and robustness.

## Key Takeaways
- The pipeline creates auditable preference pairs via deterministic mutations to generate ground truth labels for evaluation beyond simple correctness.
- Evaluation includes three deployment-relevant dimensions: metric-derived gold labels, robustness under repeated stochastic sampling, and compliance with requested output format.
- SFT followed by RL achieves the best performance across all regimes, especially on decomposable medical tasks such as PICO extraction and MedCalc.

## Context
Biomedical LLMs are increasingly used for clinical decision support but lack reliable validation due to scarce expert annotations. This work addresses the gap by providing a scalable, metric-driven evaluation framework that can be applied broadly without extensive human labeling.

## Implications
The results suggest that combining supervised fine‑tuning with reinforcement learning yields superior performance in real‑world biomedical applications. Practitioners can adopt this pipeline to benchmark models more rigorously and prioritize tasks where decomposable reasoning matters most.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29127v1)
