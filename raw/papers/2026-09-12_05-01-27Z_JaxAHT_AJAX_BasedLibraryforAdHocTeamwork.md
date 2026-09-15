---
title: JaxAHT: A JAX-Based Library for Ad Hoc Teamwork
published: 2026-09-12T05:01:27Z
authors: Caroline Wang, Rolando Fernandez, Zelal Su Mustafaoglu, Montek Kundan, Jiaxun Cui, Lingyun Xiao, Zhihan Wang, Di Yang Shi, Aditya Madhan, Johnny Liu, Arrasy Rahman, Peter Stone
url: http://arxiv.org/abs/2609.13716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JaxAHT: A JAX-Based Library for Ad Hoc Teamwork

## Abstract
Ad Hoc Teamwork (AHT) addresses the challenge of designing agents capable of coordinating with novel partners without prior coordination. However, progress in the field is hindered by the prohibitive computational cost of the AHT research lifecycle, the lack of standardized benchmark implementations, and the absence of a diverse, validated evaluation teammate suite. In this work, we introduce JaxAHT, the first open-source, JAX-based library designed to accelerate and standardize the AHT research lifecycle. Leveraging JAX's hardware acceleration and massive parallelization capabilities, JaxAHT provides a unified framework for teammate generation, ego agent training, and evaluation against unseen teammates, achieving approximately 95x wall-clock speedup over PyTorch counterparts. Alongside the library, we contribute a diverse suite of evaluation teammates across the domains of Level-Based Foraging, Overcooked, and Hanabi. To illustrate the value of the framework, we use it to conduct a large-scale, compute-controlled benchmark study comparing teammate generation and AHT agent learning methods, finding that no algorithm consistently performs best, and that agent modeling primarily offers benefits in role-based scenarios with diverse teammates.

## Metadata
- **Published**: 2026-09-12T05:01:27Z
- **Authors**: Caroline Wang, Rolando Fernandez, Zelal Su Mustafaoglu, Montek Kundan, Jiaxun Cui, Lingyun Xiao, Zhihan Wang, Di Yang Shi, Aditya Madhan, Johnny Liu, Arrasy Rahman, Peter Stone
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13716v1)