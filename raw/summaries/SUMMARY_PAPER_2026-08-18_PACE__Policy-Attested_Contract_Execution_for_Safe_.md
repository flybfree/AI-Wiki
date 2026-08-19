---
title: PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance
url: http://arxiv.org/abs/2608.17220v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_00-22-46Z_PACE_Policy_AttestedContractExecutionforSafeAIAgen.md
generated_at: 2026-08-18 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PACE, a framework that binds LLM‑driven DeFi agents to on‑chain actions via typed intents and signed Policy Decision Records, achieving zero unsafe executions in deterministic tests while incurring modest gas overhead. The authors report a 0.80 unsafe rate for the unguarded baseline versus near‑zero with PACE.

## Key Takeaways
- PACE uses typed transaction intents and cryptographically signed PDRs to ensure that only approved policy matches are executed, eliminating prompt injection risks.
- The framework adds only ~30 k gas per transaction, showing minimal performance impact despite strong safety guarantees.
- Ablation shows permissive policy settings raise the unsafe rate by 57.5 percentage points, highlighting the importance of strict policy enforcement.

## Context
Autonomous AI agents are increasingly used in decentralized finance to execute swaps and lending without human oversight, but their reliance on large language models makes them vulnerable to manipulation. This work addresses that vulnerability with a deterministic safety layer that can be audited at the logic level.

## Implications
PACE provides a template for integrating provable security into AI‑driven financial protocols, encouraging developers to adopt policy‑attested execution rather than trusting raw model outputs. The approach could become a standard practice as DeFi scales and faces more sophisticated attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17220v1)
