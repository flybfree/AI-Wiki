---
title: DUD: Decoupled Update Dynamics for Reliable Uncertainty Quantification in Large Language Models
published: 2026-08-04T10:04:33Z
authors: Yixin Bu, Runze Xia, Guanyun Zou, Yupeng Ji, Haodong Liu, Piji Li
url: http://arxiv.org/abs/2608.03411v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DUD: Decoupled Update Dynamics for Reliable Uncertainty Quantification in Large Language Models

## Abstract
Accurate Uncertainty Quantification (UQ) is critical for reliable deployment of Large Language Models (LLMs), yet traditional probability-based metrics often fail to capture the model's true epistemic state. While recent mechanistic approaches leverage hidden state dynamics, they typically aggregate residual stream updates, conflating the distinct roles of parametric memory (Feed-Forward Networks) and contextual processing (Attention). We argue that this aggregation obscures fine-grained mechanistic conflicts, such as memory-context misalignment, that are fundamental indicators of uncertainty. To address this, we introduce \textbf{D}ecoupled \textbf{U}pdate \textbf{D}ynamics \textbf{(DUD)}, a framework that explicitly decouples FFN and Attention contributions via noise-induced causal interventions. By quantifying the independent restoration capabilities of each module, we construct a dual-stream dynamic profile that captures the model's internal fragility. Extensive experiments demonstrate that DUD significantly outperforms state-of-the-art baselines in both uncertainty estimation and calibration, while exhibiting superior cross-dataset generalization, validating decoupled dynamics as a robust proxy for model faithfulness.

## Metadata
- **Published**: 2026-08-04T10:04:33Z
- **Authors**: Yixin Bu, Runze Xia, Guanyun Zou, Yupeng Ji, Haodong Liu, Piji Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03411v1)