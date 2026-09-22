---
title: Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation
url: http://arxiv.org/abs/2609.22478v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-18_18-42-03Z_ReplicationWithoutPersistenceinHostedLLMs_Measurem.md
generated_at: 2026-09-22 00:22
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper investigates the reliability of behavioral evaluations for hosted Large Language Models (LLMs) by distinguishing between three distinct types of consistency: replication, measurement sensitivity, and persistence. By utilizing a sequential environment called Regent Chess to evaluate action-time beliefs, the authors demonstrate that changes in model performance can be caused by variations in the inference configuration or specific identifiers rather than inherent model capabilities.

## Key Takeaways
- The study introduces three distinct validation questions for evaluating hosted models: replication (recovering a finding on fresh data under historical configurations), measurement sensitivity (observing changes when an evaluation configuration is rebuilt using the same identifier), and persistence (checking if findings remain consistent across different identifiers).
- In testing Gemini 3.1 Flash-Lite, the researchers confirmed that a previously reported performance deficit did recur on fresh games, but they also found that rebuilding the inference configuration resulted in a lower endpoint value. Because all six configuration components varied simultaneously during this rebuild, the study could not isolate which specific component caused the shift.
- The research highlights that behavior persistence can vary significantly between different product tiers and release dates; specifically, the comparison between Gemini 3.1 and Gemini 3.7 reversed signs under a rebuilt configuration. This suggests that model behavior is highly dependent on the specific identifier and serving period rather than being a stable property of the model's versioning.

## Context
As LLM evaluation shifts from static weights to dynamic, hosted APIs, it becomes increasingly difficult for researchers to verify consistent performance improvements or regressions. This paper addresses the "moving target" problem in AI benchmarking, where the lack of reproducibility makes it hard to distinguish between a genuine change in model intelligence and a change in the measurement environment.

## Implications
For the AI research community and industry practitioners, these findings suggest that reporting a single performance metric is insufficient for validating LLM progress. Future evaluations must explicitly index results by specific identifiers, serving periods, measurement instruments, and inference configurations to ensure that reported improvements are reproducible and not merely artifacts of a specific test run's configuration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.22478v1)
