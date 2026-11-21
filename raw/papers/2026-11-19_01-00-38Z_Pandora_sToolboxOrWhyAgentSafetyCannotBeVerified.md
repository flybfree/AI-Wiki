---
title: Pandora's Toolbox Or Why Agent Safety Cannot Be Verified
published: 2026-11-19T01:00:38Z
authors: Mario Franco, Carlos Gershenson
url: http://arxiv.org/abs/2611.25325v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pandora's Toolbox Or Why Agent Safety Cannot Be Verified

## Abstract
Present artificial intelligence agents are constructed by means of a coupling between a fixed language model with a general computing device. We show that this coupling makes safety undecidable. In particular, we show that given some dangerous program, no algorithm can predict whether an agent will run such a program that is semantically equivalent. In general, guardrails, blacklists, whitelists and certifications can only lead to imperfect safety solutions. Under finite constraints (bounded context, values and running time) safety is decidable but still intractable. Specifically, the problem is $\mathsf{PSPACE}$-complete even when the description of the agent is known. Finally, safety is not a compositional property, i.e., agents that can be proven safe on their own can still produce unsafe behavior when grouped together. We also discuss relaxed notions of safety that could be used in practice.

## Metadata
- **Published**: 2026-11-19T01:00:38Z
- **Authors**: Mario Franco, Carlos Gershenson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.25325v1)