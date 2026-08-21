---
title: EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models
url: http://arxiv.org/abs/2608.20055v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_13-52-07Z_EchoCoT_ExtractingHiddenChain_of_ThoughtfromLargeR.md
generated_at: 2026-08-20 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether hidden chain-of-thought traces from large reasoning models can be recovered with high fidelity using API interactions. It introduces EchoCoT, a multi-step attack that extracts these traces and shows strong performance across both open-source and proprietary models. The results demonstrate near-verbatim extraction success rates up to 80% on unseen datasets.

## Key Takeaways
- EchoCoT can achieve up to 66.4% near-verbatim extraction from open-source LRMs, with trace length within 10% of the target and at least 90% token match accuracy.
- The same injection trajectory generalizes to unseen datasets, reaching up to 80% extraction success under identical criteria.
- On frontier proprietary models, extracted CoTs closely align with provider-reported lengths and summaries, indicating a consistent replay surface between tool calls.

## Context
Large reasoning models generate internal chain-of-thought traces that are not exposed directly but can be accessed through API responses. Extracting these hidden traces poses a security risk as it reveals model behavior without the user's knowledge. This work addresses the challenge of reverse-engineering such traces from black-box APIs.

## Implications
If attackers can reliably extract hidden CoTs, they could manipulate reasoning processes or exploit vulnerabilities in proprietary systems. Practitioners must consider protecting internal reasoning artifacts and evaluating API responses for unintended information leakage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20055v1)
