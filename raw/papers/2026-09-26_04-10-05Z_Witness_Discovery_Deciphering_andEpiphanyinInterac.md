---
title: Witness: Discovery, Deciphering, and Epiphany in Interactive Puzzle Environments
published: 2026-09-26T04:10:05Z
authors: Guanghan Ning, Ping Liu, Linyi Li, Huangjie Zheng, Arjun Neervannan, Huu Nguyen, Michael Sklar, Deniz Zorlu, Nicolai Ouporov
url: http://arxiv.org/abs/2609.32208v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Witness: Discovery, Deciphering, and Epiphany in Interactive Puzzle Environments

## Abstract
Automated science needs agents that can work out the rules of an unfamiliar environment by interacting with it. Interactive rule-discovery puzzles offer a controlled setting for studying this ability: an agent infers hidden rules through experimentation and uses what it has inferred to reach a stated goal. We ask what limits current language models on these puzzles and whether reinforcement learning (RL) improves performance on rules held out from training. To study both, we introduce WITNESS, a 2D grid-based puzzle environment with ground-truth ASCII observations and controlled access to rules. An agentic pipeline generates games for WitnessGym, the RL training suite, and WitnessBench, comprising public validation and private test games. The validation set separately tests new compositions of trained rule primitives and primitives absent from training. Under a shared harness, the best of 18 frontier proprietary and open-weight models solves only 24\% of private test level slots, with scores sensitive to the observation interface and agent configuration. Providing ground-truth rules raises Opus-5's validation RHAE-L5 (relative human action efficiency over the first five levels) from 59.9 to 97.8, whereas a 27B open-weight model gains only 2.1 points and remains limited even with the rules provided. RL on WitnessGym raises the 27B model's private test RHAE-L5 from 2.1 to 5.4 and yields a mean gain of 4.1 points on four external discovery benchmarks. Together, these results point to rule acquisition as a major difficulty for frontier models like Opus-5 while smaller models further struggle on rule-based execution, and indicate that RL on hidden-rule puzzles transfers to broader rules and real-world tasks beyond training. Benchmark is available at: https://witnessbench.ai

## Metadata
- **Published**: 2026-09-26T04:10:05Z
- **Authors**: Guanghan Ning, Ping Liu, Linyi Li, Huangjie Zheng, Arjun Neervannan, Huu Nguyen, Michael Sklar, Deniz Zorlu, Nicolai Ouporov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32208v1)