---
title: From Generation to Simulation: How Far Are World Models from Being True Simulators?
url: http://arxiv.org/abs/2608.23070v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_10-16-05Z_FromGenerationtoSimulation_HowFarAreWorldModelsfro.md
generated_at: 2026-08-24 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates whether generative world models can replace traditional simulators by measuring them against eight predefined capabilities. The study maps 200 works from 2018 to June 2026 onto these capabilities and finds that while interaction and controllability are functional substitutes, formal physical guarantees, structured state feedback, and long‑horizon stability remain lacking.

## Key Takeaways
- Interaction and controllability have been achieved for specific scenarios but other simulator strengths persist.  
- Only six of one hundred sixty three papers expose a runtime interface for querying entity states or physical parameters, highlighting the neglect of state feedback.  
- Formal guarantees of physical laws and reproducible long‑horizon evolution are still absent across all routes.

## Context
Generative world models aim to create synthetic environments that can be used in reinforcement learning and other AI tasks. Traditional simulators provide deterministic physics and precise state tracking, which are essential for reliable training. The gap between generation and simulation affects the trustworthiness of AI agents relying on these worlds.

## Implications
For researchers, this work clarifies where generative models fall short, guiding efforts toward formalized physics and unified interfaces. For industry, it signals that replacing simulators may require hybrid approaches rather than full substitution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23070v1)
