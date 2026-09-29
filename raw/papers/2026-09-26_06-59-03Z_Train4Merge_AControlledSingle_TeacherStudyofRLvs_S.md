---
title: Train4Merge: A Controlled Single-Teacher Study of RL vs. SFT Teachers for OPD-Based Model Merging
published: 2026-09-26T06:59:03Z
authors: Jingyuan Huang, Zuming Huang, Yucheng Shi, Zhongzhi Li, Xiaoming Zhai, Wei Chu, Ninghao Liu
url: http://arxiv.org/abs/2609.32303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Train4Merge: A Controlled Single-Teacher Study of RL vs. SFT Teachers for OPD-Based Model Merging

## Abstract
Domain experts trained from a shared checkpoint can be merged into one model through on-policy distillation (OPD), where they act as teachers supervising a student on its own trajectories. One upstream choice is rarely examined: whether to build each expert with supervised fine-tuning (SFT) or reinforcement learning (RL). Yet equally strong teachers need not be equally good teachers. We probe this choice through controlled single-teacher OPD, a building block of multi-teacher OPD: in Agentic, Reasoning, and Perception, comparably performing SFT and RL teachers are trained from Qwen3.5-9B, each guiding a student initialized from it. At their best checkpoints, RL-guided students outperform SFT-guided students by 4.27, 1.50, and 0.86 percentage points in Agentic, Reasoning, and Perception, respectively, and recover more of their teachers' performance gains over the base model. The contrast is clearest in Agentic, where the best SFT-guided student recovers only 44.44% of its teacher's gain, whereas the best RL-guided student recovers 115.00%, surpassing its teacher. Our analysis points to an explanation: RL teachers stay much closer to the shared initialization in parameter space than SFT teachers and are therefore easier for their students to follow.

## Metadata
- **Published**: 2026-09-26T06:59:03Z
- **Authors**: Jingyuan Huang, Zuming Huang, Yucheng Shi, Zhongzhi Li, Xiaoming Zhai, Wei Chu, Ninghao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32303v1)