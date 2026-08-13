---
title: VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies
url: http://arxiv.org/abs/2608.12282v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_17-27-27Z_VAKRA_EvaluatingMulti_HopReasoningAcrossAPIsandRet.md
generated_at: 2026-08-12 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VAKRA, a benchmark that evaluates multi-hop reasoning across structured APIs and document collections under tool-use policies. It tests over 8,000 executable APIs in 62 domains using tasks of varying difficulty, measuring model performance on single‑hop endpoints, compositional API interactions, and policy‑constrained queries. The results show that even top models struggle beyond 70% accuracy as reasoning depth grows.

## Key Takeaways
- Single‑hop endpoint‑style tasks achieve only about 70.4% correct tool calls, indicating limited performance on straightforward queries.
- Multi‑step API interactions drop to roughly 50–51% accuracy, showing a steep decline with increasing compositional complexity.
- Policy‑constrained questions can be answered correctly as low as 2.4%, highlighting severe failures when natural‑language policies block tool use.

## Context
Current AI research often isolates reasoning benchmarks from real‑world API usage, which limits understanding of how models handle multi‑hop interactions in enterprise settings. VAKRA bridges this gap by integrating diverse APIs and policy constraints into a single evaluation suite.

## Implications
For developers deploying large language models as agents, the findings warn that performance degrades sharply beyond simple queries, necessitating better reasoning strategies or policy‑aware design. Practitioners should also monitor entity disambiguation and grounding failures to avoid costly errors in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12282v1)
