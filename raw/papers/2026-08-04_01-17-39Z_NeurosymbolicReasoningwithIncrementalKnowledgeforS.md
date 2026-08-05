---
title: Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning
published: 2026-08-04T01:17:39Z
authors: Subrat Prasad Panda, Blaise Genest, Arvind Easwaran
url: http://arxiv.org/abs/2608.02993v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neurosymbolic Reasoning with Incremental Knowledge for Sample Efficient Hierarchical Reinforcement Learning

## Abstract
(Flat) Reinforcement Learning (RL) agents face significant challenges in environments with sparse rewards that require long-horizon reasoning. A compelling approach to improve sample efficiency is to incorporate knowledge into learning and decision-making. In standard Hierarchical RL (HRL), knowledge is encoded in a fixed, non-updatable form, such as architectural choices, and remains unchanged throughout learning. With fixed HRL, reasoning with incremental knowledge learned during exploration is impractical before sufficient environmental knowledge is acquired, leading to poor sample efficiency. In this work, we propose neurosymbolic HRL with {\em Incremental Knowledge (InK)}: symbolic high-level components perform {\em symbolic planning} (e.g. using $D^*$) on an updatable representation of current InK, while low-level goal-conditioned neural modules learn motion primitives through experience using reward shaping. Experiments on navigation tasks demonstrate that incorporating InK substantially improves sample efficiency. Additionally, to perform {\em optimal} symbolic planning given {\em prior} knowledge about the world, we develop Belief World Tree Search. The code is available at https://github.com/CPS-research-group/ink_bwts.

## Metadata
- **Published**: 2026-08-04T01:17:39Z
- **Authors**: Subrat Prasad Panda, Blaise Genest, Arvind Easwaran
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02993v1)