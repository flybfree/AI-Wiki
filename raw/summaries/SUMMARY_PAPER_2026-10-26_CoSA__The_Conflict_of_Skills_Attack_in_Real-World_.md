---
title: CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems
url: http://arxiv.org/abs/2610.35082v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_09-25-38Z_CoSA_TheConflictofSkillsAttackinReal_WorldLLMAgent.md
generated_at: 2026-10-26 23:13
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Conflict of Skills Attack (CoSA), a novel adversarial threat in LLM agent ecosystems where individually compliant Skills, when composed together, produce policy violations through cross-Skill dependencies such as data leakage, unauthorized state modification, and unsafe execution. The authors demonstrate that adding as few as 5% new Skills to an existing pool increases policy-violation rates from 35.02% to 58.45% across five LLMs and three agent harnesses, and they propose a lightweight harness-level guard that reduces violations from 65.28% to 6.67% while preserving task completion rates.

## Key Takeaways
- The paper identifies four recurring mechanisms behind Conflict of Skills failures: artifacts or assessment signals produced for one purpose are reused downstream without preserving the restrictions or authorization needed for their new use. These mechanisms involve capability supplementation (adding locally admitted Skills to supply missing business operations) and relationship reshaping (altering artifact exchange, decision reuse, and target/action bindings), all while leaving existing Skills and runtime permissions unchanged.
- CoSA-Bench is a new evaluation benchmark built from real-world Skills and controlled services, comprising 288 tasks across recruiting, finance, IT, and business domains. It tests three violation categories: data leakage, unauthorized state modification, and unsafe execution. The benchmark reveals that under autonomous Skill selection, even minimal additions (capped at 5% of the original pool) cause a 23.43 percentage-point increase in policy-violation rates, demonstrating that composition-level risks are not captured by single-Skill assessments.
- The proposed harness-level guard performs information-flow and authorization checks before consequential actions. On OpenClaw recruiting tasks across five models, it reduces violations from 65.28% to 6.67% while policy-compliant task completion on matched benign controls only drops from 66.67% to 65.00%, showing that effective mitigation is achievable without sacrificing agent utility.

## Context
As LLM agents increasingly rely on modular, reusable Skill libraries to perform complex multi-step tasks, the assumption that individually validated components remain safe when composed has become a critical blind spot in agent safety research. This paper addresses a gap between single-component compliance testing and the emergent risks that arise when Skills interact through shared artifacts, decisions, and action bindings in production agent frameworks. It matters because real-world deployments in recruiting, finance, and IT involve heterogeneous Skills whose outputs flow into each other, creating attack surfaces invisible to per-Skill audits.

## Implications
For practitioners building agent pipelines, the findings argue that security reviews must extend beyond individual Skill validation to composition-level auditing, and that lightweight runtime guards checking information flow and authorization before consequential actions can dramatically reduce violations without degrading task performance. For the broader field, CoSA-Bench provides a reproducible benchmark for stress-testing agent harnesses against composition attacks, and the CoSA framework offers a structured vocabulary for classifying cross-Skill failure modes that can inform future standards for agent ecosystem governance and compliance auditing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35082v1)
