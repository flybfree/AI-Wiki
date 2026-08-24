---
title: ARQ: Agentic CodeQL Query Refinement for C/C++ Vulnerability Detection
url: http://arxiv.org/abs/2608.20637v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_00-20-55Z_ARQ_AgenticCodeQLQueryRefinementforC_C__Vulnerabil.md
generated_at: 2026-08-23 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ARQ an agentic framework that automatically refines C/C++ CodeQL queries using execution‑grounded evidence from synthesized programs. It identifies false positives and false negatives by detecting mismatches between program behavior and query verdicts then repairs the query with LLM assistance. On benchmark datasets ARQ‑refined queries increase true positive detection up to 119.8% while maintaining precision above 98%.

## Key Takeaways
- ARQ automatically refines CodeQL queries by using synthesized C/C++ programs that expose weaknesses when execution disagrees with the query’s verdict, thereby fixing false positives and false negatives without labeled data or vulnerability templates.
- The LLM‑driven refinement loop repairs queries based on these disagreements, improving detection rates significantly compared to original queries.
- ARQ successfully resolved three long‑standing GitHub issues and uncovered two new bugs in libpng and zlib, showing real‑world impact.

## Context
Static analysis tools like CodeQL rely on handcrafted queries that often produce false positives or miss vulnerabilities. Traditional refinement methods require extensive labeled datasets or vulnerability knowledge, limiting scalability. ARQ leverages AI agents to close this gap by generating synthetic evidence and refining queries autonomously.

## Implications
This approach offers a scalable solution for maintaining large query repositories without manual tuning. Practitioners can rely on automated refinement to keep tools up‑to-date with evolving codebases and emerging vulnerabilities, reducing false alarms and improving security coverage across C/C++ projects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20637v1)
