---
title: Vero: Can AI Agents Build Formally Verified Software Repositories?
url: http://arxiv.org/abs/2608.13522v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_17-41-27Z_Vero_CanAIAgentsBuildFormallyVerifiedSoftwareRepos.md
generated_at: 2026-08-13 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
Vero is the first benchmark designed to evaluate joint implementation and proof synthesis of multi‑module software using AI agents. The study shows that while frontier coding agents can produce proofs, they often fail to generate correct implementations across modules, solving only 27 of 43 instances and leaving specifications unsolved.

## Key Takeaways
- Vero is the first benchmark that evaluates both code generation and proof synthesis at the repository level rather than on isolated functions.  
- Agents frequently produce proofs but cannot create coherent implementations that span multiple modules, indicating a gap in joint reasoning.  
- The audit mechanism allows agents to prove unsatisfiability of specifications or incorrectness of reference code, improving curation reliability.

## Context
AI agents are increasingly used for programming tasks yet lack guarantees about the correctness of their output. This work addresses that gap by providing a comprehensive testbed that measures progress toward verified software synthesis across real‑world repositories.

## Implications
For industry and researchers, Vero highlights current limitations of AI‑generated code and proof generation, guiding future research on multi‑module verification and trustworthy AI systems. It also offers an open benchmark to track improvements in repository‑scale verified software synthesis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13522v1)
