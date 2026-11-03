---
title: Agentic Context Management for Multi-Turn Human-AI Conversations
url: http://arxiv.org/abs/2611.00518v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-31_01-13-55Z_AgenticContextManagementforMulti_TurnHuman_AIConve.md
generated_at: 2026-11-02 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Agentic Conversation Context Curation (AC3), a training-free method that addresses context pollution in multi-turn LLM conversations by using a separate analyzer to consolidate task specifications from user messages only, audit assistant outputs against those specifications, and edit the conversation context accordingly. The authors demonstrate that AC3 closes 55–84% of the performance gap between full context and the Assistant Omission oracle on benchmark tasks, and that the critical mechanism is rebuilding the specification rather than selectively removing spans.

## Key Takeaways
- Context pollution in multi-turn conversations occurs because the model's own earlier outputs remain in context and anchor later turns, causing early misreadings of user intent to persist even after correction. Simply dropping all assistant messages (Assistant Omission) removes this pollution but fails in referential interactions where later turns depend on drafts, decisions, and tool-call results that exist only in assistant turns.
- Pollution is contagious: an analyzer that sees the assistant's reasoning while extracting the specification performs worse than no intervention at all, and instructing it to ignore assistant turns does not close the gap. The authors therefore structurally exclude assistant turns from the analyzer's input, establishing that contamination cannot be mitigated by prompting alone.
- On the Lost in Conversation benchmark, AC3 closes 55–84% of the gap between full context and the AO oracle on three of four tasks and exceeds AO on the fourth, while an LLM that faithfully summarizes history does not reproduce the gain even with more compute. In stateful tool use (tau2-bench), AO collapses to 0% on every model while AC3 does not collapse, confirming that the method preserves referential dependencies that AO destroys.

## Context
Multi-turn conversational AI systems are increasingly deployed in production settings where users iteratively refine requests, reference prior outputs, and chain tool calls. The degradation of LLM performance across turns is a well-known but poorly solved problem, with most existing approaches either truncating context or applying attention-based filtering. This paper reframes the problem as one of specification integrity rather than token management, proposing a structural separation between user intent extraction and assistant output auditing. This connects to broader work on context engineering, retrieval-augmented generation, and agent architectures where maintaining a clean task specification across many turns is essential for reliability.

## Implications
For practitioners building conversational agents, AC3 offers a training-free intervention that can be layered onto existing systems without fine-tuning, making it immediately deployable in production pipelines where context windows are constrained or where accumulated assistant outputs degrade response quality. The finding that pollution is contagious and cannot be mitigated by instruction alone has direct architectural implications: any system that uses a secondary model to analyze conversation history must structurally isolate it from the primary model's outputs. For the broader field, this work suggests that the path to robust multi-turn interaction lies in specification reconstruction rather than in ever-larger context windows or more sophisticated attention mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00518v1)
