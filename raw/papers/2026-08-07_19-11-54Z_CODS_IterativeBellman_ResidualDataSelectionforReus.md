---
title: CODS: Iterative Bellman-Residual Data Selection for Reusable Offline Reinforcement Learning
published: 2026-08-07T19:11:54Z
authors: Ibne Farabi Shihab, Sanjeda Akter, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb, Anuj Sharma
url: http://arxiv.org/abs/2608.07719v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CODS: Iterative Bellman-Residual Data Selection for Reusable Offline Reinforcement Learning

## Abstract
Offline reinforcement learning repeatedly trains policies from a fixed transition pool, making redundant data costly across seeds and hyperparameters, while naive subsampling can remove rare transitions needed for long-horizon credit assignment. We introduce CODS, a critic-guided selector that alternates between fitting an algorithm-matched critic and acquiring high-residual transitions before freezing a reusable subset. Unlike prioritized replay, CODS produces a static artifact; unlike one-shot residual selection, it refreshes scores as the critic changes. At a 10\% budget, CODS retains 96.6\% of eligible-pool performance across 20 valid D4RL task--algorithm cells. It exceeds ReDOR and OPER on 19/20 cells and every other subset baseline on 20/20; all six subset advantages remain significant under predeclared hierarchical inference with Holm correction. Holding total selector updates fixed, five acquisition rounds improve four representative cells by 11.23 points over one round and saturate thereafter. Equal-pass and equal-hour evaluations clarify that reuse, rather than a single-run speedup, creates the compute advantage. Mechanism and corruption interventions expose both useful sparse-reward enrichment and sensitivity to outliers. Finally, a whole-trace extension retains 95.4\% of pooled ALFWorld success and 96.5\% of pooled GSM8K exact match. CODS is therefore a reusable selection procedure, not a formal coreset guarantee.

## Metadata
- **Published**: 2026-08-07T19:11:54Z
- **Authors**: Ibne Farabi Shihab, Sanjeda Akter, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb, Anuj Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07719v1)