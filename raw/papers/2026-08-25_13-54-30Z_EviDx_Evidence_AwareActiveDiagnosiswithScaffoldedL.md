---
title: EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents
published: 2026-08-25T13:54:30Z
authors: Lihang Zeng, Shaoting Zhang, Xiaofan Zhang
url: http://arxiv.org/abs/2608.24570v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents

## Abstract
Clinical diagnosis is an active evidence-seeking process in which clinicians acquire evidence, update competing hypotheses, and decide when the available evidence is sufficient for diagnosis. Yet many medical diagnosis systems built around large language models (LLMs) still formulate diagnosis as static case-to-answer prediction, with limited support for evidence acquisition. Agentic LLMs offer a dynamic alternative through tool use and intermediate diagnostic trajectories, but existing systems often under-specify how patient evidence should be exposed, scaffolded, and controlled at runtime. We introduce EviDx, an evidence-aware active diagnosis framework that pairs patient-specific diagnostic environments with a clinical diagnostic scaffold and an observer-guided runtime harness. In EviDx, $\mathcal{E}$-Synthesis constructs interactive environments from raw clinical cases; the scaffold organizes role-specialized agents, evidence tools, and evolving evidence states; and the harness regulates diagnostic termination by tracking uncertainty and evidence coverage. A 3-level evaluation pyramid assesses execution robustness, reasoning dynamics, and diagnostic outcomes. Experiments show that EviDx improves diagnostic performance and process stability while revealing model-dependent capability boundaries.

## Metadata
- **Published**: 2026-08-25T13:54:30Z
- **Authors**: Lihang Zeng, Shaoting Zhang, Xiaofan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24570v1)