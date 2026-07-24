---
title: When Does Recurrence Become an Algorithm? Convergence Selection in Weight-Tied Looped Transformers
url: http://arxiv.org/abs/2607.20594v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
generated_at: 2026-07-23 22:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper asks when a weight‑tied looped transformer implements an actual algorithm by analyzing controlled experiments on group word problems. It discovers four key findings: the budget law, architecture prior selection, non‑trivial computational walls, and portable mechanisms. These results are invisible to standard instruments that saturate at fixed points.

## Key Takeaways
- The budget law shows free training creates a linear computation frontier where v positions per loop depend on the training contract, with speed exponent ~0.98 and R²=0.99, and SGD selects the minimal frontier matching contract demands.
- Architecture prior determines algorithm: standard depth transformers learn parallel scans; weight tying flips to serial frontier even when log‑depth addressing is provided, leading untied models to extrapolate worst or fail at A5.
- The walls are not where circuit complexity says: NC1‑completeness costs nothing (A5 generalizes fully) while group order does (S5 deadlocks joint learning), and an operator‑first curriculum dissolves the wall.

## Context
This paper investigates when a weight‑tied looped transformer implements an actual algorithm, using controlled experiments on group word problems to reveal hidden dynamics between training budget and model behavior. It challenges the assumption that circuit complexity alone dictates algorithmic properties in deep networks.

## Implications
Understanding these mechanisms helps practitioners design training schedules that align with computational budgets rather than depth alone. The findings suggest that head‑instrument metrics like convergence‑time scaling can predict out‑of‑distribution performance where standard tail metrics fail, offering a more reliable guide for model deployment and generalization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20594v1)
