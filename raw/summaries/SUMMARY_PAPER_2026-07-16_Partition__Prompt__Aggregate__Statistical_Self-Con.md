---
title: Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models
url: http://arxiv.org/abs/2607.15277v1
type: paper-summary
date: 2026-07-16
source_paper: 2026-07-16_17-59-31Z_Partition_Prompt_Aggregate_StatisticalSelf_Consist.md
generated_at: 2026-07-16 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large language model estimates satisfy the law of total probability by partitioning populations into subpopulations, prompting models with descriptions of each group, aggregating their outputs, and comparing results to direct population-level predictions. Across multiple domains and frontier models, it finds systematic violations of statistical self‑consistency, revealing a “macro fallacy” where fine‑grained subpopulation estimates often align better with human references than the aggregated population estimate.

## Key Takeaways
- The law of total probability is frequently violated: aggregating subpopulation responses does not reproduce the correct marginal distribution.  
- A macro fallacy emerges: more detailed persona prompts yield outputs that are closer to human ground truth than coarse‑grained population prompts.  
- Models retain relevant knowledge about individual groups but fail to reliably propagate it into higher‑level aggregates.

## Context
Statistical self‑consistency provides a reference‑free metric for evaluating LLMs, highlighting gaps between model behavior and fundamental probability laws that are currently overlooked in standard benchmarking. This work underscores the need for consistency checks beyond accuracy scores.

## Implications
For practitioners, this suggests that improving aggregation mechanisms may be as important as enhancing individual prompt design to achieve reliable LLM performance. The findings could guide research into more robust prompting strategies that preserve subpopulation information during inference.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15277v1)
