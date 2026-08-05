---
title: ToolLIFT: Lifting Tool-Specific Trajectories into Function-Level Graphs for Generalizable Tool Planning
published: 2026-08-04T11:02:45Z
authors: Xiuhui You, Jiayi Luo, Zichao Shen, Qingyun Sun, Ziwei Zhang
url: http://arxiv.org/abs/2608.03468v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolLIFT: Lifting Tool-Specific Trajectories into Function-Level Graphs for Generalizable Tool Planning

## Abstract
Historical tool-use trajectories provide valuable experience for large language model (LLM) agents to plan and coordinate tool usage. Existing approaches directly construct tool-level graphs from these trajectories, but the resulting graphs remain tied to specific tools and are hard to generalize across tool sets. To tackle this challenge, we find that despite differences in the tools involved, analogous tasks often share a common function-level workflow structure, which serves as a potentially more transferable abstraction for tool planning. Based on this insight, we propose ToolLIFT, a framework that lifts tool-specific trajectories into a function-level workflow graph (FWG) for generalizable tool planning. Specifically, we first propose a trajectory-lifting mechanism that encodes workflow structures in the FWG and shares collaboration experience across tools. Then, building on the global structure of the FWG, we introduce decoupled workflow planning and tool selection to align individual tool choices with the overall workflow. Lastly, to ensure reliable tool dataflow, we adopt Reinforcement Learning (RL) and propose source-gated and skill-specific rewards to maintain source-traceable information flow across tool calls. Experiments on two in-distribution (ID) and three out-of-distribution (OOD) benchmarks show that ToolLIFT consistently outperforms state-of-the-art baselines, demonstrating strong generalization to unseen tool sets.

## Metadata
- **Published**: 2026-08-04T11:02:45Z
- **Authors**: Xiuhui You, Jiayi Luo, Zichao Shen, Qingyun Sun, Ziwei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03468v1)