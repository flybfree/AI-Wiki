---
title: Rethinking GRPO for Large Reasoning Model Safety Alignment
url: http://arxiv.org/abs/2610.23085v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_07-53-36Z_RethinkingGRPOforLargeReasoningModelSafetyAlignmen.md
generated_at: 2026-10-18 20:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies two critical failure modes in Group Relative Policy Optimization (GRPO) when applied to safety alignment of Large Reasoning Models: advantage collapse, where homogeneous rollout groups produce vanishing learning signals, and unsafe diversification, where unsafe outputs persist and grow more varied over training. The authors propose Beacon, a framework combining Safety Signal Recovery (SSR) and Safety-Utility Decoupled Alignment (SUDA), which recovers effective safety learning signals and decouples safety from utility optimization, achieving up to a 32.83 percentage point reduction in average safety error across multiple model variants and benchmarks while maintaining low over-refusal rates.

## Key Takeaways
- Advantage collapse occurs when rollout groups within GRPO become behaviorally homogeneous, causing within-group safety contrasts to weaken and advantages to approach zero. The paper's theoretical analysis shows that behavioral consistency directly undermines the group-relative optimization mechanism, leaving the model without meaningful safety-directed gradients. This is a fundamental structural weakness of GRPO when applied to safety alignment rather than general capability improvement.
- Unsafe diversification is a second failure mode where, once relative safety signals vanish, entropy regularization inadvertently encourages the model to produce increasingly diverse unsafe responses. Rather than converging toward safe behavior, the model's unsafe outputs proliferate in variety, making the safety problem harder to address over successive training iterations.
- Beacon addresses both failure modes through two complementary mechanisms: Safety Signal Recovery combines advantage-guided trajectory filtering with safe reference supervision to inject effective safety learning signals back into training, while Safety-Utility Decoupled Alignment uses category-aware reward design and benign-only KL anchoring to prevent over-refusal behavior. Experiments across four Qwen3 and DeepSeek-R1-Distill model variants evaluated on eight benchmarks demonstrate that Beacon achieves the best average safety and reasoning performance simultaneously.

## Context
Large Reasoning Models such as DeepSeek-R1 and Qwen3 have demonstrated remarkable chain-of-thought reasoning capabilities, yet their extended reasoning chains introduce new safety risks including hallucinated harmful outputs, over-refusal to benign queries, and inconsistent safety behavior across diverse prompts. GRPO has become the dominant reinforcement learning alignment technique for these models due to its efficiency and lack of a separate critic model, but its group-relative advantage estimation was primarily designed for capability optimization rather than safety-critical alignment. This paper fills a gap by providing both theoretical analysis of why GRPO fails for safety and a practical framework to repair those failures.

## Implications
For practitioners deploying reasoning models in production safety-critical applications, this work demonstrates that standard GRPO-based alignment pipelines may silently degrade safety performance over training, producing models that appear aligned on benchmarks but generate increasingly diverse unsafe outputs in practice. The Beacon framework offers a modular intervention that can be integrated into existing GRPO training pipelines without replacing the entire alignment stack, making it accessible for teams already invested in GRPO infrastructure. For the broader field, the identification of advantage collapse and unsafe diversification as structural failure modes provides a diagnostic lens that can guide future alignment algorithm design beyond reasoning models, including multimodal and agentic systems where safety signals are similarly sparse relative to capability signals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23085v1)
