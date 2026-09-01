---
title: Capability-Stratified Degradation in Ternary Language Models
url: http://arxiv.org/abs/2608.28809v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_19-22-38Z_Capability_StratifiedDegradationinTernaryLanguageM.md
generated_at: 2026-08-31 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how converting a pretrained Qwen3.5-0.8B model to ternary weights (weights limited to \{-1,0,+1\}) affects its capabilities and performance across 29 benchmarks, representation diagnostics, and downstream fine‑tuning tasks. It finds that while the full‑precision teacher retains most factual knowledge, the ternary model Cloe loses specialist information, as shown by a linear probe recovering only 26% of MMLU answers (near chance). However, Cloe still performs on ten tasks, averaging 77% of the teacher’s performance, and fine‑tuning can raise SST‑2 to 89.8% (95.6% of the teacher) and XSum to 79.4% teacher retention.

## Key Takeaways
- Linear probe results indicate that specialist factual information is largely lost in Cloe, recovering only 26.19% of MMLU answers compared with 43.76% from the full‑precision teacher.  
- Despite degradation, Cloe retains measurable performance on ten tasks, averaging 77.1% of the teacher’s performance.  
- Fine‑tuning improves SST‑2 to 89.8% (95.6% of the matched teacher) and XSum retention to 79.4% of the teacher.

## Context
This work addresses a growing need for ultra‑low‑bit inference in AI models, where ternary quantization approaches the theoretical limit of \log_2 3 ≈ 1.585 bits per weight. Preserving model capabilities is crucial because abrupt degradation can render deployed systems unusable without retraining or adaptation.

## Implications
For practitioners, ternary conversion should not be treated as a drop‑in replacement for full‑precision models; instead it serves as a compact substrate that must be fine‑tuned to recover useful performance. The findings highlight the importance of evaluating both representation and downstream task outcomes when adopting extreme quantization strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28809v1)
