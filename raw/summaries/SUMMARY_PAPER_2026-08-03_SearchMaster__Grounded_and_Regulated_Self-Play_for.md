---
title: SearchMaster: Grounded and Regulated Self-Play for Search Agents
url: http://arxiv.org/abs/2608.01822v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-29-11Z_SearchMaster_GroundedandRegulatedSelf_PlayforSearc.md
generated_at: 2026-08-03 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SearchMaster, a self-play framework that trains an LLM search agent using only locally generated tasks and rollouts. It overcomes issues like pseudo multi-hop questions and shallow browsing by applying three controls. Across benchmarks it boosts Qwen3.5-9B accuracy from 38.19% to 51.52%, a 30.1‑point gain on BrowseComp‑Plus.

## Key Takeaways
- The Evidence‑Chain Generator creates explicit cross‑document evidence chains, reducing pseudo multi‑hop questions that mislead the model.
- The Search‑Depth Reward evaluates task difficulty based on search depth rather than success rate, ensuring retained tasks are genuinely challenging.
- The Over‑Opening Penalty discourages excessive document opening, preventing shallow browsing and encouraging focused information gathering.

## Context
Self‑play is a promising way to generate training data for large language models without relying on human QA pairs or expert demonstrations. However, unregulated self‑generated data can produce biased or ineffective tasks that degrade performance. This work demonstrates how systematic controls can make self‑play viable for search agents.

## Implications
Practitioners can now train search agents using only internal mechanisms, lowering dependence on costly external datasets. The approach may become a standard method for scaling LLM capabilities in information retrieval and web browsing applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01822v1)
