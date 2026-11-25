---
title: Tracing Attacker Diversity Reduction in Adaptive LLM Red Teaming
published: 2026-11-23T03:23:01Z
authors: Chris Tava
url: http://arxiv.org/abs/2611.29960v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tracing Attacker Diversity Reduction in Adaptive LLM Red Teaming

## Abstract
Reinforcement learning can increase the success of automated red teaming but it also narrows the attack vector. This study asks where in the attacker-defender-judge learning loop does the narrowing begin and which mechanisms lead to a narrowing attack. Six mechanisms (defender adaptation, success edge, reward reinforcement, row cap, update size, and measurement) are tested across three experiment arms (co-trained, frozen defender, half learning rate) for twenty-four iterations. A frozen defender narrows attack diversity retention (ADR) earlier 0.496 relative to co-trained 0.891 at iteration twelve. Defender updates delay narrowing but dont prevent it. Successful attacks ("winners") have narrower attack diversity than the full set of generated attacks. Attacks closest to previous winners succeed 10-15 percentage points more often than those closest to previous failures. This winner-neighbor advantage holds after a defender update and for a fixed defender too. Attacks with a common opening have a common-opening advantage of 5-16 percentage points. The training row cap and update size account for little impact on ADR, and attack length accounts for only part of the ADR decrease. Narrowing appears to originate from the success only reward through the group-relative training advantage to the attacker update, with a persistent success edge setting the direction.

## Metadata
- **Published**: 2026-11-23T03:23:01Z
- **Authors**: Chris Tava
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.29960v1)