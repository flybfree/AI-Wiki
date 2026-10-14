---
title: EvolvAttack: Backdooring self Evolving VLM Agents
published: 2026-10-11T00:33:53Z
authors: Chuan Zou, Yang Xiang, Zexin Li, Xiaonan Luo, Simin Chen
url: http://arxiv.org/abs/2610.15244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvolvAttack: Backdooring self Evolving VLM Agents

## Abstract
Self-evolving mechanisms let vision-language model (VLM) agents continually adapt through evolving memory, but they also allow malicious behavior to emerge only after deployment. We introduce a new attack surface, the self-evolving backdoor, whose payload stays dormant in the initial agent and is progressively activated as the agent evolves. Unlike conventional backdoors, which can be exposed by testing triggered inputs on a static model, our attack requires both a visual trigger and a sufficiently evolved memory state; static scanning with clean memory thus yields near-zero attack success and may deem the agent benign. We realize this through memory-aware backdoor training, which couples trigger activation with the agent's evolving memory while preserving benign behavior unless the trigger co-occurs with payload-related memory. Across three VLM backbones, four agent pipelines, and recency-, semantic-, and reward-based memory evolution, the attack preserves normal functionality and stays nearly inactive before evolution (0.5% attack success rate), yet exceeds 95% attack success within 100 interactions, revealing a stealthy threat unique to self-evolving agents.

## Metadata
- **Published**: 2026-10-11T00:33:53Z
- **Authors**: Chuan Zou, Yang Xiang, Zexin Li, Xiaonan Luo, Simin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15244v1)