---
title: When Do Prompt-Side Agent Playbooks Transfer? Accuracy, Cost, and Runtime Shift in Agent Deployment
published: 2026-08-06T09:10:25Z
authors: Weihong Lin, Lin Sun, Xiangzheng Zhang
url: http://arxiv.org/abs/2608.05778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Prompt-Side Agent Playbooks Transfer? Accuracy, Cost, and Runtime Shift in Agent Deployment

## Abstract
Prompt-side playbooks can improve tool-using language agents without retraining, but their portability beyond the source setting is unclear. We study frozen playbook transfer under a shared distill--validate--transfer protocol. On ALFWorld, transfer is beneficial under controlled greedy decoding and, in one near-budget-matched comparison, distilled guidance outperforms five fixed demonstrations. On TAU2-Bench, a prespecified aggregate contrast supports a modest average matched-domain advantage, but global Holm correction retains only one of 135 route-level effects; the remaining grid provides descriptive evidence of compatibility-sensitive heterogeneity. On XBench-DeepSearch, one artifact--runtime pairing preserves useful first-try heuristics while producing repeated queries, delayed stopping, and substantial cost inflation after a context-runtime shift. Across benchmarks, transferred and target-derived playbooks both require target-side validation of success, termination, protocol compatibility, and cost. Frozen transfer is therefore a conditional cold-start option, not a reuse-by-default strategy or a universally preferable alternative to target-side redistillation.

## Metadata
- **Published**: 2026-08-06T09:10:25Z
- **Authors**: Weihong Lin, Lin Sun, Xiangzheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05778v1)