---
title: Theoretical Foundations of Communication-Efficient, Robust, and Practical Distributed and Federated Optimization
published: 2026-08-06T20:20:52Z
authors: Grigory Malinovsky
url: http://arxiv.org/abs/2608.06563v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Theoretical Foundations of Communication-Efficient, Robust, and Practical Distributed and Federated Optimization

## Abstract
Machine learning and optimization have advanced together, with practical demands motivating new theory and theoretical breakthroughs enabling new applications. Modern large-scale training relies on classical optimization principles, but the constraints of distributed systems require these foundations to be reconsidered. This thesis addresses seven challenges at the intersection of theory and practice, focusing on key bottlenecks in federated learning and distributed optimization. First, we introduce ProxSkip and prove that local gradient steps can accelerate communication, providing a theoretical foundation for this widely used heuristic. Second, we develop Variance Reduced ProxSkip, which eliminates the neighborhood error of stochastic local updates while balancing communication and local computation. Third, we show that local steps retain their communication acceleration under partial client participation. Fourth, we prove that server-side stepsizes and sampling without replacement improve convergence in heterogeneous settings. Fifth, for Random Reshuffling, we demonstrate that compressing gradient differences rather than gradients yields better theoretical and practical performance. Sixth, we establish that Byzantine robustness and partial participation can be achieved simultaneously using gradient-difference clipping. Finally, we develop the first theoretical framework for low-rank adaptation based on randomized asymmetric chains, providing new insights into fine-tuning large models. Across these contributions, we introduce novel algorithmic frameworks, establish sharp guarantees under realistic assumptions, and support the theory with numerical experiments.

## Metadata
- **Published**: 2026-08-06T20:20:52Z
- **Authors**: Grigory Malinovsky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06563v1)