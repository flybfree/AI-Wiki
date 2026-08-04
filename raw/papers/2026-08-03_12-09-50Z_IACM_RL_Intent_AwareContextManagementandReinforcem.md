---
title: IACM-RL: Intent-Aware Context Management and Reinforcement Learning for Complex Tool Invocation under Dynamic Intent Fluctuations
published: 2026-08-03T12:09:50Z
authors: Dingwei Zhu, Jiahan Li, Chengjun Pan, Yunxian Yang, Yunbin Zhao, Yunke Zhang, Zhonghang Lu, Zhuohui Sheng, Chenhao Huang, Jiahang Lin, Yajie Yang, Junlin Shang, Shichun Liu, Yuhui Wang, Honglin Guo, Junjie Ye, Xin Guo, Jiazheng Zhang, Ming Zhang, Shihan Dou, Zhiheng Xi, Tao Gui, Qi Zhang, Xipeng Qiu, Xuanjing Huang
url: http://arxiv.org/abs/2608.02110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IACM-RL: Intent-Aware Context Management and Reinforcement Learning for Complex Tool Invocation under Dynamic Intent Fluctuations

## Abstract
Executing long-horizon tool invocations in real-world environments is severely challenged by dynamic user intent noise. Existing methods attempt robustness via implicit history scanning or text compression, yet predominantly assume perfect instructions in simplistic scenarios. Inevitably, under fluctuating contexts, obsolete constraints dilute model attention, triggering catastrophic intent deviation and infinite API loops. To resolve this, we propose IACM-RL, a comprehensive framework for robust tool invocation. First, we introduce the DynamicIntent pipeline, synthesizing trajectories across 13 fine-grained fluctuation scenarios, paired with a five-dimensional diagnostic metric suite. Second, IACM-RL deploys a BeliefState-based Self-Generated Context Manager that proactively tracks shifting goals and isolates overwritten parameters using structural stale flags. To autonomously internalize this state-tracking capability, we optimize the policy using a hierarchical intent-driven reward alongside three auxiliary losses (action calibration, CM extraction, and state distillation). Experiments on DynamicIntent, BFCL-V3, and $\mathrmτ^2$-Bench demonstrate that IACM-RL significantly outperforms baselines, reducing infinite loops and stale context errors while enhancing out-of-domain generalization.

## Metadata
- **Published**: 2026-08-03T12:09:50Z
- **Authors**: Dingwei Zhu, Jiahan Li, Chengjun Pan, Yunxian Yang, Yunbin Zhao, Yunke Zhang, Zhonghang Lu, Zhuohui Sheng, Chenhao Huang, Jiahang Lin, Yajie Yang, Junlin Shang, Shichun Liu, Yuhui Wang, Honglin Guo, Junjie Ye, Xin Guo, Jiazheng Zhang, Ming Zhang, Shihan Dou, Zhiheng Xi, Tao Gui, Qi Zhang, Xipeng Qiu, Xuanjing Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02110v1)