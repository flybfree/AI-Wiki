---
title: agent-risk: Risk Assessment for Changes to AI Agents
published: 2026-10-12T07:05:34Z
authors: Yue Zhao, Zixiang Xu, Angela Huyue Zhang, S. Alex Yang, Xiyang Hu
url: http://arxiv.org/abs/2610.16280v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# agent-risk: Risk Assessment for Changes to AI Agents

## Abstract
Before changing a deployed AI agent (a stricter safety gate, a new model), organizations must approve the change, starting from existing logs. Extending classical risk analysis to partial records and partial changes to running systems, agent-risk replays logged episodes, assuming nothing else changes and the agent does not anticipate the change. The log settles episodes acting as before, a declared stop value settles stopped ones, and the rest need logged support, a saved-state rerun, or a bound. We prove what logs must record for exact replay and which saved states serve a gate family. For independent episodes, we bound the reruns a decision needs and tolerable drift from live behavior. In a bash sandbox, a 7,200-episode log alone decided neither of two retry gates, which let the agent act after refusals the log never shows. Rerunning only each gate's blocked episodes from saved states reached both live decisions at half the agent calls of a live test sized post hoc for them, given the log. Without per-step harm, a stopping gate's certified harm ceiling rose up to 2.5-fold, since the log hides whether harm preceded the stop. Approval thus needs evidence designed in advance: log fields, saved states, targeted reruns.

## Metadata
- **Published**: 2026-10-12T07:05:34Z
- **Authors**: Yue Zhao, Zixiang Xu, Angela Huyue Zhang, S. Alex Yang, Xiyang Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16280v1)