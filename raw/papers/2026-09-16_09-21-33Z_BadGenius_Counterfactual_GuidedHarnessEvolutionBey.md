---
title: Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts
published: 2026-09-16T09:21:33Z
authors: Guojun Zhu, Xunheng Huang, Peng Yin, Jiahui Xie, Sanguo Zhang, Doudou Zhou
url: http://arxiv.org/abs/2609.18366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Bad Genius: Counterfactual-Guided Harness Evolution Beyond Task-Specific Shortcuts

## Abstract
Reliable agent evaluation is complicated by automatic harness optimization, which repeatedly uses a released benchmark $B_{\mathrm{rel}}$ to guide a Proposer that edits prompts, memory, retrieval, tools, and control code around a fixed target agent. Task holdout varies semantic tasks but leaves the benchmark protocol fixed, so a "bad genius" Proposer can produce a cheating harness whose released-benchmark gain depends on a benchmark-wide shortcut. We introduce Counterfactual Harness Search and Evolution (CHASE), which casts harness evolution as constraint generation over validity-preserving benchmark counterfactuals. After each Proposer update, a Challenger searches for an executable protocol transformation with large gain destruction. A validity firewall checks that task semantics are preserved, while a confirmation set determines whether the counterfactual enters a finite archive. We formalize an exact shortcut-neutralized benchmark $B_0$ and establish statistical guarantees linking finite counterfactual archives to $B_0$ and characterizing sequential Challenger search. We evaluate CHASE on a synthetic benchmark and on OfficeQA, where CHASE retains strong released-benchmark gains while substantially reducing gain destruction under valid protocol changes.

## Metadata
- **Published**: 2026-09-16T09:21:33Z
- **Authors**: Guojun Zhu, Xunheng Huang, Peng Yin, Jiahui Xie, Sanguo Zhang, Doudou Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18366v1)