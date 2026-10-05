---
title: Beyond Correctness: Resolving Underspecification in Agentic Text-to-SQL
published: 2026-10-02T03:10:55Z
authors: Wen-Zhi Li, Yue Gong, Konstantinos Kanellis, Balakrishnan Murali Narayanaswamy
url: http://arxiv.org/abs/2610.02739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Correctness: Resolving Underspecification in Agentic Text-to-SQL

## Abstract
Agentic Text-to-SQL systems can interact with users to clarify underspecified queries before generating SQL. However, a correct execution result does not necessarily imply that the agent has adequately resolved the underlying underspecification: the agent may silently make unverified assumptions that happen to match the intended answer. We show that this behavior is driven in part by premature clarification termination. Although forcing an agent to ask more questions improves execution accuracy, ambiguities are concentrated in earlier interactions, making brute-force questioning inefficient. More importantly, even when explicitly prompted to plan its clarification process, the agent frequently abandons questions that it has already identified as relevant. To address this failure mode, we introduce PlanPool, which externalizes the clarification plan as a mutable question pool. Every planned question must be explicitly asked or dropped before submission, while newly discovered ambiguities can be added during interaction. Across three benchmarks derived from BIRD-Interact and Spider, PlanPool consistently improves ambiguity coverage and reduces silent failures over unconstrained and prompt-based alternatives, while maintaining competitive execution accuracy. Our results highlight an important distinction in agentic reasoning: identifying missing information is not sufficient, and the agent must also reliably maintain and resolve it before committing to an answer.

## Metadata
- **Published**: 2026-10-02T03:10:55Z
- **Authors**: Wen-Zhi Li, Yue Gong, Konstantinos Kanellis, Balakrishnan Murali Narayanaswamy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02739v1)