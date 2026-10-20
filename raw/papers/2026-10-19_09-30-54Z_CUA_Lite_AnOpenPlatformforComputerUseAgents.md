---
title: CUA-Lite: An Open Platform for Computer Use Agents
published: 2026-10-19T09:30:54Z
authors: Zhanhui Zhou, Weichen Zhang, Haoran Liu, Lingjie Chen, Tianneng Shi, Kevin Lin, Zhengyuan Yang, Lijuan Wang, Dawn Song
url: http://arxiv.org/abs/2610.26071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CUA-Lite: An Open Platform for Computer Use Agents

## Abstract
Open resources for computer use agents (CUAs) -- environments, datasets, and models -- remain scattered: without a standard, these resources cannot be integrated and scaled; additionally, evaluation, RL, and SFT cannot share one infrastructure. We present CUA-Lite, an open platform for developing CUAs, built around three standardized abstractions: (1) Unified environment interface, under which we integrate 12 benchmarks across desktop, browser, and mobile, plus lightweight VM-free sandboxes that replicate OSWorld's desktop at much lower cost, providing over 30,000 verifiable tasks. (2) Unified supervised data format, into which we convert the major public CUA datasets, from GUI grounding and understanding to full rollouts, and record our fresh rollouts from frontier CUAs on these verifiable environments. (3) Model harnesses shared across evaluation, RL, and SFT, one per model and implemented for 14 model families. Each harness runs its model in these computer environments, producing the rollouts that evaluation and RL consume, or renders stored supervised data into the model's own training format for SFT. We release reference scores across the integrated benchmarks, and show that RL and SFT through the same harness improve open-weight models. We release our dataset, code, and models, and the platform is open to contributions.

## Metadata
- **Published**: 2026-10-19T09:30:54Z
- **Authors**: Zhanhui Zhou, Weichen Zhang, Haoran Liu, Lingjie Chen, Tianneng Shi, Kevin Lin, Zhengyuan Yang, Lijuan Wang, Dawn Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26071v1)