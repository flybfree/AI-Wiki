---
title: OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue
published: 2026-09-18T08:15:34Z
authors: Haolin He, Yunfei Chu, Qi Chen, Wen Huang, Yuan Feng, Muzhi Zhu, Zheqi Dai, Haoning Xu, Dongchao Yang, Chunyat Wu, Zining Liang, Zhengxi Liu, Xiquan Li, Xie Chen, Xize Cheng, Qize Yang, Jin Xu, Qiuqiang Kong
url: http://arxiv.org/abs/2609.21465v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue

## Abstract
We define OmniVChat (Omni Video Chat) as the task of native audio-visual dialogue between a user and an omni model. In OmniVChat, omni models directly and simultaneously receive audio and video from a user and return text. The user's query is embedded in the audio and video, without a separate text question, external captioning, or speech recognition. Direct audio-visual input reduces external latency and computation while preserving perceptual cues. However, research on OmniVChat faces two constraints: data availability and evaluation. Recordings of people using their own devices are scarce. Furthermore, a good reply often needs to account for the user's surroundings, facial expressions, and nearby objects, and such responses can be expressed in many different ways, making keyword matching unreliable for evaluating reply quality. Recent progress in agent systems and video generation makes generation for comprehension viable, which means using synthesized dialogues for training and evaluation. Therefore, we present OmniVChat-Studio, a multi-agent data engine for synthesizing single- and multi-turn audio-visual dialogues. We use synthesized dialogues to build OmniVChat-Bench, an evaluation benchmark that evaluates omni models' basic dialogue abilities across five ability categories. We also present OmniVChat-RL, a reinforcement learning reward design that jointly targets reply correctness, efficiency, and style in OmniVChat. Training Qwen3-Omni-Instruct with OmniVChat-RL on synthesized dialogues improves its performance on both OmniVChat-Bench and the human-recorded OmniVChat-Bench-Human. These gains validate the reward design and show transfer to real-world dialogues in training and evaluation.

## Metadata
- **Published**: 2026-09-18T08:15:34Z
- **Authors**: Haolin He, Yunfei Chu, Qi Chen, Wen Huang, Yuan Feng, Muzhi Zhu, Zheqi Dai, Haoning Xu, Dongchao Yang, Chunyat Wu, Zining Liang, Zhengxi Liu, Xiquan Li, Xie Chen, Xize Cheng, Qize Yang, Jin Xu, Qiuqiang Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21465v1)