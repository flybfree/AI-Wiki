---
title: A Few More Tokens Ahead: Reinforcing Parallelism in Diffusion LLMs
published: 2026-10-13T11:37:04Z
authors: Jiahao Kuang, Yangfan Gao, Tao Gui, Yuanbin Wu, Qi Zhang, Xuanjing Huang, Tao Ji
url: http://arxiv.org/abs/2610.18200v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Few More Tokens Ahead: Reinforcing Parallelism in Diffusion LLMs

## Abstract
Parallel generation is widely regarded as an inherent advantage of diffusion large language models. Yet our fixed-quota evaluation of four representative models reveals severe degradation across mathematics and code, with all scores below 15% at 16 tokens per step. Token-level probes identify local predictive potential near the observed prefix, especially in mathematical text. We propose RePara, which reinforces short consecutive token blocks through group-relative policy optimization and reduces rollout and log-probability recomputation costs. On LLaDA and SDAR, \ours improves GSM8K and MATH-500 accuracy over JustGRPO under reduced denoising budgets, with a 1.96x training-step speedup in our LLaDA/MATH setup.

## Metadata
- **Published**: 2026-10-13T11:37:04Z
- **Authors**: Jiahao Kuang, Yangfan Gao, Tao Gui, Yuanbin Wu, Qi Zhang, Xuanjing Huang, Tao Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18200v1)