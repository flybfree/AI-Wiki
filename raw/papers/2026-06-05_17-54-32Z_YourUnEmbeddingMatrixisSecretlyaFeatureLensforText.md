---
title: Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings
published: 2026-06-05T17:54:32Z
authors: Songhao Wu, Zhongxin Chen, Yuxuan Liu, Heng Cui, Cong Li, Rui Yan
url: http://arxiv.org/abs/2606.07502v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings

## Abstract
Large language models exhibit impressive zero-shot capabilities across a wide range of downstream tasks. However, they struggle to function as off-the-shelf embedding models, leading to suboptimal performance on massive text embedding benchmarks. In this paper, we identify a potential cause underlying this deficiency. Our motivation stems from an unexpected observation: text embeddings tend to align with frequent but uninformative tokens when projected onto the vocabulary space. We argue that this excessive expression of high-frequency tokens suppresses the model's ability to capture nuanced semantics. To address this, we introduce EmbedFilter, a simple linear transformation designed to refine text embeddings derived from LLMs directly. Specifically, we uncover that the unembedding matrix within LLMs encodes a latent space that is actively writing these frequent tokens into embedding space. By filtering out this subspace, EmbedFilter suppress the influence of high-frequency tokens, thereby enhancing semantic representations. As a compelling byproduct, this enables an inherent dimensionality reduction, lowering index storage and speedup retrieval while fully preserving the refined embedding quality. Our experiments across multiple LLM backbones demonstrate that LLMs equipped with EmbedFilter achieve superior zero-shot downstream performance even with significantly reduced embedding dimensions. We hope our findings provide deeper insights into the mechanisms of LLM-based representations and inspire more principled designs to improve text embeddings training. Our code is available at https://github.com/CentreChen/EmbFilter.

## Metadata
- **Published**: 2026-06-05T17:54:32Z
- **Authors**: Songhao Wu, Zhongxin Chen, Yuxuan Liu, Heng Cui, Cong Li, Rui Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.07502v1)