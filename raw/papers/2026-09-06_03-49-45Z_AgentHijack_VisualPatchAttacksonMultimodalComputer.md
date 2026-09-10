---
title: AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents
published: 2026-09-06T03:49:45Z
authors: Zhihao Liu, Hongyu Sun, Zhiyuan Fu, Xiaonan Duan, Jice Wang, Shangru Zhao, Weizhi Meng, Wuxin Yang, Yangfan Zhou, Yuqing Zhang
url: http://arxiv.org/abs/2609.09212v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents

## Abstract
This paper presents an end-to-end evaluation framework for image-triggered command injection against computer-use agents (CUAs). The goal is to test whether a local visual patch can induce verifiable environmental consequences along the full chain of screenshot input, VLM generation, action parsing, and environment execution. We train and deploy patches on author-controlled GitHub Pages pages and a locally deployed CSDN clone, and evaluate them in real environments across five open-source or publicly available GUI-agent or vision-language-model (VLM) backends. Our experiment aggregates 600 instance-level online cases, with T-ASR, TAPR, and E2E-ASR reaching 84.5%, 47.0%, and 20.3%, respectively. Trajectory analysis further shows that in some successful cases the agent first executes a malicious terminal command and then continues the original benign task. These results indicate that optimized local visual signals can affect not only VLM outputs but also propagate through the execution pipeline of open CUAs and create real environmental risk.

## Metadata
- **Published**: 2026-09-06T03:49:45Z
- **Authors**: Zhihao Liu, Hongyu Sun, Zhiyuan Fu, Xiaonan Duan, Jice Wang, Shangru Zhao, Weizhi Meng, Wuxin Yang, Yangfan Zhou, Yuqing Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09212v1)