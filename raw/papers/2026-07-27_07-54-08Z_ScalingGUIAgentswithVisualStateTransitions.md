---
title: Scaling GUI Agents with Visual State Transitions
published: 2026-07-27T07:54:08Z
authors: Xiangyan Liu, Kaixin Li, Haonan Wang, Biao Wu, Meng Fang, Longxu Dou, Chao Du, Michael Qizhe Shieh, Tianyu Pang
url: http://arxiv.org/abs/2607.24112v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling GUI Agents with Visual State Transitions

## Abstract
We introduce State Transition Pretraining (STP) as a new scaling axis for GUI agents. During the STP stage, we continually pretrain a unified multimodal model on visual state transitions by jointly optimizing inverse dynamics (predicting actions from state changes) and forward dynamics (predicting next states from current states and actions). This optimization equips the model with better action-grounded visual representations and an internal world model of GUI dynamics. When subsequently fine-tuned on trajectories with task instructions, our STP-trained models consistently outperform baselines trained solely via direct trajectory fine-tuning across agent benchmarks in both desktop and mobile GUI scenarios (AgentNetBench, AndroidControl, and GUIOdyssey). Further empirical studies show that joint dynamics optimization yields stable improvements over single-objective training, and downstream performance scales steadily with the volume of transition data.

## Metadata
- **Published**: 2026-07-27T07:54:08Z
- **Authors**: Xiangyan Liu, Kaixin Li, Haonan Wang, Biao Wu, Meng Fang, Longxu Dou, Chao Du, Michael Qizhe Shieh, Tianyu Pang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24112v1)