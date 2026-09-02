---
title: Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems
url: http://arxiv.org/abs/2609.00267v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_19-09-34Z_DelegationWithoutTrust_AnEmpiricalGapAnalysisofIde.md
generated_at: 2026-09-01 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates security gaps in multi‑agent LLM systems where agents act on behalf of users. It shows that current frameworks cannot prevent four specific threats and proposes an authorization broker that closes them.

## Key Takeaways
- A threat model identifies confused deputy, token theft, replay attacks, and prompt‑injection privilege escalation as core risks in delegation.
- Existing runtimes such as LangGraph, CrewAI, AutoGen and MCP fail to meet the required security requirements, leaving agents with broad authority.
- The broker blocks all four threats, resists 11 direct attacks, rejects forged tokens, and adds only about two microseconds per decision.

## Context
Autonomous LLM agents are becoming common in applications that require real‑time tool use. Without proper governance the risk of unauthorized actions grows with each new deployment.

## Implications
Practitioners must adopt centralized authorization to limit agent autonomy and ensure compliance with policy. This work provides a scalable model for secure multi‑agent systems across industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00267v1)
