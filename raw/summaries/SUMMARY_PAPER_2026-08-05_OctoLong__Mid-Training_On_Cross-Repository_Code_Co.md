---
title: OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling
url: http://arxiv.org/abs/2608.05141v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-58-15Z_OctoLong_Mid_TrainingOnCross_RepositoryCodeContext.md
generated_at: 2026-08-05 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OctoLong, a pipeline that extends code context retrieval to millions of tokens by instrumenting AST parsers and language servers. It trains long‑context open models on a mixture of retrieved code contexts followed by instruction tuning. The results show that replacing 12 % of traditional data with OctoLong improves long‑range retrieval, state tracking, repository understanding, and downstream agentic tasks while also enhancing API usage in short‑context coding scenarios.

## Key Takeaways
- Mid‑training context extension using OctoLong yields substantial gains in long‑range retrieval and long‑term state tracking.  
- The pipeline enables dependency‑rich code contexts of millions of tokens, crucial for large models up to 14 B parameters.  
- Downstream agentic tasks improve, while API usage in short‑context coding also benefits.

## Context
As language models push context lengths beyond tens of thousands of tokens, efficient retrieval of relevant code snippets becomes a bottleneck. This work demonstrates that augmenting standard corpora with structured, recursive code references can unlock capabilities previously limited by data scarcity.

## Implications
For developers and AI researchers, OctoLong offers a practical method to train models on real‑world repository structures without massive manual annotation. It signals a shift toward embedding domain‑specific retrieval mechanisms directly into model training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05141v1)
