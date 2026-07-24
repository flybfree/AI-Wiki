---
title: From Dependency to Compositionality: A Neurosymbolic Lifting of LLM Outputs via Combinatory Categorial Grammar
url: http://arxiv.org/abs/2607.18961v2
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_10-52-10Z_FromDependencytoCompositionality_ANeurosymbolicLif.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper argues that the incremental, prefix-driven nature of LLM generation aligns with the processing model of Combinatory Categorial Grammar (CCG). By lifting LLM outputs into typed compositional derivations, the authors demonstrate a principled way to reconstruct grammatically structured text and formal languages. The approach yields two consequences: a Curry‑Howard correspondence that maps type systems across natural language, programming, logic, and query languages, and a dual‑layer checking system that flags structural errors and hallucinated content early.

## Key Takeaways
- LLM outputs can be reconstructed as incremental CCG derivations without assuming internal grammar implementation.  
- The lifting creates a Curry‑Howard correspondence linking the type systems of natural language, programming languages like Solidity, description logic, OWL, and SQL to a fixed architectural framework.  
- A two‑layer checking mechanism is introduced: compositional checks for structural failures and content checks against external knowledge sources.

## Context
Generative AI models are praised for fluency yet criticized for lacking transparent grammar. CCG offers an alternative view that emphasizes incremental, type‑completing processes, which have long been used in formal language theory. This paper bridges the gap by showing how LLM generation mirrors these formal mechanisms, enriching our understanding of both natural language and computational languages.

## Implications
For researchers, this framework provides a systematic method to audit AI outputs for grammatical correctness and factual fidelity. For industry practitioners, it enables early detection of hallucinations in generated code or queries, improving reliability in high‑stakes applications such as smart contracts and semantic reasoning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18961v2)
