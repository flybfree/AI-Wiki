---
title: How reliable are LLMs when it comes to playing dice?
url: http://arxiv.org/abs/2606.07515v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-05_17-59-42Z_HowreliableareLLMswhenitcomestoplayingdice.md
generated_at: 2026-06-11 10:54
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how reliable large language models are for discrete probability problems, comparing standard exercises with counterintuitive ones and testing both with and without Chain-of-Thought prompting. It finds that LLMs achieve high accuracy on routine tasks but lower performance on more challenging cases, and that token bias can further degrade results.

## Key Takeaways
- Models reach about 96% accuracy on routine probability exercises but drop to around 59% on counterintuitive ones.
- Performance declines sharply when canonical formulations are replaced with disguised variants, dropping by over 20%.
- Embedding misleading suggestions in the prompt can reduce performance by up to 34%, indicating no model is immune.

## Context
This study highlights a gap between LLMs' apparent competence and their actual probabilistic reasoning, revealing reliance on surface patterns rather than true understanding. It underscores that current models may fail in subtle probability contexts despite success elsewhere.

## Implications
For practitioners, the findings suggest caution in deploying LLMs for tasks requiring precise quantitative inference without explicit prompting. The research calls for more robust evaluation frameworks to detect such biases and guide safer model integration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.07515v1)
