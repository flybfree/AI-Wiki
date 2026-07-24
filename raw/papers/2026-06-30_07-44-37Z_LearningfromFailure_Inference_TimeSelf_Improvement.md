---
title: Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents
published: 2026-06-30T07:44:37Z
authors: Xueqiao Sun, Xiaohan Wang, Ludwig Schmidt, Serena Yeung-Levy, Yuhui Zhang
url: http://arxiv.org/abs/2606.31270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents

## Abstract
Computer-use agents, which leverage multimodal large language models (MLLMs) to operate computers and complete tasks, have attracted significant attention for their utility and versatility. A major challenge in developing these agents is collecting large-scale, high-quality trajectories. The standard approach generates synthetic data through a self-improving loop: an agent is placed in a verifiable environment and iteratively fine-tuned on its successful trajectories. Despite its effectiveness, this paradigm exploits only successful trajectories and discards the failed ones, even though failures carry rich information about a model's weaknesses. In this work, we explore a complementary failure-driven self-improvement loop, a data-centric paradigm that turns failed trajectories into agent improvements. Specifically, we employ an LLM to diagnose failure modes, propose inference-time solutions, and generate code patches -- lightly verified by humans -- that upgrade the agent. We validate this approach with the state-of-the-art OpenCUA-72B model on the OSWorld benchmark, improving the success rate from 42.3% to 48.9%, a gain of 6.6 percentage points, without any additional training cost and with only modest inference overhead. Our results demonstrate that failure-driven self-improvement is a viable complement to success-based pipelines, enabling more efficient agent improvement.

## Metadata
- **Published**: 2026-06-30T07:44:37Z
- **Authors**: Xueqiao Sun, Xiaohan Wang, Ludwig Schmidt, Serena Yeung-Levy, Yuhui Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.31270v1)