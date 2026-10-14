---
title: Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents
published: 2026-10-13T01:16:37Z
authors: Jianghong Zhou, Hao Rong, Chen Lin, Daoan Zhang
url: http://arxiv.org/abs/2610.17544v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents

## Abstract
Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one. We call this reasoning contraction. A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong. Most systems trust memories by counting successes and failures. We prove that such counters are badly tuned change detectors: a symmetric counter notices a partial change only after a power of its false-alarm horizon, and an unclipped one may never notice it. On five LLMs answering multi-hop questions over edited facts, ExpeL- and ACE-style counters serve 7.0-13.5x more stale answers than certified memories given the same information, and on code tasks with an exact verifier 35-73x more. Safety also has a price. When facts change and each memory is judged only by its own verified outcomes, one number, the certification load, sets how much reasoning any safe memory can skip, and under Zipf demand it yields a scaling law. Our recipe weighs each memory's failures by its own likelihood ratio, certifies its utility against live reasoning, and restarts the certificate when facts change, with the likelihood-ratio detector as the safety net for unannounced changes; for large edits it also invalidates the memory.

## Metadata
- **Published**: 2026-10-13T01:16:37Z
- **Authors**: Jianghong Zhou, Hao Rong, Chen Lin, Daoan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17544v1)