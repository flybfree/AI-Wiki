---
title: SCOPE: Score-Isolated Agentic Optimization for Video World Models
published: 2026-08-15T05:08:28Z
authors: Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
url: http://arxiv.org/abs/2608.15043v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCOPE: Score-Isolated Agentic Optimization for Video World Models

## Abstract
Video world models are increasingly used as simulators for planning and embodied decision making, yet improving them at inference time introduces a subtle evaluation problem: prompts, samplers, verifiers, and selectors may evolve together, making it difficult to attribute gains or prevent held-out feedback from shaping the final policy. We introduce \scope (\emph{\scopefullname}), a framework for auditable inference-time adaptation of frozen video world models. \scope represents external controls as a typed state, updates this state only through bounded changes supported by development evidence, and freezes the resulting policy before held-out evaluation. On Physics-IQ benchmark, \scope improves over the exact frozen base by $+14.24$ (95\% CI $[+8.10,+21.23]$). Controlled ablations further identify gains from scene specification, sampling, and learned selection, while the margin over the strongest matched agentic baseline remains unresolved. Cross-backbone and prospective evaluations reveal a complementary result: useful inference-time updates exist, but their benefits do not transfer uniformly across models and settings. Together, these findings suggest that reliable inference-time adaptation requires not only better proposals, but also a principled mechanism for deciding which updates should become part of the deployed system. Code is available at https://github.com/YuhuaJiang2002/SCOPE.

## Metadata
- **Published**: 2026-08-15T05:08:28Z
- **Authors**: Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15043v1)