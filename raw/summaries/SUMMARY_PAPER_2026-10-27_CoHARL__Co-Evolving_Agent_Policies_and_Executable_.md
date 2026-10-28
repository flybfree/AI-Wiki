---
title: CoHARL: Co-Evolving Agent Policies and Executable Harnesses with Reinforcement Learning
url: http://arxiv.org/abs/2610.36469v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_01-25-26Z_CoHARL_Co_EvolvingAgentPoliciesandExecutableHarnes.md
generated_at: 2026-10-27 20:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CoHARL introduces a population-based reinforcement learning framework that simultaneously co-evolves a shared LLM agent policy and a population of executable harnesses governing tool use and feedback. Rather than optimizing a harness for a fixed policy or training a policy under a static interface, CoHARL adapts the harness throughout the training process by using a proposer that revises harness code based on execution traces. The framework achieves a 27.6% mean resolved rate on SWE-rebench, outperforming harness-only search by 6.4 percentage points and surpassing alternative training strategies under matched budgets.

## Key Takeaways
- CoHARL addresses a fundamental coupling problem in LLM agent training: optimizing a harness for a fixed policy ignores how the policy's behavior changes during learning, while training a policy under a fixed harness leaves the interface generating training experience unchanged. By co-evolving both components simultaneously, the framework ensures the training environment adapts as the agent improves.
- The framework employs a population-based approach where the policy learns from rollouts across multiple harnesses, and a proposer uses execution traces to revise harness code during training. This population-based mechanism provides diverse training experiences and prevents the agent from overfitting to a single interface configuration.
- Under matched training budgets, CoHARL outperforms two alternative strategies: searching for a harness once before RL training, and alternating policy updates with revisions to a single active harness. This demonstrates that simultaneous co-evolution is more effective than sequential or single-harness adaptation strategies, with gains demonstrated across SWE-bench Verified and Terminal-Bench 2.0.

## Context
This paper sits at the intersection of LLM agent training, reinforcement learning, and software engineering automation. As LLM agents increasingly rely on executable harnesses to interact with environments—managing tool calls, parsing feedback, and structuring observations—the design of these harnesses becomes a critical bottleneck for agent performance. Prior work treated harness design and policy training as separate problems, creating a mismatch between the training interface and the agent's evolving capabilities. CoHARL represents a shift toward treating the agent-environment interface as a learnable component rather than a fixed scaffold, aligning with broader trends in automated program synthesis and evolutionary computation applied to AI systems.

## Implications
For practitioners building LLM-based coding agents and software engineering assistants, CoHARL suggests that investing in adaptive harness design during training yields substantially better downstream performance than post-hoc harness engineering or static tool configurations. For the broader AI research community, the co-evolution paradigm opens a new direction for agent training where the environment interface itself becomes a trainable artifact, potentially applicable beyond software engineering to any domain where agents interact with structured tool environments. Industry teams deploying agentic coding systems could benefit from population-based harness search integrated into their training pipelines rather than relying on hand-crafted or single-configuration tool interfaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36469v1)
