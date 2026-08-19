---
title: Abra: Scaling Diffusion Image Training
published: 2026-08-18T02:36:25Z
authors: Kyle Chickering, Wei-An Lin, Swayam Bhanded, Dan Saunders, Akshat Tripathi, Jiaming Song, Shyamal Buch, Xinchen Yan
url: http://arxiv.org/abs/2608.17286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Abra: Scaling Diffusion Image Training

## Abstract
Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systematic scaling law study for text-to-image diffusion models using Abra, a controlled family of flow-matching transformers trained across three orders of magnitude worth of compute ($10^{19}$ to $10^{22}$ FLOPs), reaching significantly larger compute budgets than previous works. We demonstrate that diffusion models scale just as predictably as language models but require far more data to train optimally: compute optimality occurs at approximately $200$ image tokens per parameter, ten times the Chinchilla compute-optimal prescription for LLMs. We show that unlike language models, diffusion models are robust to overtraining and that practitioners should err on the side of more data rather than a larger model. Finally, we show that this predictability extends beyond training loss to generative quality metrics, optimal CFG settings, representation quality, and even the shape of the training curves, which collapse onto a universal form.

## Metadata
- **Published**: 2026-08-18T02:36:25Z
- **Authors**: Kyle Chickering, Wei-An Lin, Swayam Bhanded, Dan Saunders, Akshat Tripathi, Jiaming Song, Shyamal Buch, Xinchen Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17286v1)