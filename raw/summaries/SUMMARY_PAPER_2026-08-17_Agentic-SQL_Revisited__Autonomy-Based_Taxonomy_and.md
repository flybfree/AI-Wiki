---
title: Agentic-SQL Revisited: Autonomy-Based Taxonomy and Empirical Benchmark Analysis for LLM Text-to-SQL
url: http://arxiv.org/abs/2608.15389v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_19-40-05Z_Agentic_SQLRevisited_Autonomy_BasedTaxonomyandEmpi.md
generated_at: 2026-08-17 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reframes LLM Text‑to‑SQL research as a leaderboard aggregation that organizes performance across an autonomy axis ranging from constrained to reasoning‑internalized generation, providing traceable provenance for each metric. The study demonstrates that Spider’s results transfer unevenly between benchmarks and that autonomy improves robustness at a non‑trivial cost, while CoT supervision mainly benefits Hard and Extra‑Hard queries.

## Key Takeaways
- Spider gains transfer unevenly to BIRD and Spider~2.0, indicating limited generalization across datasets despite similar model sizes.
- Autonomy in generation—moving from simple answer decoding to iterative agentic reasoning—yields robustness but also increases inference latency and resource usage.
- Reasoning internalization sits between answer‑only decoding and externally orchestrated agents, offering a middle ground that balances speed and accuracy.

## Context
The rapid proliferation of LLM backbones and benchmark suites has fragmented Text‑to‑SQL evaluation, making it difficult to compare methods on a common scale. This work addresses that fragmentation by creating a structured leaderboard that captures both model capability and the autonomy level of inference protocols.

## Implications
For researchers, the autonomy axis offers a clear direction for future experiments, guiding trade‑offs between speed and correctness. For practitioners, the released harness enables seamless integration of new methods into the leaderboard, fostering transparent competition and faster progress in LLM Text‑to‑SQL systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15389v1)
