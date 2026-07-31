---
title: One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs
published: 2026-07-30T09:30:03Z
authors: Enyi Shi, Fei Shen, Chuancheng Shi, Linxia Zhu, Shuyi Miao, Jinhui Tang, Tat-Seng Chua
url: http://arxiv.org/abs/2607.27917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Anchor for All: Unified Multilingual and Multimodal Safety Alignment for LVLMs

## Abstract
As large vision-language models (LVLMs) are deployed globally, the combination of multilingual instructions and visual information makes malicious attacks more covert and sophisticated than ever before. However, existing methods isolate language and modality defenses, which, coupled with the scarcity of safety data and high fine-tuning costs, makes it difficult for models to defend against compound attacks. To address this severe challenge, we propose a neuron-level cross-dimensional safety alignment framework driven by modality- and language-shared safety neurons (MLS-Neurons). First, we identify monolingual and unimodal safety neurons by comparing responses to harmful and benign samples, quantifying functional saliency through activation strength and downstream impact. Then, by intersecting these unimodal neurons within each language, we extract modality-shared safety neurons (MS-Neurons) responsive to both visual and textual risks, bridging the safety representation gap between modalities. Furthermore, using English as a semantic anchor, we intersect MS-Neurons across languages to identify modality- and language-shared safety neurons (MLS-Neurons), serving as key defenses against compound attacks. Finally, we update only this minimal subset of shared neurons (~0.03% of parameters), transferring English-only safety supervision to multilingual and multimodal scenarios. Extensive experiments show that our method significantly outperforms state-of-the-art approaches across diverse multilingual and multimodal safety benchmarks while preserving general utility.

## Metadata
- **Published**: 2026-07-30T09:30:03Z
- **Authors**: Enyi Shi, Fei Shen, Chuancheng Shi, Linxia Zhu, Shuyi Miao, Jinhui Tang, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27917v1)