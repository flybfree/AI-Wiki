---
title: Search as Computation Allocation
url: http://arxiv.org/abs/2607.27871v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_08-45-14Z_SearchasComputationAllocation.md
generated_at: 2026-07-30 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper formalizes terminal computation-allocation problems where costly computations affect decisions through loss and shows how optimal allocation can be derived under fixed budgets, priced computation, or exact certification. It connects the value of computation to information, demonstrating that myopic value equals mutual information under log loss while regret‑based value behaves as a knowledge gradient.

## Key Takeaways
- Mutual information equals myopic VOC under log loss.
- Under simple regret VOC is a knowledge-gradient quantity and can rank computations arbitrarily poorly.
- Approximate VOC maximization with frontier‑resolution recovers weighted A*, with greedy best‑first search as a limiting case.

## Context
This work extends classical bandit and search literature by treating computation as an internal resource, offering a unified framework for acquisition in AI planning that bridges exploration and exploitation.

## Implications
Practitioners can use approximate VOC to guide algorithm selection without assuming universal optimality of any rule; the theory supports hybrid approaches balancing exploration and exploitation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27871v1)
