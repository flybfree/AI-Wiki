---
title: MEMO: Multimodal Evidence Memory Organization for Long-Horizon LLM Agents
url: http://arxiv.org/abs/2609.07471v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_13-24-40Z_MEMO_MultimodalEvidenceMemoryOrganizationforLong_H.md
generated_at: 2026-09-08 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MEMO, a multimodal evidence memory organization method for long‑running LLM agents that balances retrieval and presentation within limited context budgets. It combines text and visual carriers to store selected evidence efficiently. Evaluation on four benchmarks shows reduced token usage and improved downstream performance.

## Key Takeaways
- MEMO selects relevant memory blocks using an extractor and creates units with source information and presentation requirements.
- A query‑conditioned manager assigns each unit to textual, visual, or dual‑channel carriers and chooses a layout matching the evidence structure.
- The deterministic module generates both textual packages and visual pages from the selected units.

## Context
Long‑running LLM agents face challenges in storing interaction histories beyond a single context window. Traditional memory solutions either use text with uniform token cost or images that compress details, limiting efficiency.

## Implications
Memo’s multimodal approach offers scalable memory strategies for complex agent tasks. Practitioners can reduce latency and improve accuracy by organizing evidence adaptively within tight resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07471v1)
