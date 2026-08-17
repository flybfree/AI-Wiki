---
title: Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use
published: 2026-08-14T07:53:18Z
authors: Yi Ding, Yanzhao Yu, Xili Dai, Xianbiao Qi, Peiwen Sun, Xueqian Wang, Xiangyu Yue, Jianan Wang
url: http://arxiv.org/abs/2608.14047v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use

## Abstract
This paper integrates end-to-end Visual-Language-Action (VLA) models with agentic tool-use to propose Agentic Robot with Tool-use (ART). ART is a tool-injection framework that tunes any VLA model to leverage off-the-shelf tool modules for low-level vision, high-level affordance, and embodiment enhancement. Compared to vanilla VLA models with a whole continuous action solution space, ART reduces the complexity of the action solution space through tool-use, which not only improves generalizability across different tasks but also reduces data dependency. To demonstrate the advantages (high generalizability and low data dependency) of this framework, we first built a dataset of 30K tool-use trajectories and action demonstrations, which is much smaller than those used by baseline methods. We then designed a training regimen for long-trajectory tool-use reasoning in challenging environments. Experiments show that ART achieves a 20% higher success rate than mainstream baselines on simulation and real-world tasks, such as pick-and-place in the dark at novel viewpoints. Empirical results highlight the benefits of an agent-based approach: modular tool utilization enables more efficient training, lightweight deployment, and scalable integration of new tools. This design fosters robustness, adaptability, and extensibility, paving the way for the practical deployment of VLA systems in complex real-world scenarios.

## Metadata
- **Published**: 2026-08-14T07:53:18Z
- **Authors**: Yi Ding, Yanzhao Yu, Xili Dai, Xianbiao Qi, Peiwen Sun, Xueqian Wang, Xiangyu Yue, Jianan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14047v1)