---
title: Taming the Implicit: Dual-Channel Risk-Aware Reinforcement Fine-Tuning for Continual Multimodal Post-Training
published: 2026-08-04T13:40:03Z
authors: Yibei Liu, Jiajun Chen, Qianle Zhang, Tangyue Jin, Mengying Zhu, Meng Xi, Yangyang Wu
url: http://arxiv.org/abs/2608.03660v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Taming the Implicit: Dual-Channel Risk-Aware Reinforcement Fine-Tuning for Continual Multimodal Post-Training

## Abstract
Reinforcement fine-tuning (RFT) is widely believed to inherently resist catastrophic forgetting in continual post-training of multimodal large language models. Under pronounced task distributional shifts, however, forgetting across representative RFT algorithms escalates sharply. This stems from the implicit reward-variance regularization inherent to RFT, which proves incapable of suppressing uncontrolled optimization risk. We propose Risk-Aware Policy Optimization (RAPO), the first dual-channel framework for explicit risk governance in continual RFT. On the policy channel, Risk-Aware Policy Scaling adaptively calibrates per-sample update magnitude via rollout reliability and Fisher-inspired local predictive sensitivity; on the data channel, Risk-Aware Dynamic Bucket Sampling reorganizes training batches through dynamic risk stratification, steering optimization toward informative yet stable samples. As a plug-and-play strategy requiring no cross-task memory, RAPO generalizes to any RFT algorithm without modification. On the public MLLM-CL benchmark, RAPO reduces final forgetting by 79.8% relative to its RLOO backbone while retaining new-task competitiveness.

## Metadata
- **Published**: 2026-08-04T13:40:03Z
- **Authors**: Yibei Liu, Jiajun Chen, Qianle Zhang, Tangyue Jin, Mengying Zhu, Meng Xi, Yangyang Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03660v1)