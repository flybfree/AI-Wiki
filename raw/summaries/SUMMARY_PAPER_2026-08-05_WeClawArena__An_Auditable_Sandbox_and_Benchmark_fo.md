---
title: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaboration and Security in Human-Centered Agent Networks
url: http://arxiv.org/abs/2608.03499v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_11-42-26Z_WeClawArena_AnAuditableSandboxandBenchmarkforCross.md
generated_at: 2026-08-05 01:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WeClawArena, an auditable sandbox and benchmark designed to evaluate cross‑user agent collaboration within personal workspaces. The framework creates realistic multi‑party scenarios where agents interact over shared resources while preserving user privacy and authority boundaries. Evaluation shows that both utility and attack success rates can be measured end‑to‑end, providing evidence for task breakdown, privacy leakage, or invalid authority paths.

## Key Takeaways
- WeClawArena expands 124 base tasks into 620 scenario variants with benign controls and four attack vectors per task to stress test collaboration.  
- The sandbox logs peer messages, tool calls, resource operations, governed decisions, and final workspace states, enabling auditable evidence of attacks.  
- Utility and attack success rates are reported separately, allowing precise diagnosis of successful privacy breaches or policy violations.

## Context
The rapid growth of persistent personal‑agent frameworks creates complex human‑centered networks where agents act on behalf of users while maintaining private workspaces. Existing benchmarks focus on tool use but lack end‑to‑end sandboxing for multi‑party collaboration, leaving gaps in understanding security risks across user boundaries.

## Implications
WeClawArena equips researchers and practitioners with a reproducible testbed to assess both performance and security in collaborative AI systems, informing design of safer agent architectures. Its findings guide industry efforts to embed verifiable safeguards into human‑centric agent networks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03499v1)
