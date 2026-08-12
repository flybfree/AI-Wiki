---
title: Withholding the Completing Chunk: Deterministic Pair-Completion Guardrails for Streaming LLM Output
url: http://arxiv.org/abs/2608.10279v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_22-20-26Z_WithholdingtheCompletingChunk_DeterministicPair_Co.md
generated_at: 2026-08-11 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces deterministic pair-completion guardrails to prevent unsafe streaming outputs from LLMs by withholding the first chunk that completes a predefined pair of lexical predicates. Experiments across multiple signature families and chunk sizes show that this construction reliably blocks every configured pair while avoiding false positives on safe responses.

## Key Takeaways
- The system scans only the accumulated prefix before each release, withholding the chunk where both predicates become observable, which ensures exact detection at the release boundary.
- Full-prefix scanning detects all pairs in a 512‑character window but loses precision compared to pair completion, catching 96 of 128 unsafe responses versus 38 with chunk‑local scanning.
- Fixed pairs flagged zero human safe responses and zero jury unsafe responses, confirming the method’s narrow rather than general harm coverage.

## Context
Streaming language models must balance real‑time moderation with computational cost, as full buffering can delay releases. Traditional approaches either scan entire text or rely on coarse semantic classifiers that may miss subtle hazards. This work demonstrates a lightweight deterministic guard that fits within streaming pipelines without sacrificing safety.

## Implications
For developers deploying LLM chatbots, the pair‑completion guard offers a precise release‑boundary backstop that can be integrated with existing moderation stacks. Its narrow scope means it should complement rather than replace semantic classifiers, guiding industry standards toward hybrid safety architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10279v1)
