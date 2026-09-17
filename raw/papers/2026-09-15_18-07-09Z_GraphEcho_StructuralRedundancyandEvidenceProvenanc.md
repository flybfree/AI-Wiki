---
title: GraphEcho: Structural Redundancy and Evidence Provenance in LLM Graph Agents
published: 2026-09-15T18:07:09Z
authors: Sikun Wang, Yixi Zhou, Lei Fan, Fan Zhang
url: http://arxiv.org/abs/2609.17695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraphEcho: Structural Redundancy and Evidence Provenance in LLM Graph Agents

## Abstract
A large language model (LLM) agent can follow more graph paths without acquiring more independent evidence. GraphEcho tests whether agents mistake these repeated encounters for additional corroboration. The benchmark varies path counts and evidential origins while holding evidence content fixed, and evaluates both judgments and active exploration. Controlled synthetic experiments reveal model-dependent judgment shifts, but redundant supporting paths increase the share of repeated walks across all evaluated frozen agents. Provenance-aware post-training (PAPT) reduces revisits and improves synthetic accuracy, yet covers fewer distinct sources. On scientific claims, it continues to reduce repetition while accuracy declines. These findings expose a gap between efficient exploration and effective evidence use: an agent can learn to stop repeating itself while overlooking information it needs. GraphEcho provides a controlled way to evaluate both what graph agents conclude and whether their exploration reaches distinct evidential sources.

## Metadata
- **Published**: 2026-09-15T18:07:09Z
- **Authors**: Sikun Wang, Yixi Zhou, Lei Fan, Fan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.17695v1)