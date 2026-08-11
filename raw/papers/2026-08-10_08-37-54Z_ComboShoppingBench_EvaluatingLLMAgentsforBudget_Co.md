---
title: ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons
published: 2026-08-10T08:37:54Z
authors: Adrian Li, Kelong Mao, Yudong Guo, Heming Xia, Xinwei Yang, Lirui Luo, Jace Wong, Pu Yao, Sulong Xu, Simiu Gu
url: http://arxiv.org/abs/2608.09282v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ComboShoppingBench: Evaluating LLM Agents for Budget-Constrained Basket Shopping with Coupons

## Abstract
Real-world shopping often requires constructing a basket of complementary items rather than retrieving a single product. Such combo-shopping tasks arise in device setup, meal preparation, event planning, and group takeout ordering, requiring joint reasoning about item compatibility, availability, store-level requirements, delivery fees, coupons, and budgets. Evaluation is challenging because multiple baskets may satisfy the same request, making exact-match metrics unsuitable, whereas semantic evaluation alone cannot detect infeasible orders, invalid coupon combinations, or incorrect payments. We introduce ComboShoppingBench, an agentic shopping benchmark for open-ended yet verifiable basket construction in a simulated commerce and takeout environment. During task synthesis, an exploration agent constructs a feasible and semantically coherent basket of purchasable products; this witness guides the generation of coupons, budget constraints, user queries, and aligned evaluation rubrics. During evaluation, LLM judges assess semantic satisfaction, response quality, and claim faithfulness, while deterministic validation checks product-ID validity, budget compliance, and coupon optimality. Experiments with diverse LLM agents demonstrate that even strong agents struggle on ComboShoppingBench, highlighting substantial room for improvement in reliable, constraint-aware combo shopping.

## Metadata
- **Published**: 2026-08-10T08:37:54Z
- **Authors**: Adrian Li, Kelong Mao, Yudong Guo, Heming Xia, Xinwei Yang, Lirui Luo, Jace Wong, Pu Yao, Sulong Xu, Simiu Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09282v1)