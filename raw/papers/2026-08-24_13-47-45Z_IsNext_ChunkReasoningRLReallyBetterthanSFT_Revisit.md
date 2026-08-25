---
title: Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data
published: 2026-08-24T13:47:45Z
authors: Yinhao Tang, Youqing Fang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Weiming Zhang, Bin Liu, Kuikun Liu, Wenwei Zhang, Kai Chen
url: http://arxiv.org/abs/2608.23256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data

## Abstract
Recent work proposes next-chunk reasoning RL for leveraging no-CoT data---corpora such as worked solutions and textbook derivations that contain reasoning-rich content but lack explicit chain-of-thought annotations. The method trains a model to generate implicit reasoning traces and rewards them by their ability to predict the next chunk of text. While promising, existing evaluations primarily compare against conventional SFT baselines, leaving open whether the gains come from the RL formulation itself or from more effectively exposing the model to no-CoT data. We address this question with a controlled study of next-chunk reasoning RL and a simple but previously overlooked alternative: Mixed SFT, a single supervised fine-tuning stage that jointly trains on no-CoT and long-CoT data. Despite its simplicity, Mixed SFT achieves a clearly higher post-RLVR performance ceiling than next-chunk reasoning RL while requiring over 60 times less training compute. The advantage is consistent across in-domain mathematical reasoning and out-of-domain reasoning tasks. Moreover, we show that higher pre-RLVR accuracy does not necessarily translate into higher post-RLVR accuracy, highlighting the need to evaluate no-CoT training strategies in the context of the full post-training pipeline.

## Metadata
- **Published**: 2026-08-24T13:47:45Z
- **Authors**: Yinhao Tang, Youqing Fang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Weiming Zhang, Bin Liu, Kuikun Liu, Wenwei Zhang, Kai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23256v1)