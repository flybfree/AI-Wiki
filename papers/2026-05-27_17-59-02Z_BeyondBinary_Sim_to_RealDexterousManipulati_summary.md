---
title: "Summary: 2026-05-27_17-59-02Z_BeyondBinary_Sim_to_RealDexterousManipulationwithP.md"
date: 2026-05-27
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-27_17-59-02Z_BeyondBinary_Sim_to_RealDexterousManipulationwithP.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.28812v1)
Saved: 2026-05-27 23:00
Source: 2026-05-27_17-59-02Z_BeyondBinary_Sim_to_RealDexterousManipulationwithP.md
Model: None

---


## Summary  
The paper tackles the sim‑to‑real transfer challenge for dexterous manipulation where tactile information is scarce and often reduced to coarse binary features, limiting performance on contact‑rich tasks. To preserve the richness of real‑world touch, the authors introduce Center‑of‑Pressure (CoP), a physics‑grounded representation that retains dense contact data while remaining robust across simulation and reality. CoP enables zero‑shot sim‑to‑real transfer for blind, multi‑fingered manipulation tasks such as peg‑in‑hole insertion and ball balancing, outperforming both binary‑contact and raw‑taxel baselines. The approach demonstrates that tactile policies can encode task‑relevant physical properties like object mass as emergent policy states.

## Key Contributions  
- [Finding 1] CoP is an effective tactile representation grounded in physical principles that preserves dense contact information while maintaining robustness for sim‑to‑real transfer.  
- [Finding 2] A sensor calibration scheme based on differentiable dynamics estimates taxel orientations without requiring ground‑truth force measurements, enabling the construction of CoP from simulated kinematics.  
- [Finding 3] Conditioned policies using CoP achieve zero‑shot sim‑to‑real performance on two blind, challenging contact‑rich tasks and surpass binary‑contact and raw‑taxel baselines.

## Methodology  
The authors simulate a multi‑fingered hand in which each finger is equipped with taxels. Using the underlying physics model, they compute the CoP as the weighted average of taxel positions based on object mass and contact geometry. A differentiable calibration step optimizes taxel orientation parameters to align simulated forces with physical expectations, eliminating the need for external force sensors. The resulting CoP vector is fed into a reinforcement‑learning policy that learns to manipulate objects blindly. Experiments are conducted on two tasks: peg‑in‑hole insertion (requiring precise placement) and ball balancing (requiring dynamic stabilization).  

## Results  
Across both tasks, policies conditioned on CoP reach zero‑shot sim‑to‑real transfer on the real multi‑fingered hand, achieving success rates that exceed those of binary‑contact baselines by a large margin. Moreover, compared to raw taxel inputs, CoP‑conditioned policies improve accuracy and reduce error variance. An analysis of learned policy states reveals that object mass is implicitly encoded, suggesting that CoP serves as a latent proxy for physical properties.  

## Significance  
By replacing coarse binary tactile features with a physics‑grounded representation, the work opens a path to richer, data‑efficient sim‑to‑real dexterous manipulation without extensive real‑world training. The approach reduces reliance on costly sensor calibration and enables policies that understand underlying physical dynamics, which is crucial for safe, reliable human‑like interaction.

## Related Concepts  
- Sim‑to‑Real Transfer  
- Reinforcement Learning for Manipulation  
- Physics‑Grounded Representations  
- Center‑of‑Pressure (CoP)  
- Taxel Orientation Calibration  
- Differentiable Dynamics

[[Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation]]