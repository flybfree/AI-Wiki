---
title: LAGO: Language Agents with Reusable Growing Options
url: http://arxiv.org/abs/2610.19843v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_09-12-47Z_LAGO_LanguageAgentswithReusableGrowingOptions.md
generated_at: 2026-10-14 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LAGO introduces a framework that decomposes long-horizon software engineering tasks into reusable, temporally extended "options" managed by a meta-agent, replacing the monolithic single-trajectory tool-use loop common in current language agents. Using a frozen Qwen3.5-35B-A3B model in both meta-agent and option-agent roles, the system achieves a 58.6% resolve rate on 500 SWE-bench Verified tasks, outperforming baselines like mini-SWE-agent (49.3%) and Terminus 2 (57.3%) on a fixed 150-task subset, while growing its option library across tasks without any weight updates.

## Key Takeaways
- LAGO's core architectural innovation is treating specialized language agents as reusable, temporally extended options stored in a persistent library. A meta-agent retrieves existing options or spawns new ones, dispatches sub-tasks, verifies results, and admits successful novel options into the library. This library grows across task streams without updating model weights, enabling cumulative capability improvement without fine-tuning or retraining.
- On a controlled 150-task subset where all three systems share the same policy, temperature, task IDs, and official Docker evaluator, LAGO achieves 60.3% compared to Terminus 2 at 57.3% and mini-SWE-agent at 49.3%. A 50-task component ablation reveals that removing decomposition costs four resolved tasks, shuffling reused content costs two, and removing the library entirely costs six, demonstrating that each component contributes meaningfully to performance.
- Cross-model experiments provide evidence consistent with a role for decomposition quality in driving performance gains, though the authors explicitly note that component-level causality remains task- and model-dependent, cautioning against overgeneralizing the ablation results.

## Context
Current agentic AI systems for software engineering typically rely on a single monolithic loop where one agent must handle task decomposition, execution, and verification within one trajectory, a design that struggles with long-horizon tasks requiring multi-step reasoning and tool use. LAGO addresses this by borrowing from reinforcement learning's options framework—temporally extended actions—and adapting it to language agents, creating a modular, composable system. This sits at the intersection of agent orchestration research, retrieval-augmented generation, and software engineering automation, offering an alternative to scaling model size or fine-tuning for improved task performance.

## Implications
For practitioners building agentic coding assistants, LAGO suggests that architectural decomposition and a growing library of reusable sub-task strategies can yield meaningful performance gains without retraining or swapping to larger models, making it attractive for resource-constrained deployments. For the broader field, the paper validates a modular agent design where capability accumulates through experience rather than weight updates, pointing toward systems that improve over time through structured memory rather than brute-force scaling. However, the authors' own caveat about task- and model-dependent causality signals that these gains may not transfer uniformly across domains, and practitioners should treat the component ablation findings as evidence of potential rather than guaranteed universal benefit.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19843v1)
