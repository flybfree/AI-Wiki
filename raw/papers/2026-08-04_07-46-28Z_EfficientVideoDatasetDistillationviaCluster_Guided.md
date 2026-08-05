---
title: Efficient Video Dataset Distillation via Cluster-Guided Prototype Blending
published: 2026-08-04T07:46:28Z
authors: Chongle Ren, Guang Li, Wenbo Huang, Naoki Saito, Takahiro Ogawa, Miki Haseyama
url: http://arxiv.org/abs/2608.03269v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Video Dataset Distillation via Cluster-Guided Prototype Blending

## Abstract
Video dataset distillation aims to compress a large video dataset into a compact surrogate set that preserves its training utility. Most existing approaches synthesize condensed videos through iterative optimization, whose cost is amplified by the temporal dimension. Rather than further reducing the number of optimized variables, we investigate whether effective distilled videos can be constructed without gradient-based optimization of the stored videos. Such a construction-based approach must address three challenges: selecting informative temporal segments, covering diverse intra-class variations under a limited videos-per-class budget, and increasing the information carried by each stored sample. To this end, we propose ProtoBlend, an efficient select-allocate-blend framework. First, teacher-guided temporal clip selection retains a high-confidence segment from each source video. Second, cluster-guided prototype allocation partitions the selected clips in the teacher feature space and assigns one distilled slot to each intra-class cluster. Third, each prototype is blended with an in-cluster anchor, while their teacher predictions are combined using the same coefficient to provide mixture-source supervision. Experiments on four trimmed action-recognition benchmarks demonstrate that ProtoBlend achieves a competitive accuracy-efficiency trade-off without iterative optimization of the distilled videos.

## Metadata
- **Published**: 2026-08-04T07:46:28Z
- **Authors**: Chongle Ren, Guang Li, Wenbo Huang, Naoki Saito, Takahiro Ogawa, Miki Haseyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03269v1)