---
title: EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents
url: http://arxiv.org/abs/2608.05446v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_22-29-20Z_EvoHarness_RL_LearningSelf_EvolvingRuntimeHarnessf.md
generated_at: 2026-08-06 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EvoHarness-RL, a reinforcement learning framework that learns harness policies for long-horizon LLM agents to manage external state and tool usage. It achieves high success on ALFWorld with Qwen3-8B by combining supervised fine‑tuning of harness actions with cost‑aware GRPO for state coordination. The key findings are harness annealing, where the model internalizes recurring harness calls, and harness evolution, which refines the external workspace into a compact adaptive state.

## Key Takeaways
- EvoHarness-RL learns to construct useful external state offline and updates it online during task execution.
- Harness annealing reduces frequent harness calls by integrating patterns into the policy.
- Progress updates and experience consolidation create a compact, task‑adaptive state substrate.

## Context
Long‑horizon LLM agents face challenges in maintaining consistent external workspace usage without manual engineering. Existing solutions rely on static prompts or heuristics that limit adaptability across tasks. This work demonstrates that trainable harness policies can dynamically shape the agent’s interaction with tools and memory.

## Implications
Automating harness construction could lower development effort for complex multi‑step AI agents, enabling more reliable long‑term planning. Practitioners may adopt EvoHarness‑style RL to create self‑evolving external workspaces, improving performance without enlarging model size or adding heavy tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05446v1)
