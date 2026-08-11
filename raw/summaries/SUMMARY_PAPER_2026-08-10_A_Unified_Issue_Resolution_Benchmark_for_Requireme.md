---
title: A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents
url: http://arxiv.org/abs/2608.09072v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_03-22-04Z_AUnifiedIssueResolutionBenchmarkforRequirementClar.md
generated_at: 2026-08-10 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes SWE-RPG, a repository‑level benchmark that evaluates coding agents not only on final patch correctness but also on intermediate steps such as requirement clarification and implementation planning. Using 163 tasks across Python and Java repositories, the study shows that popular agents like Claude Code and Codex resolve only about one‑third of requests. The results highlight implicit‑requirement recovery as a major bottleneck.

## Key Takeaways
- SWE-RPG adds executable patch evaluation with ground‑truth references for requirement clarification and planning, enabling retrospective diagnosis of agent trajectories.
- Agents fail primarily when they cannot recover implicit requirements, accounting for 24.5% to 46.0% of runs.
- The average resolved rate across evaluated agents is 31.5%, indicating a significant gap between request satisfaction and successful implementation.

## Context
Current coding‑agent research often measures success solely by test pass rates, overlooking the complex reasoning chain needed from user intent to code generation. This narrow view limits understanding of where failures occur and hampers targeted improvements in agent design.

## Implications
For industry practitioners, SWE-RPG provides a concrete framework to diagnose and address requirement ambiguity in real‑world repositories. Researchers can leverage its intermediate GTs to develop better prompting strategies and architecture changes that improve implicit‑requirement recovery.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09072v1)
