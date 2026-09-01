---
title: The Fragility of Jailbreak Robustness Across Operational States
published: 2026-08-31T13:14:47Z
authors: Yuna Park, Hwang Youn Kim, Yujin Kim, Won Woo Ro, Suhyun Kim, Jae-In Hwang
url: http://arxiv.org/abs/2608.30748v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Fragility of Jailbreak Robustness Across Operational States

## Abstract
Existing jailbreak evaluations typically characterize robustness using a single attack success rate (ASR) measured in a default configuration (the vanilla state). However, user-LLM interactions can induce diverse operational states beyond the vanilla state. In this work, we find that jailbreak robustness is highly fragile to operational-state variation: even when the attack remains fixed, changing only an ordinary system prompt not designed to affect safety can dramatically alter attack success rates. We systematically investigate this phenomenon across seven aligned models and three representative jailbreak attacks, observing substantial differences in ASR between vanilla and non-vanilla operational states. In one case, ASR increases by up to 56 percentage points (2% to 58%) solely due to a change in operational state. Remarkably, these increases occur even for attacks originally designed and optimized under vanilla-state evaluation. We further show that state-dependent robustness variation is systematically associated with differences in hidden representations along a refusal-related axis, and that projections onto this axis strongly predict jailbreak outcomes. Our results show that a single vanilla-state evaluation may not fully characterize jailbreak robustness, motivating evaluations that also examine how robustness changes across non-vanilla operational states.

## Metadata
- **Published**: 2026-08-31T13:14:47Z
- **Authors**: Yuna Park, Hwang Youn Kim, Yujin Kim, Won Woo Ro, Suhyun Kim, Jae-In Hwang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30748v1)