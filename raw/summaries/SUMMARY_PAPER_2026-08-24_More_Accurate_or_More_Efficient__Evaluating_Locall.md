---
title: More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning
url: http://arxiv.org/abs/2608.22048v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_17-24-28Z_MoreAccurateorMoreEfficient_EvaluatingLocallyDeplo.md
generated_at: 2026-08-24 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a rigorous evaluation framework for locally hosted compact open‑weight language models when solving mathematical reasoning tasks. The study compares three 4‑billion‑parameter models—Gemma3:4b, Phi3:3.8b, and Qwen3:4b—across diverse math datasets while measuring accuracy, runtime, energy consumption, and output token usage. Results show that no single model is universally superior; each excels in specific areas but also incurs higher computational costs.

## Key Takeaways
- Accuracy varies by dataset and model, with Qwen3:4b leading on two domains yet consuming three times more energy per correct answer than Gemma3:4b.
- Gemma3:4b achieves the highest efficiency, delivering roughly three times as many correct answers per watt‑hour while generating fewer tokens.
- Phi3:3.8b shows low extraction‑failure rates suggesting incorrect answers rather than unparsed output, though prompt format effects remain a potential confound.

## Context
The rapid deployment of large language models on edge devices raises concerns about privacy, cost, and sustainability. Existing evaluations often prioritize accuracy alone, ignoring the environmental impact and resource efficiency required for real‑world local inference. This work bridges that gap by quantifying both performance and operational costs under controlled conditions.

## Implications
For practitioners selecting a model for offline math assistance, efficiency metrics such as answers per watt‑hour are as critical as raw accuracy scores. The findings suggest that trade‑off analysis between speed, energy use, and correctness is essential to align AI deployment with practical constraints in education and industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22048v1)
