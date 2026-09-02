---
title: WHALE: A Simple Recipe for Joint Harness-Weight Optimization
published: 2026-08-31T18:12:55Z
authors: Haechan Kim, Yoonho Lee, Gisang Lee, Chelsea Finn, Kangwook Lee
url: http://arxiv.org/abs/2609.00196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WHALE: A Simple Recipe for Joint Harness-Weight Optimization

## Abstract
Agent performance depends jointly on the model parameters and the executable harness code that manages context and control flow. Optimizing either component in isolation can leave the system bottlenecked by its frozen counterpart: weight updates can change which harness is effective, while harness updates can change which model capabilities are exposed. Existing joint-adaptation methods optimize weights and textual prompts but leave the broader harness fixed. We propose Weight-Harness Alternating LEarning (WHALE), a simple recipe that alternates two phases: updating the model under the current harness, then searching for a better harness under the updated model. We instantiate these two phases with online rejection-sampling fine-tuning and Meta-Harness, respectively. When to switch is a key design choice: to separate real improvements from noise without over-optimizing against a changing counterpart, WHALE uses either fixed phase durations or an adaptive patience rule over training signals. Using Qwen3.5-2B/4B agents across three domains (search question answering, mathematical reasoning, and chess puzzles), WHALE outperforms weight-only, harness-only, and Fast-Slow Training by 4.15-24.38 percentage points in best mean@8 accuracy. Either component can be the bottleneck: harness search matches peak weight-only accuracy with far fewer rollouts in SearchQA, but improves math accuracy only after a weight update. Small interleaved updates also outperform stagewise weight-then-harness optimization in accuracy and rollout cost. The code is available at https://github.com/krafton-ai/WHALE.

## Metadata
- **Published**: 2026-08-31T18:12:55Z
- **Authors**: Haechan Kim, Yoonho Lee, Gisang Lee, Chelsea Finn, Kangwook Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00196v1)