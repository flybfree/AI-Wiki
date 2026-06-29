---
title: Agentic Hardware Design as Repository-Level Code Evolution
published: 2026-06-26T17:21:06Z
authors: Cunxi Yu, Chenhui Deng, Nathaniel Pinckney, Brucek Khailany
url: http://arxiv.org/abs/2606.28279v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Hardware Design as Repository-Level Code Evolution

## Abstract
We present HORIZON, a self-evolving agent framework that treats hardware design as repository-level code evolution. A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, an acceptance predicate, and a git/runtime policy; a hands-free agent loop then evolves an isolated git worktree, using repository operations for state management, tracing, and replay. This extends prior works of repository-scale self-evolution from EDA software systems, to hardware-design artifacts themselves. We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100\% benchmark completion across all suites with a fully hands-free agentic loop. However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design. Section~\ref{sec:discuss} examines the limitations of the current study and highlights open research challenges.

## Metadata
- **Published**: 2026-06-26T17:21:06Z
- **Authors**: Cunxi Yu, Chenhui Deng, Nathaniel Pinckney, Brucek Khailany
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.28279v1)