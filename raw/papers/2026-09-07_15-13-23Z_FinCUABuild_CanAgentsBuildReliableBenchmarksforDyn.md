---
title: FinCUABuild: Can Agents Build Reliable Benchmarks for Dynamic Financial Computer Use?
published: 2026-09-07T15:13:23Z
authors: Jingpu Yang, Fengxian Ji, Jinri Guo, Tianhao Li, Qian Jiang, Fan Zhang, Min Peng, Qianqian Xie, Preslav Nakov, Zhuohan Xie
url: http://arxiv.org/abs/2609.07603v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinCUABuild: Can Agents Build Reliable Benchmarks for Dynamic Financial Computer Use?

## Abstract
Financial scenarios are diverse and complex, spanning varying data conditions, tool configurations, and workflows. Yet existing CUA, Computer-Using Agent, evaluation tasks remain largely manually constructed, limiting scalable coverage of real-world financial scenarios. Then, can agents autonomously construct diverse CUA evaluation tasks for financial scenarios? Evaluating this capability poses three key challenges: scenario coverage of construction requests, fair comparison across construction methods, and reliable assessment of generated task quality. To solve these, we introduce FinCUABuildBench, a benchmark for evaluating financial CUA task construction, featuring: (i) 576 construction requests covering 24 financial workflows and three types of runtime variation; (ii) standardized input, budget, and output specifications; and (iii) a task qualification mechanism based on execution tests and quality checks. We further introduce FinCUABuildAgent, a multi-agent system for automatically constructing dynamic financial CUA evaluation tasks. It consists of three modules that jointly construct tasks, environments, and validators. On FinCUABuildBench, under the same model backbone, existing agent-based construction methods achieve strict qualification rates of only 1.3-8.3%, while FinCUABuildAgent reaches 31.3%. Downstream evaluations further show that the constructed tasks can effectively differentiate CUA task-execution capabilities. These results demonstrate that agents can autonomously construct financial CUA tasks with meaningful evaluation value, offering a practical path toward broader evaluation coverage in financial scenarios. Code: https://github.com/FengxianJi/FinCUABuild

## Metadata
- **Published**: 2026-09-07T15:13:23Z
- **Authors**: Jingpu Yang, Fengxian Ji, Jinri Guo, Tianhao Li, Qian Jiang, Fan Zhang, Min Peng, Qianqian Xie, Preslav Nakov, Zhuohan Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07603v1)