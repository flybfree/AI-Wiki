---
title: World of SWECraft: Agent Collaboration at Scale via Simulated Software Worlds
published: 2026-10-16T17:59:39Z
authors: Shannon Zejiang Shen, Yapei Chang, Qiyao Liang, Benjamin Newman, Jenny Liang, Rulin Shao, Ziqiao Ma, Junjie Oscar Yin, Yung-Sung Chuang, Weijia Shi, Yejin Choi, Luke Zettlemoyer, Pang Wei Koh, Mohit Iyyer, Tongshuang Wu, David Sontag
url: http://arxiv.org/abs/2610.24061v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# World of SWECraft: Agent Collaboration at Scale via Simulated Software Worlds

## Abstract
As teams of AI agents take on larger projects and long-standing open problems, agent collaboration offers another dimension for scaling inference-time compute. To understand what makes such collaboration effective and scalable, we develop Software World, a framework for simulating multi-agent coworking in realistic software ecosystems. It comes with a pipeline to create environments of real, interdependent Python packages of different topics, sizes, and dependency structures, which we call software worlds. In a simulation, agents maintain packages in the world with a high-level goal of improving software efficiency, and they are free to discover tasks to work on and collaborate with others. We evaluate agents' work in a world collectively by measuring speedup in hidden dependent packages. The framework allows us to study different elements of collaboration by varying communication, ownership, and resource allocation. We run simulations in three different worlds, totaling more than 10,000 hours of agent work across eight models. Overall, performance improvement scales with inference-time compute, with the best model improving downstream efficiency by up to 31%. We show that most agents can find meaningful tasks via collaboration, but some frontier models can prematurely stop looking for improvements and make little progress. We release the simulation framework and traces to support future studies of agent collaboration at https://szj.io/sw.

## Metadata
- **Published**: 2026-10-16T17:59:39Z
- **Authors**: Shannon Zejiang Shen, Yapei Chang, Qiyao Liang, Benjamin Newman, Jenny Liang, Rulin Shao, Ziqiao Ma, Junjie Oscar Yin, Yung-Sung Chuang, Weijia Shi, Yejin Choi, Luke Zettlemoyer, Pang Wei Koh, Mohit Iyyer, Tongshuang Wu, David Sontag
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24061v1)