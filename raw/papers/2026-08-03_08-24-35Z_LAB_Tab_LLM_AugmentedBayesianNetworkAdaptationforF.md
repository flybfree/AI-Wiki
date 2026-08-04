---
title: LAB-Tab: LLM-Augmented Bayesian Network Adaptation for Few-Shot Tabular Generation
published: 2026-08-03T08:24:35Z
authors: Zijian Shen, Taijie Chen, Bin Zhou, Ziyang Jiang, Jintao Ke
url: http://arxiv.org/abs/2608.01879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LAB-Tab: LLM-Augmented Bayesian Network Adaptation for Few-Shot Tabular Generation

## Abstract
Tabular data generation supports analysis and decision-making when target-domain data are scarce, yet collecting complete target samples is often costly. A practical but underexplored setting provides only a few target records together with richer source data from a related domain. Existing few-shot tabular generators often either fit sparse target statistics directly, which can overfit incidental patterns, or reuse source-domain generators, which may preserve dependencies that no longer hold in the target domain. To address this problem, we propose LAB-Tab, an LLM-augmented Bayesian network (BN) adaptation framework for source-aware few-shot tabular generation. LAB-Tab first fits a BN from source data and then uses an LLM to propose plausible target-domain BN edges that are absent from the source BN graph. This step converts semantic and weak statistical evidence into explicit structural hypotheses, thereby expanding the editable edge space beyond the source-fitted graph. Because the proposed edges may be noisy and interact with existing dependencies, a PPO policy calibrates edges in the augmented BN through edge-level actions, including keep, weaken, strengthen, flip, and deactivate. The PPO policy is trained with a reward that combines distributional alignment, downstream utility, and preservation of target-relevant dependencies. The adapted BN is then sampled to synthesize target-domain tables. Across six source--target distribution-shift scenarios built from three US Census (ACS) prediction tasks, LAB-Tab achieves the best performance at the 10% target-data budget, leads four of the six individual scenarios, and reduces the macro Overall score by 33.8% relative to the strongest baseline. It also obtains the best macro JSD, WAPE, and UtilityGap while maintaining competitive feature--label preservation.

## Metadata
- **Published**: 2026-08-03T08:24:35Z
- **Authors**: Zijian Shen, Taijie Chen, Bin Zhou, Ziyang Jiang, Jintao Ke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01879v1)