---
title: Not All Experience Belongs in the Weights: Component Routing for Self-Improving GUI Agents
published: 2026-10-01T14:34:32Z
authors: Beining Wu, Zihao Ding, Jun Huang
url: http://arxiv.org/abs/2610.01787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All Experience Belongs in the Weights: Component Routing for Self-Improving GUI Agents

## Abstract
Self-improving GUI agents keep the trajectories they produce and return them to the agent, by fine-tuning or by retrieval into the prompt, and studies that compare the two destinations disagree. We attribute this to the unit of experience: a trajectory bundles items with different properties, so a conclusion about the bundle depends on its mix. To address this, (i) we introduce component routing, which splits the experience into locators, procedures, state facts and lessons and sends each component to the context or to the weights, compared on the same items across three backbone families, two environments and three seeds. One pool has two destinations: locators and lessons win in the weights, procedures and state facts in the context. (ii) We fit a rule in two properties measured before any training, recurrence and state-conditionality; it recovers the destination of a held-out backbone family in 24 of 24 cells, two interventions move a component toward the boundary, and routing by the rule beats every whole-trajectory baseline and, by +3.5 points on average, the better single destination of each backbone. (iii) We identify how training and producer-consumer differences change the value of the two destinations: note readout decreases after the same component is written into the weights, most for the items that recur most, context gains increase with the information gap, and weights gains decrease with the policy gap. Code and data will be released.

## Metadata
- **Published**: 2026-10-01T14:34:32Z
- **Authors**: Beining Wu, Zihao Ding, Jun Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01787v1)