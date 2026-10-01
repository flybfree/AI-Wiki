---
title: Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools
published: 2026-09-30T05:23:25Z
authors: Shijia Ge, Alex Zhou, Jianshu Zeng, Yexing Wan, Di Wu, Zelin Zheng, Yazhe Wang, Zhiqi Jia, Xuan Shangguan, Jay Zhu, Yijun Liu, Lingyu He, Sihang Wu, Xiao He, Hongcheng Gao
url: http://arxiv.org/abs/2609.39018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools

## Abstract
Frontier models can control robots, but reasoning through every reach, grasp, and retreat makes manipulation slow and token-intensive. We revisit code as policy with a different division of labor: models build executable tools, code handles multi-phase motions, and models decide what to do next. We introduce URAI (Universal Robot-Agent Interface), which couples a programming agent that constructs robot tools with an execution agent that uses them in a feedback loop. The programming agent writes reusable and task-specific tools from task intent and refines them through execution feedback and human guidance. The execution agent selects and parameterizes these tools from current observations; each call runs a complete motion locally before returning control to the agent. Unlike delegating subsequent decisions to a generated program, this design retains model-level decision-making between tool executions. Validated tool revisions persist across episodes without updating foundation-model weights, and a shared GUI and API make the same tools available to humans and agents. Across five RoboDojo tasks and four frozen execution agents, URAI raises aggregate success from 18.0% to 53.0% relative to direct fingertip control, with the largest gain on Swap Blocks; with the same tools, a program written in advance reaches only 24% against 56% for two agents deciding after each call. Three of the four agents also finish episodes 1.3-1.5 times faster with 1.5-1.7 times fewer execution-agent output tokens; DeepSeek-V4-Flash's cost barely changes. We further evaluate URAI on seven real-world AgileX dual-arm tasks, spanning object manipulation, cloth folding, and human-interactive tic-tac-toe. URAI connects the coding and decision-making capabilities of frontier agents, organizing robot control around reusable tools that agents can both invoke and revise.

## Metadata
- **Published**: 2026-09-30T05:23:25Z
- **Authors**: Shijia Ge, Alex Zhou, Jianshu Zeng, Yexing Wan, Di Wu, Zelin Zheng, Yazhe Wang, Zhiqi Jia, Xuan Shangguan, Jay Zhu, Yijun Liu, Lingyu He, Sihang Wu, Xiao He, Hongcheng Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39018v1)