---
title: OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference
published: 2026-07-31T13:17:05Z
authors: Zhikang Xie, Xichen Ye, Yifan Wu, Haoshen Yu, Li chenan, Peizhu Gong, Weizhong Zhang, Cheng Jin
url: http://arxiv.org/abs/2607.29398v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference

## Abstract
Diffusion models have revolutionized generative tasks but incur high latency due to iterative denoising. While cache-based strategies accelerate inference by reusing intermediate features, they largely rely on static, sample-agnostic schedules. We argue that this rigidity overlooks two facts empirically validated in this paper: (i) generation difficulty varies across prompts, requiring adaptive resource allocation--complex inputs demand more computation while simpler ones require less; (ii) error sensitivity fluctuates across timesteps, where static policies may cache high-error steps or waste computation on low-error ones. We therefore propose OnlineCache, a dynamic caching framework that jointly learns when to cache and how to correct approximation errors. We leverage policy gradient to train a lightweight network for adaptive speed-quality trade-offs, and incorporate a learnable corrector to mitigate caching-induced errors. Both modules are jointly optimized under a bilevel optimization framework, with the policy targeting global generation quality and the corrector minimizing local errors. Our method automatically allocates computational resources across both samples and timesteps, improving overall generation quality. Extensive experiments demonstrate clear superiority. On FLUX.1-dev model, OnlineCache achieves nearly 3 speedup while preserving generation fidelity. On DiT and CogVideoX, it similarly delivers competitive acceleration without compromising quality; across all scenarios, it consistently outperforms existing cache-based acceleration baselines.

## Metadata
- **Published**: 2026-07-31T13:17:05Z
- **Authors**: Zhikang Xie, Xichen Ye, Yifan Wu, Haoshen Yu, Li chenan, Peizhu Gong, Weizhong Zhang, Cheng Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29398v1)