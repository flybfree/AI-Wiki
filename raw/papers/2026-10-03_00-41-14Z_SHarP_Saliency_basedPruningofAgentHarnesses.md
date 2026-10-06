---
title: SHarP: Saliency-based Pruning of Agent Harnesses
published: 2026-10-03T00:41:14Z
authors: Xinyi Gao, Qiucheng Wu, Kaizhi Qian, Handong Zhao, Shiyu Chang, Yang Zhang
url: http://arxiv.org/abs/2610.04178v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SHarP: Saliency-based Pruning of Agent Harnesses

## Abstract
Agent harnesses are systems that coordinate model calls, tool use, and task execution to help large language models complete complex tasks. To meet task requirements and address failures, these systems are often iteratively refined by amending and patching their instructions, tools, and workflows, continuously increasing harness complexity. It is therefore unclear whether some resulting harness modules are redundant, introducing substantial token overhead with little, if any, performance gain. Inspired by neural network pruning, in this paper, we study harness pruning as a means of striking a better balance between task performance and token cost. We propose SHarP (Saliency-based Harness Pruning), a simple yet effective pruning strategy based on the saliency of each harness module with respect to performance and efficiency. Specifically, we first identify tools, instructions, and supporting mechanisms as components that can be individually disabled. We then estimate the saliency of each module by ablating it and assessing its task performance and token cost relative to the full set of single-module ablations. Modules with the smallest contribution to performance or largest computational overhead are subsequently pruned. Our evaluation across various harnesses on held-out validation sets reveals a surprising finding: most harnesses that we studied are highly redundant and can maintain comparable performance and efficiency even after a substantial portion of their modules are pruned. Our pruning approach and empirical findings provide new perspectives on agent harness design and optimization.

## Metadata
- **Published**: 2026-10-03T00:41:14Z
- **Authors**: Xinyi Gao, Qiucheng Wu, Kaizhi Qian, Handong Zhao, Shiyu Chang, Yang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04178v1)