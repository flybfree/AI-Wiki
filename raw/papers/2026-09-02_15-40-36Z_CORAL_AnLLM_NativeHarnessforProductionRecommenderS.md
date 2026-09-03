---
title: CORAL: An LLM-Native Harness for Production Recommender Systems
published: 2026-09-02T15:40:36Z
authors: Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang, Yuchen Wang, Rahul Sharma, Matthew DeSousa, Jiayi Liu, Xin Guo, Lizhu Zhang, Xiangjun Fan
url: http://arxiv.org/abs/2609.02730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CORAL: An LLM-Native Harness for Production Recommender Systems

## Abstract
Production recommender systems shape what billions of people see, and sustaining their performance requires continual optimization: as content, user behavior, and upstream models shift, the choices governing retrieval, ranking, and serving must be revisited. Traditionally, human engineers test such changes through online experiments--a slow, reactive process limited by engineering effort, leaving parts of the system unrevised as conditions change. Although large language models have been applied to ranking, user modeling, and offline model development, few systems place an agent in a continual closed loop that acts on a live recommender and learns from the measured effects of its decisions. We present CORAL (Constraint-Optimized Recommender via an Agentic Loop), an LLM-native harness that closes this loop: each cycle, the agent observes operating signals, reasons over a memory of past decisions and outcomes, and invokes tools--including a numerical optimizer that keeps changes within a fixed operating budget--to reconfigure the recommender, with measured outcomes informing the next cycle. We formulate this as a partially observed, non-stationary, constrained optimization problem in which the policy improves in context, without parameter updates, from its prior actions. Across two large-scale social platforms, evaluated with A/B experiments, the same harness improves engagement at no additional serving cost on one and reduces serving cost without degrading engagement on the other, spanning the engagement-efficiency frontier. Performance improves as the loop iterates, suggesting that a single agentic loop can automate continual optimization work traditionally performed by human algorithm engineers under explicit guardrails.

## Metadata
- **Published**: 2026-09-02T15:40:36Z
- **Authors**: Muhammad Rafay Azhar, Yuhang Zhou, Gilbert Jiang, Yuchen Wang, Rahul Sharma, Matthew DeSousa, Jiayi Liu, Xin Guo, Lizhu Zhang, Xiangjun Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02730v1)