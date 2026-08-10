---
title: Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection
published: 2026-08-06T06:32:27Z
authors: Yuewei Sun, Lang Qin, Zechuan Tian, Jingwen Li, Guiqin Wang, Shengzeng Huo, Wenxin Ren, Tao Fang, Xiaochen Zhang, Guanqing Deng, Xiang Wang, Xiaowen Dong, Qinghai Guo, Yuxin Ma
url: http://arxiv.org/abs/2608.06434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection

## Abstract
Embodied intelligence demands both long-horizon reasoning and real-time closed-loop responsiveness. Recent dual-system Vision-Language-Action (VLA) architectures combine fast reactive control with slow deliberative reasoning to balance inference speed and task success rate. However, existing dual-process VLAs tightly couple the fast module to intermediate representations of the slow module, necessitating end-to-end joint training and limiting modularity, extensibility and flexible system switching. In this paper, we propose Environment-aware Model Selection (EMS), an adaptive VLA inference framework that switches between two fully decoupled systems of different scales through environment-aware model selection. The large-scale deliberative system provides globally consistent trajectory planning to ensure task success, while a lightweight reactive system enables high-frequency closed-loop control. A reinforcement-learning-based switching policy dynamically selects which system to invoke based on real-time feedback, enabling sparse use of the slow system and thereby balancing pretrained knowledge utilisation with runtime efficiency. Our design offers three key advantages over prior hierarchical VLA frameworks: (1) a fully decoupled and modular dual-system architecture that supports plug-and-play model replacement; (2) an adaptive, environment-aware switching strategy; (3) high-frequency inference for responsive closed-loop control. We extensively evaluate EMS in both simulation and real-world environments. On the LIBERO benchmark, EMS achieves success rates comparable to the large-scale baseline while increasing the effective action frequency to 93.4 Hz. The framework further demonstrates strong extensibility in real-world dual-arm manipulation tasks, where it accelerates task completion while maintaining robust performance.

## Metadata
- **Published**: 2026-08-06T06:32:27Z
- **Authors**: Yuewei Sun, Lang Qin, Zechuan Tian, Jingwen Li, Guiqin Wang, Shengzeng Huo, Wenxin Ren, Tao Fang, Xiaochen Zhang, Guanqing Deng, Xiang Wang, Xiaowen Dong, Qinghai Guo, Yuxin Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06434v1)