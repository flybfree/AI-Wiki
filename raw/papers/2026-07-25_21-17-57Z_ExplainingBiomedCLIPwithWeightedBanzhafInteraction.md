---
title: Explaining BiomedCLIP with Weighted Banzhaf Interactions Supported by Tree-Gram Parsing
published: 2026-07-25T21:17:57Z
authors: Jakub Rymarski, Adam Rempała, Bartłomiej Sobieski, Przemysław Biecek
url: http://arxiv.org/abs/2607.23368v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explaining BiomedCLIP with Weighted Banzhaf Interactions Supported by Tree-Gram Parsing

## Abstract
Vision-Language Models (VLMs) are demonstrating significant capabilities in medical tasks like radiology analysis, yet providing faithful and interpretable explanations remains a key consideration for their responsible deployment in clinical settings. However, existing explanation methods, such as the widely used FIxLIP framework, often struggle with the fine-grained nature of modern tokenizers. The tokenization problem fragments clinical concepts---splitting terms like "saddle embolus" into scattered, meaningless subwords---which leads to noisy, semantically incoherent cross-modal attributions. Such fragmentation also results in a combinatorial explosion of interaction possibilities, obscuring the model's true reasoning. To address this, we introduce ParseFIxLIP, an extension that incorporates the Tree-Gram Parsing into the Banzhaf interaction game used by FIxLIP. This semantically informed strategy utilizes dependency parsing trees to define explanation players by grouping related text tokens into semantically coherent units. Our smart_depth grouping strategy, merging tokens according to spaCy token dependency tree, successfully mitigates concept fragmentation, yielding substantially more interpretable cross-modal interactions by unifying complex medical concepts. Quantitatively, while baselines struggled with the high dimensionality of long captions, our parsing approach maintained statistical robustness and semantic parsimony. Qualitative analysis on BiomedCLIP, validated on medical imagery (ROCOv2) and general examples, confirms that the approach accurately captures the synergistic influence of grouped words on model predictions. In conclusion, our work offers intuitive and clinically relevant insights into VLM decision-making, fulfilling the critical need for coherent explanations in the medical domain.

## Metadata
- **Published**: 2026-07-25T21:17:57Z
- **Authors**: Jakub Rymarski, Adam Rempała, Bartłomiej Sobieski, Przemysław Biecek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23368v1)