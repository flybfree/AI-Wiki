---
title: AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents
published: 2026-09-25T14:26:04Z
authors: Weida Liang, Shi Qiu, Zhun Wang, Simon Sure, Xiaoyuan Liu, Tianneng Shi, Zhaorun Chen, Wenbo Guo, Dawn Song
url: http://arxiv.org/abs/2609.31318v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents

## Abstract
AI agents combine language models with external data and tools that can modify files, call APIs, or execute code. Security failures can arise when adversarial content changes an agent's tool use or when the surrounding software contains vulnerabilities such as path traversal or command injection. We study authorized white-box pre-deployment auditing, where the auditor has access to the target repository and a controlled runtime, but successful attacks must still act through the task-defined attacker interface and be confirmed by an external verifier. We present AgentXploit, a two-role auditing system that separates repository-level attack-path discovery from runtime exploitation. The Analyzer Agent traces attacker-controlled inputs to sensitive operations and records code-supported candidate attack paths; the Exploiter Agent turns these paths into concrete attacks and revises them using runtime feedback. We also introduce AgentXploit-Bench, containing 72 reproducible vulnerabilities across 12 open-source AI-agent systems and frameworks. Across three runs, AgentXploit reaches 59.3% end-to-end success, compared with 38.4% for Codex. Under a token-budget-matched comparison, Codex reaches 46.3%. On AgentDojo, where injection points are provided, the Exploiter Agent reaches 79.2% attack success versus 52.7% for AgentVigil. These results highlight repository discovery and runtime exploitation as distinct challenges in end-to-end agent security auditing.

## Metadata
- **Published**: 2026-09-25T14:26:04Z
- **Authors**: Weida Liang, Shi Qiu, Zhun Wang, Simon Sure, Xiaoyuan Liu, Tianneng Shi, Zhaorun Chen, Wenbo Guo, Dawn Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31318v1)