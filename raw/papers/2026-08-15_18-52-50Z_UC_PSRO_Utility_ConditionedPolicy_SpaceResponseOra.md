---
title: UC-PSRO: Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum for Game-Theoretic Course-of-Action Generation in Adversarial Swarms
published: 2026-08-15T18:52:50Z
authors: Phillip Jiang
url: http://arxiv.org/abs/2608.15372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UC-PSRO: Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum for Game-Theoretic Course-of-Action Generation in Adversarial Swarms

## Abstract
We study generating game-theoretically optimized Courses of Action (COAs) for a Blue UAS swarm against an adaptive Red adversary in a communication-degraded environment, motivated by (but not derived from) a public U.S. Air Force SBIR solicitation. We propose UC-PSRO (Utility-Conditioned Policy-Space Response Oracles with a Communication-Dropout Curriculum), combining three mechanisms: (i) PSRO self-play, so Blue and Red policies train as approximate best responses to each other rather than one side against a fixed scripted opponent; (ii) FiLM conditioning of the Blue policy on a Commander's-Intent weight vector, sampled from a Dirichlet distribution during training, so one trained policy is re-steerable at execution time without retraining; and (iii) a curriculum annealing communication-graph edge dropout during training, so the swarm learns decentralized, peer-to-peer fallback instead of depending on full connectivity. We evaluate on a synthetic, unclassified stand-in for the solicitation's maritime scenario, with 5 seeds at N=25 Blue agents and a scalability sweep to N=200. We find a genuine trade-off, not a uniform win: the communication-dropout curriculum alone gives the strongest, most robust mission-completion rates of any learned method, improving counter-intuitively as denial increases (35% to 62% success as dropout rises from 0 to 0.75); adding utility-conditioning and PSRO self-play substantially slows convergence within a fixed budget, and we find no reliable exploitability advantage for self-play over a fixed-opponent policy, both statistically indistinguishable from a small, near-zero gap. We report this honestly as a convergence cost not yet offset by a demonstrated robustness benefit, rather than overstating one method as dominant, and provide a fully vectorized, open environment training at N=200 agents in single-digit milliseconds per step on a single consumer GPU.

## Metadata
- **Published**: 2026-08-15T18:52:50Z
- **Authors**: Phillip Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15372v1)