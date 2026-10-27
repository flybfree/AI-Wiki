---
title: MultiEvoSkill: Structure-Aware Multi-Agent Skill Evolution for Generalizable Skill Artifacts
published: 2026-10-25T12:43:01Z
authors: Kounianhua Du, Jianxing Liu, Ruoshui Shan, Yucheng Zhang, Ke Li, Xing Sun, Weinan Zhang
url: http://arxiv.org/abs/2610.34260v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MultiEvoSkill: Structure-Aware Multi-Agent Skill Evolution for Generalizable Skill Artifacts

## Abstract
Skill documents are becoming the default adaptation surface for frozen large language model (LLM) agents, but current skill generators face two key limitations. First, humans and different LLMs differ in how they organize procedural knowledge and approach task solving. Skills authored from a human or single-model perspective may therefore fail to align with the reasoning behaviors of other backbones, limiting cross-model generalization. Second, sequential skill descriptions inadequately represent procedures with parallel branches and explicit dependencies, while existing skill optimizers primarily operate on prose and lack explicit support for graph-structured skill evolution. We introduce MultiEvoSkill, a skill-optimization framework comprising three core components: 1) Skill compiler casts the skill as a typed graph with tailored operators, producing a compact, informative representation with explicit procedural topology; 2) Heterogeneous agent system proposes revision advices using collective intelligence, where minimal and informative issues are identified based on multiple sets of experiences. 3) Structure-aware debate and evolution mechanism organizes candidate edits into a heterogeneous graph, resolves them under dependency and importance constraints, and distills the collective proposal into the artifact. Multi-dimensional gating ensures the information gain and topological correctness of each evolution. Optimal skills are then obtained when the system converges at a consistent state. Various experiments and ablations against SOTA methods validate the effectiveness and generalization of MultiEvoSkill.

## Metadata
- **Published**: 2026-10-25T12:43:01Z
- **Authors**: Kounianhua Du, Jianxing Liu, Ruoshui Shan, Yucheng Zhang, Ke Li, Xing Sun, Weinan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34260v1)