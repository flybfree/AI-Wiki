---
title: PRECEPT: Security Self-Improvement of Coding Agents via Evolving Principles
url: http://arxiv.org/abs/2611.33519v1
type: paper-summary
date: 2026-11-25
source_paper: 2026-11-24_22-52-27Z_PRECEPT_SecuritySelf_ImprovementofCodingAgentsviaE.md
generated_at: 2026-11-25 21:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PRECEPT, a framework that enables AI coding agents to achieve security self-improvement by learning from their own security failures across sessions. The authors demonstrate that while coding agents like Codex, Claude Code, and Qwen Code can fix vulnerabilities when prompted, they consistently reintroduce the same vulnerability classes in new sessions, revealing a critical gap between capability and retention. PRECEPT addresses this by maintaining an evolving library of secure coding principles that are progressively revised against the agent's own failure patterns, achieving 97.1% secure working code on unseen task families compared to 81.9% for the strongest unaided agent.

## Key Takeaways
- The paper empirically demonstrates a persistent retention failure in AI coding agents: across 14 task sequences, agents fixed a vulnerability 85.7% of the time when shown the failing security test, yet reintroduced the same vulnerability class in a new session 26.7% of the time—nearly identical to agents that had never encountered the vulnerability (27.5%). This shows the capability to fix exists but the knowledge is not activated across sessions.
- Neither recording repairs in persistent context nor supplying published secure coding principles closes the gap. Recorded fixes remained tied to the specific task family they originated from, and human-oriented principles were too general to apply to the code at hand, highlighting that static knowledge injection is insufficient for cross-session security improvement.
- PRECEPT's evolving library starts from authoritative secure coding principles and iteratively revises them against the agent's own failures so each principle fires on the specific code where that agent actually goes wrong. Revisions are validated through fresh executions, kept only if they improve security while maintaining functional success within a small tolerance, and improvement continues across evolution steps rather than saturating after the first iteration.

## Context
As AI coding agents increasingly write and submit production code with limited human review, the security of generated code becomes a critical concern in software engineering pipelines. This paper addresses a fundamental gap in the AI agent literature: while much research focuses on improving functional correctness or single-session task performance, the persistence of learned security knowledge across sessions remains largely unaddressed. The finding that agents treat each session as a fresh start, discarding hard-won security lessons, represents a systemic vulnerability in autonomous code generation workflows that existing mitigation strategies like persistent memory or static principle injection fail to resolve.

## Implications
For practitioners deploying AI coding agents in production environments, PRECEPT offers a practical mechanism to reduce the recurring security vulnerabilities that currently require costly human review and repeated remediation cycles. The approach of evolving principles from the agent's own failure patterns rather than relying on generic human-oriented guidelines suggests a path toward agents that genuinely learn from their mistakes over time. For the broader field, this work signals that security self-improvement—distinct from functional self-improvement—requires purpose-built mechanisms that tie learned principles to the specific failure modes of individual agents, raising important questions about how autonomous systems should be designed to accumulate and apply domain-specific knowledge across operational boundaries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.33519v1)
