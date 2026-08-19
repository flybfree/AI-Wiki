---
title: Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch
url: http://arxiv.org/abs/2608.17684v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_11-57-44Z_AuditingSelf_EvolutioninFinancialAgents_Capability.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits three self‑evolving financial agent components—SkillOpt, Agent Workflow Memory (AWM), and ReasoningBank—in simulated e‑banking to see how capability gains affect security drift and interface mismatches. It finds that while utility improves, exposure to malicious content rises sharply, unauthorized state changes increase, and overall attack success rate only modestly goes up.

## Key Takeaways
- SkillOpt’s benign utility jumps from 0.741 to 0.837 but injected‑content exposure climbs to 0.943, indicating a trade‑off between performance and safety.
- Conditional attacks succeed less often after exposure (0.562 vs 0.605) yet the overall ASR rises to 0.530 and unauthorized financial state changes reach 0.685, showing hidden security erosion.
- The AWM evaluation is broken by a literal WebArena text‑action envelope that disables native function calls; removing it restores utility to 0.756 while exposing the system to far higher risk.

## Context
Self‑evolving agents promise continuous improvement but lack formal auditing mechanisms, leading to hidden regressions in security and functionality. This work demonstrates that evaluating only accuracy is insufficient for financial systems where state integrity matters.

## Implications
Financial institutions must monitor not just capability gains but also attack‑surface contact, unauthorized state changes, and compatibility of evolving artifacts with execution interfaces. Ignoring these factors could enable silent breaches that compromise user funds and trust.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17684v1)
