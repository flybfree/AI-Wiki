---
title: TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents
published: 2026-08-04T14:02:55Z
authors: Han Xiao, Hongjun Xu, Xin Zhang, Yidong Chen, Xiaodong Shi
url: http://arxiv.org/abs/2608.03699v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents

## Abstract
Persistent memory helps long-term agents retain knowledge, yet a single update error can repeatedly distort future retrieval and reasoning. Most existing systems reduce memory updating to a binary Write/Hold decision, which cannot distinguish whether new information should be added, ignored, used to revise an outdated belief, rejected as unreliable, or deferred for verification. These choices may share the same binary label while producing fundamentally different memory states. We introduce TARL, a memory state update framework that maps each statement to one of five executable actions. TARL identifies the affected memory, resolves its temporal scope, compares source reliability, and updates accepted, pending, and rejected ledgers. It is further trained by comparing the memory states produced by alternative update operations, encouraging the model to select the operation that leads to the correct result. We also introduce TARL-Mem, a benchmark with fine-grained action labels and next-state targets. Across in-domain, cross-source, temporal, counterfactual, and sequential evaluations, TARL improves action prediction and state recovery, reduces memory pollution, preserves conflicting evidence, and limits cumulative corruption. The complete model implementation is provided in the supplementary material.

## Metadata
- **Published**: 2026-08-04T14:02:55Z
- **Authors**: Han Xiao, Hongjun Xu, Xin Zhang, Yidong Chen, Xiaodong Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03699v1)