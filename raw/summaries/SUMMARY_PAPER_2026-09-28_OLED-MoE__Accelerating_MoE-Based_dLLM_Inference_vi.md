---
title: OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading
url: http://arxiv.org/abs/2609.33385v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_09-05-06Z_OLED_MoE_AcceleratingMoE_BaseddLLMInferenceviaInte.md
generated_at: 2026-09-28 21:53
model: qwen3.6-35b-a3b
---

## Summary
OLED-MoE introduces an expert offloading system designed to accelerate Mixture-of-Experts diffusion large language models on memory-constrained GPUs by shifting from intra-iteration prefetching to inter-iteration expert retention. By exploiting strong routing overlap between adjacent denoising iterations and using token confidence to predict reuse, the method retains high-value experts in GPU memory without extra traffic, achieving near-full-residency performance with only 40% of the expert memory footprint while significantly reducing decoding latency.

## Key Takeaways
- OLED-MoE reorients optimization from intra-iteration layer-wise prefetching to inter-iteration retention, addressing the failure of existing prefetch-based systems in dLLMs where block-wise routing expands the active expert set and makes timely prediction difficult.
- The system leverages token confidence scores to guide expert selection across iterations, allowing it to retain experts likely to be reused while compensating for unavoidable cache misses through dynamic CPU-GPU cooperative execution that accounts for computation load and future reuse patterns.
- OLED-MoE reduces time per output token by 1.23x-7.93x and improves expert cache utilization by 1.44x-4.23x compared to state-of-the-art offloading, approaching full-residency performance with a 60% reduction in memory footprint while incurring only a 23% TPOT overhead.

## Context
Semi-autoregressive diffusion language models offer improved decoding parallelism through iterative block-wise denoising but face scalability challenges when combined with MoE layers due to massive parameter footprints that exceed GPU capacity. Existing serving infrastructure optimized for autoregressive decoding relies on layer-wise prefetching strategies that do not align with the expanded

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33385v1)
