---
title: Adaptive-GEPA: Make Your Harness Fit Heterogeneous Requests
url: http://arxiv.org/abs/2609.38762v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_01-45-45Z_Adaptive_GEPA_MakeYourHarnessFitHeterogeneousReque.md
generated_at: 2026-09-30 21:00
model: qwen3.6-35b-a3b
---

## Summary
Adaptive-GEPA introduces a framework that simultaneously learns to partition heterogeneous requests and evolve specialized solution programs under a unified search budget. By co-evolving a routing mechanism with a library of expert programs, the system achieves superior performance on mixed workloads compared to single-program optimizers or fixed multi-program approaches, demonstrating automatic task discovery without requiring explicit family labels.

## Key Takeaways
- Adaptive-GEPA employs a reflective optimization process that evolves both a router and a diverse library of specialist programs within a single search budget; the router dynamically divides incoming requests while specialists handle specific sub-tasks, with all components described in human-readable text that is iteratively refined based on execution feedback.
- Experimental results using Qwen3-8B show the method automatically evolves four distinct experts for a mixture of four task families without supervision; the router achieves perfect agreement with ground-truth partitions across 651 test requests, and the family-mean test score improves from 52.6 to 70.6, significantly outperforming GEPA's full-program adapter (62.5) and GRPO (54.0) at a nominal budget of 18,000 scored calls.
- The framework addresses the limitation of existing reflective optimizers by explicitly managing heterogeneous request distributions; unlike methods that rely on implicit division in source-code search or pre-fixed program separation, Adaptive-GEPA aligns specialists based on handled requests and inherits descriptions alongside programs to effectively combine branches and adapt to diverse tool usage and reasoning modes.

## Context
Reflective optimizers such as GEPA have demonstrated the ability to enhance language model capabilities by rewriting prompts, tools, and control flow based on execution traces and evaluator feedback. However, practical deployments often encounter heterogeneous request streams requiring distinct solution strategies, a scenario where current methods struggle due to either implicit task division in shared programs or rigid pre-defined partitions for separate programs.

## Implications
Adaptive-GEPA offers a scalable path toward autonomous system adaptation, enabling practitioners to build AI agents that automatically discover and exploit structural diversity in user requests without manual intervention or labeling overhead. This capability can significantly improve the robustness and efficiency of deployed language model applications by ensuring optimal resource allocation and specialized handling for varied input distributions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38762v1)
