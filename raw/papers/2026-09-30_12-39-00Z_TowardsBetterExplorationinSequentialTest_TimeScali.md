---
title: Towards Better Exploration in Sequential Test-Time Scaling
published: 2026-09-30T12:39:00Z
authors: Joseph Rance, Fabio Pizzati, Juil Sock, Woody Bayliss, Marc Górriz Blanch, Philip Torr, Adel Bibi
url: http://arxiv.org/abs/2609.39632v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Better Exploration in Sequential Test-Time Scaling

## Abstract
Test-time scaling improves language model reasoning by spending additional compute at inference. However, both classes of existing methods often fail to continue improving over long timescales. Parallel methods repeatedly sample independent answers from the model, scaling poorly on problems the model is unlikely to solve in a single attempt. In contrast, sequential methods build on previous answers to access new ideas, yet so far have not been shown to reach answers beyond those found by parallel scaling. First, we show that sequential scaling often stops improving because it becomes prematurely trapped in an attractor: a set of answers that prevents exploration of different answers once entered. Across 27 combinations of scaling methods, models, and benchmarks, we find that 53.8% of sequential scaling trajectories enter an attractor within four iterations. Second, we show that a simple model-mixing intervention helps escape attractors. This reduces the attractor hit rate by 21.2 percentage points on average, expands solution coverage beyond a compute-matched parallel baseline, and improves accuracy of recursive self-aggregation by at least 2.2 percentage points. Our results motivate refocusing long-horizon test-time scaling from parallel methods to sequential methods that improve previous answers.

## Metadata
- **Published**: 2026-09-30T12:39:00Z
- **Authors**: Joseph Rance, Fabio Pizzati, Juil Sock, Woody Bayliss, Marc Górriz Blanch, Philip Torr, Adel Bibi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39632v1)