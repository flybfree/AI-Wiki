---
title: CoBRA: Learning Tool-Use Boundaries via Counterfactual Margins
published: 2026-09-01T09:24:11Z
authors: Wenhao Zou, Xianglong Liu, Wendong Bi, Hanjie Wang, Simin Zhao, Gong Zhi
url: http://arxiv.org/abs/2609.00967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoBRA: Learning Tool-Use Boundaries via Counterfactual Margins

## Abstract
As large language models increasingly act through external tools, deciding when to call a tool has become a central problem alongside deciding how to use it. Unnecessary tool calls introduce latency, cost, retrieval noise, and error propagation, while missed calls hurt knowledge-intensive queries or questions requiring up-to-date evidence. Existing methods typically trigger tools from absolute query or generation signals, such as difficulty, confidence, or final task reward, and therefore lack an explicit estimate of the instance-level marginal benefit of tool use. We propose CoBRA, a counterfactual boundary-learning framework for tool-augmented language models. CoBRA first constructs internal and external experts from the same base model, collects paired trajectories, and estimates the reward margin between answering with and without tools. This margin partitions data into internal-favored, external-favored, and ambiguous cases. CoBRA then uses clear-margin samples for Boundary-Aware Cold-Start SFT, followed by MARS-RL with reference-split rollouts and counterfactual marginal advantages to optimize boundary decisions. Experiments with retrieval as the main tool on Qwen3-4B show that CoBRA improves tool-use efficiency and boundary-sensitive answer accuracy while maintaining strong performance on tool-dependent out-of-distribution questions.

## Metadata
- **Published**: 2026-09-01T09:24:11Z
- **Authors**: Wenhao Zou, Xianglong Liu, Wendong Bi, Hanjie Wang, Simin Zhao, Gong Zhi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00967v1)