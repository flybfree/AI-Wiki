---
title: Relative Time Intervals Representation for Word-level Timestamping with Masked Training
published: 2026-08-25T03:59:42Z
authors: Quanwei Tang, Zhiyu Tang, Xu Li, Dong Zhang,  Shoushan, Guodong Zhou
url: http://arxiv.org/abs/2608.24041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Relative Time Intervals Representation for Word-level Timestamping with Masked Training

## Abstract
Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively transforming them from ``content understanding machines" into ``temporal-aware content understanding machines". Specifically, we replace traditional absolute timestamps with relative timestamps, achieving a more compact vocabulary and stronger generalization capabilities. To efficiently infuse timestamp prediction ability into pre-trained large language models, we introduce a hybrid fine-tuning strategy: full-parameter fine-tuning of the timestamp-augmented embedding layer and language model head, combined with LoRA fine-tuning of the decoder layers. Moreover, we design a masked timestamp training objective, preventing the model from over-relying on ground-truth timestamps, and thereby enhancing robustness against noisy real-world annotations. Extensive experiments demonstrate that our approach achieves significant improvements in timestamp prediction accuracy while maintaining strong speech transcription performance.

## Metadata
- **Published**: 2026-08-25T03:59:42Z
- **Authors**: Quanwei Tang, Zhiyu Tang, Xu Li, Dong Zhang,  Shoushan, Guodong Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24041v1)