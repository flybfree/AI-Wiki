---
title: SAF-OPD: Stable Advantage Fusion for On-Policy Distillation
published: 2026-07-31T09:28:16Z
authors: Yifan Ding, Xincheng Wei, Yoshua Y. Li, Ziheng Li, Yuquan Lu, Siyu Zhang, Dongsheng Ma, Rongxiang Weng, Xunliang Cai, Yun Chen
url: http://arxiv.org/abs/2607.29209v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAF-OPD: Stable Advantage Fusion for On-Policy Distillation

## Abstract
Reinforcement learning with verifiable rewards (RLVR) broadcasts a single response-level reward to every token, while on-policy distillation (OPD) scores each token against a stronger teacher for a dense advantage but caps performance at teacher quality and discourages exploration beyond it. Their complementarity makes combining RLVR and OPD promising, but we find that fusing the two advantages with a fixed coefficient triggers entropy collapse from two miscalibrations: a magnitude mismatch, where token-level OPD advantages can spike far beyond the bounded RLVR advantage and erase its signal, and a temporal mismatch, where sustained full-strength OPD keeps pulling the student toward the teacher and limits exploration needed to surpass it. We propose SAF, a Stable Advantage Fusion framework that resolves both issues via a lightweight, four-stage pipeline applied only to the OPD advantage: a sparsify-then-compress mechanism for magnitude control paired with a warm-up-then-anneal mechanism for temporal control, with each stage independently switchable and adding negligible overhead. Instantiating RLVR with GRPO, we evaluate SAF across seven mathematical reasoning and code generation benchmarks with Qwen3-1.7B/4B/8B: SAF avoids entropy collapse and consistently outperforms fixed-coefficient GRPO+OPD fusion, improving the aggregate score by 0.51-2.70% across all six model-domain settings while achieving more stable training.

## Metadata
- **Published**: 2026-07-31T09:28:16Z
- **Authors**: Yifan Ding, Xincheng Wei, Yoshua Y. Li, Ziheng Li, Yuquan Lu, Siyu Zhang, Dongsheng Ma, Rongxiang Weng, Xunliang Cai, Yun Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29209v1)