---
title: Crypto Accounting Bench: Evaluating Frontier and Open-Weight Models on Crypto-Asset Accounting Tasks
url: http://arxiv.org/abs/2609.14811v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-13_21-59-07Z_CryptoAccountingBench_EvaluatingFrontierandOpen_We.md
generated_at: 2026-09-14 22:24
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces Crypto Accounting Bench (CAB), a specialized benchmark designed to evaluate how effectively both proprietary and open-weight language models can reconstruct complete, balanced journal entries for cryptocurrency transactions. By testing twelve distinct models across 118 real-world tasks derived from pseudonymized organizations, the authors demonstrate that while current AI systems achieve high accuracy in calculating base currency amounts, they still struggle significantly with selecting the correct accounts and composing fully structured financial entries. The leading model reached a mean score of 77.43% and a Pass@3 rate of 56.78%, underscoring substantial room for improvement in complex accounting reasoning.

## Key Takeaways
- CAB comprises 118 evaluation tasks sourced from seven pseudonymized organizations, each integrating transaction mechanics, asset quantities, base-currency values, wallet and legal-entity context, counterparty evidence, related transaction legs, recurrence patterns, tax-lot documentation, and the organization’s complete chart of accounts to simulate realistic accounting workflows.
- The benchmark evaluates twelve distinct models across three independent attempts per task, generating 4,248 total trajectories and reporting performance through Mean Score, Best@3, and Pass@3 metrics, with the top-performing model reaching a mean score of 77.43% and a best Pass@3 of 56.78%.
- Diagnostic analysis reveals that while models excel at determining base-amount values (97.8% agreement), they face significant difficulty in selecting the correct accounts (56.3% accuracy), identifying account selection and complete-entry composition as the primary remaining challenges for AI-driven financial accounting systems.

## Context
As cryptocurrency adoption expands, organizations increasingly require automated tools to handle complex multi-leg transactions

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14811v1)
