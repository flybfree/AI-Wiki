---
title: Coverage Aware Active Evaluation for Failure Discovery with Paired Systems
published: 2026-08-13T19:26:25Z
authors: Anjali Parashar, Rachel Luo, Apoorva Sharma, Sushant Veer, Edward Schmerling, Carson Sobolewski, Mingxin Yu, Chuchu Fan, Marco Pavone
url: http://arxiv.org/abs/2608.13719v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coverage Aware Active Evaluation for Failure Discovery with Paired Systems

## Abstract
Autonomous systems can fail in rare and heterogeneous ways, making real-world failure discovery difficult under limited testing budgets. Although cheaper proxies such as simulators, lower-fidelity systems, or related policies can be sampled extensively to find failures, proxy failures often do not transfer to the real world due to sim-to-real and system-to-system gaps. The key challenge is therefore to effectively leverage proxy system information for accurate prediction of severe target system failures. We propose an adaptive failure discovery method that combines proxy evaluations with limited target system results to guide scenario selection for target system testing. Our method learns a local predictor of target risk by correcting proxy failure signals using control-variate-inspired residual modeling. To find failures that are both likely and diverse, we combine this predictor with a support-aware mutual-information objective that favors realistic, well-supported regions while expanding coverage across failure modes. Across autonomous driving, manipulation, and quadruped velocity-tracking tasks, our method discovers up to 2$\times$ as many failures as random sampling and active-learning baselines, including severe and diverse failures missed by competing methods.

## Metadata
- **Published**: 2026-08-13T19:26:25Z
- **Authors**: Anjali Parashar, Rachel Luo, Apoorva Sharma, Sushant Veer, Edward Schmerling, Carson Sobolewski, Mingxin Yu, Chuchu Fan, Marco Pavone
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13719v1)