---
title: OEIS Open: How many conjectures can language models turn into theorems?
url: http://arxiv.org/abs/2608.11941v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_11-28-36Z_OEISOpen_Howmanyconjecturescanlanguagemodelsturnin.md
generated_at: 2026-08-12 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces OEIS Open, a benchmark that tests whether language models can solve open mathematical conjectures using only minimal tools and a limited budget. The authors report that LMs resolve 147 of 492 conjectures at $50 per attempt, achieving 30% accuracy on the full set, while a cheaper subset yields 44% with $200 per attempt.  

## Key Takeaways  
- The benchmark demonstrates that generic language models can solve many open conjectures when given only basic computational tools and a modest budget.  
- Evaluation is secured against cheating by using formalized Lean statements and open-source code, ensuring results reflect genuine reasoning.  
- Providing LMs with the full mathematics literature does not improve performance on this specific task.  

## Context  
This work addresses the challenge of evaluating autonomous problem-solving in AI beyond narrow tasks. By focusing on unsolved conjectures, it tests whether models can perform mathematical discovery without external assistance or large datasets.  

## Implications  
The findings suggest that LMs may be viable for low‑cost automated research, opening possibilities for cost‑effective proof generation and hypothesis testing. Practitioners could leverage such benchmarks to benchmark model capabilities in real‑world scientific workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11941v1)
