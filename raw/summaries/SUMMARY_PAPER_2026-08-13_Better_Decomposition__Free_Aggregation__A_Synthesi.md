---
title: Better Decomposition, Free Aggregation: A Synthesizer-Folding Framework for Multilingual Multi-Hop Question Answering
url: http://arxiv.org/abs/2608.13160v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_12-25-59Z_BetterDecomposition_FreeAggregation_ASynthesizer_F.md
generated_at: 2026-08-13 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Syfer, a synthesizer-folding framework for multilingual multi-hop QA that avoids default translation and greedy decomposition. It achieves competitive accuracy while balancing performance and cost across languages.

## Key Takeaways
- The method defers translation rather than applying it by default, preserving native linguistic information and reducing noise.
- Greedy decomposition is replaced with a format‑constrained decomposer that produces a sub‑question graph in the original language and checks its quality before proceeding.
- When the check fails, an English translation pathway using bilingual alignment is activated only as a fallback.

## Context
Multilingual QA systems often rely on translating documents or queries to align semantics across languages, which can degrade cultural nuance and increase computational load. Current decomposition strategies generate redundant sub‑questions that compound errors during reasoning, leading to poorer final answers.

## Implications
This approach offers a more efficient and culturally aware solution for deploying multilingual QA in real‑world applications where latency and accuracy both matter. Practitioners can adopt Syfer to improve system robustness without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13160v1)
