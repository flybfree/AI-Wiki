---
title: Language-Conditional Dequantization: Recovering What Quantization Steals from Non-English Languages
url: http://arxiv.org/abs/2608.11786v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_08-28-03Z_Language_ConditionalDequantization_RecoveringWhatQ.md
generated_at: 2026-08-12 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how aggressive quantization degrades multilingual performance and proposes Language-Conditional Dequantization (LCD) to recover lost quality for non‑English models. On Qwen2.5-3B and Llama‑3.2‑3B, LCD restores 70–83% of the perplexity gap for scripts outside Latin and 17–28% of the GlobalMMLU accuracy gap while adding only 0.12% extra parameters.

## Key Takeaways
- Aggressive INT3 GPTQ quantization causes 2‑4× larger perplexity loss on non‑English languages compared with English, highlighting language‑specific damage.  
- LCD adds a tiny per‑language LoRA correction (0.12% parameters) and recovers most of the lost performance without retraining the whole model.  
- The method outperforms both data‑free low‑rank baseline LQER and equal‑capacity language‑agnostic corrections by several points on typologically distant languages.

## Context
Quantization is essential for deploying large language models efficiently, yet its impact varies across linguistic domains. This work demonstrates that standard techniques ignore the distinct error propagation patterns between early and late layers of different architectures, affecting multilingual fairness.

## Implications
For practitioners, LCD offers a lightweight post‑hoc fix that can be applied to existing quantized deployments, preserving performance for diverse user bases. In industry, it supports equitable AI services without massive retraining budgets or additional hardware costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11786v1)
