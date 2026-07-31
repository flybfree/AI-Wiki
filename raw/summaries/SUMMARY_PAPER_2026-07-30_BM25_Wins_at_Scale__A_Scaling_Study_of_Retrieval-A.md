---
title: BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms
url: http://arxiv.org/abs/2607.26497v2
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_05-46-11Z_BM25WinsatScale_AScalingStudyofRetrieval_Augmented.md
generated_at: 2026-07-30 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper conducts a controlled scaling study of retrieval‑augmented generation paradigms across 28 nested corpus sizes. It finds that BM25 becomes the dominant method at larger scales while file‑system agents excel only on tiny shared tiers.

## Key Takeaways
- At the smallest shared tier, the File‑System Agent achieves the highest accuracy but its sequential exploration consumes 39 times more query tokens than BM25 at the bedrock size.
- Around ten million corpus tokens, BM25 overtakes the File‑System Agent and leads all larger shared tiers, with a margin approaching twenty points at full scale.
- Lexical retrieval such as BM25 anchors the low‑cost end of the Pareto frontier without requiring LLM‑based construction.

## Context
This study addresses a longstanding challenge in RAG research by isolating how different retrieval strategies scale with data size, which is essential for reliable system design. The results highlight the importance of benchmarking across multiple scales rather than single‑size evaluations.

## Implications
For practitioners, the finding that lexical retrieval remains a cost‑effective default suggests focusing on scalable ranking models rather than complex agentic search at scale. Researchers should adopt multi‑tiered evaluation protocols to capture these scale‑dependent tradeoffs in future RAG experiments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26497v2)
