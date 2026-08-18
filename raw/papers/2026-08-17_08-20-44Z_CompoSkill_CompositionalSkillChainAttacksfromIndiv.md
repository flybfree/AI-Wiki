---
title: CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills
published: 2026-08-17T08:20:44Z
authors: Mingxiao Liu, Zhoumian Jiang, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang
url: http://arxiv.org/abs/2608.16246v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills

## Abstract
Autonomous AI agents tackling Long Horizon Tasks depend on marketplace skills that are certified one at a time: a scanner returns a safety verdict for each skill and declares the ecosystem safe if every package passes. We show that this assumption fails under skill composition. A skill may pass the per-skill scanner individually yet participate in a risky composition when an agent connects its outputs, capabilities, or side effects with those of other scanner-passing skills. This makes skill composition risk a path level property rather than a node level property, explaining why existing skill scanners that inspect individual packages achieve limited interception. To study this threat, we present CompoSkill, a framework that constructs skill composition attacks through a dual attacker system. The white-box attacker knows the victim's installed skill pool and directly injects explicit skill-id sequences; the black-box attacker knows only a role profile, downloads the top marketplace skills for that scenario, builds a Skill Composition Graph, and searches for high risk chains whose implicit lures never name skill identifiers. We further construct CompoSkill-Bench, a benchmark of 1,140 records built from long-horizon professional workflows across five threats and six scenarios on OpenClaw and Nanobot. CompoSkill achieves risk Chain Formation Rates (CFR) up to 83.3% in the white box setting and 80.6% in the black box setting, while existing skill scanners block only a limited fraction of the risky compositions. Finally, we observe a bridge-bonus-then-hop-decay pattern: a bridge skill can increase attack success, but Attack Success Rate (ASR) decreases once additional hops make the risk chain longer than three skills. These results expose a systematic gap in single skill certification for autonomous AI agents.

## Metadata
- **Published**: 2026-08-17T08:20:44Z
- **Authors**: Mingxiao Liu, Zhoumian Jiang, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16246v1)