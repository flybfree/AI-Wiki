---
title: Router Sensitivity Under Lightweight Fine-Tuning Identifies Prunable Experts in Mixture-of-Experts Models
published: 2026-08-08T03:36:41Z
authors: Ali Janati, Kaoutar El Maghraoui, Xinyi Luo, Wenyuan Shen, Owen Zou, Yankai Mao
url: http://arxiv.org/abs/2608.07890v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Router Sensitivity Under Lightweight Fine-Tuning Identifies Prunable Experts in Mixture-of-Experts Models

## Abstract
Mixture-of-Experts (MoE) models decouple total parameters from per-token compute, but deployment still requires storing every expert. Recent theory shows that pruning experts with the smallest router-norm changes during fine-tuning can preserve accuracy, but assumes full fine-tuning. We test whether lightweight adaptation can recover this signal. We briefly fine-tune with a parameter-efficient adapter, rank experts by the induced $\ell_2$ router change, and prune the least-changed experts in one shot. On Mixtral-8$\times$7B-Instruct (44.83% MMLU-Pro), router-only LoRA trains 0.002% of parameters and outperforms all-module LoRA at matched rank with half the experts removed (27.54% vs. 24.42%); signal quality declines as adaptation spreads to attention and expert weights. Accuracy improves monotonically with LoRA rank, reaching 28.76%. IA3, which leaves router weights frozen, matches direct router adaptation, whereas unconstrained additive adapters degrade the signal. Router-guided MMLU-Pro accuracy decays quasi-linearly rather than collapsing, remains nearly 1.8 times that of magnitude-based or random pruning at maximal compression, and reduces memory by 49% and per-token latency by 37%. At 25% compression, retention is competitive with methods using full activation statistics. The criterion also transfers to Qwen1.5-MoE fine-tuned for mathematics, retaining 49.7% mean accuracy over eleven benchmarks with half the experts removed while random pruning falls to single digits. Router sensitivity under lightweight fine-tuning therefore makes provably motivated expert pruning practical at scale.

## Metadata
- **Published**: 2026-08-08T03:36:41Z
- **Authors**: Ali Janati, Kaoutar El Maghraoui, Xinyi Luo, Wenyuan Shen, Owen Zou, Yankai Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07890v1)