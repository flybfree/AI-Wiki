---
title: TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents
published: 2026-10-12T07:51:02Z
authors: Yutong Zhi, Jie Zhang, Xiuqi Lu, Jiayuan Xu, Jing Shao
url: http://arxiv.org/abs/2610.16333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents

## Abstract
As AI agents increasingly act through external tools, tool results are no longer simple outputs but execution artifacts that must remain correctly associated with the context that produced them. Yet as results persist across caches, recovery mechanisms, and shared runtime state, this association can break, causing a real and unmodified result to be consumed in an incompatible execution context and lead the agent to an unsafe action. We characterize this failure as tool-result misbinding. To systematically study this failure, we introduce ReplayBench, a benchmark that uses controlled tool-result replay to evaluate misbinding across 19 representative agent scenarios, 4 failure properties, and 3 replay mechanisms. Across eight LLMs, three agent frameworks, and diverse stateful workflows, we find widespread replay-induced failures, with a mean Final-State Error Rate of 0.649 under cross-task replay. Stage-wise analysis localizes these failures to model-side action generation. Further analyses show that replay susceptibility varies with task similarity, shows little dependence on object similarity, and remains high under result staleness and implicit environment changes. These findings motivate runtime validity mechanisms that eliminate final-state errors in our evaluated settings while preserving legitimate recovery. The results call for explicit contextual binding in tool-using agent runtimes. Our work is public at https://github.com/Phitooo/Replaybench.

## Metadata
- **Published**: 2026-10-12T07:51:02Z
- **Authors**: Yutong Zhi, Jie Zhang, Xiuqi Lu, Jiayuan Xu, Jing Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16333v1)