---
title: An Exact Generate - Transform Decomposition of Small-LLM Team Scaling Across Orchestration Architectures
url: http://arxiv.org/abs/2609.36104v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_18-40-39Z_AnExactGenerate_TransformDecompositionofSmall_LLMT.md
generated_at: 2026-09-29 20:47
model: qwen3.6-35b-a3b
---

## Summary
This study evaluates the impact of scaling small language model teams across eight orchestration architectures to determine if increased collaboration enhances accuracy and identifies optimal structural configurations. By testing instruction-tuned 7-9B models on arithmetic, multiple-choice, and code benchmarks up to 30 calls, the authors find that performance improvements are highly task-dependent rather than uniform. The research introduces an exact generate-transform decomposition to explain why some architectures excel at converting candidate coverage into accuracy for specific tasks while failing in others.

## Key Takeaways
- Accuracy gains from team scaling vary drastically by domain; arithmetic benchmarks like GSM8K and GSMHard show improvements of up to 17 points when scaling calls from three to thirty, whereas multiple-choice datasets such as ARC, GPQA, and MMLU improve by at most four points regardless of the architecture used.
- The Proposer-Critic architecture achieves the steepest scaling for arithmetic tasks and outperforms all others at maximum budgets, yet it ranks among the weakest performers on other benchmarks, demonstrating that no single orchestration method wins across all task types.
- An exact generate-transform decomposition partitions workflow accuracy into coverage dividends and transformation efficiency; arithmetic benefits from coverage headroom converted by critics, while code generation suffers vanishing recovery, and token costs can vary by 2

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.36104v1)
