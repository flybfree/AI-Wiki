---
title: Pricing the Risk of Runtime Compression: Anytime-Valid Admission and a Served-Output Law for Compressed Serving State
url: http://arxiv.org/abs/2608.15810v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_15-37-44Z_PricingtheRiskofRuntimeCompression_Anytime_ValidAd.md
generated_at: 2026-08-17 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a pricing framework for runtime compression in serving state that balances quality and capacity while providing guaranteed risk bounds. It demonstrates that the union bound over event counts exhausts on all long requests, replacing it with an anytime-valid ledger that halves fallback rate from 30% to 14%. A machine‑checked design law translates served TV target into a threshold knob, quantifying the remaining gap.

## Key Takeaways
- The union budget is exhausted on every long request in production serving stack, achieving 100% coverage.
- An anytime‑valid ledger halves exact‑fallback rate from 0.30 to 0.14 while keeping risk at matched level.
- A machine‑checked design law (TV ≤ tanh(a_q w_thr)) turns served TV into a threshold knob, with quantified gap and audit layers.

## Context
Runtime compression is essential for scaling AI serving systems but often lacks formal guarantees. This work bridges the gap by providing provable risk budgets that survive unseen requests using order‑statistic bounds instead of vacuous conformal certificates. The use of Lean 4 verification underscores a shift toward mathematically rigorous AI infrastructure.

## Implications
Practitioners can now budget compression costs explicitly, reducing surprise failures and improving user experience. The framework offers a clear pricing model for risk trade‑offs, encouraging more conservative yet efficient serving strategies in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15810v1)
