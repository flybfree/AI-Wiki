---
title: EmoRSS: Mitigating Emotion-Induced Over-Refusal in Large Language Models
published: 2026-10-04T06:40:16Z
authors: Shuyi Miao, Yaojin Ma, Chenhang Cui, Xiaohao Liu, Dang Jisheng, Shengda Zhuo, Fei Shen, Tat-Seng Chua
url: http://arxiv.org/abs/2610.04998v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EmoRSS: Mitigating Emotion-Induced Over-Refusal in Large Language Models

## Abstract
Emotional expression can influence the safety decisions of large language models (LLMs), offering a potential avenue for improving safety alignment. Existing studies have mainly focused on how emotional expressions facilitate attacks under harmful requests, while overlooking their effects on benign requests. We find that emotional expression can also systematically increase refusal tendencies on benign requests, leading to unnecessary over-refusal. Based on this observation, we propose emotion-guided refusal subspace steering (EmoRSS), an activation-steering method that mitigates emotion-induced over-refusal while preserving refusal behaviour on harmful requests. Specifically, we first identify a refusal-sensitive layer using layer-wise linear probes and construct a refusal subspace from sparse autoencoder (SAE) features aligned with the probe direction. Next, we use paired regular and emotional requests with the same queries to estimate the mean activation shift in the features defining the refusal subspace. Finally, we decode this shift into an activation intervention vector and apply it in the reverse refusal direction during inference, without updating the backbone parameters. Experiments on two LLMs show that, when requests contain emotional expressions, our method achieves a more favourable trade-off between refusing harmful requests and answering benign ones than prior over-refusal mitigation baselines, while better preserving general task performance.

## Metadata
- **Published**: 2026-10-04T06:40:16Z
- **Authors**: Shuyi Miao, Yaojin Ma, Chenhang Cui, Xiaohao Liu, Dang Jisheng, Shengda Zhuo, Fei Shen, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04998v1)