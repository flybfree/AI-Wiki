---
title: AIR: Adaptive Interleaved Reasoning with Code in MLLMs
published: 2026-06-22T17:58:54Z
authors: Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
url: http://arxiv.org/abs/2606.23678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AIR: Adaptive Interleaved Reasoning with Code in MLLMs

## Abstract
Following the paradigm shift initiated by OpenAI o3, interleaved reasoning with code to enhance multimodal large language models (MLLMs) has become a pivotal research frontier. The existing literature focuses primarily on tool-use within vision-perception tasks. However, such approaches typically rely on predefined heuristics for visual manipulation and are inherently incapable of addressing numerical computation problems due to their exclusive focus on visual operations. This paper empowers MLLMs with adaptive interleaved reasoning capabilities through extended reinforcement learning training on code-augmented complex numerical computation tasks. To this end, we propose a comprehensive three-component solution consisting of: a two-stage cold-start data construction pipeline, data filtering strategies for RL dataset curation, and an adaptive tool-invocation strategy leveraging a group-constrained reward function for interleaved reasoning trajectories. Extensive experiments demonstrate that after Reinforcement Learning training with the group-constrained reward function, performance improves by an average of 6.1 percentage points (pp) on evaluation benchmarks. Specifically, the accuracy for interleaved reasoning samples increases by 9.9 pp, and the overall success rate of tool-use exceeds 95%. Our data and code are available at: https://github.com/CongHan0808/AIR.git.

## Metadata
- **Published**: 2026-06-22T17:58:54Z
- **Authors**: Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.23678v1)