---
title: Multi-Agent Self-Improving Reinforcement Learning for Video Reasoning
published: 2026-08-25T07:46:32Z
authors: Mingwen Zhang, Jisheng Dang, Minqiang Yang, Bimei Wang, Bin Hu, Tat-Seng Chua
url: http://arxiv.org/abs/2608.28675v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Agent Self-Improving Reinforcement Learning for Video Reasoning

## Abstract
Video reasoning tasks such as grounded video question answering and temporal grounding require selecting temporal evidence that supports the query. In many current training setups, temporal supervision is applied through local objectives such as boundary regression or span generation, while verification is used mainly to rerank candidate segments at inference time. We study whether a frozen verifier can also guide training. Our multi-agent framework couples a trainable \emph{Grounder} with a frozen \emph{Verifier}: the Grounder samples candidate trajectories and evidence segments, the Verifier assigns query-conditioned segment scores, a group-relative policy-gradient objective favors trajectories that outperform their within-input peers, and a bootstrapped calibration loss steers temporal predictions toward verifier-preferred spans. Trained on source tasks and evaluated without target-dataset fine-tuning, a two-billion-parameter instantiation transfers zero-shot across grounded question answering, temporal grounding, and long-video question answering, reaching 28.7\% intersection-over-union and 25.4\% answer-grounding accuracy on a grounded-question-answering benchmark, 46.1\% intersection-over-union on a temporal-grounding benchmark, and 54.1\% on a long-video question-answering benchmark. Relative to a strong same-scale baseline, the gains are modest but consistent, with the clearest improvements on relevance-oriented metrics such as intersection-over-union and moderate-overlap recall. Within the tested benchmarks and transfer setting, the results support frozen verification as a training signal for evidence selection, while showing that strict boundary precision remains comparatively weaker. Code and models are available at https://anonymous.4open.science/r/MASIRL-E50C/

## Metadata
- **Published**: 2026-08-25T07:46:32Z
- **Authors**: Mingwen Zhang, Jisheng Dang, Minqiang Yang, Bimei Wang, Bin Hu, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28675v1)