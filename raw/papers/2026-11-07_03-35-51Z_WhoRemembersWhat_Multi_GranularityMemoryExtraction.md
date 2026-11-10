---
title: Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction
published: 2026-11-07T03:35:51Z
authors: Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang, Shabnam Ghadar, Peng Tang
url: http://arxiv.org/abs/2611.10439v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction

## Abstract
Self-evolving agents improve their own skills, memory, and harness code from experience without retraining the base LLM, and group-evolving agents go further by sharing these lessons across agents. Yet most such systems overlook that sharing across users and heterogeneous agents requires deciding who can benefit from each lesson and what information must remain private. We present MixUA, a memory system that distills independent user-agent trajectories into lessons and assigns each lesson to a user-agent pair, user, agent, or global scope according to whom it benefits and what it may disclose. For evaluation, we introduce CrossLearnBench, a mixed-user-agent benchmark that pairs established agent tasks with user preferences and privacy probes that test whether private facts leak into memory other users can read. With five users and seven agents, MixUA raises pass rates by up to 16 points over no memory and 5 over a single global memory, even on tasks previously tried only by other users on other agents. It retains up to 90% of previously stated preferences, and at most 0.02% of privacy probes find a planted private fact in a forbidden scope. We hope MixUA offers a scalable path toward a global system where users and agents co-evolve.

## Metadata
- **Published**: 2026-11-07T03:35:51Z
- **Authors**: Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang, Shabnam Ghadar, Peng Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.10439v1)