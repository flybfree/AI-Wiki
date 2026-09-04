---
title: Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents
published: 2026-09-03T06:48:41Z
authors: Zhaoyuan Huang, Tianjie Ju, Pengzhou Cheng, Zheng Wu, Yansi Li, Chuanbiao Song, Jun Lan, Huijia Zhu, Weiqiang Wang, Zhuosheng Zhang
url: http://arxiv.org/abs/2609.03438v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents

## Abstract
Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: agents that perform well on feasible tasks often continue to execute blindly under conflicting instructions. To mitigate this behavior, we propose CONFLICTGUARD, an inference-time framework that aligns an agent's feasibility awareness with its action generation. CONFLICTGUARD contains two coupled components: a feasibility verification protocol that guides the agent to assess instruction logic and GUI-side evidence before acting, and a conditional action modulation mechanism that steers agents from over-compliant execution into termination-oriented behavior. Experiments across five widely-used agents demonstrate that CONFLICTGUARD improves average conflict task success rate significantly, while preserving normal GUI-task performance. These results validate that a lightweight inference-time intervention can substantially boost GUI Agent's competence to identify inappropriate execution scenarios and refrain from unnecessary actions.

## Metadata
- **Published**: 2026-09-03T06:48:41Z
- **Authors**: Zhaoyuan Huang, Tianjie Ju, Pengzhou Cheng, Zheng Wu, Yansi Li, Chuanbiao Song, Jun Lan, Huijia Zhu, Weiqiang Wang, Zhuosheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03438v1)