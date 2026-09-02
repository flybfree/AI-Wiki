---
title: It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning
url: http://arxiv.org/abs/2609.00638v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_03-17-02Z_ItTakesTwotoMatch_Co_EvolvingGenerativeRetrieverwi.md
generated_at: 2026-09-01 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoGR, a co-evolving generative retrieval framework that trains LLMs to produce compact keyword sets on both query and item sides for direct matching via inverted index. It replaces downstream retriever with joint optimization of generators using GRPO aligned to F1 metric. On 10 baselines it improves F1 by 10.9% internally and 36.1% on WANDS.

## Key Takeaways
- CoGR jointly optimizes query‑side and item‑side keyword generators with a counterfactual marginal reward, enabling direct matching without a separate retriever.
- The two‑stage pipeline first aligns keywords via supervised fine‑tuning before co‑evolving the generators using GRPO on opposite frozen indexes.
- Experiments show stable co‑evolution and better alignment of query‑item keyword spaces across sparse, dense, and generative datasets.

## Context
Modern search systems rely heavily on LLMs for query expansion but still delegate final matching to traditional retrievers. This work bridges that gap by integrating generation directly into the retrieval representation space, reducing reliance on downstream models.

## Implications
CoGR offers a more efficient pipeline where generation serves as the primary retrieval signal, potentially lowering latency and cost in large‑scale search. Practitioners can adopt this framework to improve F1 scores without overhauling existing infrastructure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00638v1)
