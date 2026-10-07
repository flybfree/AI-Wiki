---
title: Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents
published: 2026-10-05T21:55:52Z
authors: Ziyang Cai, Christos Ziakas, Vasilis Kontonis, Tim Pearce, Siddhartha Sen, Akshay Krishnamurthy, Shivam Garg, Dimitris Papailiopoulos
url: http://arxiv.org/abs/2610.07447v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents

## Abstract
Autoresearch agents tackle open-ended problems by repeatedly proposing candidate solutions, evaluating them, and using feedback to guide subsequent experiments. We show that independent runs of the same agent on the same task often plateau at substantially different scores, with gaps that persist even after considerable additional compute. Embedding their candidate artifacts by functional similarity provides further evidence that trajectories remain in localized regions of the solution space, which we call idea basins. To help agents escape these basins, we study a simple periodic intervention, fork-and-flush. Our method forks the agent into parallel trajectories, each inheriting the accumulated workspace but starting with a fresh chat context. After running each trajectory for a fixed horizon, the agent continues from the highest-scoring one. Across 13 long-horizon research and engineering tasks, with individual agent runs lasting up to several days, fork-and-flush outperformed the single-run and best-of-N baselines by a relative improvement of 66.0% and 44.4%, respectively, on the min-max normalized average score under an equal compute budget.

## Metadata
- **Published**: 2026-10-05T21:55:52Z
- **Authors**: Ziyang Cai, Christos Ziakas, Vasilis Kontonis, Tim Pearce, Siddhartha Sen, Akshay Krishnamurthy, Shivam Garg, Dimitris Papailiopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07447v1)