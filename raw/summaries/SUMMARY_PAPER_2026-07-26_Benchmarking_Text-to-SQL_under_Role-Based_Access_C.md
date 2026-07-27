---
title: Benchmarking Text-to-SQL under Role-Based Access Control
url: http://arxiv.org/abs/2607.22115v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_09-10-58Z_BenchmarkingText_to_SQLunderRole_BasedAccessContro.md
generated_at: 2026-07-26 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a benchmarking framework for text-to-SQL that incorporates realistic role-based access control (RBAC) constraints, addressing the gap between unrestricted benchmark scores and practical performance. The authors augment existing datasets by generating plausible user roles and access policies through an LLM‑assisted reasoning process, then evaluate state‑of‑the‑art models under these constraints to reveal RBAC‑specific failures.

## Key Takeaways
- The framework demonstrates that many high‑scoring open‑weight LLMs degrade sharply when RBAC is enforced, often violating permissions or rejecting queries that could be answered with permitted data.  
- Role synthesis is performed by the LLM as a structured reasoning task that infers application context from the schema and derives role responsibilities consistent with access scopes.  
- Human‑in‑the‑loop quality control using metric‑guided screening ensures that generated roles are plausible and align with domain expectations.

## Context
Current text-to-SQL benchmarks assume unrestricted database access, which masks how models behave under real‑world security policies such as RBAC. This paper highlights the importance of evaluating AI systems not only on query accuracy but also on compliance with access controls to ensure trustworthy deployment in enterprise environments.

## Implications
For practitioners, this work underscores that benchmarking must include security constraints to predict actual system behavior. For industry stakeholders, it signals a need for integrated evaluation pipelines that combine utility metrics with access‑control compliance to avoid costly production failures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22115v1)
