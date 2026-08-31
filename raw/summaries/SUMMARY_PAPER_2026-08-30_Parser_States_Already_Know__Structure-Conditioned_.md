---
title: Parser States Already Know: Structure-Conditioned KV Persistence for Structured Generation
url: http://arxiv.org/abs/2608.28276v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_12-38-56Z_ParserStatesAlreadyKnow_Structure_ConditionedKVPer.md
generated_at: 2026-08-30 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PASK, a parser-aware KV persistence method that improves structured generation in LLMs by using task-sensitive signals. It boosts performance on JSON and SQL tasks with 17.39% higher accuracy and better throughput.

## Key Takeaways
- PASK converts parser-derived structure into layer-group-specific KV decisions to protect critical schema elements.
- The offline calibration creates a persistence policy that limits online attention distortion while preserving necessary signals.
- Under a 0.33 total KV budget, PASK outperforms compressed baselines and reduces GPU memory usage.

## Context
Structured generation is essential for LLM agents handling JSON, SQL, and function calls where errors are costly. Current compression techniques ignore the structural risk, leading to higher failure rates.

## Implications
This approach enables more reliable agent behavior with minimal resource cost, encouraging adoption of structured output in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28276v1)
