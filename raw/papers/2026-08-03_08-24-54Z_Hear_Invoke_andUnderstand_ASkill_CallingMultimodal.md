---
title: Hear, Invoke, and Understand: A Skill-Calling Multimodal Agent for Large Audio Language Models
published: 2026-08-03T08:24:54Z
authors: Yuwen Wang, Tian-Hao Zhang, Minghao Cai, Yilin Ren, Ziyang Jiang, Xin Wang, Zhichao Wang, Pan Zhou, Kun Zhan, Xinyuan Qian
url: http://arxiv.org/abs/2608.01881v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hear, Invoke, and Understand: A Skill-Calling Multimodal Agent for Large Audio Language Models

## Abstract
Complex acoustic problems may require models to perform acoustic operations, interact with external tools and reason over the resulting textual or processed-audio observations rather than answer directly from a fixed audio input. We study such problems as tool-interactive audio reasoning and develop SpeechAgent-R, an audio agent that coordinates its intrinsic multimodal understanding with external skills and tools. To support this capability, we construct HIU-Corpus, comprising 65,492 interaction trajectories and 507.6 hours of audio across 24 tasks, 8 skills and 9 tools. SpeechAgent-R first learns structured interaction behaviors through trajectory-based supervised fine-tuning and then improves its decisions through multi-turn reinforcement learning. We further introduce HIU-Bench to jointly evaluate task performance, interaction quality and generalization to diverse task settings. It contains 1,395 samples across 56 tasks, including in-distribution (ID) and out-of-distribution (OOD) splits with substantial shifts in tool usage and workflow composition. SpeechAgent-R achieves 84.17 on ID tasks and 70.94 on OOD tasks, improving over the base model under the same agent harness by 15.40 and 14.23 points. These results demonstrate that learning skill and tool coordination improves audio agents' ability to handle diverse task settings and adaptive tool interactions.

## Metadata
- **Published**: 2026-08-03T08:24:54Z
- **Authors**: Yuwen Wang, Tian-Hao Zhang, Minghao Cai, Yilin Ren, Ziyang Jiang, Xin Wang, Zhichao Wang, Pan Zhou, Kun Zhan, Xinyuan Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01881v1)