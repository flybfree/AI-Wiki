---
title: Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets
url: http://arxiv.org/abs/2608.17360v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_04-26-39Z_FairASR_Re_EvaluatingBlack_BoxJailbreaksunderShare.md
generated_at: 2026-08-18 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Fair‑ASR, an evaluation protocol for black‑box jailbreak attacks under shared target‑call budgets B, and re‑evaluates 11 representative attacks to show that their rankings shift dramatically as the budget changes. It finds that simple stochastic perturbations remain highly competitive when target access is equal, while no LLM‑driven method is efficient in both target and attacker calls.

## Key Takeaways
- Attack rankings change substantially across target‑call budgets, indicating that ASR alone is insufficient for fair comparison.
- Simple stochastic perturbations and hand‑crafted templates achieve high success rates with low target call usage, showing they are budget‑efficient.
- No evaluated LLM‑driven method is efficient in both target and attacker calls, highlighting a gap between model complexity and computational cost.

## Context
Evaluating language model safety often ignores the resource constraints of attacks, leading to misleading rankings. This work addresses that by using directly observable target‑call budgets as a common metric. The methodology enables transparent comparison across heterogeneous models without assuming FLOPs estimation.

## Implications
Practitioners can now prioritize jailbreak defenses based on both success probability and computational efficiency. The ReCode compositional attack demonstrates how combining low‑cost primitives yields high ASR with minimal attacker calls, offering a template for future efficient adversarial research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17360v1)
