---
title: OPD-V: Visual On-Policy Self-Distillation with Modality Balance
published: 2026-08-05T17:53:06Z
authors:  Aniri, Jinhe Bi, Peng Liao, Zengjie Jin, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua
url: http://arxiv.org/abs/2608.05131v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OPD-V: Visual On-Policy Self-Distillation with Modality Balance

## Abstract
On-Policy Self-Distillation (OPSD) has become a standard post-training approach for improving visual reasoning in multimodal large language models (MLLMs). Existing methods draw privileged information from diverse input sources to guide self-distillation. Yet these designs overlook Modality Imbalance, a challenge inherent to MLLM reasoning. When textual information dominates generation, the model cannot fully integrate its multimodal input. Consequently, carefully designed privileged information remains underused, limiting the effectiveness of OPSD. To examine this limitation, we construct a Positive Teacher with the Zoom-In Image and a Negative Teacher with the Mask Image, which exhibit different degrees of Modality Imbalance. Changes in their reasoning correctness and token logits reveal that Modality Balance can itself serve as privileged information. Motivated by this finding, we introduce OPD-V, a visual OPSD paradigm that instantiates such information through the Positive Teacher and Negative Teacher. Positive Modality-Balance Logits Margins define a Modality-Balance Trust Region that selects the on-policy tokens used for self-distillation. Experiments across 6 benchmarks, 4 MLLM backbones, and 5 post-training methods show that OPD-V consistently improves reasoning performance while reducing training cost.

## Metadata
- **Published**: 2026-08-05T17:53:06Z
- **Authors**:  Aniri, Jinhe Bi, Peng Liao, Zengjie Jin, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05131v1)