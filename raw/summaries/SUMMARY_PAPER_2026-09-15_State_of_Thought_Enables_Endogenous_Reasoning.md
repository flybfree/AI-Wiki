---
title: State of Thought Enables Endogenous Reasoning
url: http://arxiv.org/abs/2609.16055v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-13_05-55-03Z_StateofThoughtEnablesEndogenousReasoning.md
generated_at: 2026-09-15 20:32
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces State of Thought (SoT), a novel reasoning paradigm that shifts Large Language Model inference from externally controlled, token-by-token chains to an endogenous process governed by the model's internal state. By extracting a compact dynamics-geometric representation and employing a lightweight controller on frozen backbones, SoT dynamically selects relevant historical evidence based on the current reasoning context. This approach consistently boosts accuracy across diverse reasoning tasks while significantly cutting computational overhead and latency.

## Key Takeaways
- SoT replaces rigid external control mechanisms with an endogenous framework where a 582-parameter controller leverages frozen LLM backbones to dynamically activate historically relevant reasoning support, effectively framing inference as a state-conditioned process over evidence rather than a fixed token sequence.
- Empirical evaluations across three LLM architectures and sixteen datasets demonstrate substantial performance gains, including 1.34x improvements in quantitative tasks, 1.62x in general reasoning, 1.76x in symbolic-and-code domains, and 2.51x in long-context scenarios, all while reducing generated tokens by over 62% and end-to-end latency by nearly 45%.
- The methodology extends effectively to Vision-Language Models, yielding a 3.8-point accuracy increase with 74.9% fewer completion tokens compared to search-based baselines, and maintains robust performance under resource-constrained settings while achieving high trajectory-judging agreement across multiple API models.

## Context
Test-time compute has become a critical lever for enhancing LLM capabilities, yet current paradigms are bottlenecked by rigid external control structures that hinder scalability and adaptability. This research addresses a fundamental gap in dynamic reasoning architectures by demonstrating how internal state dynamics can be harnessed to guide inference efficiently. The work aligns with the broader AI community's push toward

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.16055v1)
