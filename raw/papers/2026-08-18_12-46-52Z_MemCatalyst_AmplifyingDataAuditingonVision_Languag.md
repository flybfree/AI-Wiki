---
title: MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning
published: 2026-08-18T12:46:52Z
authors: Xukun Luan, Jinyan Liu, Yuhui Gong, Yuanguo Bi, Bing Hu, Xuesong Li, Di Wang
url: http://arxiv.org/abs/2608.17722v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning

## Abstract
Vision-Language models (VLMs) achieve outstanding performance largely due to the amount of training data available on the internet. At the same time, data holders (e.g., artists) urgently need to determine whether their data has been used for model training without authorization, which concerns both intellectual property rights and personal privacy. Data auditing, particularly through membership inference (MI), has attracted attention as a direct tool. This work proposes MemCatalyst, a set of data poisoning tools, aiming to amplify the data auditing performance on VLMs. MemCatalyst employs two strategies: Poisoning Text (PT) and Poisoning Image (PI). MemCatalyst forces VLMs to over-learn specific inconsistencies between image features and textual semantics during training, thereby increasing their susceptibility to membership information auditing. Crucially, the transferability of poisoned samples across different VLM architectures is demonstrated to be effective in the black-box setting. Extensive evaluations using five state-of-the-art data audits on two prominent VLMs demonstrate that MemCatalyst markedly enhances MI AUC scores with a minimal budget of poisoned samples, while maintaining a negligible impact on model performance.

## Metadata
- **Published**: 2026-08-18T12:46:52Z
- **Authors**: Xukun Luan, Jinyan Liu, Yuhui Gong, Yuanguo Bi, Bing Hu, Xuesong Li, Di Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17722v1)