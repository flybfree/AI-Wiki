---
title: Diversity over Scale: Recursive Self-Improvement with Ensembles of Small Open-Weight Models
url: http://arxiv.org/abs/2611.28420v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_23-46-36Z_DiversityoverScale_RecursiveSelf_ImprovementwithEn.md
generated_at: 2026-11-23 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces DiVE (Diverse Models Evolve), an ensemble-based approach to recursive self-improvement (RSI) that leverages multiple small open-weight language models (8–12B parameters) instead of relying on a single frontier-scale model. By combining a shared memory, a failure log, and best-idea-wins selection rounds, DiVE enables small models to collaboratively generate and refine machine-learning solutions, achieving performance that rivals or exceeds much larger single models at a fraction of the computational cost.

## Key Takeaways
- DiVE addresses a critical failure mode of small open-weight models in RSI loops: when used alone, these models produce programs that frequently crash and whose iterative improvements stall. The ensemble architecture—comprising a shared memory pool, a structured failure log, and best-idea-wins selection rounds—allows each model to write candidate solutions from a common context while retaining only the strongest idea at every iteration, thereby stabilizing the improvement trajectory.
- On 22 MLE-bench Lite competitions, an ensemble of five 8–12B open-weight models achieved 25.4% lower test error than the average performance of its individual members and 16.7% lower error than Llama 3.3 70B used as a single model. The ensemble came within 7.1% of Qwen 3.5 122B-A10B while operating at approximately 75% of that model's cost, demonstrating that diversity among small models can substitute for a meaningful portion of the scale that traditional RSI pipelines depend upon.
- The method fundamentally shifts the RSI paradigm from "one very large model making hundreds of calls" to "several small models collaborating through structured memory and selection mechanisms," reducing per-run cost while improving solution diversity and creativity in generated programs.

## Context
Recursive self-improvement has emerged as a powerful paradigm for automating machine-learning engineering tasks, but current RSI pipelines are tightly coupled to frontier proprietary or very large open-weight models, making them expensive and inaccessible to smaller research groups or resource-constrained deployments. This paper sits at the intersection of model ensembling, program synthesis, and automated machine learning, challenging the prevailing assumption that scaling model size is the only viable path to effective RSI. By showing that architectural coordination among small models can recover much of the performance gap, the work opens a practical alternative for democratizing access to automated ML engineering.

## Implications
For practitioners and industry teams operating under compute budgets, DiVE suggests that deploying a handful of small open-weight models in a coordinated ensemble can deliver competitive automated ML engineering results without the cost or licensing constraints of frontier models. For the broader research community, the findings motivate further investigation into diversity-aware ensemble architectures as a general strategy for reducing dependence on monolithic large models, potentially reshaping how future RSI systems are designed, evaluated, and deployed in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.28420v1)
