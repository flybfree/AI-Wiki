---
title: How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation
published: 2026-07-27T23:22:17Z
authors: Funda Durupinar
url: http://arxiv.org/abs/2607.25140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation

## Abstract
This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outward expression. The architecture contains no hand-authored mechanism for directly transferring affective state between agents; instead, inter-agent influence arises through the perception-appraisal-expression loop. The agent representation draws on the Big Five personality model and Russell's circumplex model of affect. To limit latency, low-level steering and navigation are handled by a conventional crowd simulator operating independently of the LLM-based cognitive layer.   We evaluate the architecture across five scenario environments spanning alarming, joyful, and neutral situations in different spatial layouts. The results show that the system produces emotional contagion dynamics with spatial, temporal, and personality-dependent structure in sparse, small crowds. Alarm spreads from seeded agents as a traveling front, the mean alarmed fraction settles at a nonzero plateau, and the distribution of prompted personality profiles determines whether an ambiguous alarm ignites panic and whether a provocation is interpreted as anger or fear. We further evaluate the appraisal step through controlled experiments across prompt variants, sampling temperatures, and four model backends, showing that the dynamics are backend-dependent.

## Metadata
- **Published**: 2026-07-27T23:22:17Z
- **Authors**: Funda Durupinar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25140v1)