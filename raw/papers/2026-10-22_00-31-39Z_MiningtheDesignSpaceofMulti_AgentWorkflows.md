---
title: Mining the Design Space of Multi-Agent Workflows
published: 2026-10-22T00:31:39Z
authors: Xavier Cadet, Junyan Cheng, Peter Chin, Kyle Richardson
url: http://arxiv.org/abs/2610.31709v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mining the Design Space of Multi-Agent Workflows

## Abstract
Designing large language model (LLM) multi-agent systems (MAS) still relies on trial and error and informal "folk wisdom." Manual studies test only a few communication structures or topologies (e.g., sequential, parallel, shared-memory, or debate), while automated optimizers discard search trajectories after selecting a task-specific workflow. We present a two-phase pipeline for mining reproducible design principles from workflow code and execution traces. We repurpose AFlow's MCTS optimizer across six composable operators and 26 deterministically verified Enigmata tasks, retaining all intermediate rounds to build a corpus of 28,568 executable workflows. A sandboxed AutoResearch loop then mines orchestration code and prompt templates under an $L_0$-penalized validation objective and tests candidate principles on held-out searches. Across 300 feature-mining trials, we identify effects that persist on held-out searches across three levels of workflow design: workflows beginning with independent solvers and one-shot aggregation (Star-first) perform worse ($Δ= -0.045$); persistent shared documents (SharedMemory) outperform debate ($Δ= +0.135$); and prompt specificity and placeholder-based context routing yield gains comparable to communication-structure selection ($Δ= +0.118$). More broadly, our pipeline and results show the feasibility of turning discarded search trajectories into a statistical testbed for discovering and validating multi-agent workflow design principles.

## Metadata
- **Published**: 2026-10-22T00:31:39Z
- **Authors**: Xavier Cadet, Junyan Cheng, Peter Chin, Kyle Richardson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31709v1)