---
title: SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents
url: http://arxiv.org/abs/2608.08055v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_10-42-31Z_SodaMem_Evidence_GroundedTemporalGraphMemoryforLLM.md
generated_at: 2026-08-10 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SodaMem, an evidence-grounded temporal graph memory that stores fact events with provenance and handles updates via SUPERSEDES/CONTRADICTS/UPDATES edges, enabling LLMs to answer questions with citable evidence. On LongMemEval-S it achieves 92.8% accuracy at a cost of about $0.0016 per question using DeepSeek-V4-Flash.

## Key Takeaways
- SodaMem extracts typed FactEvents with mandatory provenance spans, preserving mention time, occurrence time, and validity to support ordered temporal reasoning.
- It persists these events under hybrid lexical-dense indexing and uses SUPERSEDES/CONTRADICTS/UPDATES edges for versioned memory updates.
- The planner-reader loop gathers citable evidence before composing a response, yielding high accuracy with minimal token cost.

## Context
LLM agents must retain factual knowledge over long conversations while providing verifiable answers. Traditional retrieval methods like RAG diaries lack temporal reasoning and provenance tracking, limiting usefulness in multi-session interactions.

## Implications
This work shows that storing structured temporal graphs can improve both accuracy and cost efficiency for LLM agents, encouraging industry adoption of evidence‑grounded memory systems in conversational AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08055v1)
