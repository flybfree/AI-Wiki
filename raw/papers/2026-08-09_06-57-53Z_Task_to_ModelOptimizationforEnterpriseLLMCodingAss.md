---
title: Task-to-Model Optimization for Enterprise LLM Coding Assistants: A Data-Driven Framework for Cost-Optimal Routing
published: 2026-08-09T06:57:53Z
authors: Srinivasan Manoharan, Junhua Zhao, Fangbo Tu, Haifeng Wu, Jian Wan, Maliah Rajan M, Ashwin Hegde, Mithun Sasidharan, Kalyan Chakravarthi Podamekala
url: http://arxiv.org/abs/2608.08528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Task-to-Model Optimization for Enterprise LLM Coding Assistants: A Data-Driven Framework for Cost-Optimal Routing

## Abstract
Enterprise AI coding assistants incur substantial inference spend, and naive token-cost minimization often fails to reduce end-to-end cost once retries, escalations, and developer wait time are included. We present Task-to-Model Optimization (T2MO), a data-driven methodology for optimizing model selection in production coding workflows. We treat each developer session as a task that can be discovered, classified, graded for difficulty, benchmarked in a production-like harness, and routed to the cheapest model able to complete it within quality and latency constraints. The framework is a nine-stage pipeline spanning telemetry instrumentation, taxonomy discovery, difficulty grading, benchmark construction, candidate evaluation, optimal mix derivation, forecasting and version planning, staged routing deployment, and continuous governance. Unlike token-centric routing rules, our objective is cost per completed task, with failure escalation priced in explicitly. We show that this expected-completion-cost objective weakly dominates token-cost minimization under escalation, and we derive the routing boundary, the minimum pass rate a cheaper model must reach on a given cell to be worth deploying. Decisions are organized as a two-level hierarchy of task category difficulty tier, and per-cell displacement opportunities are aggregated into a traffic-weighted savings waterfall that ranks replacement candidates by realized dollar impact. The framework supports developer guidance, spend forecasting, and a staged transition from static policies to shadow-mode classifiers, verified cascades, and ultimately an intelligent router. We describe the methodology, optimization objective, evaluation protocol, and governance loop in a form suitable for production deployment and future empirical study.

## Metadata
- **Published**: 2026-08-09T06:57:53Z
- **Authors**: Srinivasan Manoharan, Junhua Zhao, Fangbo Tu, Haifeng Wu, Jian Wan, Maliah Rajan M, Ashwin Hegde, Mithun Sasidharan, Kalyan Chakravarthi Podamekala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08528v1)