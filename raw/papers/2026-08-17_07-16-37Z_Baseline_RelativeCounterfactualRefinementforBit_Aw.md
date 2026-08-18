---
title: Baseline-Relative Counterfactual Refinement for Bit-Aware Visual Token Communication
published: 2026-08-17T07:16:37Z
authors: Jia Guo, Xiaohan Zhao, Changwang Liu, Shuqing He, Chenyang Zhang, Bingchuan Zhao, Jinqi Zhu
url: http://arxiv.org/abs/2608.16192v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Baseline-Relative Counterfactual Refinement for Bit-Aware Visual Token Communication

## Abstract
Generative visual-token communication reduces transmission load by sending only selected discrete tokens and reconstructing missing content at the receiver. However, existing token-selection criteria based on local uncertainty, importance, or diversity do not directly determine whether changing the current selection improves the final reconstruction under the same packet budget. To address this problem, we propose Gated Counterfactual Refinement for Communication (GCR-C), a rollout-style correction layer over Local-MDL. GCR-C constructs a compact diversified candidate set, evaluates each candidate through matched full-budget Local-MDL continuation, and replaces the baseline action only when a positive baseline-relative reconstruction gain is obtained. Experiments on CIFAR-10, STL-10, a coded 5G-LDPC link, and a limited high-resolution Kodak transfer show that GCR-C consistently improves reconstruction quality at active low- and medium-rate operating points without increasing the realized packet rate, while remaining effective across changes in dataset, channel condition, resolution, token grid, and tokenizer. The results also reveal a clear quality--computation tradeoff due to the additional encoder-side counterfactual evaluation.

## Metadata
- **Published**: 2026-08-17T07:16:37Z
- **Authors**: Jia Guo, Xiaohan Zhao, Changwang Liu, Shuqing He, Chenyang Zhang, Bingchuan Zhao, Jinqi Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16192v1)