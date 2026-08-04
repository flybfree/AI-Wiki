---
title: What Could the Agent See at 19:05? Generating Temporal Enterprise Scenarios from Real Research and Replaying Them to Evaluate Agents
published: 2026-08-02T06:56:56Z
authors: Tezan Sahu, Himani Arora
url: http://arxiv.org/abs/2608.01042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Could the Agent See at 19:05? Generating Temporal Enterprise Scenarios from Real Research and Replaying Them to Evaluate Agents

## Abstract
Enterprise AI agents act across many apps whose data changes continuously, so an answer is correct only relative to what data existed and who could see it at the moment it was asked. Offline evaluation today grades against a single static snapshot, effectively the end of the episode. So, it can only evaluate one situation, the final one, even though every earlier moment of the episode is a different situation that invites its own realistic questions with its own correct answers. Recreating each of those moments as a separate snapshot would mean re-provisioning a whole tenant per instant, which is prohibitively costly; and even a single snapshot leaks future state hidden inside records and cannot represent the multi-app, time-ordered way real work happens. Our system closes two gaps at once: it generates a realistic, persona-driven, temporally-evolving enterprise world from real research, and replays that world at any chosen moment to evaluate any pluggable agent. A schema-inferred temporal description drives a deterministic-plus-LLM rebuild of each record's past state; because the queryable moments are finite, all rebuilds are precomputed into a compact difference cache, making evaluation a fast, reproducible lookup with no model in the path. We describe the design, an architecture spanning both flows, and early experience evaluating enterprise agents.

## Metadata
- **Published**: 2026-08-02T06:56:56Z
- **Authors**: Tezan Sahu, Himani Arora
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01042v1)