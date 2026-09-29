---
title: Long-Horizon Scaling: How Model Capabilities Shape the Returns to Computation
published: 2026-09-28T14:11:57Z
authors: Haoyu Zheng, Zhengyu Chen, Huaisheng Zhu, Ruishan Fang, Teng Xiao, Yiwei Li, Jingang Wang, Wenqiao Zhang
url: http://arxiv.org/abs/2609.35236v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Long-Horizon Scaling: How Model Capabilities Shape the Returns to Computation

## Abstract
Long-horizon agents improve solutions through sustained interaction, execution, and task feedback. Scaling studies relate performance to resources and capabilities, yet how existing capabilities shape returns to extended interaction remains less understood. To address this gap, we analyze AutoLab and EdgeBench, two long-horizon benchmarks. We find that starting performance and subsequent growth are associated with different capabilities: within a task category, similar early scores can precede different later gains. To formalize this finding, we model capability-time scaling with category-specific logistic power laws shared across models. Fitted to early trajectories, these curves extrapolate the observed models' category-average scores to later computation. However, rising average scores mask narrowing improvement opportunities: later gains concentrate among fewer improving models. High final scores and continued improvement also have distinct capability profiles. Predicted mean gains estimate each model's fraction of improving tasks; averaging these estimates forecasts the average share of improving models. These uneven returns motivate deciding whether a specific run should continue. We therefore derive a continuation policy to save time and compute with limited score loss. The policy conditions growth predictions on the run's observed progress and weighs immediate and delayed gains against computation costs. In replay with training and price calibration based on other models' histories, the policy saves roughly one-third of full-run time, with relative score losses of 2.4% on AutoLab individual runs and 3.3% on EdgeBench published mean curves. Our repository is available at https://github.com/Chihaya-Anon-chan/long-horizon-scaling.

## Metadata
- **Published**: 2026-09-28T14:11:57Z
- **Authors**: Haoyu Zheng, Zhengyu Chen, Huaisheng Zhu, Ruishan Fang, Teng Xiao, Yiwei Li, Jingang Wang, Wenqiao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35236v1)