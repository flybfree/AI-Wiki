---
title: SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task
published: 2026-07-25T06:47:46Z
authors: Lang Mei, Xiaohan Yu, Chong Chen, Liyan Liu, Xiangnan Chen, Jinchao Ma, Chao Feng, Li Huang, Siyu Mo, Sichen Kang, Yunkun Xu, Zhihan Yang, Zhujun Xue, Jingren Zhang, Qing He, Yingdi Huang, Hao Jiang, Ziao Ma, Zewei Pan, Minhao Sun, Zhuo Tao, Jinzhao Xiao, Gangtao Xin, Huanyao Zhang, Wenjian Zhang, Jiangshan Zhang, Guojie Zhu, Jiaxin Mao, Wentao Zhang
url: http://arxiv.org/abs/2607.24850v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task

## Abstract
Recent advances in large language models (LLMs) have enabled search agents to autonomously tackle complex tasks across extended search and reasoning horizons. However, training effective search agents remains challenging due to the lack of scalable and long-horizon tasks, and the difficulty of evaluating and correcting intermediate reasoning and tool-use behaviors. We introduce SearchArt, a scalable framework for training long-horizon search agents through verification-driven task synthesis and a multi-stage post-training pipeline. SearchArt constructs large-scale datasets for complex search-, research- and user-oriented tasks by synthesizing diverse information-seeking QA pairs and corresponding search trajectories from web documents and automatically generated evidence graphs. To ensure the reliability of the synthesized data, we design a verification pipeline that jointly evaluates QA consistency, trajectory quality, and the relevance of retrieved evidence. The verified trajectories are subsequently used in a multi-stage training process comprising supervised fine-tuning and reinforcement learning-based policy optimization. Search agents trained with SearchArt exhibit adaptive search planning, iterative evidence aggregation, and complex reasoning over extended interaction horizons. Experimental results demonstrate that, with only (Qwen3.5-) 27B parameters, SearchArt scores 74.39 on BrowseComp-ZH, 70.06 on BrowseComp, and 52.55 on Deepresearch-bench, matching or surpassing frontier closed-source agents on both deepsearch and deepresearch benchmarks.

## Metadata
- **Published**: 2026-07-25T06:47:46Z
- **Authors**: Lang Mei, Xiaohan Yu, Chong Chen, Liyan Liu, Xiangnan Chen, Jinchao Ma, Chao Feng, Li Huang, Siyu Mo, Sichen Kang, Yunkun Xu, Zhihan Yang, Zhujun Xue, Jingren Zhang, Qing He, Yingdi Huang, Hao Jiang, Ziao Ma, Zewei Pan, Minhao Sun, Zhuo Tao, Jinzhao Xiao, Gangtao Xin, Huanyao Zhang, Wenjian Zhang, Jiangshan Zhang, Guojie Zhu, Jiaxin Mao, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24850v1)