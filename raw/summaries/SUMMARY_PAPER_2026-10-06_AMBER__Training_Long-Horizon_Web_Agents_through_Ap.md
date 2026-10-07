---
title: AMBER: Training Long-Horizon Web Agents through Append-Only Memory
url: http://arxiv.org/abs/2610.07118v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-05_17-11-07Z_AMBER_TrainingLong_HorizonWebAgentsthroughAppend_O.md
generated_at: 2026-10-06 21:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AMBER introduces an append-only memory framework for language-model web agents that must operate over long, multi-step interaction trajectories. Instead of repeatedly rewriting a fixed-size memory, the agent learns to reason, act, and write new memory entries while the append-only rule guarantees that previously recorded facts and corrective feedback are retained. The paper shows that this design improves long-horizon web task success compared with overwrite-based memory baselines, even when trained only from sparse outcome rewards.

## Key Takeaways
- AMBER addresses a central failure mode of overwrite-based memory: although overwrite memory can theoretically preserve any information, it must learn to carry every important fact through each rewrite, which is difficult when training signals are sparse and delayed. In interactive web-agent settings, the paper finds that overwrite memories can delete key task-relevant information and environmental corrective feedback, causing agents to lose progress or repeat mistakes.
- The append-only memory design provides retention by construction rather than relying on the model to learn perfect memory maintenance. By allowing the agent to write free-form memory entries that are never overwritten, AMBER preserves evidence, execution errors, and corrective signals across long trajectories. This makes the memory mechanism more reliable for tasks where early observations or failures matter for later decisions.
- AMBER can be trained end-to-end with reinforcement learning from outcome rewards, reducing dependence on expensive curated supervised fine-tuning data. On WebArena Lite, it improves average success over overwrite-based memory by 4.09 percentage points and increases the fraction of tasks solved across five repeated runs by 4.8 percentage points, while matching a more expensive supervised baseline and maintaining a practical token budget.

## Context
Long-horizon agent research is increasingly constrained by context-window limits and the difficulty of preserving useful information across many actions. Web agents are a particularly challenging setting because tasks require tracking page states, intermediate observations, failed attempts, and environment feedback over extended trajectories. AMBER matters because it offers a simple architectural alternative to complex memory rewriting or periodic summarization, showing that structural memory guarantees can improve reliability without requiring large amounts of curated training data.

## Implications
For practitioners building autonomous web agents, AMBER suggests that memory design can be as important as model scale or reward engineering. Append-only memory may be especially valuable in applications where agents must recover from errors, maintain factual state, and avoid losing critical evidence over long runs. More broadly, the result supports the idea that reinforcement learning can be made more effective when the agent’s memory system is designed to preserve the information needed for credit assignment and long-horizon planning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07118v1)
