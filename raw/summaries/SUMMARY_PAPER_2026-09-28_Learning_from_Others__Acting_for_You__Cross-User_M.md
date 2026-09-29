---
title: Learning from Others, Acting for You: Cross-User Memory Sharing for LLM Agents
url: http://arxiv.org/abs/2609.32511v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_11-59-39Z_LearningfromOthers_ActingforYou_Cross_UserMemorySh.md
generated_at: 2026-09-28 20:42
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces ShareMem, a memory architecture for LLM agents that enables cross-user memory sharing while preserving individual user preferences to solve related tasks more efficiently. It decouples reusable experience from specific values by using shared experiences to guide actions and local memories to supply concrete user requirements, refined through two-stage consolidation. Evaluations demonstrate that ShareMem significantly improves step success, task completion, and coding scores across multiple benchmarks compared to isolated user-local memory baselines.

## Key Takeaways
- ShareMem utilizes a two-stage consolidation process where shared experiences are refined locally before accepted edits are integrated into a common pool, ensuring quality control; during execution, scope-first retrieval jointly selects local and shared experiences under a budget, supported by user-bound channels for initial and agent-initiated preference retrieval.
- The architecture was evaluated across web navigation (Mind2Web), personalized interaction (VitaBench~2.0), and multi-session coding (MemoryCode) using four backbone models, consistently outperforming matched user-local memory in step success, average task success, and dialogue-macro coding scores for all tested models.
- Analysis indicates that cross-user sharing provides the most benefit when relevant local experience is scarce, while source quality and cross-user preference interference limit useful transfer, highlighting the complementarity between passive experience guidance and active preference retrieval mechanisms.

## Context
As LLM agents are increasingly deployed to serve multiple users simultaneously, the isolation of agent memories creates inefficiencies where valuable problem-solving strategies remain siloed within individual user sessions rather than contributing to collective intelligence. This work addresses a critical challenge in scalable agent architectures by exploring how knowledge transfer can occur across user boundaries without compromising personalization or introducing preference conflicts that degrade performance for the receiving user.

## Implications
For practitioners building multi-user agent systems, ShareMem offers a practical framework to reduce redundant learning and improve task efficiency by leveraging collective experience while maintaining strict adherence to individual user constraints. This approach suggests that future agent frameworks should prioritize hybrid memory structures that dynamically balance global knowledge reuse with localized preference grounding to maximize utility across diverse user bases without sacrificing safety or relevance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32511v1)
