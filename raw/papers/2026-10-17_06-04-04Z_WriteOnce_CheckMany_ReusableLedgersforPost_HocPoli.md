---
title: Write Once, Check Many: Reusable Ledgers for Post-Hoc Policy Compliance Auditing of Agent Trajectories
published: 2026-10-17T06:04:04Z
authors: Ashwin Nagarajan, Gursimran Panesar, Alicia Yang, Mona T. Diab, Virginia Smith, Aashiq Muhamed
url: http://arxiv.org/abs/2610.24483v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Write Once, Check Many: Reusable Ledgers for Post-Hoc Policy Compliance Auditing of Agent Trajectories

## Abstract
Auditing LLM agents against policies is critical to ensure safety but requires rereading long trajectories once per policy. Can we instead record each trajectory once and reuse that record for policies not known in advance? We propose write once, check many, a framework in which a writer model converts each agent trajectory into a policy-independent ledger of the agent's actions and outcomes. A reader then checks each new policy against the ledger alone, without access to the original trajectory. On 900 trajectories from SHADE-Arena, $τ$-bench, and $τ^2$-bench, we show that a 12B reader of narrative ledgers can either match or in fact achieve higher AUC than the same 12B model reading full trajectories. On SHADE-Arena policies that combine several facts, our approach outperforms a 31B model reading the trajectory (.777 vs. .713 AUC). When checking eight SHADE-Arena policies separately, ledgers use about $5\times$ fewer tokens, including the cost of writing them. A deeper analysis shows that rule-based extraction performs better on some single-action policies, and ledgers can miss evidence in long tool outputs and message contents. Our results suggest that reusable, policy-independent records can make retrospective agent auditing more efficient and effective, and highlight important considerations in ledger design.

## Metadata
- **Published**: 2026-10-17T06:04:04Z
- **Authors**: Ashwin Nagarajan, Gursimran Panesar, Alicia Yang, Mona T. Diab, Virginia Smith, Aashiq Muhamed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24483v1)