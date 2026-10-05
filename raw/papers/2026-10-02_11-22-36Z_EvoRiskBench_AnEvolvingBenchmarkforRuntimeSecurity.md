---
title: EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents
published: 2026-10-02T11:22:36Z
authors: Shiyi Kuang, Xuemei Luo, Kun Liu, Junhai Li, Rui Tian, Feng Shi, Bo Shen, Nianyu Li, Dehui Li, Ping Chen
url: http://arxiv.org/abs/2610.03153v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents

## Abstract
Workspace agents combine large language models with execution harnesses to perform stateful, multi-step tasks that access or modify external resources. Existing benchmarks leave gaps in executable coverage of their runtime security risks, while evolving model capabilities, harnesses, tools, and threats motivate benchmark evolution. We introduce EvoRiskBench, an evolving benchmark organized around the EP-Path-EF framework, which links an initial risk entry point to a one-hop technical effect through an agent-mediated risk path. The framework defines nine entry-point categories and five effect categories; a 20-participant study supports their interpretability and classification consistency on representative cases. Guided by this framework, an automated end-to-end workflow constructs and executes risk cases in isolated environments and independently verifies outcomes using runtime traces and environment states. The benchmark provides a reproducible dataset of 450 adversarial tasks across six scenarios. We evaluate nine model-harness configurations spanning three models (GPT-5.6 Sol, DeepSeek-V4-Pro-0813, and Claude Opus 5) and three harnesses (Claude Code, Codex, and OpenClaw). Our results reveal substantial vulnerabilities across systems. The most vulnerable configuration, Codex with DeepSeek-V4-Pro-0813, reaches a 68.44% attack success rate (ASR), indicating that configuration of workspace agent is insufficient to ensure secure autonomous execution. ASR varies more across models than harnesses, and harness differences depend on the model. The benchmark cases and evaluation platform will be released after completion of artifact safety and reproducibility checks.

## Metadata
- **Published**: 2026-10-02T11:22:36Z
- **Authors**: Shiyi Kuang, Xuemei Luo, Kun Liu, Junhai Li, Rui Tian, Feng Shi, Bo Shen, Nianyu Li, Dehui Li, Ping Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03153v1)