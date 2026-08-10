---
title: Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks
url: http://arxiv.org/abs/2608.07335v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_15-29-15Z_Aftab_AComprehensiveBenchmarkofCNNEncodersandAdvan.md
generated_at: 2026-08-09 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Aftab, a novel composite architecture for parallelized Q-networks that combines optimized convolutional encoders with advanced value‑function heads to improve sample efficiency and robustness on Atari benchmarks. The authors evaluate eight CNN topologies under strict parameter limits, integrate Hadamax encoding, distributional ensembles, ensemble heads, and dueling heads, and report a human‑normalized IQM score of 6.479 for the Atari‑57 task, which is an 0.86 probability improvement over baseline PQN. Structural resilience tests on Procgen Hard also show out‑of‑distribution performance gains.

## Key Takeaways
- Aftab achieves a higher IQM score than standard PQN by using optimized CNN encoders that balance sample efficiency with parameter constraints.
- The integration of Hadamax encoding and advanced Q‑learning extensions (distributional, ensemble, dueling heads) yields both improved learning stability and out‑of‑distribution generalization.
- Experimental results demonstrate a 0.86 probability of improvement over PQN on Atari‑57 and a notable increase in Procgen Hard IQM from 0.382 to 0.418.

## Context
Parallelized Q-networks have become popular for their memory‑efficient, off‑policy learning without replay buffers or target networks. However, the choice of visual encoder architecture remains largely unexplored within this framework, limiting potential gains in sample efficiency and robustness. This work bridges that gap by systematically exploring CNN designs tailored to PQN.

## Implications
For practitioners developing model‑free reinforcement agents, Aftab offers a practical template for enhancing encoder performance without sacrificing the simplicity of unbuffered training. The open‑source framework enables rapid prototyping and can be adapted to other Atari or non‑Atari environments, encouraging broader adoption of efficient parallelized learning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07335v1)
