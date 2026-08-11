---
title: OBLIVION: Workflow-Level Operational Skill Unlearning for Deployed Agents
published: 2026-08-08T17:51:51Z
authors: Zhengyang Shan, Xu Qian, Jiayun Xin, Kun Li, Yue Zhang, Minghui Xu
url: http://arxiv.org/abs/2608.08264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OBLIVION: Workflow-Level Operational Skill Unlearning for Deployed Agents

## Abstract
Large language model agents are becoming operational interfaces to files, memories, registries, and external tools. This deployment shift creates a new skill revocation problem: after a skill is removed from an explicit registry, an agent may still reconstruct it from residual carriers such as archives, transcripts, schemas, or memory entries. We study this problem as operational skill unlearning, where the goal is not parameter-level forgetting, but preventing a deployed agent from rebuilding a revoked skill through primitive tools. We introduce OBLIVION, a controlled benchmark and defense harness for revoked-skill resurrection. OBLIVION models each episode as a source-to-sink workflow, applies Cross-Surface Coherent Erasure to reduce residual carriers, and uses frozen workflow remediation near dangerous sinks. On the locked 88 attack episodes, the no-defense arm reaches formal attack success rate 1.0. OBLIVION reduces the rate to 0.114 and impact-weighted exposure to 0.115 while keeping locked utility at 1.0 and benign block rate at 0. In a separate skill-attack-derived sandbox, OBLIVION reduces attack success from 1.0 to 0.2 and impact-weighted exposure from 1.0 to 0.213 while preserving all utility controls. These results support workflow-level evaluation beyond checking explicit skill entries.

## Metadata
- **Published**: 2026-08-08T17:51:51Z
- **Authors**: Zhengyang Shan, Xu Qian, Jiayun Xin, Kun Li, Yue Zhang, Minghui Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08264v1)