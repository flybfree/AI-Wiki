---
title: SKILL.state: Scalable Long-Horizon Agent Skills
published: 2026-08-26T18:00:06Z
authors: Sanket Badhe, Priyanka Tiwari, Jonghyun Chung
url: http://arxiv.org/abs/2608.26263v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SKILL.state: Scalable Long-Horizon Agent Skills

## Abstract
Large Language Models (LLMs) increasingly act as autonomous agents executing complex, long-running procedural skills. Existing agent runtimes maintain execution by continually appending observations, actions, and intermediate reasoning traces to an ever-growing conversation history, causing latency degradation and context-poisoning failures over long horizons. We present SKILL.state, a runtime architecture that replaces append-only conversational history with an explicit, mutable execution state. At each execution step, the model receives only the immutable skill specification, the current structured execution state, and the latest observation. Intermediate reasoning is discarded immediately after producing a validated state update, preventing prompt growth with execution history. Across diverse datasets, models, and execution environments, SKILL.state improves task accuracy while substantially reducing cumulative token consumption. Our results demonstrate that explicit execution state is an effective and architecture-agnostic abstraction for scalable long-horizon agent skills.

## Metadata
- **Published**: 2026-08-26T18:00:06Z
- **Authors**: Sanket Badhe, Priyanka Tiwari, Jonghyun Chung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26263v1)