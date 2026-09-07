---
title: Harbor Adapters and Harbor-Index: Infrastructure and a Curated Meta-Dataset for Large-Scale Agentic Evaluation
url: http://arxiv.org/abs/2609.04298v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_16-26-20Z_HarborAdaptersandHarbor_Index_InfrastructureandaCu.md
generated_at: 2026-09-06 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Harbor Adapters, a unified infrastructure that allows evaluation of over 80 agentic benchmarks on arbitrary language models, and presents Harbor-Index, a curated set of 82 challenging tasks selected from those benchmarks. The authors evaluate eight models across fifty‑four benchmarks using Terminus‑2 and three native harnesses, achieving pass rates up to 28 % for the strongest model GPT‑5.5 with Codex.

## Key Takeaways
- Harbor Adapters enable porting of more than 80 existing agentic benchmarks to evaluate any new model through code review and parity experiments.
- The large‑scale evaluation across eight models on fifty‑four benchmarks provides a comprehensive view of capability tiers and failure modes beyond single benchmark results.
- Harbor‑Index is a curated subset of eighty‑two high‑quality tasks that maintains challenge while keeping evaluation affordable, with no configuration exceeding 30 % pass rate.

## Context
Agentic evaluation has become essential as language models are deployed in complex environments where their behavior must be measured across diverse tasks. Traditional benchmarks often require bespoke setups, limiting comparability and scalability. This work addresses those limitations by providing a standardized adapter layer and a manageable curated task suite.

## Implications
For researchers the open‑source adapters and results enable reproducible large‑scale agent testing. For industry practitioners they offer a reliable benchmark to assess model suitability for real‑world deployment without costly custom infrastructure. The findings highlight the importance of both breadth and depth in evaluating language models, guiding future work toward more holistic assessment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04298v1)
