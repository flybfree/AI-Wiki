---
title: SegBench-GC: Testing Segmentation Invariance in Multi-Step Offline Goal-Conditioned Reinforcement Learning
published: 2026-08-27T20:07:36Z
authors: Musa Shams
url: http://arxiv.org/abs/2608.27678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SegBench-GC: Testing Segmentation Invariance in Multi-Step Offline Goal-Conditioned Reinforcement Learning

## Abstract
Offline goal-conditioned reinforcement learning (GCRL) often uses trajectory structure for future-goal sampling and multi-step targets, yet logged trajectories may be partitioned for administrative reasons that do not correspond to termination. We introduce SegBench-GC, a controlled stress test of segmentation invariance that holds transitions, source trajectories, goal sampling, optimization settings, and evaluation fixed while varying only artificial backup boundaries and whether those boundaries retain continuation value. Continuation-valid targets (CVT) provide the segmentation-consistent control: reward accumulation stops at an artificial cut, but the target bootstraps from its stored successor. In a matched-count PointMaze study with 35,000 artificial cuts, three segmentation realizations, and three optimization seeds, final 50-episode-per-task success is 50.5% uncut, 39.1% with CVT, and 19.1% when the same cuts are treated as absorbing; across segmentation realizations, naive mean success ranges from 4.8% to 31.9%. An independent published n-step baseline (n=25) from the Decoupled Q-Chunking codebase shows the same failure on Puzzle-4x5: 47.2% uncut, 58.5% CVT, and 0.27% naive across three optimization seeds. A target-level diagnostic verifies the analytic target difference to numerical precision, and learned-critic diagnostics show a large optimistic shift under naive handling while CVT remains approximately aligned with the uncut critic. CVT applies standard continuation bootstrapping rather than a new Bellman rule; the contribution is the controlled benchmark, failure isolation, and cross-learner evidence that administrative segmentation can materially change multi-step offline GCRL.

## Metadata
- **Published**: 2026-08-27T20:07:36Z
- **Authors**: Musa Shams
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27678v1)