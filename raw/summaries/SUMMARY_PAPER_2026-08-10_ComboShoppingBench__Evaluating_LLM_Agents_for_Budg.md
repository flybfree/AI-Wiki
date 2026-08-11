---
title: ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons
url: http://arxiv.org/abs/2608.09282v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-37-54Z_ComboShoppingBench_EvaluatingLLMAgentsforBudget_Co.md
generated_at: 2026-08-10 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ComboShoppingBench, a benchmark designed to evaluate large language model agents in constructing feasible basket of complementary items under budget and coupon constraints. The authors demonstrate that even top‑performing LLM agents often produce infeasible or suboptimal baskets, indicating significant room for improvement in constraint‑aware reasoning.

## Key Takeaways
- ComboShoppingBench generates a full shopping scenario including coupons, budgets, and queries, then uses an exploration agent to create a valid witness basket that guides the evaluation rubric.
- Evaluation combines semantic satisfaction checks with deterministic validation of product IDs, budget compliance, and coupon optimality, preventing exact‑match metrics from masking infeasible orders.
- The results show that strong LLM agents still fail on complex combo‑shopping tasks, highlighting limitations in joint reasoning about compatibility, availability, and financial constraints.

## Context
Combo shopping is a common real‑world task where users must select multiple items whose compatibility and pricing interact. Current benchmarks often focus on single product retrieval or ignore multi‑item feasibility, making it difficult to assess agents that must balance many constraints simultaneously.

## Implications
For practitioners, ComboShoppingBench provides a standardized way to test the robustness of LLM agents in real‑world shopping scenarios, encouraging research into better constraint handling and verification mechanisms. In industry, adopting such benchmarks could lead to safer recommendation systems that respect user budgets and coupon policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09282v1)
