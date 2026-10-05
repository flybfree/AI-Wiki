---
title: Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite
url: http://arxiv.org/abs/2610.02826v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_05-17-40Z_ScalingTrajectoriesforComplexTasksthroughRecursive.md
generated_at: 2026-10-04 21:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Recursive Self-Rewrite (RSR), a framework that leverages a single base model (Qwen-3.8-27B) to discover successful solutions across diverse task harnesses and then reconstructs those solutions into reusable training trajectories under a general harness. By combining a planner, critic, and executor pipeline, RSR expands 2,001 successful source trajectories into 11,094 rewritten trajectories for supervised finetuning, yielding substantial performance gains on terminal-based coding and task-completion benchmarks compared to both the base model and direct trajectory SFT.

## Key Takeaways
- RSR demonstrates that combining three different task harnesses jointly solves 759 tasks out of approximately 3,000 self-curated terminal tasks, representing a 34.3% improvement over the strongest individual harness in the recorded pool. This shows that harness diversity is a meaningful source of complementary problem-solving capability that can be harvested and consolidated into a single model.
- The framework's three-component pipeline—planner, critic, and executor—serves a critical quality-control function: the planner extracts procedures into runbooks, the critic screens for verifier leakage and solution leakage while guiding recursive revision, and the executor follows qualified runbooks in fresh sandboxes. This iterative filtering and rewriting process is what enables the expansion from 2,001 source trajectories to 11,094 rewritten training trajectories without propagating errors or shortcuts from the original harnesses.
- Training on RSR-generated trajectories produces measurable improvements across multiple benchmarks: pass@3 on Terminal-Bench 2 rises from 57.0% to 74.2%, Terminal-Bench 4 from 1.5% to 9.1%, a self-curated Terminal-Bench Hard from 39.0% to 63.0%, and Software Terminal-Bench from 3.0% to 6.0%. Process reward on Long-Horizon Terminal-Bench also improves from 0.21 to 0.29, indicating gains not just in final outcomes but in the quality of intermediate reasoning steps.

## Context
A persistent challenge in training large language models for complex, multi-step tasks is that the specialized scaffolding or "harnesses" used during data collection—such as tool-use frameworks, verification loops, or domain-specific environments—are often unavailable at deployment time, creating a train-test mismatch. RSR addresses this gap by treating diverse harness-assisted experiences as raw material that can be distilled into general-purpose training data, effectively decoupling the discovery of solutions from the conditions under which they are learned. This positions the work within the broader research thread on data augmentation, self-improvement, and curriculum construction for agentic models.

## Implications
For practitioners building agentic or tool-using models, RSR offers a practical recipe for harvesting high-quality supervision from heterogeneous task environments without requiring access to those environments at inference time, which could reduce the engineering burden of maintaining multiple specialized harnesses during training. For the broader field, the results suggest that recursive self-rewriting with leakage screening can serve as a scalable data-generation strategy, potentially applicable beyond terminal tasks to software engineering, scientific reasoning, and other domains where specialized scaffolding aids discovery but general deployment is required.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02826v1)
