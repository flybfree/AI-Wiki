---
title: OpenVisTool: An Open Recipe for Synthesizing Instructive Visual Tool-Use Trajectories
published: 2026-08-09T08:01:05Z
authors: Changhao Xiang, Shilin Zhang, Zheng Ma, Kanzhi Cheng, Ruize Ma, Yi Feng, Jianbing Zhang, Zhi Wang, Zhen Wu, Xinyu Dai, Lewei Lu
url: http://arxiv.org/abs/2608.08557v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OpenVisTool: An Open Recipe for Synthesizing Instructive Visual Tool-Use Trajectories

## Abstract
Visual tool use has emerged as a fundamental capability for multimodal agents to actively acquire evidence beyond a fixed image encoding. The prevailing recipe learns this capability from teacher-generated trajectories filtered for answer correctness, implicitly assuming that every successful demonstration provides effective supervision. We argue this assumption is flawed: a strong teacher often reaches the correct answer without needing its tool calls, and imitating such trajectories teaches a student that tool calls accompany correct answers, not that tool observations ground them. We present OpenVisTool, an open framework for constructing instructive visual tool-use trajectories that provide effective supervision for tool learning. The key insight is that a trajectory should be retained only if its answer is correct (outcome validity) and its tool observations causally contribute to that answer (causal utility). The framework operates in three stages: difficulty screening to select queries that are not reliably answerable without tools, domain-specific trajectory synthesis to elicit coherent tool-use trajectories, and supervision verification to jointly test both conditions. Rather than encouraging models to imitate tool calls, the resulting supervision teaches when and how visual evidence should be acquired. Using this framework, we construct OpenVisTool-42K, a dataset spanning five visual reasoning domains, together with OpenVisTool-Bench, a benchmark covering the same domains. Across four backbones (4B-27B), fine-tuning on OpenVisTool-42K consistently improves visual tool-use performance and yields gains on two out-of-distribution benchmarks; the larger models approach leading closed-source systems. The evidence suggests that effective visual tool use is learned from causally grounded supervision rather than tool-calling patterns.

## Metadata
- **Published**: 2026-08-09T08:01:05Z
- **Authors**: Changhao Xiang, Shilin Zhang, Zheng Ma, Kanzhi Cheng, Ruize Ma, Yi Feng, Jianbing Zhang, Zhi Wang, Zhen Wu, Xinyu Dai, Lewei Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08557v1)