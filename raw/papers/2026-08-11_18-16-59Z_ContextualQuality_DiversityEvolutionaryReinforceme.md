---
title: Contextual Quality-Diversity Evolutionary Reinforcement Learning for HVAC Control in Tropical Commercial Buildings
published: 2026-08-11T18:16:59Z
authors: Tran Le Vu
url: http://arxiv.org/abs/2608.11324v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contextual Quality-Diversity Evolutionary Reinforcement Learning for HVAC Control in Tropical Commercial Buildings

## Abstract
This paper proposes a contextual quality-diversity evolutionary reinforcement-learning controller, CQD-ERL, for the supervisory control of a tropical, water-cooled chiller plant and its associated air side. Rather than converging to a single scalarised policy, the controller maintains a product archive of specialised policies indexed jointly by a data- driven operating context, a cluster of daily weather and load regime, and a context-invariant behaviour descriptor, filled by a gradient-free evolutionary operator and a soft-actor-critic policy-gradient operator that share one replay buffer. Every action is filtered through a deterministic safety shield before execution. The controller is trained on a two-tier reduced-order environment representing the latent load, cooling-tower approach and humidity constraints of a Singapore commercial building, and is evaluated over a full annual backtest against an ASHRAE Guideline 36 baseline.

## Metadata
- **Published**: 2026-08-11T18:16:59Z
- **Authors**: Tran Le Vu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11324v1)