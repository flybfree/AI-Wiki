---
title: SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval
published: 2026-09-02T09:18:27Z
authors: Zineb Lahrichi, Marc Ferras, Gaël Richard, Geoffroy Peeters
url: http://arxiv.org/abs/2609.02343v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval

## Abstract
Recent advances in audio-language modeling have been driven by large-scale audio captioning datasets. However, existing datasets remain limited by low semantic diversity, generic descriptions lacking acoustic details, and one-to-one audio-caption mappings that poorly reflect the inherent ambiguity of auditory perception. We introduce SonicCaps, a large-scale audio captioning dataset comprising ~15M captions paired with ~700k audio clips, generated using a multi-modal large language model (Qwen3-Omni) conditioned on both audio and text. To explicitly promote diversity, we generate around 24 captions per audio via structured prompt engineering and few- shot generation, spanning main descriptions, rephrased variants (verbosity, style) and semantic tags. Human evaluation shows that SonicCaps is rated significantly higher than existing captioning datasets, with fine-grained analyses indicating that our captions are perceived as more descriptive and precise, which strongly correlates with quality judgments. Finally, training CLAP models on SonicCaps with a multi-caption sampling strategy consistently improves audio retrieval and zero-shot classification, with stronger generalization across public and commercial benchmarks. We release both SonicCaps and two specialized CLAP models on hugging face: https://huggingface.co/datasets/Zineb/SonicCaps.

## Metadata
- **Published**: 2026-09-02T09:18:27Z
- **Authors**: Zineb Lahrichi, Marc Ferras, Gaël Richard, Geoffroy Peeters
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02343v1)