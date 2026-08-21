---
title: Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation
published: 2026-08-19T23:02:07Z
authors: Prachi Garg, Steve Xing, Prahit Yaugand, Saurabh Gupta, Derek Hoiem
url: http://arxiv.org/abs/2608.19490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation

## Abstract
State-of-the-art vision-language-action (VLA) models such as $π_{0.5}$ exhibit strong semantic understanding, instruction following and task behavior. However, when deployed on new robots, even minor mismatches in hardware configuration relative to pretraining can cause severe performance drops. Finetuning the VLA on in-domain expert data from the new embodiment improves performance on the expert task but leads to a loss in its original instruction following and behavioral priors. In this paper, we propose a self-supervised method that generates online interaction rollouts from the zero-shot VLA as additional training data for finetuning. Our experiments show this finetuning scheme yields strong multi-task policies that, on the target robot, (1) inherit prior tasks distilled from the zero-shot model, (2) enable generalist instruction following, while (3) learning new skills from expert data with improved sample efficiency. We demonstrate the success of our approach across test sets probing generalization on a real ALOHA robot and a new simulation benchmark in RoboTwin. Video results are available at https://self-supervised-control.pages.dev/

## Metadata
- **Published**: 2026-08-19T23:02:07Z
- **Authors**: Prachi Garg, Steve Xing, Prahit Yaugand, Saurabh Gupta, Derek Hoiem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19490v1)