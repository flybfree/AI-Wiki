---
title: Learning from Multimodal Pseudo-Labels for Robust Open-Vocabulary Instance and Panoptic Segmentation
published: 2026-08-12T05:39:57Z
authors: Duy Tran Thanh, Yeejin Lee, Byeongkeun Kang
url: http://arxiv.org/abs/2608.11681v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Multimodal Pseudo-Labels for Robust Open-Vocabulary Instance and Panoptic Segmentation

## Abstract
This work addresses the challenge of open-vocabulary instance segmentation (OVIS) and open-set panoptic segmentation (OSPS), which aim to recognize both predefined and unseen object categories without exhaustive human annotations. Existing methods often suffer from noisy pseudo-masks, limited visual-textual grounding, and difficulty handling synonyms or out-of-vocabulary (OOV) words. To overcome these challenges, we propose a multimodal framework that leverages pre-trained vision-language models for automatic pseudo-label generation, CLIP-guided synonym filtering, and GPT-based caption reconstruction. In our target-vocabulary-assisted pseudo-labeling setting, the framework first constructs pseudo segmentation masks, descriptive captions, and semantically aligned synonym sets using Grounded SAM, LLaVA, and CLIP, providing multimodal supervision without manual annotation. We then enhance visual-textual alignment through three complementary training objectives: an extended grounding loss that incorporates visually grounded synonyms, a semantic consistency loss, and a generative caption reconstruction loss. Extensive experiments on the COCO dataset demonstrate that the proposed method consistently outperforms previous state-of-the-art approaches under this protocol, achieving substantial improvements on both OVIS and OSPS benchmarks.

## Metadata
- **Published**: 2026-08-12T05:39:57Z
- **Authors**: Duy Tran Thanh, Yeejin Lee, Byeongkeun Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11681v1)