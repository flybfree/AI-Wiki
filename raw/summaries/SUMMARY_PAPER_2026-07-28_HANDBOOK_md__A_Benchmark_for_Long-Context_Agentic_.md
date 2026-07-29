---
title: HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following
url: http://arxiv.org/abs/2607.25398v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_07-58-07Z_HANDBOOK_md_ABenchmarkforLong_ContextAgenticInstru.md
generated_at: 2026-07-28 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HANDBOOK.md, a benchmark that evaluates long-context agentic instruction following by placing language models in realistic company environments governed by lengthy standard operating procedures. It tests how agents adhere to binding policies over extended tool-use horizons and finds most frontier models fail to meet deterministic rubrics.

## Key Takeaways
- The benchmark consists of 65 tasks with unique handbook modifications, ensuring no two share a policy and preventing memorization.
- Evaluation is fully deterministic using 824 programmatic criteria; only the best model passes about one-third of trials while most frontier models are below 25%.
- Common failure modes include agents overriding policies for plausible in‑environment requests or losing rule details over long horizons.

## Context
Long-context instruction following remains a critical challenge as AI agents must respect complex, multi-page policies. Existing benchmarks focus on task completion rather than policy adherence, highlighting a gap in measuring real‑world compliance.

## Implications
For industry practitioners, HANDBOOK.md provides a standardized test to gauge whether models can reliably follow detailed SOPs, informing deployment decisions and prompting research into better long‑context reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25398v1)
