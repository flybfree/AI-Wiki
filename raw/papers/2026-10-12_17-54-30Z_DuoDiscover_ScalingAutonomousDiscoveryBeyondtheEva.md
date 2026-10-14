---
title: DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck
published: 2026-10-12T17:54:30Z
authors: Shubham Agarwal, Akshat Gupta, Mike Heddes, Dilara Soylu, Rui Meng, Patrick Tser Jern Kon, Jiefeng Chen, Mert Cemri, Shu Liu, Abe Gonzalez, Akanksha Jain, Bhavana Dalvi Mishra, Linfeng Song, Vilobh Meshram, Xiangru Tang, Jinsung Yoon, Aditya Parameswaran, Ion Stoica, Vahab Mirrokni, Burak Gokturk, Parthasarathy Ranganathan, Tomas Pfister, Nanyun Peng, Chun-Liang Li
url: http://arxiv.org/abs/2610.17184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck

## Abstract
Evaluation has been central to advances in AI, and it is equally critical to autonomous discovery. Yet scaling autonomous discovery to real-world engineering challenges faces a fundamental bottleneck: the cost of evaluating progress. In real settings, a single true evaluation, such as a full benchmark or serving trace, can take hours, so a search can afford only a handful of true evaluations. We present DuoDiscover, a search system that jointly discovers what to optimize and how to evaluate progress efficiently, through three mechanisms. First, each worker in a fleet of coding agents co-discovers an optimization target and a fast, tailored proxy evaluator, which we call a yardstick. The agent then hill-climbs the yardstick rather than the true evaluation. Second, since search can exploit gaps between a yardstick and the true objective, fidelity tests continually recheck each yardstick's ranking and invalidate any that drift. Third, the fleet is bottom-up, with no central decomposition of the problem. A lightweight orchestrator spawns and terminates agents, briefs running ones, and seeds new agents with others' confirmed work. DuoDiscover enables autonomous optimization from software to chip architecture. We demonstrate DuoDiscover on two repository-level benchmarks and four GPU and TPU kernel suites covering hundreds of kernels. On SWE-fficiency, it doubles the average speedup of human experts. On SOL-Exec, it ranks first on 121 of 235 kernels and in the top three on 212. On the heavily optimized vLLM and SQLite engines, DuoDiscover achieves 1.92$\times$ and 1.38$\times$ gains over the base code. On a CPU microarchitecture optimization task with evaluations of up to 28 hours, DuoDiscover surpasses both AlphaEvolve-based ArchAgent v2 and the best human design, with 1.65$\times$ ArchAgent v2's gain in 16.7 days versus more than 40 days, advancing the frontier of autonomous chip design.

## Metadata
- **Published**: 2026-10-12T17:54:30Z
- **Authors**: Shubham Agarwal, Akshat Gupta, Mike Heddes, Dilara Soylu, Rui Meng, Patrick Tser Jern Kon, Jiefeng Chen, Mert Cemri, Shu Liu, Abe Gonzalez, Akanksha Jain, Bhavana Dalvi Mishra, Linfeng Song, Vilobh Meshram, Xiangru Tang, Jinsung Yoon, Aditya Parameswaran, Ion Stoica, Vahab Mirrokni, Burak Gokturk, Parthasarathy Ranganathan, Tomas Pfister, Nanyun Peng, Chun-Liang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17184v1)