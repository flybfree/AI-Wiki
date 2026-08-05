---
title: CUADebug: Diagnosing and Repairing Computer-Use Agent Failures
published: 2026-07-31T13:59:45Z
authors: Weijia Zhang, Kunlun Zhu, Zeyi Liu, Yinting Chen, Tianyi Ma, Jiateng Liu, Jiaxun Zhang, Bingxuan Li, Xiangru Tang, Heng Ji, Jiaxuan You
url: http://arxiv.org/abs/2608.02643v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CUADebug: Diagnosing and Repairing Computer-Use Agent Failures

## Abstract
Computer-use agents (CUAs) operate real desktop and web interfaces through screenshots, mouse and keyboard actions, and stateful UI feedback, yet their failures remain difficult to diagnose and repair. Unlike text-only agents, CUA failures arise from coupled visual perception, spatial grounding, low-level interaction, task reasoning, and environment dynamics, making debugging a distinctive multimodal causal localization problem. We introduce CUADebug, a framework for diagnosing and repairing CUA failures. CUADebug includes a CUA-specific error taxonomy, CUAErrorBench, a human-annotated OSWorld failure benchmark, and CUADebugger, a tool-augmented debugger. Instead of prompting over the full trajectory once, CUADebugger actively inspects suspicious steps with paired before/after screenshots and action traces, then submits a structured diagnosis containing the root-cause step, error type, grounded evidence, and corrective strategy for re-execution. Human annotations over 204 failed trajectories show that task reasoning and control is the largest failure family (110/204), followed by perception (36), grounding/interaction (25), external/system (13), and an others category of 20 OSWorld infeasible-task cases. On the main Claude-agent split, CUADebugger improves joint subtype-and-step diagnosis from 11.2% to 19.6% with Gemini 2.5 Pro and improves consistently across debugger backbones. In single re-execution package evaluation, RCA-based conditions achieve higher task completion than history-only continuation (28.47% with machine RCA and 29.90% with our method, versus 13.89%); in continual re-execution, our method improves success from 12.2% to 25.86%, while human-oracle guidance reaches 29.21%. These results show that CUA root-cause diagnosis can provide actionable repair signals rather than merely post-hoc explanations.

## Metadata
- **Published**: 2026-07-31T13:59:45Z
- **Authors**: Weijia Zhang, Kunlun Zhu, Zeyi Liu, Yinting Chen, Tianyi Ma, Jiateng Liu, Jiaxun Zhang, Bingxuan Li, Xiangru Tang, Heng Ji, Jiaxuan You
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02643v1)