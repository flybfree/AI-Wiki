---
title: CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity
url: http://arxiv.org/abs/2608.07460v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_17-55-48Z_CreativeInstruct_ScalablyTeachingLLMstoBalanceQual.md
generated_at: 2026-08-09 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
CreativeInstruct is a scalable instruction‑tuning approach that teaches large language models to generate outputs that combine the quality of post‑training and the creativity of base models. The method injects special [StartCreativity] spans to bias generation toward creative content while preserving overall quality, and it uses a graph edit distance metric to measure narrative diversity. On narrative tasks CreativeInstruct matches or exceeds multi‑model baselines without sacrificing performance.

## Key Takeaways
- CreativeInstruct learns to inject [StartCreativity] spans that steer the model toward more creative outputs while keeping the quality of post‑trained models, enabling balanced generation.
- The structural diversity metric based on graph edit distance captures narrative level variation beyond lexical and semantic measures, revealing deeper story complexity.
- Human evaluation shows CreativeInstruct generations are rated as more creative than those from post‑trained LLMs in 70.3% of cases.

## Context
The field is moving toward models that can produce high‑quality yet diverse content for applications like reinforcement learning where creativity drives reward shaping. Traditional instruction tuning often reduces diversity, limiting usefulness in tasks requiring originality. This work addresses the trade‑off by providing a method that preserves both quality and variety at scale.

## Implications
Practitioners can deploy CreativeInstruct checkpoints to improve RL performance on benchmarks such as AMC and MATH without needing multiple models or extra inference complexity. The approach offers a practical way to inject creativity into existing LLM pipelines, opening new avenues for creative AI research and commercial applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07460v1)
