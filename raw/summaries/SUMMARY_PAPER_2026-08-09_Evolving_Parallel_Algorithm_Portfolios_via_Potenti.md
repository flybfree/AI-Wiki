---
title: Evolving Parallel Algorithm Portfolios via Potential-Aware Instance Generation with LLMs
url: http://arxiv.org/abs/2608.06808v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_05-00-29Z_EvolvingParallelAlgorithmPortfoliosviaPotential_Aw.md
generated_at: 2026-08-09 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the Potential‑aware Instance and Algorithm Co‑evolution (PIAC) framework to improve the performance of LLM‑based portfolio construction for combinatorial optimization problems. By generating hard instances without reference solutions and using a new potential gain metric, PIAC achieves a 19.76% relative improvement over state‑of‑the‑art baselines on TSP and CVRP.

## Key Takeaways
- The framework eliminates the need for high‑quality reference solutions by estimating generalization gain through algorithm perturbation, which is called potential gain.
- It uses LLM‑driven instance mutators that explore a wider region of problem‑instance space, increasing diversity beyond single‑mode generation patterns.
- Evaluation on six data distributions shows PIAC consistently outperforms existing LLM‑ACP methods, especially for Greedy Constructive portfolios.

## Context
Current AI research focuses on scaling language models to solve real‑world optimization tasks, yet few approaches handle the combinatorial explosion of problem instances. Generating diverse training examples is essential but hampered by reliance on reference solutions and limited mutator capabilities.

## Implications
PIAC offers a practical path for deploying LLM‑based portfolio systems in industry where reference data are scarce and instance diversity matters. Practitioners can leverage this framework to boost generalization without costly solution references, accelerating deployment of automated optimization tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06808v1)
