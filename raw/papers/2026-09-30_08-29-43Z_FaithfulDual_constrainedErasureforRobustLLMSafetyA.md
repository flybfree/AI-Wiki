---
title: Faithful Dual-constrained Erasure for Robust LLM Safety Alignment
published: 2026-09-30T08:29:43Z
authors: Jiaqing Li, Shide Zhou, Zhibo Zhang, Yuxi Li, Tianlong Yu, Kailong Wang
url: http://arxiv.org/abs/2609.39279v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Faithful Dual-constrained Erasure for Robust LLM Safety Alignment

## Abstract
Machine unlearning has emerged as a crucial mechanism for removing hazardous knowledge and enforcing safety alignment in Large Language Models (LLMs). However, recent studies reveal a persistent security risk: unlearned models remain highly vulnerable to retraining attacks, where suppressed malicious behaviors rapidly resurface after benign fine-tuning. In this work, we investigate the optimization dynamics of unlearning and identify that this vulnerability stems from shallow alignment. Rather than effectively erasing target knowledge, models often exploit a shortcut by activating previously dormant parameters to act as spurious suppressors, forming a fragile inhibitory shell over intact malicious representations. To address this issue and enforce authentic memory deletion, we propose FDCU, a novel dual-constrained subspace projection framework. FDCU restricts parameter updates through a highly scalable, element-wise dual-masking rule: it preserves general knowledge manifolds via Fisher Information and strictly prohibits the abnormal activation of spurious suppressors via the Principle of Minimal Functional Intervention (PMFI). By reliably blocking the model's ability to superficially hide knowledge, FDCU promotes the authentic dismantling of target representations. Extensive experiments across specific knowledge erasure and safe output control tasks demonstrate that FDCU achieves state-of-the-art robustness against retraining attacks while maintaining near-lossless general utility, ensuring durable safety for LLMs.

## Metadata
- **Published**: 2026-09-30T08:29:43Z
- **Authors**: Jiaqing Li, Shide Zhou, Zhibo Zhang, Yuxi Li, Tianlong Yu, Kailong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39279v1)