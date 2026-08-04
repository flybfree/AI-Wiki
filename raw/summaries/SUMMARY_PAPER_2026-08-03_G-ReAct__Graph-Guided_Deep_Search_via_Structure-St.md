---
title: G-ReAct: Graph-Guided Deep Search via Structure-State Co-Evolution
url: http://arxiv.org/abs/2608.01324v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_15-43-37Z_G_ReAct_Graph_GuidedDeepSearchviaStructure_StateCo.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
G-ReAct proposes a reasoning framework that treats deep search as state evolution over a fixed-topology query graph. It generates high-quality trajectories for supervised fine‑tuning and provides structured guidance at inference time, achieving 52.6% on BrowseComp-ZH and 79.0% on XBench while using only 1.9K generated trajectories.

## Key Takeaways
- The framework explicitly tracks search progress through an evolving graph state, preventing context forgetting.
- It converts textual exploratory search into constrained graph‑guided reasoning, improving consistency over long horizons.
- Fine‑tuning with a small set of trajectories outperforms larger RL datasets on benchmark tasks.

## Context
Deep search is essential for LLMs to answer complex open‑domain questions but suffers from memory loss and drift in long sequences. This work addresses those issues by embedding state management directly into the reasoning process, offering a more reliable alternative to purely sequential methods.

## Implications
The approach can be integrated into existing LLM pipelines without retraining large models, enabling consistent performance across tasks. Practitioners will benefit from inference‑time guidance that boosts accuracy with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01324v1)
