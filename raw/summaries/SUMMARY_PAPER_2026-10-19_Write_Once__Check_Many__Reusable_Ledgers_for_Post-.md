---
title: Write Once, Check Many: Reusable Ledgers for Post-Hoc Policy Compliance Auditing of Agent Trajectories
url: http://arxiv.org/abs/2610.24483v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_06-04-04Z_WriteOnce_CheckMany_ReusableLedgersforPost_HocPoli.md
generated_at: 2026-10-19 20:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a "write once, check many" framework for auditing LLM agent trajectories against safety policies. A writer model converts each agent trajectory into a policy-independent ledger, and a reader model then checks new policies against the ledger without needing access to the original trajectory. The authors demonstrate that a 12B reader model using narrative ledgers can match or exceed the performance of the same model reading full trajectories, while using approximately five times fewer tokens when checking multiple policies.

## Key Takeaways
- On 900 trajectories from SHADE-Arena, τ-bench, and τ²-bench, a 12B reader of narrative ledgers achieved equal or higher AUC compared to the same 12B model reading full trajectories. For SHADE-Arena policies combining several facts, the ledger approach outperformed a 31B model reading the raw trajectory, achieving 0.777 AUC versus 0.713 AUC, demonstrating that structured records can compensate for smaller model capacity.
- Efficiency gains are substantial: when checking eight SHADE-Arena policies separately, the ledger approach uses about five times fewer tokens, including the one-time cost of writing the ledger. This makes retrospective auditing of agents against many unknown-in-advance policies far more computationally feasible than re-reading full trajectories per policy.
- The authors acknowledge important limitations: rule-based extraction outperforms ledgers on some single-action policies, and ledgers can miss critical evidence embedded in long tool outputs or message contents. This highlights that ledger design choices—what to include, how to structure narratives, and how to handle dense tool outputs—materially affect auditing accuracy.

## Context
As LLM agents are increasingly deployed in high-stakes environments involving tool use, multi-step reasoning, and interaction with external systems, post-hoc compliance auditing becomes essential for safety and regulatory accountability. Current auditing approaches require re-reading lengthy agent trajectories for every policy check, creating a scalability bottleneck as the number of policies grows. This paper addresses that bottleneck by decoupling trajectory recording from policy evaluation, proposing a reusable intermediate representation that separates the expensive trajectory-reading step from the policy-checking step.

## Implications
For practitioners deploying agent systems in regulated domains such as finance, healthcare, or government, this framework offers a path toward auditing agents against evolving or unforeseen policies without reprocessing raw trajectories each time, dramatically reducing compute costs and enabling continuous compliance monitoring. For the broader AI safety community, the work highlights that structured, policy-independent records can serve as a practical bridge between agent behavior and governance requirements, while also cautioning that ledger design must carefully preserve evidence from tool outputs and message contents to avoid blind spots in auditing coverage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24483v1)
