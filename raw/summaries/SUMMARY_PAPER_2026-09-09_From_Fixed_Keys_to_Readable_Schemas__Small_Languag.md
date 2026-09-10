---
title: From Fixed Keys to Readable Schemas: Small Language Models for Vehicle Agent Function Calls
url: http://arxiv.org/abs/2609.09476v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_21-46-35Z_FromFixedKeystoReadableSchemas_SmallLanguageModels.md
generated_at: 2026-09-09 20:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how small language models can be used to convert natural‑language requests into vehicle function calls under tight memory and latency limits. It compares two representation strategies – functional tokens versus schema‑in‑prompt – across a benchmark of 9,822 examples and four SLMs, finding that performance plateaus at modest sizes while schema generalization improves with scale.

## Key Takeaways
- Functional tokens restrict inference to functions known during training, leading to zero accuracy on held‑out functions.
- Schema‑in‑prompt enables generalization but incurs longer prompts and higher latency as context grows.
- The 0.6B model achieves the best overall performance, showing that function‑surface representation matters more than raw model scale.

## Context
Vehicle assistants must handle diverse user commands efficiently without cloud reliance, a challenge for on‑device AI. Recent work shows that model size alone does not guarantee robust behavior; how functions are exposed to the model is equally critical. This study contributes a systematic benchmark and analysis of function representation in SLM deployment.

## Implications
For automotive AI developers, choosing between compact tokens or schema prompts shapes both capability and failure modes. Practitioners can balance latency with generalization by selecting appropriate function‑surface designs rather than chasing larger models alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09476v1)
