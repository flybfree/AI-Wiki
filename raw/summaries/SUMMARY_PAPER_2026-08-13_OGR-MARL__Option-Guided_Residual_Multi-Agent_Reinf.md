---
title: OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways
url: http://arxiv.org/abs/2608.12995v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_09-19-10Z_OGR_MARL_Option_GuidedResidualMulti_AgentReinforce.md
generated_at: 2026-08-13 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces OGR-MARL, an option‑guided residual multi‑agent reinforcement learning framework for heterogeneous USV cooperative pursuit in constrained port waterways. It decouples the method from a specific MARL algorithm and adds shared evader belief, role‑conditioned targets, adaptive penalties, and residual policy learning. Experiments show that OGR-MASAC reaches 75% capture rate, outperforming other methods.

## Key Takeaways
- The framework uses a residual policy on top of rule‑guided behaviors to correct actions without full environment exploration.
- It achieves high mission effectiveness with 75% capture rate in the Xiazhimen port scenario while complying with navigation and traffic rules.
- Zero‑shot transfer to a QGIS/AIS‑informed map works without retraining, showing generalization.

## Context
This work advances MARL research by separating rule enforcement from learning, reducing reliance on complex policy architectures. It demonstrates that modular backbones can be extended with lightweight correction mechanisms, which is valuable for real‑world deployment where constraints are strict and data limited.

## Implications
Practitioners in maritime security or autonomous logistics can adopt OGR-MARL to design compliant multi‑agent systems without extensive simulation training. The approach lowers development cost and enables rapid adaptation across different port environments, fostering safer and more efficient cooperative operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12995v1)
