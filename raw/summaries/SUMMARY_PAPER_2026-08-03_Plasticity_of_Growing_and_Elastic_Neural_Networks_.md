---
title: Plasticity of Growing and Elastic Neural Networks in Online Continual Learning
url: http://arxiv.org/abs/2608.01475v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_20-12-32Z_PlasticityofGrowingandElasticNeuralNetworksinOnlin.md
generated_at: 2026-08-03 23:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how growing and elastic neural networks maintain plasticity during online continual learning tasks. Experiments in supervised settings show that adaptive growing networks keep high accuracy despite increasing dead units, while elastic networks also prune dead units to stay compact without losing performance.

## Key Takeaways
- Adaptive growing networks preserve prediction accuracy as the proportion of dead hidden units rises by dynamically adding randomly initialized units and adapting existing connections.  
- Elastic networks achieve excellent accuracy through both progressive addition of new units and periodic removal of estimated dead units, keeping the network size nearly constant.  
- Both architectures demonstrate that structural adaptability can sustain plasticity in online continual learning scenarios.

## Context
Online continual learning faces challenges such as catastrophic forgetting and loss of plasticity, which are critical issues for real‑world applications where models must update continuously. This work addresses those problems by exploring architectures that evolve their structure to match new tasks, offering a more biologically inspired alternative to static network updates.

## Implications
These findings suggest that growing and elastic networks could be deployed in systems requiring long‑term stability and adaptability, such as robotics or autonomous agents. Practitioners may adopt these methods to build models that retain learning capacity over time without sacrificing performance or computational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01475v1)
