---
title: AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces
published: 2026-08-24T09:45:08Z
authors: Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
url: http://arxiv.org/abs/2608.23041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

## Abstract
LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic. We propose AutoSaddler, an automatic harness optimization framework that formulates harness improvement as an offline learning problem and iteratively updates the harness using failure signals from mini-batches. AutoSaddler combines failure-trace diagnosis, structured patch generation that treats the harness as code, and validation-based update selection. Experiments on GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0 show that AutoSaddler substantially improves agent performance over the corresponding base harnesses, achieving gains of 9.0, 9.6, and 10.0 percentage points, respectively. Ablation studies further suggest that effective harness optimization benefits from three ingredients: deep debugging rather than shallow reflection, targeted modifications rather than unconstrained editing, and generalization-aware selection rather than trajectory-specific repair. Together, these results suggest that automatic harness optimization is a promising path toward more performant and reliable agent systems.

## Metadata
- **Published**: 2026-08-24T09:45:08Z
- **Authors**: Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23041v1)