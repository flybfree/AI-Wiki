---
title: SkillForge: Compositional Skill Synthesis with Verification-in-the-Loop for Generating Formally Verified Dafny Programs
url: http://arxiv.org/abs/2608.29841v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_15-15-00Z_SkillForge_CompositionalSkillSynthesiswithVerifica.md
generated_at: 2026-08-31 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SKILLFORGE, a framework that generates formally verified Dafny programs from natural language specifications by decomposing the synthesis task into a set of atomic skills. Each skill is defined with a prompt template, tool binding, and a decidable success criterion, allowing deterministic verification-driven iteration. The system repeatedly synthesizes candidate code, submits it to the Dafny verifier, diagnoses failures, and applies targeted repair skills until correctness is achieved or a budget ends.

## Key Takeaways
- SKILLFORGE separates synthesis into reusable modules such as specification inference, body generation, invariant creation, error diagnosis, and targeted repair, each with its own success metric.  
- The verification harness routes failures deterministically to the appropriate skill, enabling rapid convergence and often verifying programs on the first attempt without exceeding token budgets.  
- Ablation results show that every component contributes measurably to performance gains over state‑of‑the‑art agentic methods.

## Context
Program synthesis combined with formal verification is a central challenge in AI research, where agents must produce code that satisfies complex logical properties. Existing approaches often lack determinism or require extensive retries, leading to high token consumption and long latency. SKILLFORGE addresses these issues by embedding verification directly into the generation pipeline.

## Implications
For industry practitioners, SKILLFORGE offers a reliable way to automate the creation of certified code from natural language requirements, reducing manual effort and risk of undetected bugs. Its deterministic skill composition can be integrated into larger development workflows, providing a scalable path toward fully verified software systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29841v1)
