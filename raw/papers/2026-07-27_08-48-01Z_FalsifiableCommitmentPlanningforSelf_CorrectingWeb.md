---
title: Falsifiable Commitment Planning for Self-Correcting Web Agents
published: 2026-07-27T08:48:01Z
authors: Guangyi Liu, Huan Zhao, Quanming Yao
url: http://arxiv.org/abs/2607.24167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Falsifiable Commitment Planning for Self-Correcting Web Agents

## Abstract
Long-horizon web agents often go off track before final failure: a trajectory can remain locally plausible even after the current state, reused skill, or plan assumption no longer supports the user instruction. Existing agents can plan, reflect, or reuse experience, but their plans rarely specify the evidence under which an active step should still be trusted. We propose FCPAgent, a falsifiable commitment planning framework for robust long-horizon web agents. FCPAgent represents each plan step as a Falsifiable Commitment Unit (FCU): a subgoal grounded in a reusable skill, together with confirming evidence, falsifying evidence, and a confidence score. Execution is organized as a plan-test-repair loop. The hybrid commitment testing module checks candidate actions before they modify the browser and checks observations after execution; for efficiency, it combines lightweight evidence matching with LLM-based diagnostic verification. When evidence falsifies a commitment, scope-aware repair localizes the contradiction to the execution, skill, or planning level and revises the smallest adequate part. On WebArena, FCPAgent achieves a 13.8% relative improvement in average success over the strongest baseline, with especially large gains on long-horizon tasks.

## Metadata
- **Published**: 2026-07-27T08:48:01Z
- **Authors**: Guangyi Liu, Huan Zhao, Quanming Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24167v1)