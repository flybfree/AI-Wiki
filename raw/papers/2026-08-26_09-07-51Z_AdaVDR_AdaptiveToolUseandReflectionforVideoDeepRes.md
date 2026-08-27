---
title: AdaVDR: Adaptive Tool Use and Reflection for Video Deep Research
published: 2026-08-26T09:07:51Z
authors: Xintong Zhang, Xiaomeng Fan, Shilin Yan, Ekko He, Zicheng Liu, Zijian Zou, Guannan Zhang, Yuwei Wu, Zhi Gao, Hongwei Xue
url: http://arxiv.org/abs/2608.25559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AdaVDR: Adaptive Tool Use and Reflection for Video Deep Research

## Abstract
Video deep research answers complex questions by jointly understanding video content and retrieving external knowledge from the open Web. However, diverse questions and videos require different tool-use strategies, and inappropriate tool calls can produce incorrect results. Uncertain grounding and retrieval also make unnecessary interactions costly and error-prone, increasing latency and reasoning errors. To address these challenges, we propose AdaVDR, an adaptive video deep research agent with adaptive tool invocation and reflection. AdaVDR selects tools according to the task and its capabilities, and backtracks only when unreliable intermediate results require correction. To enable these capabilities, we develop a video deep research data construction pipeline. We first discover retrieval-relevant events and entities in diverse videos and acquire detailed information through grounding and external retrieval to construct high-quality QA pairs. For each QA, task-specific prompts organize the information acquisition process into a tool-use trajectory, allowing different question and video types to follow different grounding and retrieval strategies. We further introduce model-conditioned tool necessity filtering, which evaluates tool calls against the target model's video understanding and internal knowledge, removing tools or tool chains the model can bypass. This yields trajectories tailored to the target model's video understanding capability and knowledge. Using this pipeline, we construct training data and VDR-EE, a benchmark covering entity-centric and event-centric questions. We perform supervised fine-tuning followed by reinforcement learning with a redundancy-aware reward to strengthen adaptive tool invocation and reflection. Experiments show that our method performs best among the evaluated open-source models on VDR-EE and substantially improves over its base models on VideoDR.

## Metadata
- **Published**: 2026-08-26T09:07:51Z
- **Authors**: Xintong Zhang, Xiaomeng Fan, Shilin Yan, Ekko He, Zicheng Liu, Zijian Zou, Guannan Zhang, Yuwei Wu, Zhi Gao, Hongwei Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25559v1)