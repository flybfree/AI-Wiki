---
title: Frozen Cores Need Task Signal: Fisher-Whitened Cross-Covariance for Low-Resource LLM Adaptation
published: 2026-09-01T05:52:38Z
authors: Wentao Ye, Zhanming Shen, Zhiqing Xiao, Yao Ding, Haobo Wang, Gang Chen
url: http://arxiv.org/abs/2609.00762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Frozen Cores Need Task Signal: Fisher-Whitened Cross-Covariance for Low-Resource LLM Adaptation

## Abstract
Parameter-efficient fine-tuning is usually framed as a question of how many parameters to update. Under a severe trainable-state budget, however, where those coefficients act is equally consequential. We study this choice through frozen-core adaptation: a calibration pass fixes left and right bases for each weight matrix, and fine-tuning optimizes only an $r\times r$ core. This removes the ability of trainable factors to repair a poor initial span and makes subspace quality directly observable. We introduce FCCA, which estimates the signed input--error cross-covariance, whitens it with diagonal Fisher moments, truncates it in the resulting local metric, maps the selected directions back, and applies thin QR to obtain stable core coordinates. Under a matched $r^2$ budget, we compare eight basis constructors on 11 tasks, four model settings, and three seeds. On Qwen2.5-3B, FCCA reaches an 83.0 macro-average, 2.3 points above the next-best matched-budget constructor, and exceeds its unwhitened RawGrad control on all 11 tasks. It ranks first at all three Qwen scales and finishes within 0.13 points of the best method on Llama-3.2-1B. Controlled ablations show gains of 2.7--17.2 points from whitening and identify QR as necessary for stable core optimization in the tested regime. Finally, FCCA comes within 0.32 and 0.23 average points of LoRA and DoRA while optimizing 36.9K rather than roughly 7.4M parameters. These results show that a carefully selected fixed span can recover most of the benefit of movable low-rank factors at a much smaller trainable and optimizer-state cost.

## Metadata
- **Published**: 2026-09-01T05:52:38Z
- **Authors**: Wentao Ye, Zhanming Shen, Zhiqing Xiao, Yao Ding, Haobo Wang, Gang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00762v1)