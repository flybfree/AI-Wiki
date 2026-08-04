---
title: Bole: Efficient Tree Speculation for Hybrid-Attention Language Models
url: http://arxiv.org/abs/2608.01651v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_03-43-14Z_Bole_EfficientTreeSpeculationforHybrid_AttentionLa.md
generated_at: 2026-08-03 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Bole, a kernel‑runtime co‑design that enables efficient tree speculation for hybrid‑attention large language models, achieving up to 4.72× offline decode throughput and reducing memory usage by 82–99×. It integrates with SGLang and cuts TTFT and TPOT by large percentages.

## Key Takeaways
- Bole transforms the linear‑attention recurrence into a tree‑structured closed form, allowing verification of all proposal nodes in parallel.
- The GPU kernel materializes state updates as token‑level factors, reconstructing only the selected state after sampling to cut transient memory dramatically.
- Integration with SGLang provides a batch‑wide verification budget that scales with the complete hybrid forward, boosting throughput and freeing KV cache capacity.

## Context
Hybrid‑attention models aim to balance full attention’s accuracy with linear attention’s speed, but their decoding remains limited by memory. Tree speculation promises acceleration without sacrificing quality, yet prior work struggles with recurrent layers’ state management.

## Implications
Bole demonstrates that kernel co‑design can unlock large gains for LLM serving, making high‑throughput inference feasible on existing hardware and setting a new standard for efficient speculative decoding in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01651v1)
