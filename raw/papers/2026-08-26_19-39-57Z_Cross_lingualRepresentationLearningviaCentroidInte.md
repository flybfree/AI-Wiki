---
title: Cross-lingual Representation Learning via Centroid Intervention Fusion
published: 2026-08-26T19:39:57Z
authors: Wei Sun, Marie-Francine Moens
url: http://arxiv.org/abs/2608.26357v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-lingual Representation Learning via Centroid Intervention Fusion

## Abstract
Large language models (LLMs) exhibit uneven multilingual performance, especially when dealing with low-resource languages. Inference-time intervention offers a lightweight way to improve cross-lingual transfer by modifying the hidden states produced by the LLMs during the forward pass, without updating model parameters. However, existing cross-lingual intervention methods typically learn separate projections from source to target languages, which limits scalability and prevents knowledge sharing across languages. We propose Centroid Intervention Fusion (CIF), a projection fusion framework that consolidates multiple multilingual intervention projections into a single language-shared operator. Across multilingual commonsense reasoning, natural language inference, factual editing, and machine translation benchmarks, CIF outperforms the strongest prior pairwise intervention baseline by up to +3.378 pp on average across four model backbones, while supporting performance gains for low resource languages. The code is available at https://github.com/VRCMF/CIF.git.

## Metadata
- **Published**: 2026-08-26T19:39:57Z
- **Authors**: Wei Sun, Marie-Francine Moens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26357v1)