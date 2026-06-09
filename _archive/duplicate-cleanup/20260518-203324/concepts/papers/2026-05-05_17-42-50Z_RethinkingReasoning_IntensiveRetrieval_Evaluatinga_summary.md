# Summary: 2026-05-05_17-42-50Z_RethinkingReasoning_IntensiveRetrieval_Evaluatinga.md
Saved: 2026-05-07 22:08
Source: 2026-05-05_17-42-50Z_RethinkingReasoning_IntensiveRetrieval_Evaluatinga.md
Model: None

---

## Summary
This paper argues that reasoning-intensive retrieval should be evaluated as an evidence-construction problem, not just a relevance-ranking problem. It introduces a richer benchmark and a synthetic training corpus designed to improve retrievers in agentic search settings where multiple complementary passages matter.

## Key Takeaways
- Introduces BRIGHT-Pro with multi-aspect gold evidence and both static and agentic evaluation.
- Builds RTriever-Synth with complementary positives and positive-conditioned hard negatives.
- Fine-tunes RTriever-4B from Qwen3-Embedding-4B using LoRA.
- Shows that agentic, aspect-aware evaluation reveals behaviors hidden by standard metrics.

## Context
The work targets retrieval for iterative search-and-synthesis agents, where a retriever must support downstream reasoning rather than merely match topical similarity. It critiques existing benchmarks for narrow gold sets and single-passage relevance objectives.

## Implications
The findings suggest retriever training and evaluation should account for evidence portfolios and search trajectories. This can improve the robustness of agentic search systems and provide a stronger foundation for reasoning-oriented retrieval models.

## Original Reference
- Title: Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems
- Authors: Yilun Zhao, Jinbiao Wei, Tingyu Song, Siyue Zhang, Chen Zhao, Arman Cohan
- URL: http://arxiv.org/abs/2605.04018v1
- Published: 2026-05-05T17:42:50Z