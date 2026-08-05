---
title: MAFIA: Query-Only Memory Attacks via Probing and Factual Injection against Audited LLM Agents
url: http://arxiv.org/abs/2608.03844v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_15-50-26Z_MAFIA_Query_OnlyMemoryAttacksviaProbingandFactualI.md
generated_at: 2026-08-05 01:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MAFIA, a query‑only memory attack framework that exploits probing and factual injection to compromise audited LLM agents. The authors demonstrate that MAFIA can achieve up to 90.7% success while keeping audit detection below 8%, highlighting vulnerabilities in both large benign memory pools and active input auditing.

## Key Takeaways
- MAFIA’s placement strategy uses probing, budget allocation, and scheduling to ensure injected records compete effectively for retrieval despite high competition from legitimate memories.
- The payload employs compact factual cloaks that preserve semantic similarity while bypassing audit checks by masking malicious content within innocuous facts.
- Evaluation shows a dramatic reduction in detection rates from 83.3% to 7.4%, proving that current defenses are insufficient against coordinated memory poisoning.

## Context
Memory‑augmented LLM agents rely on extensive context for long‑horizon tasks, but their reliance on stored data creates an exploitable attack surface. As these systems grow more integrated into real‑world applications, the need to understand and mitigate memory‑based threats becomes critical.

## Implications
The findings urge developers of agentic AI to design memory modules with stronger provenance checks and to treat retrieved data as untrusted input. Practitioners must also consider that query‑only attacks can bypass surface‑level audits, prompting a shift toward more robust, multi‑layered security architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03844v1)
