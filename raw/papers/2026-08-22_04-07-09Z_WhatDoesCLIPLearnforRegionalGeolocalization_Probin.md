---
title: What Does CLIP Learn for Regional Geolocalization? Probing Visual Cues and Scene Configuration After Adaptation
published: 2026-08-22T04:07:09Z
authors: Changyu Lee, Yeonsoo Park, Abdullah Alfarrarjeh, Seon Ho Kim
url: http://arxiv.org/abs/2608.21761v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Does CLIP Learn for Regional Geolocalization? Probing Visual Cues and Scene Configuration After Adaptation

## Abstract
Large collections of street-view imagery provide rich visual information about urban environments, but extracting fine-grained geographic information from such data remains challenging. In particular, fine-grained regional geolocalization is challenging because nearby areas often share coarse geographic cues. We study regional geolocalization within a metropolitan area and ask whether pretrained CLIP features are sufficient for regional discrimination, and what visual information supports performance after adaptation. Using 9,085 street-view images from eight Greater Los Angeles regions, we compare zero-shot CLIP, frozen-encoder readouts, partial encoder updating, Low-Rank Adaptation (LoRA), and full fine-tuning. Frozen readouts remain near the 39.03% zero-shot accuracy, whereas encoder adaptation achieves 75.94-82.10%. Full fine-tuning also reduces the mean distance to the predicted region center from 12.30 km to 3.86 km. We probe these gains through semantic cue removal, appearance reduction using edge maps and blur, and scene-configuration disruption using patch scrambling. Adapted models achieve higher edge and blur accuracy and switch 42.92-45.56% of predictions after scrambling, compared with 10.79-14.60% for frozen methods. However, adaptation does not improve the fraction of performance retained after appearance reduction, while vegetation and sky remain influential. A Caltech101 control further shows that scrambling sensitivity is not unique to geolocalization. Overall, encoder adaptation substantially improves nearby-region discrimination and is associated with greater sensitivity to intact scene configuration, without evidence that coarse structure alone becomes sufficient for prediction. These conclusions concern viewpoint variation near known locations rather than geographically disjoint generalization.

## Metadata
- **Published**: 2026-08-22T04:07:09Z
- **Authors**: Changyu Lee, Yeonsoo Park, Abdullah Alfarrarjeh, Seon Ho Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21761v1)