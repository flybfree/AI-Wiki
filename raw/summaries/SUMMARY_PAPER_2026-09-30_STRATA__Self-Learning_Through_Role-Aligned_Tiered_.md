---
title: STRATA: Self-Learning Through Role-Aligned Tiered Agents for Real-Time Strategy Games
url: http://arxiv.org/abs/2609.38881v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_03-31-06Z_STRATA_Self_LearningThroughRole_AlignedTieredAgent.md
generated_at: 2026-09-30 20:54
model: qwen3.6-35b-a3b
---

## Summary
STRATA introduces a role-aligned hierarchical multi-agent framework for Real-Time Strategy games that addresses the latency and static prompt limitations of existing LLM-based systems by enabling continuous self-learning through experience compression. The system delegates decisions across Strategic, Logistics, and Tactical Agents, utilizing a Review Agent to distill game traces into validated experience cards that enhance future decision-making. Evaluation demonstrates significant performance gains, including a win rate increase from 30% to 100% in fixed scenarios after learning, while successfully adapting to diverse opponent play styles over time.

## Key Takeaways
- STRATA decomposes RTS complexity by assigning specific responsibilities to specialized agents: a Strategic Agent handles high-level directives based on global state and experience cards, while Logistics and Tactical Agents manage execution, mitigating the inference latency issues common in monolithic LLM approaches.
- The framework implements a closed-loop learning process where a Review Agent analyzes post-match traces to extract candidate experiences, validates them against subsequent game evidence, and compresses successful strategies into concise experience cards that are retrievable by the Strategic Agent for future matches.
- Empirical evaluations show that incorporating learned experience cards dramatically improves agent performance, boosting win rates from 30% to 100% in controlled scenarios, and demonstrates the system's ability to accumulate distinct long-term strategic knowledge when sequentially facing AI opponents with varying tactical styles.

## Context
This research addresses critical bottlenecks in applying large language models to complex, dynamic environments like RTS games, where real-time decision-making requires balancing long

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38881v1)
