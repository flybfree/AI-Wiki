---
title: Kalman Meets Curriculum: Efficient Dynamic Prompt Selection for Adaptive RL Finetuning
published: 2026-07-30T02:55:02Z
authors: Haodong Zhu, Yangyang Ren, Yanjing Li, Sheng Xu, Haiguang Liu, Linlin Yang, Baochang Zhang
url: http://arxiv.org/abs/2607.27610v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Kalman Meets Curriculum: Efficient Dynamic Prompt Selection for Adaptive RL Finetuning

## Abstract
Reinforcement learning (RL) finetuning significantly enhances the reasoning capabilities of large language models (LLMs), yet its effectiveness critically depends on selecting prompts of appropriate difficulty for the current policy. This is challenging because prompt difficulty evolves throughout training. Existing online methods therefore face a trade-off: evaluation-based approaches are accurate but expensive, while prediction-based approaches are efficient but typically assume stationary difficulty, making them ill-suited to RL's non-stationary training dynamics. To address these issues, we propose a Kalman-Guided Prompt Selection method (KGPS), which reformulates prompt selection as a dynamic state estimation problem rather than static difficulty prediction. KGPS models each prompt's latent success rate in logit space using a linear-Gaussian state-space model, with process noise coupled to the magnitude of policy updates so that uncertainty increases when the policy changes more substantially. A Kalman filter then maintains a calibrated Gaussian posterior over prompt difficulty, and prompts are selected by maximizing a posterior-expected training utility that favors intermediate-difficulty prompts while naturally revisiting uncertain ones. The resulting procedure is adaptive to policy drift and requires no additional rollouts beyond standard policy training. Extensive experiments across mathematics, planning, and geometry reasoning benchmarks, as well as multiple RL algorithms, show that KGPS consistently improves both final accuracy and rollout efficiency over strong baselines, establishing state-of-the-art performance among online prompt selection methods. For example, on DeepSeek-R1-Distill-7B, KGPS uses 83% fewer rollouts than DS while even improving the average performance by 0.12 point across six math reasoning benchmarks.

## Metadata
- **Published**: 2026-07-30T02:55:02Z
- **Authors**: Haodong Zhu, Yangyang Ren, Yanjing Li, Sheng Xu, Haiguang Liu, Linlin Yang, Baochang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27610v1)