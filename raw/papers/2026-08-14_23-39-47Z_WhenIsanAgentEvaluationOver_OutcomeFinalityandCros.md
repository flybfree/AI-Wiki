---
title: When Is an Agent Evaluation Over? Outcome Finality and Cross-Unit Separation
published: 2026-08-14T23:39:47Z
authors: Avyay M. Casheekar
url: http://arxiv.org/abs/2608.14940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Is an Agent Evaluation Over? Outcome Finality and Cross-Unit Separation

## Abstract
Current agent evaluations score models on the state visible at the end of a stopped run which they count as one trial. However, interpreting the score as a final result would require two conditions that the endpoint does not itself necessarily establish: outcome finality and cross-unit separation. These conditions are independent, since reconciling a delayed outcome can settle the label while runs still share state and isolating runs can prevent carryover while the scored outcome remains unfinished. We develop a completion argument that specifies the evidence needed for each decision and argue that a final label is justified only when anything that could still change the claimed outcome is resolved, bounded, or retained as uncertainty. First, in a controlled replay to demonstrate the mechanism where an agent's actions were held fixed, we find that the endpoint and terminal labels differ for every delayed operation, while a delayed write changes the next run's score when service state persists between runs but not after isolation or verified reset. Second, in a review of ten public protocols, we find that all protocols identify when a run stops and what is scored, while unfinished operations and the evidence for treating runs as separate trials are documented less consistently. Finally, we propose an open-effects record that lists operations or resources that may remain relevant after the endpoint, their current status, and whether they could change the scored outcome or affect another run.

## Metadata
- **Published**: 2026-08-14T23:39:47Z
- **Authors**: Avyay M. Casheekar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14940v1)