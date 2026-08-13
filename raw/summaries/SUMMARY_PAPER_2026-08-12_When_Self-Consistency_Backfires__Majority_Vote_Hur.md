---
title: When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems for Small LLMs
url: http://arxiv.org/abs/2608.11403v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_20-08-51Z_WhenSelf_ConsistencyBackfires_MajorityVoteHurtsthe.md
generated_at: 2026-08-12 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how majority voting in self‑consistency backfires on small instruction‑tuned language models when solving hard science questions, showing a significant drop in accuracy across many problems.

## Key Takeaways
- 56.6 % of the 198 Diamond benchmark questions suffer reduced per‑problem accuracy for Qwen2.5‑7B and 65.7 % for Llama‑3‑8B due to majority voting, with both models outperforming a near‑chance baseline.  
- Confidence does not reliably track correctness; in the highest‑agreement bin the plurality answer is correct only about half the time for Qwen, while that same bin is less accurate than its lowest‑agreement bin.  
- No verifier‑free gate (plurality‑agreement or token‑entropy) can surpass fixed‑budget voting at N = 64, indicating the mechanism itself limits improvement.

## Context
Self‑consistency is a popular method to stretch inference budgets by sampling multiple reasoning chains and selecting the majority answer. This study reveals that for small models with limited reasoning capacity, the approach can actually degrade performance on challenging scientific tasks.

## Implications
Practitioners should reconsider deploying self‑consistency on these model sizes and explore alternative verification strategies; the field must also test reasoning‑native models separately to understand their behavior under similar constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11403v1)
