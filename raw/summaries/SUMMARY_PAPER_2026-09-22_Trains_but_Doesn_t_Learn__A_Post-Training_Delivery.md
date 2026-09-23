---
title: Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers
url: http://arxiv.org/abs/2609.25237v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-21_18-01-24Z_TrainsbutDoesn_tLearn_APost_TrainingDeliveryBenchm.md
generated_at: 2026-09-22 20:07
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces a new benchmark designed to evaluate Large Language Model (LLM) agents acting as Forward-Deployed Engineers (FDEs) within the context of Post-Training as a Service (PTaaS). It specifically addresses the "Trains but Doesn't Learn" (TBDL) phenomenon, where an agent might successfully navigate training procedures and minimize loss metrics without actually improving the model's underlying capabilities or performance.

## Key Takeaways
- Shift from Metric Improvement to Reliable Delivery: The authors argue that current benchmarks fail to measure if an agent can be trusted to deliver a fine-tuned model under strict constraints, such as specific budgets, human approval gates, and reproducibility requirements.
- Identification of the TBDL Failure Mode: A significant contribution is the identification of "Trains but Doesn't Learn" (TBDL) runs—scenarios where every signal remains green during training, yet the final output is no better than the base model, representing a critical silent failure in automated pipelines.
- Multi-Stage Evaluation and Comparison: The research employs a governed delivery plane to score ten distinct stages against an oracle. It evaluates several frontier models across various GPU configurations and compares agent performance directly against human FDE benchmarks to establish a baseline for reliability.

## Context
This paper arrives at a critical juncture where AI development is transitioning from experimental prototyping to commercialized, production-grade services. As organizations increasingly rely on automated pipelines for model fine-tuning, the industry requires standardized methods to verify that these automated agents are producing reliable results rather than just "faking" progress through optimized training metrics.

## Implications
For researchers and practitioners, this work highlights the necessity of incorporating "acceptance gates" and corruption detectors into automated workflows to prevent wasted compute resources on non-learning runs. It suggests a shift in evaluation criteria from simple performance gains toward the reliability and trustworthiness of the agent's ability to navigate complex, multi-step engineering tasks autonomously.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.25237v1)
