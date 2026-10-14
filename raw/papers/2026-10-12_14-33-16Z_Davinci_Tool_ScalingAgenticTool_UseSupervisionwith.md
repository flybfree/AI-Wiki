---
title: Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments
published: 2026-10-12T14:33:16Z
authors: Xiaoyang Yuan, Ji Zhao, Xingyu Hu, Wenhan Wang, Yutao Hu, Qiaosheng Zhang, Pengfei Liu, Yu Qiao, Yi Bin, Wenqi Shao
url: http://arxiv.org/abs/2610.16867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments

## Abstract
Reliable agentic tool use requires training data that pair diverse multi-step workflows with executable evidence that the requested outcomes were achieved. Scaling either trajectory coverage or verification alone is insufficient as new environments introduce distinct states, rules, and dependencies that must also be reflected in the success criteria. To address this challenge, we introduce Davinci-Tool, a 30B tool-use model, and Davinci-ToolData, an execution-grounded dataset designed to scale environment coverage and outcome verification together. Davinci-ToolData preserves restorable states, execution traces, outcomes, and verifiers as a unified substrate for supervision. Two complementary pipelines populate this substrate: Execution-Grounded Task Synthesis (EGTS) derives verified demonstrations from independently authored systems, and Executable Environment Synthesis (EES) synthesizes auditable environments, state-grounded tasks, and executable verifiers across single and coordinated domains. These pipelines yield 30,395 verified trajectories spanning 2,260 invoked tool names. We first train on these demonstrations with supervised fine-tuning, then reuse EES states and verifiers to compare alternative actions and construct outcome-grounded preferences for Direct Preference Optimization. Davinci-Tool improves Qwen3-Coder-30B-A3B-Instruct from 52.4 to 88.2 on $τ^2$-bench, from 30.4 to 62.8 on BFCL v4 multi-turn, and from 16.9 to 56.2 on MCP-Atlas, outperforming Qwen3-Coder-480B-A35B-Instruct on all three benchmarks with only 1/16 of its total parameters. Code is available at https://github.com/MassLab-SII/Davinci-Tool.

## Metadata
- **Published**: 2026-10-12T14:33:16Z
- **Authors**: Xiaoyang Yuan, Ji Zhao, Xingyu Hu, Wenhan Wang, Yutao Hu, Qiaosheng Zhang, Pengfei Liu, Yu Qiao, Yi Bin, Wenqi Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16867v1)