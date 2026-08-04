---
title: PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent
url: http://arxiv.org/abs/2608.00969v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_03-48-41Z_PROGRESS_Coverage_guidedRLtoTrainSearch_augmentedL.md
generated_at: 2026-08-03 20:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PROGRESS, a coverage‑guided reinforcement learning method that trains search‑augmented LLM agents to generate decomposed queries using teacher models. It replaces outcome‑level rewards with explicit query‑decomposition guidance, improving reasoning and task performance.

## Key Takeaways
- Teacher models decompose complex queries into essential search queries, providing lightweight supervision over the policy’s decomposition decisions.
- The coverage reward explicitly shapes the agent’s ability to generate accurate decomposed queries rather than relying on final answer rewards.
- Integrated within an R1‑style training framework, PROGRESS yields better overall task performance compared with baseline RL approaches.

## Context
Search‑augmented LLM agents aim to combine large language model reasoning with external knowledge retrieval, but current reinforcement learning pipelines lack fine‑grained control over search strategies. This work addresses that gap by introducing a teacher‑guided coverage reward.

## Implications
For practitioners developing autonomous AI assistants, PROGRESS shows that explicit supervision of query decomposition can significantly boost utility without heavy compute overhead. The method may become a standard component in next‑generation agentic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00969v1)
