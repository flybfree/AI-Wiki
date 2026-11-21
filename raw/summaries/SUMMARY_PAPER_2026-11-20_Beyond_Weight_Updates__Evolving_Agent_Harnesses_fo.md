---
title: Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization
url: http://arxiv.org/abs/2611.25380v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-19_02-20-06Z_BeyondWeightUpdates_EvolvingAgentHarnessesforDomai.md
generated_at: 2026-11-20 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates an alternative to traditional weight-update approaches for specializing LLM agents to specific domains. Rather than fine-tuning model weights through RL or SFT, the author proposes evolving the agent harness—the system prompt, tool schemas, skill library, and planning scaffolding—while keeping the underlying policy frozen. Using a reflective evolutionary optimizer called GEPA, the resulting harness adapters require no GPU training and can be loaded per vertical domain. Experiments on SWE-bench Verified, OfficeBench, and Terminal-Bench demonstrate that harness evolution recovers most of the performance gains of weight updates at a small fraction of the compute cost, and that combining both approaches yields the best overall results.

## Key Takeaways
- Harness evolution treats the agent's scaffolding components (system prompts, tool schemas, skill libraries, planning structures) as an optimizable outer loop analogous to RL, instantiated via GEPA, a reflective evolutionary optimizer. This reframes domain specialization as a system-design problem rather than purely a model-training problem, enabling specialization without any GPU training and producing adapters that are loadable per vertical domain and composable with existing weight-based RL pipelines.
- Empirical results across three benchmarks (SWE-bench Verified, OfficeBench, Terminal-Bench) using Codev, a Claude Code-style coding agent, reveal a consistent pattern: weight updates deliver the strongest single-path performance gains, but harness evolution recovers most of those gains at a small fraction of the compute budget. Combining both paths produces the best overall performance, suggesting they are complementary rather than competing strategies.
- The paper identifies a specific failure mode of SFT-based specialization: shortened reasoning chains and increased truncation in generated outputs. Harness adapters avoid this failure mode by construction because they modify the agent's planning scaffolding and tool interactions without altering the model's internal reasoning behavior, making them a non-destructive alternative for domain adaptation.

## Context
The dominant paradigm for specializing LLM agents to vertical domains has been weight-based fine-tuning through reinforcement learning or supervised fine-tuning, which demands substantial GPU compute, risks catastrophic forgetting, and produces monolithic checkpoints that are difficult to maintain across multiple domains. This paper challenges that framing by demonstrating that a significant portion of domain-specific performance can be recovered through prompt engineering, tool schema design, and planning scaffolding optimization—components that are already part of every deployed agent system. This matters because it opens a practical path for organizations that lack large training infrastructure but still need domain-specialized agents.

## Implications
For practitioners and industry teams deploying vertical agents, this work suggests that harness-level optimization can serve as a low-cost, non-destructive first step before committing to expensive weight fine-tuning, dramatically reducing compute requirements while preserving the option to layer weight updates on top later. For the broader AI research community, the paper validates a systems-level perspective on agent specialization and highlights a concrete failure mode of SFT that practitioners should watch for, potentially shifting how future agent frameworks are designed and evaluated across benchmarks like SWE-bench and Terminal-Bench.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.25380v1)
