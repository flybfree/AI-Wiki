---
title: We Are What We Remember: Mental-State-Driven Memory for Long-Term Character Dialogue
url: http://arxiv.org/abs/2611.16223v1
type: paper-summary
date: 2026-11-14
source_paper: 2026-11-12_03-17-19Z_WeAreWhatWeRemember_Mental_State_DrivenMemoryforLo.md
generated_at: 2026-11-14 21:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MindMem, a mental-state-driven memory framework for long-term character dialogue that treats shared conversational history as evolving relational understanding rather than a passive fact store. It evaluates the framework on MemReal-Bench, a longitudinal benchmark built from month-long real-user interactions, and reports strong gains on both relational memory realization and direct question answering.

## Key Takeaways
- The central critique is that mainstream conversational memory systems often retrieve topically similar records from external fact stores, which can miss relationally pivotal experiences; MindMem instead consolidates shared experiences into source-linked mental states for the character, the user, and their relationship.
- At each turn, a specialized mental-state reasoner uses persistent states to anticipate latent user needs, form proactive intentions, and recover episodic evidence that surface-level similarity overlooks, making memory retrieval more adaptive and history-sensitive than factual recall alone.
- MemReal-Bench pairs Direct Question Answering with Situated Memory Realization to test whether agents can bridge knowing past facts and naturally using shared history, world rules, and relational trajectories; MindMem reaches 59.03% SMR and 82.58% DQA, exceeding the strongest baseline by 24.19 and 9.19 percentage points respectively.

## Context
This work matters because long-term dialogue memory is increasingly central to assistants, companions, and social agents that must maintain continuity across many turns and sessions. It addresses a gap between retrieval-oriented memory architectures and cognitive models of self-memory, suggesting that relational state representation may be more important than simple semantic similarity.

## Implications
For practitioners, the paper suggests building memory systems around evolving mental states, source-linked evidence, and proactive intention formation rather than only embedding similarity or fact lookup. For industry applications such as personalized assistants and character agents, it implies that better long-term engagement may depend on remembering how relationships change, not merely what facts were stated.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.16223v1)
