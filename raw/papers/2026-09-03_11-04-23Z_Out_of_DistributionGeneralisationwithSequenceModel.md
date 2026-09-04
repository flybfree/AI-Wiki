---
title: Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning
published: 2026-09-03T11:04:23Z
authors: Oussama Hidaoui, Omer Ebead, Ulrich Armel Mbou Sob, Siddarth Singh, Juan Claude Formanek, Felix Chalumeau, Omayma Mahjoub, Sasha Abramowitz, Ruan John de Kock, Wiem Khlifi, Louay Ben Nessir, Simon Verster Du Toit, Daniel Rajaonarivonivelomanantsoa, Asim Awad Osman, Arnol Manuel Fokam, Refiloe Shabe, Arnu Pretorius
url: http://arxiv.org/abs/2609.03667v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning

## Abstract
Generalising to unseen tasks remains a fundamental challenge in offline multi-agent reinforcement learning (MARL). In this work, we present a principled analysis of zero-shot task generalisation in the offline setting and conduct an extensive empirical investigation into the scaling behaviour governing task diversity, dataset size, and network capacity. To facilitate this study, we extend offline sequence modelling architectures to handle multi-task observation and action spaces alongside variable agent counts across tasks. Our primary finding is that scaling task diversity---rather than sheer dataset size is the dominant factor in achieving robust zero-shot transfer. Through large-scale experiments across four challenging environments (Connector, RWARE, SMAX, and LBF), we demonstrate that our multi-task approach achieves a mean improvement of 3.2x on held-out test tasks compared to single-task models and consistently outperforms strong behaviour cloning baselines. These results suggest that the development of generalisable MARL agents should prioritise the diversity of the training distribution with varying numbers of agents, providing a roadmap for scaling offline MARL effectively.

## Metadata
- **Published**: 2026-09-03T11:04:23Z
- **Authors**: Oussama Hidaoui, Omer Ebead, Ulrich Armel Mbou Sob, Siddarth Singh, Juan Claude Formanek, Felix Chalumeau, Omayma Mahjoub, Sasha Abramowitz, Ruan John de Kock, Wiem Khlifi, Louay Ben Nessir, Simon Verster Du Toit, Daniel Rajaonarivonivelomanantsoa, Asim Awad Osman, Arnol Manuel Fokam, Refiloe Shabe, Arnu Pretorius
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03667v1)