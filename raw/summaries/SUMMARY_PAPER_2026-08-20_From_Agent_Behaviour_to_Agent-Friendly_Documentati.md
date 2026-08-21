---
title: From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of How Coding Agents Discover, Read, and Write Technical Documentation
url: http://arxiv.org/abs/2608.20195v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_15-51-54Z_FromAgentBehaviourtoAgent_FriendlyDocumentation_An.md
generated_at: 2026-08-20 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how autonomous coding agents interact with technical documentation during software development. It reveals that agents primarily create agent‑focused artefacts, and that their consultation of human‑written docs is rare and not linked to immediate code changes.

## Key Takeaways
- Agents’ documentation work is dominated by agent‑facing artefacts such as instruction files and working notes, accounting for 60.5% of all interactions versus only 10.6% for classical technical documentation.
- The probability that a consultation leads directly to the next edit is very low (unadjusted three‑event lift 1.05), indicating no clear validation sequence between reading docs and modifying code.
- Consultation is mostly self‑initiated (70.2%) rather than triggered by failures, and when both documentation changes and code edits occur in a pull request, code modifications precede documentation updates four times more often.

## Context
The study addresses the growing reliance on AI agents for software engineering tasks while highlighting gaps in how these systems handle human‑written technical documentation. It contributes to understanding agent behavior beyond simple task completion toward more realistic workflows that involve knowledge sharing and verification.

## Implications
For developers, this suggests that current “agent‑friendly” docs may not be effectively used by autonomous agents, leading to inefficiencies. For industry, it calls for redesigning documentation practices to support AI collaboration rather than assuming existing docs are sufficient.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20195v1)
