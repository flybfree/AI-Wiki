---
title: CoLT-Drive: Counterfactual Long-Tail Benchmarking and Knowledge-Preserving Adaptation for Driving Affordance Prediction
url: http://arxiv.org/abs/2609.00242v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-44-30Z_CoLT_Drive_CounterfactualLong_TailBenchmarkingandK.md
generated_at: 2026-09-01 22:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoLT-Drive, a counterfactual long-tail benchmark for autonomous driving affordance prediction, and KPA, a knowledge-preserving adaptation framework that improves rare-object handling while keeping pretrained model knowledge. Experiments show KPA reaches 60.8% pair accuracy on the benchmark versus 50.3% baseline.

## Key Takeaways
- CoLT-Drive measures whether models correctly infer high-level action pairs when rare objects appear in fixed scenes, focusing on decision-critical affordance prediction rather than simple object recognition.
- KPA combines structured prompting, SLERP expert merging and RegMoE to allocate adaptation capacity per driving regime while preserving open-world knowledge.
- The framework achieves 60.8% pair accuracy on CoLT-Drive, outperforming pretrained Qwen3-VL-2B (50.3%) and LoRA SFT (32.4%), yet maintains in-domain performance.

## Context
Autonomous driving systems face long-tail failures where rare objects cause incorrect action predictions, a problem beyond rare-object recognition. This work addresses the need for benchmarks that evaluate decision-level affordance prediction and lightweight adaptation methods that retain large model knowledge.

## Implications
The CoLT-Drive benchmark provides a standardized way to assess drive affordance prediction across diverse rare scenarios, guiding research on robust and adaptable vision-language models. Practitioners can leverage KPA to fine‑tune small VLMs without sacrificing general knowledge, accelerating deployment of safe autonomous driving solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00242v1)
