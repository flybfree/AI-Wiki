---
title: Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures
published: 2026-09-14T09:46:59Z
authors: Yuhang Wang
url: http://arxiv.org/abs/2609.15293v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures

## Abstract
When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores it. Closing the gap requires a single conditional check -- fewer than 20 lines of code -- and reduces attack success by more than fourfold in large-scale experiments across frontier models, all five major agent frameworks, and an independent benchmark. We prove formally that when enforcement probability is near zero, detection quality is irrelevant to security. We further identify two compounding failure modes -- unreliable auditors and unparseable verdicts -- that explain every collapse pattern in Emergence World. A GRPO-trained enforcement controller resolves the ambiguity case. Together these results motivate a three-requirement Audit Enforcement Specification that is absent from every deployed framework today.

## Metadata
- **Published**: 2026-09-14T09:46:59Z
- **Authors**: Yuhang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15293v1)