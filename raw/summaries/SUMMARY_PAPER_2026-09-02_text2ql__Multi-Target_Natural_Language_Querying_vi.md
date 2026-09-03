---
title: text2ql: Multi-Target Natural Language Querying via a Language-Agnostic Intermediate Representation
url: http://arxiv.org/abs/2609.02115v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_05-09-51Z_text2ql_Multi_TargetNaturalLanguageQueryingviaaLan.md
generated_at: 2026-09-02 20:50
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces text2ql, a Python framework that enables multi‑target natural language querying using a language‑agnostic Intermediate Representation (QueryIR). It combines deterministic and LLM‑backed modes to generate queries for both SQL and GraphQL while providing runtime confidence scores. The deterministic mode achieves 100 % execution accuracy with zero parse errors, whereas the LLM‑backed mode reaches 62–70 % exact match on benchmark data.

## Key Takeaways
- A single seven‑stage detection pipeline serves both SQL and GraphQL targets, eliminating separate pipelines for each target language.  
- The framework delivers a runtime confidence score between 0.15 and 0.97 computed from an additive signal model, allowing users to filter out low‑confidence outputs.  
- Schema‑aware prompting is the most impactful improvement, raising exact‑match accuracy by 18.4 percentage points over a schema‑free baseline.

## Context
Current natural language database interfaces rely heavily on large language models that generate queries at query time, leading to latency and cost issues. Deterministic approaches often lack adaptability across different data schemas or target APIs. This work bridges the gap by providing a unified representation and confidence‑driven generation, offering a more reliable alternative to LLM‑only solutions.

## Implications
For practitioners developing AI‑enhanced query tools, text2ql reduces operational risk through deterministic fallback modes and quantifiable confidence metrics. In industry settings where query accuracy directly impacts data integrity, the framework’s schema‑aware prompting boosts performance without increasing API costs. The open‑source release under Apache 2.0 encourages broader adoption across research and commercial applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02115v1)
