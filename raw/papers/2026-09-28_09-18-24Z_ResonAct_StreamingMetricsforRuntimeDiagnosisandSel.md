---
title: ResonAct: Streaming Metrics for Runtime Diagnosis and Self-Healing in Multi-Agent Systems
published: 2026-09-28T09:18:24Z
authors: Tarun Chintada, Neelamadhav Gantayat, Ishaan Romil, Renuka Sindhgatta, Soujanya Soni, Sameep Mehta
url: http://arxiv.org/abs/2609.34701v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ResonAct: Streaming Metrics for Runtime Diagnosis and Self-Healing in Multi-Agent Systems

## Abstract
Multi-agent systems (MAS) are increasingly used to automate enterprise workflows involving multiple specialized agents, external tools, and long-running task execution. Failures may arise from tool degradation, context propagation errors, coordination breakdowns, or repeated agent interactions that prevent task completion. While existing observability frameworks provide traces and logs, diagnosis and remediation are largely performed after execution completes, limiting opportunities for recovery during runtime. We present ResonAct, a runtime self-healing framework that enables continuous monitoring, diagnosis, and remediation of multi-agent systems through streaming operational metrics. ResonAct ingests execution traces, agent interactions, and tool invocations into a streaming analytics layer that continuously derives task progress, context health, and tool reliability metrics. These metrics serve as runtime control signals for detecting anomalous execution patterns and localizing root causes using a structured failure model. Based on the diagnosed failure, ResonAct dynamically selects remediation policies and performs actions. The framework operates as an external control plane, enabling intervention without modifying application agents or orchestration logic. We evaluate ResonAct across enterprise workflow scenarios and AppWorld benchmarks. The results show that the streaming metric-based analysis identifies execution degradations and localizes faults. Furthermore, policy-driven remediation improves task completion rates by up to 10.00 percentage points, with detection precision ranging from 70.59% to 82.91%, recall from 63.09% to 100%, recovery rates from 10.48% to 46.67%, and runtime overhead ranging from $-0.25%$ to 14.12% across the evaluated configurations.

## Metadata
- **Published**: 2026-09-28T09:18:24Z
- **Authors**: Tarun Chintada, Neelamadhav Gantayat, Ishaan Romil, Renuka Sindhgatta, Soujanya Soni, Sameep Mehta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34701v1)