---
title: SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale
published: 2026-08-24T02:27:50Z
authors: Jiaqi Liu, Maolin Ran, Xiaoyang Lu, Jian Wang, Weiwen Liu, Jianghao Lin, Yong Yu, Weinan Zhang
url: http://arxiv.org/abs/2608.22725v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale

## Abstract
Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck. Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent. Once assembled, these small discrepancies amplify into severe visual breaks. We present SEAM (Shot Entity-Attribute Memory), a training-free, model-agnostic memory graph that repairs continuity entirely at the prompt-text layer by extracting a multi-dimensional state for every shot, retrieving only causally prior context over the resulting graph, filtering it selectively, and injecting the surviving constraints by natural-language prompt rewriting. We further release SEAM-Bench, a double-blind continuity storyboarding benchmark, on which SEAM raises cross-episode continuity recall from 0.700 to 0.946, generalizes across six mainstream text models, and yields consistent, though not yet significant, gains at the generated-image layer. Deployed as a mandatory stage in CreativeFitting's SEAM-Agent production pipeline over 201 shots, SEAM reaches a 96.5% director-acceptance rate with zero unsafe injections; a conservative counterfactual attributes at least 21.9 percentage points of that rate to its cross-episode memory.

## Metadata
- **Published**: 2026-08-24T02:27:50Z
- **Authors**: Jiaqi Liu, Maolin Ran, Xiaoyang Lu, Jian Wang, Weiwen Liu, Jianghao Lin, Yong Yu, Weinan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22725v1)