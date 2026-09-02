---
title: How Correct Is Your Answer? A Semantic Correctness Framework for Open QA Evaluation
url: http://arxiv.org/abs/2609.01369v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-06-39Z_HowCorrectIsYourAnswer_ASemanticCorrectnessFramewo.md
generated_at: 2026-09-01 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a semantic correctness taxonomy for open-ended QA answers and evaluates it with new benchmarks. It introduces CAP-Correctness, an 8.8k example dataset, and CAP-Statements, converting pairs into NLI statements. The reference-based metric CAP outperforms existing methods while respecting the taxonomy ordering.

## Key Takeaways
- The semantic correctness taxonomy classifies open-ended answers into eight ordered classes that differentiate verbose-but-correct responses from those containing hallucinations or contradictions.
- CAP-Correctness provides a large, diverse benchmark spanning multiple QA datasets to test these classifications in practice.
- CAP (Context-Aware Precision) uses bidirectional NLI on statement pairs and respects the taxonomy’s ordering, achieving better performance than prior baselines.

## Context
Open-ended question answering is central to evaluating language model capabilities beyond fixed answer formats. Current evaluation methods often fail to capture subtle correctness issues such as overgeneration or premise endorsement, limiting reliable assessment of LLMs.

## Implications
This framework offers practitioners a more nuanced way to judge model outputs, supporting better alignment with user expectations. It also sets a standard for benchmarking that respects semantic quality rather than surface similarity alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01369v1)
