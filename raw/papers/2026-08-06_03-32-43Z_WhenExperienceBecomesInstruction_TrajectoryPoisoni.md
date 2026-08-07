---
title: When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems
published: 2026-08-06T03:32:43Z
authors: Jialuo Chen, Lingqi Jiang, Xinhao Deng, Xiaohu Du, Jianan Ma, Yunhao Feng, Yuqi Qing, Zhihao Yuan, Linkang Du, Jingyi Wang
url: http://arxiv.org/abs/2608.05563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems

## Abstract
Self-evolving skill (SES) systems distill agent trajectories into persistent skills, allowing untrusted experience to become trusted instruction. We introduce PoisonedEvolution, a trajectory-poisoning attack on this promotion process. Our skill-visible black-box attacker can inspect a target skill and contribute bounded evidence, but cannot observe private pools or evolution logic or edit the skill bank. Artifact poisoning requires Inclusion, Evolution Attribution, and Realization. Attribution is the distinctive bottleneck: the target behavior must appear causally useful, recurrent, and generalizable before promotion. We evaluate four representative security-effect families using inert canary specifications. At 10% attacker support, across six mainstream LLM evolvers in SkillClaw, PoisonedEvolution embeds target behaviors in 546/600 trials (91.0% SER). On the structurally different Trace2Skill pipeline at the same ratio, it embeds target behaviors in 369/600 trials (61.5% SER), demonstrating transfer across evolution architectures. In a representative controlled study, three consistent attacker records suffice in a 30-record batch, whereas a single record is much weaker. Ablations identify recurring support, causal framing, and domain-aligned encoding as the main determinants of success. These findings expose evidence promotion as a security boundary for self-evolving agents.

## Metadata
- **Published**: 2026-08-06T03:32:43Z
- **Authors**: Jialuo Chen, Lingqi Jiang, Xinhao Deng, Xiaohu Du, Jianan Ma, Yunhao Feng, Yuqi Qing, Zhihao Yuan, Linkang Du, Jingyi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05563v1)