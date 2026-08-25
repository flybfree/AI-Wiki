---
title: ParallelWorld: Test-Time Scaling for Embodied Reasoning
published: 2026-08-24T08:32:37Z
authors: Min Chen, Shengjun Zhang, Yuxin Li, Zhang Zhang, Xin Fei, Chong Xia, Yueqi Duan
url: http://arxiv.org/abs/2608.22971v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ParallelWorld: Test-Time Scaling for Embodied Reasoning

## Abstract
Embodied Reasoning constitutes a fundamental capability of embodied intelligence, serving as the basis for autonomous perception, reasoning, and interaction within physical environments. Recent studies have shifted the paradigm of embodied reasoning from static perception toward dynamic exploration, where agents acquire task-relevant information through interactions with the environment. However, existing active reasoning approaches generally generate exploration trajectories incrementally without long-horizon planning. Even recently emerged test-time scaling frameworks often resort to myopic, single-step lookaheads, which struggle to resolve the delayed feedback inherent in complex, occluded spatial environments. To address this limitation, we propose ParallelWorld, a multi-horizon test-time scaling framework for embodied reasoning. Instead of greedy, single-step trials, ParallelWorld empowers agents to simulate and evaluate multi-step future trajectories in parallel before committing to an action. Specifically, we introduce a verifier-guided tree-search paradigm. Starting from the current state, ParallelWorld branches into multiple parallel trajectories and rolls them out continuously across a multi-step horizon. At each simulation step, a verifier agent evaluates the intermediate state transitions, dynamically pruning unpromising branches and prioritizing paths with the highest information gain. Once the multi-step prospective simulation is complete, the agent synthesizes the long-horizon outcomes to commit to the optimal action sequence. Finally, an answer agent performs reasoning over the selected trajectory to produce the final reasoning. Extensive experiments on ESI-Bench demonstrate that ParallelWorld consistently improves active perception and reasoning performance.

## Metadata
- **Published**: 2026-08-24T08:32:37Z
- **Authors**: Min Chen, Shengjun Zhang, Yuxin Li, Zhang Zhang, Xin Fei, Chong Xia, Yueqi Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22971v1)