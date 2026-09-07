---
title: Testing Interchangeability in LLM Agent Teams
published: 2026-09-04T15:32:20Z
authors: Jianxin Gao, Tianyi Yu, Linna Deng, Runze Li, Zining Wang
url: http://arxiv.org/abs/2609.05279v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Testing Interchangeability in LLM Agent Teams

## Abstract
Production multi-agent systems replace agents constantly, on the assumption that an agent filling a role is interchangeable with any other agent that can do the job. We test that assumption. Eight teams per setting are formed independently from one base model on the same tasks, each agent keeping a private notebook across ten formation episodes; we then trade role-matched agents between teams and measure what changes on held-out tasks. Against a placebo that reproduces the disruption of a roster change without changing who occupies the seat, a swap costs little in task score but raises the communication a team spends per unit of progress by 16 to 63 percent, and in Hanabi a swapped agent is more expensive than an inexperienced one, consistent with interference from conventions learned with its former partner. In Collab-Overcooked, when the agent that sets the agenda is replaced, most of the extra communication comes from the agent that stayed. Three ablations, over base models, decoding temperature and formation length, move the swap penalty alongside one other quantity: how far independently formed teams drift apart. Greedy decoding lowers both; doubling a team's history raises both. In these settings, agents are more fungible in task outcome than in coordination efficiency, with larger swap effects after longer formation histories.

## Metadata
- **Published**: 2026-09-04T15:32:20Z
- **Authors**: Jianxin Gao, Tianyi Yu, Linna Deng, Runze Li, Zining Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05279v1)