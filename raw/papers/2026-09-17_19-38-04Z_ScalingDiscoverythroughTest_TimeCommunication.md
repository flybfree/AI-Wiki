---
title: Scaling Discovery through Test-Time Communication
published: 2026-09-17T19:38:04Z
authors: Jongho Park, Vasilis Kontonis, Shivam Garg, Akshay Krishnamurthy, Dimitris Papailiopoulos
url: http://arxiv.org/abs/2609.21032v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Discovery through Test-Time Communication

## Abstract
Science advances not in isolation but through collaboration, yet existing agentic systems capture little of this. Whether communicating agents help remains an open question with mixed prior results. We show that test-time communication can substantially outperform independent parallel attempts on challenging tasks, where sharing a breakthrough can push the whole group forward. We first study the effect of scaling multi-agent test-time communication, where agents have no predefined roles and communicate via a shared directory, on ARC-AGI-3, a benchmark requiring novel problem solving. We find that a team of $k$ communicating agents, team@$k$, matches the success rate of $4k$ independent agents, and this advantage grows with $k$, suggesting gains compound with scale. The effect is not merely efficiency: a task that no single agent can solve, a team of agents can solve reliably. Furthermore, these gains transfer to research-oriented tasks, given sufficient compute. On polyomino packing, communicating agents outperform best@$k$ and exceed the prior best-known score. On MNIST classifier compression, communication surpasses the best-known human solution. A team of four agents produced a 1,957-byte classifier submission achieving 99.4% test accuracy, smaller than both the best-known human solution and the best single-agent result. These gains are not unconditional. Independent agents may outperform communication when compute is limited or when a clear measure of progress is absent. However, under sufficient compute and clear feedback, multi-agent communication consistently yields stronger results.

## Metadata
- **Published**: 2026-09-17T19:38:04Z
- **Authors**: Jongho Park, Vasilis Kontonis, Shivam Garg, Akshay Krishnamurthy, Dimitris Papailiopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21032v1)