---
title: WEAVE: Weaving Real-World Code Evolution into Dependency-Structured Tasks for Benchmarking and Training Code Agents
published: 2026-10-15T15:12:56Z
authors: Weihao Li, Zihang Xu, Zhongqiu Wang, Songwei Yu, Wenqiang Zhu, Yuechen Luo, Jingxuan Xu, Yanan Wu, Haoyang Huang, Ken Deng
url: http://arxiv.org/abs/2610.22039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WEAVE: Weaving Real-World Code Evolution into Dependency-Structured Tasks for Benchmarking and Training Code Agents

## Abstract
Real-world software engineering rarely consists of isolated changes. Features, migrations, and systematic fixes often unfold across multiple pull requests (PRs), requiring coordinated modifications across a repository. Yet most executable repository-level benchmarks retain a single issue or PR as the task unit, while existing multi-PR settings rely on coarse aggregation and structure-agnostic evaluation. This mismatch obscures dependencies among changes and limits progress measurement and learning signals for long-horizon code agents. We introduce WEAVE, a framework that transforms verified PR histories into executable, dependency-structured tasks. WEAVE leverages repository-calibrated typed change loci to organize related PRs into bounded DAGs and instantiate each as a unified executable task. We further introduce Graph Credit, a deterministic, test-grounded metric that measures dependency-consistent partial progress and supports dense, verifiable rewards for reinforcement learning. Experiments on task construction, agent evaluation, supervised fine-tuning, and reinforcement learning show that WEAVE yields coherent executable tasks, enables more faithful progress measurement than flat scoring, and provides effective supervision and verifiable rewards for training code agents.

## Metadata
- **Published**: 2026-10-15T15:12:56Z
- **Authors**: Weihao Li, Zihang Xu, Zhongqiu Wang, Songwei Yu, Wenqiang Zhu, Yuechen Luo, Jingxuan Xu, Yanan Wu, Haoyang Huang, Ken Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22039v1)