---
title: PG-SFT: Balancing Capability Acquisition and Retention in Offline Agent Fine-Tuning
published: 2026-10-01T02:32:20Z
authors: Ronghua Li, Zi Liang, Zhishan Li, Shinan Liu
url: http://arxiv.org/abs/2610.00949v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PG-SFT: Balancing Capability Acquisition and Retention in Offline Agent Fine-Tuning

## Abstract
Supervised fine-tuning (SFT) on offline agent trajectories is the standard approach for training specialized tool-using agents, but forcing models to imitate reasoning and actions token by token may harm other capabilities (e.g., general reasoning, tool calling, code generation) of the base model. In this work, we focus on studying \emph{how to better balance the trade-off between acquiring new capabilities and preserving existing ones during agent trace SFT}. By comparing several baselines in our setup, standard SFT improves the target benchmark while lowering several non-target benchmark scores; meanwhile, simply constraining distributional drift using KL penalty or limiting the update magnitude did not avoid this regression trend. Motivated by recent token-wise adaptive learning objectives, this work proposes \textbf{Privilege-Guided SFT (PG-SFT)} to leverage turn-level information gain of agent trajectories as an indicator to adjust supervision strength. PG-SFT yields a more favorable observed trade-off on the evaluated benchmarks, substantially reducing distributional drift and broad capability degradation at the cost of slight degradation in target-task performance. Our findings suggest that balancing the acquisition--retention trade-off depends not only on whether the model is anchored to its base behavior, but also on where and how strongly supervision should depart from that behavior.}

## Metadata
- **Published**: 2026-10-01T02:32:20Z
- **Authors**: Ronghua Li, Zi Liang, Zhishan Li, Shinan Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00949v1)