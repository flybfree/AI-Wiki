---
title: Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery
published: 2026-09-23T18:31:44Z
authors: Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
url: http://arxiv.org/abs/2609.28693v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery

## Abstract
Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. Providing an agent with access to every internal tool leads to oversized context windows, degraded tool selection, and severe governance vulnerabilities - as system policies defined purely in prompts remain probabilistic advice rather than hard constraints. Existing mitigations, such as multi-agent domain delegation, decentralize audit logs and fail to guarantee policy compliance across sessions. We introduce skilder, a framework that packages capabilities into roles: bundles of skills, tools, and instructions, together with the limits that bound them. An agent begins with a minimal role catalog, learns the roles a task requires, and receives each role's skills, instructions, and tools through a single MCP server. Because tools reach the agent only inside learned skills, the same server enforces the scope of what was learned deterministically. We evaluate skilder against flat-context tool selection and multi-agent orchestration across 13 tasks using six models (10 runs each). Our results show that, when models completed discovery and issued a governed call, the skilder simulated authorization layer enforced governance boundaries: no unauthorized tool call or parameter violation (e.g., a spending-limit breach) executed. Aggregate task pass rates also reflect whether each model followed the discovery protocol and satisfied response-quality checks; those misses are not authorization failures. Furthermore, by allowing agents to dynamically acquire cross-role capabilities mid-task, skilder preserves problem-solving flexibility while providing hard system-level enforcement.

## Metadata
- **Published**: 2026-09-23T18:31:44Z
- **Authors**: Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28693v1)