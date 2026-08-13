---
title: Retry, Switch, or Abstain? Learning Strategy-Aware Tool-Use Policies via Controlled Error Injection
url: http://arxiv.org/abs/2608.11977v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_12-08-39Z_Retry_Switch_orAbstain_LearningStrategy_AwareTool_.md
generated_at: 2026-08-12 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces BENCH2ROBUST, a framework that injects controlled tool failures into existing tool‑use benchmarks to study how language models recover when tools fail. Experiments across seven models and multiple benchmark families show a universal robustness gap, with Bayesian Tool Memory (BTM) boosting performance by up to 16.8 percentage points on Retail tasks without retraining, while curriculum reinforcement learning learns complementary recovery strategies that remain useful even after BTM is disabled.

## Key Takeaways
- The study demonstrates that tool failures create a near‑universal robustness gap across diverse models and benchmarks.  
- Bayesian Tool Memory (BTM) provides an environment‑specific recovery context that improves performance by up to 16.8 percentage points on Retail tasks without requiring model retraining.  
- Curriculum reinforcement learning teaches agents to switch or abort when no viable path remains, yielding a complementary benefit that persists even after BTM is removed.

## Context
Tool‑use in large language models often assumes reliable execution, but real‑world deployments encounter transient failures that can derail task completion. This work addresses the need for robust recovery mechanisms by systematically exposing agents to failure scenarios and evaluating their resilience.

## Implications
For practitioners, integrating BTM or learning recovery strategies can significantly enhance reliability of deployed LLM systems without costly retraining cycles. The findings suggest a hybrid approach—combining environment‑specific knowledge with learned behavior—to build more resilient AI agents in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11977v1)
