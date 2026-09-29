---
title: Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery
published: 2026-09-28T14:48:57Z
authors: Yingming Pu, Hongyu Chen, Tao Lin
url: http://arxiv.org/abs/2609.35315v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Collaborative Principle Evolution via Evidence Transfer for Scientific Discovery

## Abstract
Large Language Model (LLM)-based agents promise to automate scientific discovery, yet exploring the vast hypothesis space remains costly. Existing principle-evolution methods accelerate this loop, but operate sequentially, which caps exploration breadth and wastes wall-clock time on challenging problems. To address this, we formulate collaborative scientific discovery as evidence transfer between parallel principle-evolution branches. We present COEVOLVE, which realizes this transfer through a coordination core over parallel branches. By integrating value-of-information-gated routing and context-discounted likelihood injection, COEVOLVE enables branches to collaborate through shared measurements while keeping their principle posteriors separate. Across six scientific-discovery tasks under a matched evaluation budget, COEVOLVE attains a mean solution quality of 66.5% versus 57.0% for single-branch principle evolution, with a 1.80x mean wall-clock speedup on the GPT-5.6-Terra backbone; on five auto-research tasks delegated to an autonomous research harness, it is the only arm whose mean stays above the published SOTA anchor on every task. These results establish when evidence sharing accelerates parallel discovery and when transfer safeguards are necessary to limit negative or inert transfers

## Metadata
- **Published**: 2026-09-28T14:48:57Z
- **Authors**: Yingming Pu, Hongyu Chen, Tao Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35315v1)