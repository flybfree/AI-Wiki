---
title: Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems
url: http://arxiv.org/abs/2609.00237v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-42-57Z_LearningWhattoRetain_Gated_MemoryRoutingforEfficie.md
generated_at: 2026-09-01 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Gated-Memory Routing, a method that conditions LLM agent decisions on a compact learned execution memory to improve reasoning accuracy and reduce cost. Experiments show it beats the strongest baseline by 2.44 points while cutting HumanEval inference time by 31.9%. The approach balances effective collaboration with efficient resource use.

## Key Takeaways
- Gated-Memory Routing uses a learned Memory Write Gate that only commits non-redundant reasoning steps, eliminating unnecessary context accumulation.
- A Retrieval Gate selects a compact subset of the memory for each agent decision, ensuring decisions condition on clean and informative state.
- The Adaptive Halting Controller stops execution once sufficient evidence is stored in the memory, preventing over-processing.

## Context
Multi-agent LLM systems must dynamically orchestrate agents to handle complex tasks efficiently. Traditional routing methods either ignore intermediate progress or process all history, leading to high computational overhead. This paper addresses that gap by proposing a compact, adaptive memory mechanism.

## Implications
The results demonstrate that accuracy and efficiency can be jointly improved in multi-agent reasoning pipelines. Practitioners can adopt Gated-Memory Routing to reduce inference costs without sacrificing performance, making large-scale collaborative AI more scalable and cost-effective.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00237v1)
