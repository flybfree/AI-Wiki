---
title: Leak-Resistant Unlearning: A New Benchmark for Evaluating Multi-Hop Reasoning Consistency and Recovery Robustness
url: http://arxiv.org/abs/2608.04519v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_06-53-20Z_Leak_ResistantUnlearning_ANewBenchmarkforEvaluatin.md
generated_at: 2026-08-05 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the Leak-Resistant Unlearning benchmark to evaluate how well large language models remove sensitive knowledge across diverse multi‑hop reasoning paths and survive recovery attacks such as lightweight post‑unlearning adaptation. Experiments on three models, six unlearning methods, and two curated datasets reveal that existing techniques are vulnerable to both leakage through alternative reasoning routes and partial recovery after unlearning. The study also highlights a trade‑off between forgetting quality, robustness, and model utility.

## Key Takeaways
- Knowledge is not isolated; diverse multi‑hop paths can cause knowledge leakage even when the target fact is removed.  
- Unlearning may be fragile because lightweight adaptation techniques can partially recover unlearned information, making static evaluation inadequate.  
- The benchmark demonstrates that current methods suffer from both leakage and recovery issues, exposing a trade‑off among forgetting quality, robustness, and model utility.

## Context
Current LLM unlearning benchmarks focus on single‑hop queries and limited multi‑hop tasks, which does not capture real‑world reasoning complexity. This paper expands the evaluation to include complex reasoning paths and post‑unlearning attacks, addressing a gap in understanding how knowledge removal behaves under realistic conditions.

## Implications
For practitioners, the findings warn that unlearning is not a one‑size‑fits‑all solution; robustness must be balanced with utility loss. Industry adoption of such benchmarks can guide safer deployment of sensitive data removal techniques and improve trust in AI systems handling confidential information.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04519v1)
