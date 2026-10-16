---
title: All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents
url: http://arxiv.org/abs/2610.21147v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_03-02-24Z_All_in_OneMemory_Process_RewardedReinforcementLear.md
generated_at: 2026-10-15 22:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces All-in-One Memory (AiO-Mem), a reinforcement learning framework that unifies retrieval, memory writing, and stopping decisions for LLM memory agents under a single shared reward space. By treating these operations as transitions over a common evidence state and training a process reward model to score each action, AiO-Mem achieves consistent improvements in answer accuracy on long-context memory benchmarks compared to both static memory systems and prior RL-trained memory agents.

## Key Takeaways
- AiO-Mem addresses a critical gap in existing memory-augmented LLM systems: the lack of a shared reward space for evaluating search, writing, and stopping decisions. Instead of optimizing retrieval and memory construction as separate pipelines, the framework compiles heterogeneous interaction histories into source-traceable multi-view events, creating a unified substrate that both retrieval and memory-writing operations can reference and act upon.
- The training pipeline combines a unified memory policy actor that rolls out complete interaction trajectories over the shared evidence state with a trajectory-conditioned process reward model. This reward model is trained through evidence-grounded supervised fine-tuning and trajectory-level Direct Preference Optimization (DPO), enabling it to assign fine-grained process scores to individual actions within a trajectory rather than only evaluating final outcomes.
- The optimization algorithm, Process-Aligned DAPO (PA-DAPO), aggregates process scores into an action-balanced trajectory reward to update the memory policy. This ensures that each memory operation—whether retrieving, writing, or deciding to stop—is evaluated on its semantic quality contribution, preventing reward hacking and encouraging coherent multi-step memory strategies.

## Context
Memory-augmented large language models have become essential for handling long-horizon tasks such as multi-session dialogues, document analysis, and agent-based reasoning over extended histories. However, the field has largely treated retrieval and memory construction as independent subsystems, each optimized with its own heuristics or reward signals. This fragmentation limits the ability of agents to learn coherent, end-to-end memory strategies. AiO-Mem represents a shift toward holistic, process-level reinforcement learning for memory agents, aligning with broader trends in RLHF and process reward modeling that aim to supervise intermediate reasoning steps rather than only final outputs.

## Implications
For practitioners building conversational agents, document-grounded assistants, or autonomous systems that must maintain and reason over long-term memory, AiO-Mem offers a principled recipe for training memory policies that jointly optimize what to store, what to retrieve, and when to stop searching. The process-reward approach reduces reliance on hand-crafted retrieval heuristics and static memory schemas, potentially lowering maintenance costs and improving robustness across diverse long-context tasks. For the research community, the unified reward-space formulation and the PA-DAPO training procedure provide a transferable template for applying process-level RL supervision to any agent architecture that involves sequential decision-making over an evolving state.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21147v1)
