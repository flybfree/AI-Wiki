---
title: When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory
url: http://arxiv.org/abs/2608.12888v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_07-10-22Z_WhenYourAgentOpenstheChatApp_Agent_ControlledSearc.md
generated_at: 2026-08-13 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the performance gains of agent‑memory systems stem from the structure they impose on conversation logs or from effective retrieval over raw logs. ReFind demonstrates that a simple, agent‑controlled lexical search can outperform complex graph and tree‑based memory models without building any semantic index.

## Key Takeaways
- ReFind achieves 58.2 mean accuracy on MemoryAgentBench, surpassing the best graph‑ and tree‑based systems (HippoRAG 2 at 53.2) using only a GPT‑4o‑mini backbone and no LLM‑generated index.  
- The system relies on four chat‑native controls—session‑aware rank fusion, local context expansion, temporal narrowing, and skipping already‑inspected sessions—to improve retrieval quality over a basic iterative keyword loop.  
- On LongMemEval‑S/M with GPT‑5‑mini, ReFind reaches 93.2 ± 3.3 for precise‑retrieval tasks and 89.3 ± 6.0 for fact tracking, showing that lexical retrieval can match or exceed structured memory capabilities.

## Context
Current AI agents often rely on elaborate memory structures such as graphs or trees to answer questions from conversation histories. While these structures promise rich reasoning, they also introduce overhead in index construction and maintenance. This work shows that a lightweight, agent‑driven search approach can deliver comparable or better performance, suggesting that heavy structural modeling may not be necessary.

## Implications
For developers building conversational agents, the findings encourage a shift toward simpler, retrieval‑centric designs that keep raw logs intact. Practitioners can focus on optimizing query control and feedback loops rather than investing in complex memory indexing, potentially reducing latency and computational cost while maintaining high accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12888v1)
