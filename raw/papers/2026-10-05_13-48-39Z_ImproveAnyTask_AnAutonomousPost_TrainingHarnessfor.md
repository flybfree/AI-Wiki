---
title: ImproveAnyTask: An Autonomous Post-Training Harness for Iterative Model Self-Improvement
published: 2026-10-05T13:48:39Z
authors: Xingbo Yao, Xiaoman Wang, Zhengwu Lei, Tinghui Luo, YiLin Zhang, Yuefeng Wu, Yijie Xu, Tianfu Wang, Qingyuan Zhan, Ye Guo, Daoxin Zhang, Zhe Xu, Jian Liu, Hui Xiong
url: http://arxiv.org/abs/2610.06347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ImproveAnyTask: An Autonomous Post-Training Harness for Iterative Model Self-Improvement

## Abstract
Adapting general-purpose large language models to specific tasks requires substantial human effort in designing data and training strategies. Sustaining improvement is especially challenging because model updates change the error distribution, requiring strategies to be continually refined. We introduce ImproveAnyTask, an autonomous post-training harness that improves task performance under a limited compute budget. Drawing inspiration from gradient-based parameter optimization, the harness organizes adaptation into error attribution, update-direction selection, and executable model updates. It combines metric-level and case-level analysis to identify a focal problem, then investigates research-backed strategies and compares their reported gains and reproduction difficulty. The selected strategy is translated into training data and a training configuration, with small-scale execution checks preceding full post-training. Subsequent evaluation guides model selection and further adaptation, while validated strategies and scripts are retained for reuse. Across 11 tasks, ImproveAnyTask achieves mean gains of 18.29 and 11.97 percentage points on the Base and Instruct models, respectively, with a maximum gain of 41.96 points, under a 24-hour budget with resources equivalent to eight H20 GPUs.

## Metadata
- **Published**: 2026-10-05T13:48:39Z
- **Authors**: Xingbo Yao, Xiaoman Wang, Zhengwu Lei, Tinghui Luo, YiLin Zhang, Yuefeng Wu, Yijie Xu, Tianfu Wang, Qingyuan Zhan, Ye Guo, Daoxin Zhang, Zhe Xu, Jian Liu, Hui Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06347v1)