---
title: HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving
published: 2026-08-31T12:13:41Z
authors: Boyang Mu, Zhiwei Wei, Mugen Peng, Wenjia Xu
url: http://arxiv.org/abs/2608.30672v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving

## Abstract
Recent advances in large language models and multimodal models have pushed remote sensing (RS) processing from simple perception models to agentic systems designed to tackle complex, long-horizon RS tasks. However, existing systems often rely on monolithic decision-making frameworks, which fail to accommodate the multi-stage, interdependent nature of RS tasks. This centralized approach leads to challenges such as unstable task execution, incorrect tool usage, and error propagation across stages. To address these issues, we propose HiRS-Agent, a hierarchical multi-agent system for long-horizon RS task solving. HiRS-Agent adopts a two-level collaborative architecture: the Manager Layer handles dynamic routing, step-level verification, replanning, and termination control, while the Specialist Layer organizes domain-specific tools according to the RS workflow and is responsible for subtask reasoning and tool execution. To further enhance the system's capability, we introduce a two-stage supervised tuning strategy and a verification-guided hierarchical reinforcement learning stage to jointly optimize coordination and tool-use policies. Experiments on Earth-Agent Benchmark and ThinkGeo show that HiRS-Agent substantially improves long-horizon tool-use capability and final-task correctness, demonstrating the effectiveness of structured multi-agent collaboration for reliable RS agents. The code is publicly available at https://github.com/IntelliSensing/HiRS-Agent.

## Metadata
- **Published**: 2026-08-31T12:13:41Z
- **Authors**: Boyang Mu, Zhiwei Wei, Mugen Peng, Wenjia Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30672v1)