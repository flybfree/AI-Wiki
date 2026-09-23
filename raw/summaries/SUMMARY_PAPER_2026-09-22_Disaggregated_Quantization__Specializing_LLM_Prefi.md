---
title: Disaggregated Quantization: Specializing LLM Prefill and Decode
url: http://arxiv.org/abs/2609.26333v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-22_12-44-16Z_DisaggregatedQuantization_SpecializingLLMPrefillan.md
generated_at: 2026-09-22 20:09
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces "disaggregated quantization" (DQ), a novel framework that optimizes Large Language Model (LLM) inference by tailoring quantization formats, weights, and storage placement specifically for the distinct requirements of prefill and decode phases. By specializing these components, the researchers demonstrate significant improvements in both inference speed—particularly time-to-first-token—and model accuracy across various tasks without increasing overall computational costs.

## Key Takeaways
- Specialized Activation Quantization: The research demonstrates that removing activation quantization specifically during the decode phase improves accuracy on decode-heavy tasks without increasing inference cost, showing that different phases benefit from distinct precision levels.
- Compute-Native Prefill Weights: Training separate prefill weights optimized for computation allows for faster prompt processing compared to standard weight-only inference while maintaining or exceeding accuracy at 2-3 bit decodes across both decode-heavy and prefill-heavy tasks.
- Offloaded Disaggregated Prefill (ODP): To accommodate multiple checkpoints on a single device, the authors developed ODP, which streams weights from SSD during the prefill phase; this method achieved a 1.78x time-to-first-token speedup over weight-only baselines for 8K prompts in llama.cpp using a 27B model.

## Context
As LLM inference costs remain a primary barrier to widespread adoption, optimizing the efficiency of both prompt processing and token generation is critical for practical deployment. Current quantization methods often apply a uniform approach that may not be optimal for the distinct hardware constraints of prefill versus decode phases; this paper addresses that gap by treating them as separate optimization problems.

## Implications
These findings suggest a shift toward heterogeneous inference strategies where model weights are specialized based on their role in the pipeline rather than being uniformly compressed. For practitioners, these techniques could allow much larger models to be served on hardware with limited VRAM by intelligently offloading prefill-specific data from storage during the initial prompt processing phase.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.26333v1)
