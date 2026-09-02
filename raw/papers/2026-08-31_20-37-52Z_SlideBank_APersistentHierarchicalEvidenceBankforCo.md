---
title: SlideBank: A Persistent Hierarchical Evidence Bank for Consistent Whole-Slide Reasoning
published: 2026-08-31T20:37:52Z
authors: Beidi Zhao, Gexin Huang, Ciro Zhang, Anqi Li, Yusheng Tan, Chen Zhou, Gang Wang, Zu-hua Gao, Xiaoxiao Li
url: http://arxiv.org/abs/2609.00342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SlideBank: A Persistent Hierarchical Evidence Bank for Consistent Whole-Slide Reasoning

## Abstract
Whole-slide images (WSIs) are challenging for vision-language reasoning because diagnostically relevant morphology is sparse, heterogeneous, and distributed across gigapixel-scale images and multiple spatial resolutions. Existing WSI models and pathology agents can aggregate slide features or actively acquire evidence, but the information retained after exploration is often difficult to access semantically while preserving its connection to the original visual evidence. We introduce SlideBank, a training-free framework that represents each WSI as a persistent, concept-indexed, and spatially grounded evidence bank. SlideBank performs question-independent coarse-to-fine exploration to identify informative regions and multi-scale views, converts them into explicit morphological observations, and grounds pathology signals to their supporting patches and WSI coordinates. At inference time, questions are routed to relevant signals and evidence scales, and the linked global, regional, and patch evidence is integrated through confidence-based cross-level consensus. Experiments on WSI-VQA and SlideBench-BCNB show that with Patho-R1, SlideBank reaches 52.77% on WSI-VQA and with Quilt-LLaVA, it reaches 50.92% average accuracy on SlideBench-BCNB, while structured signal-guided retrieval consistently outperforms random evidence sampling. Reusing the same bank across repeated queries further achieves over 99% rephrasing consistency and substantially reduces amortized inference cost through persistent evidence reuse.

## Metadata
- **Published**: 2026-08-31T20:37:52Z
- **Authors**: Beidi Zhao, Gexin Huang, Ciro Zhang, Anqi Li, Yusheng Tan, Chen Zhou, Gang Wang, Zu-hua Gao, Xiaoxiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00342v1)