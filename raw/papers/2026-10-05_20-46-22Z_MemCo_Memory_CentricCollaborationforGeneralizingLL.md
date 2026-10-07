---
title: MemCo: Memory-Centric Collaboration for Generalizing LLM Agents to Unseen Environments
published: 2026-10-05T20:46:22Z
authors: Xinting Liao, Siyan Liu, Rabab K. Ward, Holger R. Roth, Xiaoxiao Li
url: http://arxiv.org/abs/2610.07376v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemCo: Memory-Centric Collaboration for Generalizing LLM Agents to Unseen Environments

## Abstract
Large language model (LLM) agents increasingly operate in interactive environments, where they need to make sequential decisions through observation, action, and feedback. Although memory can help agents reuse experience, existing work designs memory in isolation, where collecting enough trajectories to populate it is expensive. Existing shared-memory approaches mitigate isolated experience by pooling episodic memories across tasks and environments. However, retrieving shared memory is challenged by the granularity, where retrieved memories can be either too specific to preserve current grounding or too coarse to support the next action. In this work, we propose MemCo, a memory-centric collaboration framework for generalizing LLM agents to unseen interactive environments. It maintains complementary local and global memory spaces, preserving environment-specific details locally while promoting transferable workflows induced from local trajectories to global memory. During online interaction, MemCo routes relevant local and global memories in terms of the agent's current state and decision phase, enabling agents to reuse the experience of other agents without blindly transferring environment-specific details. Experiments on interactive decision-making benchmarks show that MemCo improves task success and reduces redundant exploration compared with isolate-memory and shared-memory baselines. Our code is available at https://github.com/SYannL/nvdamas.

## Metadata
- **Published**: 2026-10-05T20:46:22Z
- **Authors**: Xinting Liao, Siyan Liu, Rabab K. Ward, Holger R. Roth, Xiaoxiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07376v1)