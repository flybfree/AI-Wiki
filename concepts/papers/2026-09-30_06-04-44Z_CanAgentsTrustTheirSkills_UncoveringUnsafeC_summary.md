---
title: "Summary: Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents"
published: 2026-09-30T06:04:44Z
authors: [Yan Wang, Zhihao Zhang, Ke Chen, Kai Chen, Yaqin Zhang, Duohe Ma, Jun Dai, Xiaoyan Sun]
type: paper-summary
tags: [paper-summary, arxiv, agent-security, skills]
source_paper: "2026-09-30_06-04-44Z_CanAgentsTrustTheirSkills_UncoveringUnsafeChainsof.md"
---
# Summary: Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents

## Finding
TrustProbe analyzes source-to-sink paths from skill-controlled content to security-sensitive operations, generates realistic malicious skill seeds, evolves them through feedback-guided mutation, and validates observable harm. Across 11 open-source agents, it reportedly identifies 104 taint-style vulnerabilities. In trials using public skill hubs, 25.1% of skill-agent trials exercised vulnerable paths and payload injection weaponized 15 vulnerabilities.

## Why it matters
Installable skills create a chain of trust: users delegate authority to an agent, while skill instructions and resources enter the agent context with insufficient validation. Skill packages therefore need provenance, capability boundaries, taint tracking, runtime authorization, and adversarial evaluation—not merely prompt-level filtering.

## Caveat
The results are reported by the paper authors and should be reproduced against current agent frameworks, skill registries, and realistic permissions. The measured harm depends on the tool and credential surface exposed by each agent.

## Canonical original paper
[ArXiv: Can Agents Trust Their Skills?](http://arxiv.org/abs/2609.39065v1)
