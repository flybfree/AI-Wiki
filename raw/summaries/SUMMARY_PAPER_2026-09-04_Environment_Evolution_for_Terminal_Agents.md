---
title: Environment Evolution for Terminal Agents
url: http://arxiv.org/abs/2609.04128v1
type: paper-summary
date: 2026-09-04
source_paper: 2026-09-03_17-26-33Z_EnvironmentEvolutionforTerminalAgents.md
generated_at: 2026-09-04 15:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces environment evolution, a method for incrementally increasing the difficulty of synthetic environments off‑policy during terminal agent training. By evolving environments along three derived directions and generating them generation by generation, the approach supplies continuous learning signals as frontier models become stronger. Experiments with Hy4 preview, Claude Opus 5, GPT‑5.6 Sol, Qwen3.6‑27B and Qwen3.6‑35B‑A3B show that evolved environments are consistently more challenging and improve performance on Terminal‑Bench 2.1 by up to 18 percentage points.

## Key Takeaways
- Environment evolution continuously generates harder synthetic tasks off‑policy, unlike co‑evolution methods that rely solely on on‑policy rollouts.  
- The method defines three evolution directions tied to the multi‑turn learning objective, enabling systematic difficulty scaling across generations.  
- Quantitative results demonstrate a measurable performance boost for large language models, with Qwen3.6‑35B‑A3B gaining 18 percentage points on Terminal‑Bench 2.1.

## Context
Scaling interactive and verifiable environments remains a bottleneck for training advanced agents as models surpass existing benchmarks. Traditional co‑evolution approaches struggle to maintain learning signals when rollouts become too aligned with the model’s current capabilities, limiting generalization. This work addresses that gap by decoupling environment difficulty from on‑policy data.

## Implications
The continuous evolution framework can be integrated into any terminal agent training pipeline without sacrificing sample efficiency. Practitioners may adopt it to keep models challenged as they improve, fostering more robust and adaptable agents in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04128v1)
