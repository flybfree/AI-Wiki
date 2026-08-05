---
title: Trajectory inference via Acceleration Matching
published: 2026-08-04T16:42:04Z
authors: Bartolo Dazzini, Giovanni Conforti, Alain Durmus, Aram-Alexandre Pooladian
url: http://arxiv.org/abs/2608.03916v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trajectory inference via Acceleration Matching

## Abstract
Trajectory inference is a fundamental problem in many scientific domains: given a collection of unpaired snapshots of observations at discrete time points, the goal is to generate smooth trajectories that best resemble and interpolate the data. Existing algorithms exhibit computational challenges: they either rely on preprocessing subroutines to enforce smoothness or on simulation-based training objectives, both of which can be expensive. In order to overcome these limitations, we propose a new algorithm called Acceleration Matching (\texttt{AM}). Our approach consists of lifting the original interpolation problem to phase space and then regressing onto an explicit conditional acceleration field that induces random, smooth trajectories that agree with the prescribed marginals. Importantly, our resulting training algorithm only requires positional data, avoids trajectory simulation during training, and is devoid of expensive preprocessing. We provide ample numerical evidence suggesting that \texttt{AM} is competitive with or superior to existing algorithms on several benchmark problems from the existing literature.

## Metadata
- **Published**: 2026-08-04T16:42:04Z
- **Authors**: Bartolo Dazzini, Giovanni Conforti, Alain Durmus, Aram-Alexandre Pooladian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03916v1)