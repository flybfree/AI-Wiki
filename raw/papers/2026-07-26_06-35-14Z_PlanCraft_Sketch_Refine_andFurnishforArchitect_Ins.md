---
title: PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation
published: 2026-07-26T06:35:14Z
authors: Pengyu Zeng, Yuqin Dai, Jun Yin, Ziyang Han, Ng Cheuk Hei, Jing Zhong, Chaoyang Shi, ZhanXiang Jin, Maowei Jiang, Yuxing Han, Shuai Lu
url: http://arxiv.org/abs/2607.23491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation

## Abstract
Two structural insights have been overlooked in automated residential floor plan generation. First, design is inherently progressive. Architects begin with rough strokes and refine them over time, whereas existing methods typically require their conditioning representation to be fully specified before generation, a fundamental mismatch with how design actually works. Second, the 2D floor plan is not an optional intermediate but an irreplaceable spatial contract. Once room boundaries, doors, and windows are fixed, furnishing reduces from open-ended spatial reasoning to bounded constraint satisfaction. Bypassing this contract, as existing 3D systems do by delegating layout to language models, yields overlapping rooms and implausible proportions; directly calling general-purpose language models likewise produces geometrically invalid layouts. Guided by these insights, we present PlanCraft. SketchPlan supplies the missing training signal by replaying the architect's drawing process on 80K real floor plans, producing partial sketches at every completeness level. PlanCraft-Diff progressively sharpens an incomplete sketch into a geometrically precise, vectorizable floor plan through a coarse-to-fine strategy. With the spatial contract established, PlanCraft-Agent then furnishes the scene within well-defined room boundaries. Experiments show that PlanCraft achieves a 61.1\% lower FID than the best existing 2D method and surpasses existing 3D systems by 15 points in expert-rated spatial rationality, with a sketch at only 25\% completion already outperforming all fully specified baselines.

## Metadata
- **Published**: 2026-07-26T06:35:14Z
- **Authors**: Pengyu Zeng, Yuqin Dai, Jun Yin, Ziyang Han, Ng Cheuk Hei, Jing Zhong, Chaoyang Shi, ZhanXiang Jin, Maowei Jiang, Yuxing Han, Shuai Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23491v1)