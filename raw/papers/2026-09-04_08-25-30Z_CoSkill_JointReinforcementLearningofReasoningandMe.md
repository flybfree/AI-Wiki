---
title: CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution
published: 2026-09-04T08:25:30Z
authors: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
url: http://arxiv.org/abs/2609.04865v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution

## Abstract
Skill libraries improve the sample efficiency of agentic reinforcement learning (RL) by enabling large language model (LLM) agents to reuse procedural knowledge. Yet existing paradigms exhibit structural shortcomings: they either decouple skill evolution from policy optimization or instantiate meta-skills as fixed workflows. Both treat skills as passive objects to be managed, limiting the flexible evolution of skills and their co-adaptation with the reasoning agent. To address the limitations, we propose CoSkill, a unified multi-agent RL framework that recasts the static meta-skill workflow as a learnable Meta-Skill Agent and jointly trains it with a Reasoning Agent over a hierarchical skill library. By modeling the Reasoning and Meta-Skill Agents as a cooperative team sharing a single backbone, CoSkill enables end-to-end co-adaptation: the Reasoning Agent conditions its actions on a retrieved task skill and step skills selected from its child set, while its task performance guides the Meta-Skill Agent in refining those step skills. Experiments on ALFWorld and WebShop show that CoSkill substantially outperforms prior skill-based and RL baselines, achieving success rates of 98.4% and 90.6%, respectively (+3.5 and +6.2 pp). As shown in Figure 1, CoSkill achieves superior early-stage sample efficiency, asymptotic performance, and wall-clock efficiency. Our code is available at https://github.com/jinyuan-cookie/CoSkill.

## Metadata
- **Published**: 2026-09-04T08:25:30Z
- **Authors**: Jinyuan Feng, Dongmin Li, Yiqun Chen, Yang Gao, Xing Chen, Huimu Wang, Zhiqiang Pu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04865v1)