---
title: Long-Time Trajectory Approximation via SA-NODEs: Model Predictive and Floquet Strategies
url: http://arxiv.org/abs/2608.10738v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_09-55-54Z_Long_TimeTrajectoryApproximationviaSA_NODEs_ModelP.md
generated_at: 2026-08-11 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces two training strategies for semi‑autonomous neural ordinary differential equations (SA‑NODEs) that avoid the double exponential error growth typical of a single network trained over an entire horizon. The model predictive strategy partitions the trajectory into adaptive windows and restarts each window from observed data, yielding a uniform tolerance with a linear parameter budget under bounded reachable tube conditions. The Floquet strategy targets autonomous systems with stable limit cycles, providing a certified contraction of the learned return map that limits error to linear growth in elapsed periods.

## Key Takeaways  
- Model predictive strategy partitions the horizon adaptively and restarts every window from observed data, achieving uniform tolerance on each window and a composite model that meets it uniformly across time with a parameter budget linear in the horizon for targets with a bounded, uniformly regular reachable tube.  
- Floquet strategy addresses autonomous targets with a stable limit cycle, using no data at deployment; a certified contraction of the learned return map confines error to linear growth in the number of elapsed periods.  
- For the time‑periodic architecture we deploy, the scalar certificate degenerates; instead we prove a uniform‑in‑time orbital guarantee whose hypotheses are measured on the trained model and an obstruction showing that small one‑period error cannot coexist with a contracting stroboscopic map.

## Context  
This work tackles the scalability problem of long‑horizon trajectory approximation where conventional neural ODE models suffer catastrophic error growth, a barrier for real‑time applications. By introducing reset‑based training strategies, it offers practical solutions that keep errors bounded linearly rather than exponentially, opening avenues for reliable long‑term predictions.

## Implications  
Practitioners can deploy SA‑NODEs in robotics and control where long‑term stability is critical, reducing the need for extensive retraining. The linear error guarantees enable dependable predictions over extended periods, supporting safety‑critical systems that require predictable behavior over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10738v1)
