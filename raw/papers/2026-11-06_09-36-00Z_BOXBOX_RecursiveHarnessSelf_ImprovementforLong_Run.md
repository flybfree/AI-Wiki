---
title: BOXBOX: Recursive Harness Self-Improvement for Long-Running Performance Optimization
published: 2026-11-06T09:36:00Z
authors: Yuhao Tan, Hanyun Jiang, Fangkai Yang, Yuan Yao, Taolue Chen, Bo Qiao, Yu Kang, Lu Wang, Pu Zhao, Xiaoxing Ma, Qingwei Lin
url: http://arxiv.org/abs/2611.09218v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BOXBOX: Recursive Harness Self-Improvement for Long-Running Performance Optimization

## Abstract
Automated harness optimization improves agents by learning from trajectories and task feedback. Existing offline methods use reference answers to optimize harnesses for reuse on held-out tasks. However, many real-world tasks are open-ended, while long runs expose new difficulties that offline-optimized harnesses may not address. To study harness optimization in these settings, we introduce PerfRace, a benchmark for long-running performance optimization of software projects, and investigate whether agents can use task-specific experience to recursively improve their harnesses during an ongoing task. To this end, we introduce BOXBOX, which enables agent-triggered harness revision and kernel-managed hot reloading while preserving execution context. We evaluate BOXBOX on PerfRace under matched test-time budgets, comparing it with Frozen Harness, offline Harness Evolution, and Harness Scaling. BOXBOX achieves higher speedup with more efficient use of task time and model cost, reaching a Speedup@4h of 1.70x, compared with 1.54x for the strongest baseline.

## Metadata
- **Published**: 2026-11-06T09:36:00Z
- **Authors**: Yuhao Tan, Hanyun Jiang, Fangkai Yang, Yuan Yao, Taolue Chen, Bo Qiao, Yu Kang, Lu Wang, Pu Zhao, Xiaoxing Ma, Qingwei Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.09218v1)