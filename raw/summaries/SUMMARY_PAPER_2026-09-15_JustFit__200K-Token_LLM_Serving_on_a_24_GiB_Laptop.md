---
title: JustFit: 200K-Token LLM Serving on a 24 GiB Laptop with Just-in-Time State Management
url: http://arxiv.org/abs/2609.17475v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-15_17-15-48Z_JustFit_200K_TokenLLMServingona24GiBLaptopwithJust.md
generated_at: 2026-09-15 21:07
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
JustFit introduces an MLX-based inference runtime engineered to overcome severe memory constraints when serving large language models on consumer-grade laptops. By integrating compressed key-value execution, dynamic component residency management, and state-preserving transitions, the system successfully extends single-request context windows by nearly seven times while maintaining high throughput and complex reasoning accuracy on a 24 GiB M4 Pro MacBook.

## Key Takeaways
- The runtime combines three core mechanisms—KVExec for compressed KV cache handling, PhaseSwap for managing component residency, and StateTrans for preserving state during serving transitions—which collectively enable just-in-time materialization and release independent of model-weight quantization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.17475v1)
