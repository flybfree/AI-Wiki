---
title: TraceCLIP: Recovering Local Semantics from Patch-to-CLS Contributions
published: 2026-07-28T11:25:27Z
authors: Xinran Liu, Shouqian Shi, Yutong Chen, Ge Wang, Xin-Wei Yao, Sheng Zhong
url: http://arxiv.org/abs/2607.26107v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TraceCLIP: Recovering Local Semantics from Patch-to-CLS Contributions

## Abstract
Dense vision-language understanding, including object localization, region recognition, and open-vocabulary semantic segmentation, requires associating language concepts with spatially grounded visual regions. CLIP provides a strong foundation for these tasks by learning a shared image-text embedding space from large-scale contrastive pre-training. However, its image-level objective aligns text with a CLS-derived global representation, leaving local vision-language correspondence only indirectly constrained. Existing methods either introduce additional supervision, external models, or task-specific adaptation, while training-free approaches mainly recover dense responses from existing patch features without examining where local semantics become most accessible within CLIP. We introduce TraceCLIP, a training-free framework that recovers latent patch-level semantic evidence by isolating the patch-specific terms written into the CLS attention output. TraceCLIP further converts contribution-derived semantic responses into a semantic-geodesic topology gate that calibrates final-layer patch affinity for dense feature reconstruction. Diagnostic experiments show that these contribution features exhibit strong local semantic discrimination and text-conditioned spatial alignment. On eight zero-shot semantic segmentation benchmarks, TraceCLIP achieves gains of 1.3 to 4.5 points in average mIoU over the strongest prior training-free methods across both backbones and background settings, without additional training, external vision foundation models, or region-level supervision. More broadly, these findings suggest that spatially localized semantics may remain accessible within the internal construction of globally aligned representations.

## Metadata
- **Published**: 2026-07-28T11:25:27Z
- **Authors**: Xinran Liu, Shouqian Shi, Yutong Chen, Ge Wang, Xin-Wei Yao, Sheng Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26107v1)