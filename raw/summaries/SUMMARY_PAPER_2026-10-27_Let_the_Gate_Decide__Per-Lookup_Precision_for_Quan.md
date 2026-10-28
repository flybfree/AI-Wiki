---
title: Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs
url: http://arxiv.org/abs/2610.35985v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_11-53-58Z_LettheGateDecide_Per_LookupPrecisionforQuantizedCo.md
generated_at: 2026-10-27 20:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces GateRQ, a per-lookup precision quantization scheme for conditional memory layers (such as DeepSeek's Engram) in large language models. The authors demonstrate that the conventional approach of allocating more bits to frequently accessed rows actually degrades performance, and they trace this failure to the gating mechanism that scales retrieved rows. GateRQ instead uses a gate-aware residual quantization ladder, storing only a 1-bit code in GPU memory to compute the gate and selectively reading deeper quantization levels only for lookups the gate deems most critical, achieving a 7.8x reduction in GPU table memory with minimal accuracy loss.

## Key Takeaways
- Conditional memory layers like DeepSeek's Engram are critical to model performance: removing them from DeepSeek-V4.1-Flash costs 36.8 PopQA points, making their quantization a high-stakes engineering problem. Low-bit quantization disproportionately destroys long-tail factual knowledge, which is precisely where these memory tables provide the most value.
- The standard quantization heuristic of giving more bits to frequently accessed rows actively backfires. The authors show that refining lookups by access frequency performs worse than refining them at random, because the gate that scales each retrieved row is small for frequent n-grams and large for rare long-tail entity n-grams. This means the quantization error is effectively weighted by the gate, making frequency-based allocation misaligned with actual error impact.
- GateRQ stores each row as a ladder of 1-bit residual codes, keeping only level 1 in GPU memory to compute the gate, and reading deeper levels on demand only for the lookups the gate ranks highest. Without any retraining, this achieves a 7.8x reduction in GPU table memory on DeepSeek-V4.1-Flash, raising vLLM throughput by 11% to 31% over FP8 tables, while losing only about 1 PopQA point at 1.50 bits read per lookup and 0.2 points at 2.10 bits across two models.

## Context
Conditional memory layers represent a growing architectural pattern in frontier LLMs, where large hashed n-gram lookup tables are attached to transformer models to inject factual knowledge without retraining. As models like DeepSeek-V4.1-Flash scale these tables to hundreds of gigabytes, GPU memory pressure becomes a hard bottleneck for deployment. This paper matters because it identifies a fundamental misalignment between how quantization error propagates through gated retrieval mechanisms and how practitioners currently allocate precision, offering a principled correction that operates entirely at inference time without retraining.

## Implications
For practitioners deploying large language models with conditional memory components, GateRQ provides a drop-in quantization strategy that dramatically reduces GPU memory requirements and increases serving throughput, making these architectures viable on smaller or more constrained hardware. The finding that frequency-based bit allocation is counterproductive challenges a widely held assumption in quantization engineering and suggests that gate-aware, per-lookup adaptive precision should become a standard design principle for any gated retrieval-augmented architecture in production LLM serving stacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35985v1)
