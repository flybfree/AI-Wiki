---
title: Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents
published: 2026-08-24T14:42:23Z
authors: Wenqi Liu, Shijie Ma, Yunxiao Wang, Meng Liu, Qile Su, Han Liu, Bohan Hou, Xuanyu Zheng, Changyi Liu, Tianke Zhang, Haonan Fan, Kaiyu Jiang, Yingxin Li, Jiankang Chen, Xu Wang, Bin Wen, Tingting Gao, Han Li, Jianhua Yin, Yinwei Wei, Xuemeng Song
url: http://arxiv.org/abs/2608.23329v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents

## Abstract
Open-world video understanding often requires a model to locate sparse visual evidence and acquire external knowledge that is absent from the video and its parametric memory. While Thinking-with-Videos enables active temporal perception and Deep Research supports multi-step information seeking, the two capabilities are typically developed in isolation. We introduce VideoRover, a unified Video Deep Research framework that iteratively coordinates video cropping, multimodal search, and webpage browsing. Given a video-question pair, VideoRover uses each tool result to select the next action, so localized video clips guide external retrieval and retrieved evidence triggers further video inspection and verification. To develop this capability, we construct an automated data curation pipeline, producing 26K verified SFT trajectories and 3K challenging RL instances. We also introduce VideoRover-Bench, a benchmark stratified by video duration and research difficulty. Experiments on VideoDR and VideoRover-Bench show that our VideoRover-8B-RL achieves performance comparable to proprietary models in the direct-answer setting without tool use while outperforming larger open-source models equipped with the same tool suite. Ablation studies and training dynamics further validate the complementary roles of active video grounding, external retrieval, and long-horizon reinforcement learning.

## Metadata
- **Published**: 2026-08-24T14:42:23Z
- **Authors**: Wenqi Liu, Shijie Ma, Yunxiao Wang, Meng Liu, Qile Su, Han Liu, Bohan Hou, Xuanyu Zheng, Changyi Liu, Tianke Zhang, Haonan Fan, Kaiyu Jiang, Yingxin Li, Jiankang Chen, Xu Wang, Bin Wen, Tingting Gao, Han Li, Jianhua Yin, Yinwei Wei, Xuemeng Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23329v1)