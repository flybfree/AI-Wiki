---
title: DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology
published: 2026-08-08T14:15:43Z
authors: Junfei Ling, Bangzheng Pu, Bingsen Xue, Tianle Li, Ruying Hu, Cheng Jin
url: http://arxiv.org/abs/2608.08148v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DoGMA: A Central-Dogma-Guided Foundation Model for Multi-Omics Alignment and Multi-Task Learning in Oncology

## Abstract
Attention mechanisms have been widely utilized in modern deep learning, and many existing multi-omics models inherit their conventional use to allow unrestricted bidirectional interactions. However, the fundamental logic of life is directional. Existing designs often overlook the directionality suggested by the central dogma, potentially limiting transfer across heterogeneous cancers, downstream tasks, and incomplete modality settings.In this work, we present DoGMA, a central-dogma-guided foundation model for pan-cancer multi-omics analysis, arguing that robust transfer requires representations with domain-specific inductive bias. Concretely, we build it on a Transformer-MoE architecture where directed attention biases inter-omics communication toward central-dogma information flow. We further pretrain our model with masked hierarchical omics reconstruction to guide it toward learning central-dogma-consistent interactions. Across diverse downstream tasks, including cancer representation learning, survival prediction, and metastasis prediction, DoGMA consistently demonstrates strong predictive performance. Ablations and analyses further suggest that the performance gains arise from the synergy between central-dogma-guided directed attention and reconstruction-based pretraining, which together promote more biologically consistent cross-omics information exchange. Overall, DoGMA demonstrates that domain-specific inductive biases can improve the robustness and transferability of multi-omics foundation models, offering new insights into the design of attention mechanisms for multi-omics representation learning.

## Metadata
- **Published**: 2026-08-08T14:15:43Z
- **Authors**: Junfei Ling, Bangzheng Pu, Bingsen Xue, Tianle Li, Ruying Hu, Cheng Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08148v1)