---
title: Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents
url: http://arxiv.org/abs/2606.30306v1
type: paper-summary
date: 2026-06-29
source_paper: 2026-06-29_13-47-42Z_Always_OnAgents_ASurveyofPersistentMemory_State_an.md
generated_at: 2026-06-29 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper surveys persistent memory and governance aspects of always‑on agents, focusing on how state accumulates across interactions. It proposes the Always‑On Evaluation Protocol to assess state mutation and recovery obligations beyond answer quality.

## Key Takeaways
- The literature emphasizes accumulating durable state such as memories, ledgers, permissions, and audit trails rather than governing that state.
- A lifecycle view is introduced covering write, validate, organize, retrieve, act upon, update, forget, audit, and rollback of state.
- The AOEP‑v0 pilot evaluates these governance requirements by scoring mutation and recovery obligations.

## Context
Always‑on agents represent a shift from transient AI interactions to systems that retain persistent state across sessions. This work bridges AI with database and distributed system concepts, highlighting the need for formal governance in machine learning agents.

## Implications
Practitioners must design agents that manage long‑term state securely and auditably. The framework encourages integration of capability security and unlearning mechanisms into agent architectures, influencing future research on persistent AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.30306v1)
