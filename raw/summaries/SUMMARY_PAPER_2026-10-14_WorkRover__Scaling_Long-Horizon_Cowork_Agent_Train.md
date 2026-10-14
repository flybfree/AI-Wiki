---
title: WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution
url: http://arxiv.org/abs/2610.18067v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_09-52-02Z_WorkRover_ScalingLong_HorizonCoworkAgentTrainingVi.md
generated_at: 2026-10-14 00:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
WorkRover presents a framework for training long-horizon cowork agents by recursively evolving interactive environments used in reinforcement learning post-training. The paper introduces a harness-driven synthesis pipeline that jointly constructs and validates aligned work contexts, executable tasks, and evidence-grounded verifiers, alongside novel training mechanisms called Factorial Compatibility Replay and Verifier-to-Turn Credit Assignment. Post-training Qwen3.5-35B-A3B with WorkRover yields substantial performance gains across multiple cowork-agent benchmarks, including 26.27 percentage points on JobBench, 29.32 points on OfficeQA Pro, and 413.25 Elo points on GDPval v2.

## Key Takeaways
- WorkRover addresses a critical gap in existing environment construction pipelines by enabling iterative refinement of task components while keeping work contexts, executable tasks, and verifiers semantically aligned. Rather than following a fixed construction workflow, construction agents adapt their actions based on workspace state and execution feedback, enabling recursive environment evolution that supports ongoing correction of defects in tasks and their associated verification logic.
- Factorial Compatibility Replay (FCR) introduces a dependency-closed replay mechanism that evaluates combinations of component revisions using rollout feedback. It selects the smallest validated repair among tested candidates while preserving task requirements and evaluation constraints, providing a principled way to evolve environments without breaking previously validated task semantics.
- Verifier-to-Turn Credit Assignment (VTCA) augments trajectory-level GRPO advantages with signals from deterministic workspace-progress checks, assigning a bounded share of positive-progress credit to prerequisite turns using recorded tool-output and artifact dependencies. This provides finer-grained training signals that help agents learn which specific actions in a long trajectory contribute to task completion.

## Context
Training long-horizon agents through reinforcement learning depends heavily on the quality and scalability of interactive environments used during training. Existing pipelines for constructing these environments tend to treat task generation, context creation, and verification as separate, fixed steps, making it difficult to iteratively refine components when defects are discovered. WorkRover sits at the intersection of agent training methodology and environment engineering, addressing how to scale RL-based post-training for agents that must perform multi-step, tool-augmented work tasks over extended horizons.

## Implications
For practitioners building agentic systems that handle complex, multi-step professional tasks, WorkRover offers a scalable recipe for generating and refining training environments without manual curation bottlenecks. The recursive evolution approach and finer-grained credit assignment could reduce the cost of training capable cowork agents while improving their reliability on realistic workplace benchmarks. More broadly, the framework suggests that environment quality and training signal granularity are as important as model architecture for advancing long-horizon agent capabilities, pointing toward a future where environment engineering becomes a first-class concern in agent development pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18067v1)
