---
title: End-to-End Learning of Safe Optimal Feedback Control in High Dimensions with Control Barrier Function Layers
url: http://arxiv.org/abs/2607.20674v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_19-17-11Z_End_to_EndLearningofSafeOptimalFeedbackControlinHi.md
generated_at: 2026-07-23 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles the challenge of learning high‑dimensional semi‑global feedback controllers that respect hard safety constraints using control barrier functions (CBFs). By embedding a quadratic‑program safety filter within an end‑to‑end policy network, the authors overcome computational and differentiation bottlenecks that previously limited CBF methods to low‑dimensional systems. Their approach combines operator splitting with Jacobian‑Free Backpropagation, enabling scalable training up to 1200 state dimensions and 400 control dimensions while preserving safety guarantees.

## Key Takeaways
- The authors introduce a quadratic‑program based safety filter that is integrated as an optimization layer within the end‑to‑end policy, allowing safe learning in high‑dimensional settings.  
- They employ Jacobian‑Free Backpropagation to differentiate through the barrier constraints without forming explicit Jacobians, thus removing computational and gradient‑computation bottlenecks.  
- Theoretical justification via nonsmooth analysis ensures that safety guarantees remain intact throughout training, even for large state and control spaces.

## Context
The integration of safety filters into deep reinforcement learning remains a critical research area as autonomous systems grow more complex. Prior work has struggled with the curse of dimensionality, limiting practical deployment to modest problem sizes. This paper advances the field by proving that scalable end‑to‑end training is feasible when combined with operator splitting and JFB techniques.

## Implications
For industry practitioners developing safe robotics or multi‑agent systems, this method offers a pathway to train policies that are both optimal and compliant without sacrificing performance. The theoretical foundation also provides confidence for deploying safety‑critical applications where failure is not an option.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20674v1)
