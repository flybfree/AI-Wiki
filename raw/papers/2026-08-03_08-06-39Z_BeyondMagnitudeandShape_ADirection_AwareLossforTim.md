---
title: Beyond Magnitude and Shape: A Direction-Aware Loss for Time Series Forecasting
published: 2026-08-03T08:06:39Z
authors: Seunghan Lee, Jaehoon Lee, Jun Seo, Junhyeok Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
url: http://arxiv.org/abs/2608.01857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Magnitude and Shape: A Direction-Aware Loss for Time Series Forecasting

## Abstract
The direction of change --- whether a series will move up or down --- is often as important as its exact value in decisiondriven applications such as risk management and financial forecasting. However, most forecasting losses optimize either point magnitude or shape and frequency structure, and none explicitly targets the direction of change. In this paper, we find that MSE-trained forecasters fail on the direction of small moves. To address this, we propose CosDir, a simple yet effective direction-aware loss that aligns the difference vectors of the prediction and the target via cosine similarity. Being scale-invariant, CosDir keeps a directional gradient on small moves, re-injecting learning signal exactly where MSE neglects it. CosDir is a lightweight, plug-in term that attaches to any backbone without architectural modification. Since the best ratio for mixing the directional and magnitude terms differs across datasets, we further propose CosDir-UW, an extension that makes this ratio adaptive by learning it during training, matching a per-dataset tuned weight with no hyperparameter. We conduct over 100K experiments, demonstrating that our method consistently and significantly improves directional accuracy while preserving magnitude accuracy, and that it outperforms various loss functions. Code is available at: https://github.com/seunghan96/cosdir.

## Metadata
- **Published**: 2026-08-03T08:06:39Z
- **Authors**: Seunghan Lee, Jaehoon Lee, Jun Seo, Junhyeok Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01857v1)