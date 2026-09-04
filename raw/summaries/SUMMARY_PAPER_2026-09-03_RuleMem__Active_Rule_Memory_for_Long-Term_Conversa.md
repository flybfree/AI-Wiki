---
title: RuleMem: Active Rule Memory for Long-Term Conversational Agents
url: http://arxiv.org/abs/2609.03915v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_14-30-18Z_RuleMem_ActiveRuleMemoryforLong_TermConversational.md
generated_at: 2026-09-03 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
RuleMem introduces a rule-based memory framework that creates logical rules from conversation history to actively guide evidence retrieval and reasoning. The system demonstrates superior performance on long-term dialogue benchmarks.

## Key Takeaways
- RuleMem constructs natural-language Horn clauses from dialogues, enabling the agent to retrieve semantically distant evidence.
- These clauses are directly usable for answer generation, bridging retrieval and reasoning.
- It validates these rules using Rule Perplexity Consistency (RPC), ensuring logical consistency and reliability of derived inference.
- The framework outperforms 14 baselines on LoCoMo, achieving the highest accuracy and exceeding the baseline average by 27.47 points, which is a 54.3% relative improvement.

## Context
Long-term conversational agents must maintain coherent reasoning across extensive dialogue histories where existing memory mechanisms often treat past facts passively, resulting in semantic gaps.

## Implications
This approach could enhance the reliability of AI assistants that need to recall and reason over long conversation logs, providing a scalable method for integrating logical inference into retrieval systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03915v1)
