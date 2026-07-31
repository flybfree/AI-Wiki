---
title: Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B
url: http://arxiv.org/abs/2607.28576v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-38-23Z_SampleMore_ReflectLess_Self_RefineandReflexionLose.md
generated_at: 2026-07-30 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether self-refining language models outperform simple repeated sampling when token budgets are equal, using open models from 1.5B to 7B parameters on math benchmarks. It finds no reliable advantage of reflection methods over baseline sampling, with some methods even worse. The best approach is to sample eight times and pick the most common answer.

## Key Takeaways
- Repeated sampling often outperforms self-refine and reflexion methods at equal token cost because generating more text does not guarantee better accuracy.
- Self-inspection techniques such as reflection cause models to generate significantly more tokens without improving performance, especially on 7B models where gains vanish.
- The optimal strategy is to use Best-of-N with eight samples rather than letting the model self-correct, which beats reflection by a small margin.

## Context
This work addresses a common assumption in AI research that introspection improves output quality, but empirical evidence shows token efficiency is paramount. The study provides rigorous statistical tests and open data for reproducibility, highlighting the need to prioritize cost-effective methods over complex reasoning loops.

## Implications
For practitioners, this suggests abandoning costly self-reflection pipelines in favor of simple sampling strategies when token budgets are limited. Researchers should focus on models that generate concise answers rather than those that spend tokens on internal critique. The findings guide resource allocation and model selection in real-world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28576v1)
