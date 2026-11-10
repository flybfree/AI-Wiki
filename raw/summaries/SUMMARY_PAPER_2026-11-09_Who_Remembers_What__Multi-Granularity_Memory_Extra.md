---
title: Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction
url: http://arxiv.org/abs/2611.10439v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-07_03-35-51Z_WhoRemembersWhat_Multi_GranularityMemoryExtraction.md
generated_at: 2026-11-09 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MixUA, a multi-granularity memory extraction system designed for multi-user, multi-agent environments that distills independent user-agent interaction trajectories into reusable lessons and assigns each lesson to a specific scope—user-agent pair, individual user, individual agent, or global—based on who benefits and what information must remain private. The authors also present CrossLearnBench, a benchmark combining agent tasks with user preferences and privacy probes, and demonstrate that MixUA improves task pass rates by up to 16 percentage points over a no-memory baseline while keeping privacy leakage at 0.02% or below.

## Key Takeaways
- MixUA addresses a critical gap in self-evolving and group-evolving agent systems: most existing approaches share learned lessons globally without considering that different users and heterogeneous agents have different needs, permissions, and privacy boundaries. MixUA solves this by assigning each extracted lesson to one of four granular scopes, ensuring that a lesson learned by one user on one agent is only visible to the entities that can legitimately benefit from it.
- The evaluation benchmark CrossLearnBench pairs established agent tasks with user-specific preferences and planted private facts, testing both whether agents can transfer knowledge across users and agents they have not previously interacted with, and whether private information leaks into memory scopes where it should not appear. With five users and seven agents, MixUA achieves up to 16-point pass-rate gains over no memory and 5-point gains over a single global memory, even on tasks previously attempted only by other users on other agents.
- Privacy preservation is quantified rigorously: MixUA retains up to 90% of previously stated user preferences while ensuring that at most 0.02% of privacy probes detect a planted private fact in a forbidden memory scope, demonstrating that fine-grained scope assignment can nearly eliminate cross-user information leakage without sacrificing utility.

## Context
Self-evolving agents that improve their skills, memory, and harness code from experience without retraining the base LLM represent a rapidly growing research direction in AI systems. Group-evolving agents extend this by sharing lessons across multiple agents, but the literature has largely treated shared memory as a monolithic global store. This paper matters because real-world deployments involve multiple users with distinct preferences and heterogeneous agents with different capabilities, making naive global sharing both ineffective and privacy-violating. MixUA and CrossLearnBench fill a gap by formalizing the multi-granularity memory assignment problem and providing a benchmark to evaluate it.

## Implications
For practitioners building multi-user agent platforms, MixUA offers a scalable architectural pattern that avoids the privacy risks and performance degradation of a single global memory while enabling cross-user and cross-agent knowledge transfer. The 16-point improvement on tasks previously seen only by other users and agents suggests that properly scoped memory can unlock collaborative learning at scale without retraining base models. For the broader field, this work signals a shift from single-agent memory designs toward co-evolving ecosystems where users and agents jointly improve, raising new questions about governance, consent, and auditability of shared agent knowledge that industry deployments will need to address.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10439v1)
