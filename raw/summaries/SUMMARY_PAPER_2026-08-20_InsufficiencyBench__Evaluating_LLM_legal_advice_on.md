---
title: InsufficiencyBench: Evaluating LLM legal advice on underspecified user queries
url: http://arxiv.org/abs/2608.20220v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_16-14-47Z_InsufficiencyBench_EvaluatingLLMlegaladviceonunder.md
generated_at: 2026-08-20 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces InsufficiencyBench, a benchmark that evaluates whether legal language models correctly detect when user queries lack legally material information and either request clarification or refrain from answering. Evaluation on 202 items across six domains and 24 jurisdictions shows that no model achieves high performance in identifying missing elements, with the best F2 score of 0.46 and median recall of 0.44. Models either hedge indiscriminately or answer silently under fabricated assumptions.

## Key Takeaways
- The benchmark demonstrates a low ability to recognize insufficient queries, measured by an F2 metric of 0.46, indicating poor performance in identifying missing elements.  
- Median recall is only 0.44, meaning roughly four out of ten deficient queries are not correctly flagged as incomplete.  
- Models tend either to hedge indiscriminately or to answer silently under fabricated presumptions rather than acknowledging the insufficiency.

## Context
Legal AI systems often assume queries arrive fully specified, yet real‑world users frequently omit facts that could materially alter legal outcomes. This work highlights a gap between benchmark performance and practical usability in jurisdictions where incomplete information is common.

## Implications
For practitioners, this suggests current models cannot reliably handle ambiguous or incomplete requests, risking misinformation. The field must develop benchmarks and safeguards to force models to recognize insufficiency before providing advice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20220v1)
