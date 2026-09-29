---
title: AsynCodeBench: Benchmarking Collaboration of Asynchronous Multi-Agent Systems in Software Engineering
published: 2026-09-26T14:19:40Z
authors: Kaituo Zhang, Zhen Xiong, Zhimeng Jiang, Mingyu Zhong, Zhouyuan Yuan, Zhecheng Li, Bowen Lin, Chia-Yuan Chang, Mingzhi Hu, Huazheng Wang, Ying Lin
url: http://arxiv.org/abs/2609.32662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AsynCodeBench: Benchmarking Collaboration of Asynchronous Multi-Agent Systems in Software Engineering

## Abstract
Multi-agent coding has emerged as an increasingly active direction in software engineering, where complex development tasks are decomposed across multiple specialized agents working on different parts of the problem. Despite the shift from individual problem solving to distributed collaboration, multi-agent systems still lack a direct measure of collaboration and are largely evaluated through task-level outcomes inherited from single-agent coding, conflating individual coding capability with cross-agent coordination. We introduce AsynCodeBench, a dependency-centric benchmark for asynchronous multi-agent software engineering that represents each task with an explicit dependency graph and executable Dependency Checkers. Through this dependency-tracking process, we propose two complementary measures: Asynchronous Dependency Pass Rate (ADPR), which measures how many cross-agent dependencies are ultimately satisfied, and Dependency Resolution Step (DRS), which measures when each dependency first becomes satisfied during execution. AsynCodeBench comprises 19 tasks from real-world repositories, exposing 52 directed dependencies as explicit units for evaluating cross-agent collaboration. Experiments across model families, scales, and generations reveal a clear gap between coding and collaboration capability: improvements in coding performance do not necessarily translate into stronger collaboration, and task-level metrics can diverge substantially from dependency-level collaboration measures. Dependency-trajectory analysis further reveals that successful coordination often emerges not gradually, but through concentrated bursts in which many dependencies become resolved over a short portion of the execution trajectory, a pattern we term a hopping window.

## Metadata
- **Published**: 2026-09-26T14:19:40Z
- **Authors**: Kaituo Zhang, Zhen Xiong, Zhimeng Jiang, Mingyu Zhong, Zhouyuan Yuan, Zhecheng Li, Bowen Lin, Chia-Yuan Chang, Mingzhi Hu, Huazheng Wang, Ying Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32662v1)