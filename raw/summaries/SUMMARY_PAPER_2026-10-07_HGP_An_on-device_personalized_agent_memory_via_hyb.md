---
title: HGP:An on-device personalized agent memory via hybrid graph storage
url: http://arxiv.org/abs/2610.10071v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_13-37-38Z_HGP_Anon_devicepersonalizedagentmemoryviahybridgra.md
generated_at: 2026-10-07 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HGP is a hybrid graph memory framework designed to address the challenges of personalized, on-device LLM agent interactions by replacing single-vector memory representations with structured graph-based storage for episodic, semantic, and procedural memories. The framework introduces a lightweight self-enhancement classifier that routes personalized memories efficiently, reducing reliance on large-model calls and enabling practical on-device deployment. Experiments demonstrate a significant performance improvement, with HGP achieving an S-score of 35.58 on the PAL-Set solution selection benchmark, surpassing the strongest baseline by nearly 7 points.

## Key Takeaways
- Existing memory mechanisms for LLM agents rely on single-vector representations that blur critical type distinctions and relational structures among heterogeneous, multi-typed, and implicitly constrained long-term interaction traces, leading to inaccurate routing and retrieval especially in on-device settings where personalization is essential.
- HGP constructs three distinct graph-based memory types—episodic, semantic, and procedural—while also extracting working memory as a state trajectory to capture the agent's current state and implicit constraints, ensuring reliable decision-making across personalized interactive tasks.
- The lightweight self-enhancement classifier serves a dual purpose: it enables personalized memory routing without requiring expensive large-model inference calls, thereby making on-device deployment feasible, while the graph storage architecture supports accurate retrieval and incremental refinement of user profiles over time.

## Context
The broader challenge in LLM-based agent systems is managing long-term, heterogeneous interaction traces that span multiple memory types and carry implicit constraints, particularly when agents must operate on-device with limited computational resources. Most prior approaches flatten these complex traces into single-vector embeddings, losing the relational and categorical structure needed for accurate personalization. HGP addresses this gap by introducing a structured, graph-based alternative that preserves type distinctions and relational semantics, positioning itself within the growing research effort to make agentic memory systems both efficient and expressive.

## Implications
For practitioners building on-device personal assistants and edge-deployed agents, HGP offers a practical path toward accurate personalized memory without the latency and cost overhead of repeated large-model inference calls, making it viable for resource-constrained environments. For the research community, the framework demonstrates that graph-structured memory representations can meaningfully outperform vector-based baselines in solution selection tasks, suggesting that future agent memory architectures should prioritize relational and type-aware storage over monolithic embeddings. The incremental user profile refinement capability also points toward more adaptive, privacy-preserving personalization pipelines for consumer-facing AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10071v1)
