---
title: FinHardBench: Can LLMs Generate Latency-Aware Hardware for Financial Computing?
published: 2026-08-02T00:30:13Z
authors: Weimin Fu, Hejia Zhang, Minghao Shao, Zeng Wang, Johann Knechtel, Ozgur Sinanoglu, Muhammad Shafique, Ramesh Karri, Xiaolong Guo
url: http://arxiv.org/abs/2608.00909v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinHardBench: Can LLMs Generate Latency-Aware Hardware for Financial Computing?

## Abstract
Can large language models generate not just correct, but fast hardware? This paper investigates the question in financial FPGA design, where 5-10 nanoseconds of latency determines competitive advantage and designs iterate continuously as protocols, strategies, and regulations evolve. FinHardBench, a benchmark of 33 financial computing tasks, is presented together with three experiments that mirror the real-world FPGA iteration cycle: generating new modules from specifications, tuning system-level configurations across a 6-stage trading pipeline, and adapting existing modules to specification changes. Evaluation of six LLMs on 1530+ experiment rounds yields three findings: (1) models achieve 19-61% functional correctness with timing degradation up to 13.7$\times$ on specific tasks; (2) in system-level design space exploration, top LLMs converge to the optimal configuration with higher reliability than random search, simulated annealing, and Bayesian optimization baselines (5/5 seeds vs. 0-4/5 at the same 24-round budget); (3) strategy-level specification changes remain unsolved for most models. Across the six models, generation and DSE rankings overlap moderately: the strongest code generator is not the fastest architecture optimizer, and the weakest code generator (MiniMax M2.7) still reaches the system optimum on 4 of 5 seeds. On the tasks in FinHardBench, difficulty tracks training data pattern availability more closely than abstraction level. FinHardBench is released as an open-source benchmark.

## Metadata
- **Published**: 2026-08-02T00:30:13Z
- **Authors**: Weimin Fu, Hejia Zhang, Minghao Shao, Zeng Wang, Johann Knechtel, Ozgur Sinanoglu, Muhammad Shafique, Ramesh Karri, Xiaolong Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00909v1)