---
title: The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability
published: 2026-07-22T15:48:39Z
authors: Abigail Woodring, Adrian Chan, Rana Muhammad Shahroz Khan, Sukwon Yun, Chau-Wai Wong, Tianlong Chen
url: http://arxiv.org/abs/2607.20301v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional Spaces Explains Temporal Portability

## Abstract
Fine-tuning has been widely used to adapt large language models (LLMs) for domain-specific tasks. Parameter efficient fine-tuning (PEFT) methods such as low-rank adaptation (LoRA) are frequently used to reduce computational costs. PortLLM is a training-free and data-free scheme used to adapt LLMs after continual pretraining. Although the initial PortLLM results show that LoRA patches exhibit short-term temporal portability, the long-term performance of PortLLM across several updates of continual pretraining remains underexplored. Furthermore, the intriguing effectiveness of PortLLM is not well understood from a theoretical standpoint. We address these two open questions by (1) performing an extensive empirical study of the long-term temporal portability of PortLLM patches across 10 continual pretraining steps using base models Mistral, Gemma, and Qwen; and (2) offering two theoretical analyses to explain our observation that the simple PortLLM method achieves competitive performance. We find empirically that the portability persists across longer time duration, indicating that repeated fine-tuning is not required when the base model is periodically updated. We find theoretically that near-orthogonality of high-dimensional vectors is a key justification for temporal portability. Our analyses also demonstrate a geometric perspective of the loss landscape in facilitating the theoretical comparison of different adaptation options.

## Metadata
- **Published**: 2026-07-22T15:48:39Z
- **Authors**: Abigail Woodring, Adrian Chan, Rana Muhammad Shahroz Khan, Sukwon Yun, Chau-Wai Wong, Tianlong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20301v1)