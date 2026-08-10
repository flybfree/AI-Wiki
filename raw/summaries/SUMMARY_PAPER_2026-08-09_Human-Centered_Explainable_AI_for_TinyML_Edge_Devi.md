---
title: Human-Centered Explainable AI for TinyML Edge Devices: A Pareto-Based Selection Framework with LLM-Guided Design
url: http://arxiv.org/abs/2608.07091v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_10-40-53Z_Human_CenteredExplainableAIforTinyMLEdgeDevices_AP.md
generated_at: 2026-08-09 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a human-centered explainable AI selection framework for TinyML edge devices that balances explanation quality with computational and deployment constraints. It uses an LLM‑guided interface to map stakeholder preferences to XAI methods, then applies Pareto optimization to reveal trade‑offs between fidelity, stability and proxy cost. The evaluation on skin lesion classification demonstrates how the method identifies efficient trade‑off points.

## Key Takeaways
- The framework translates qualitative stakeholder preferences into quantitative criteria for XAI method selection using an LLM‑driven mapping step.
- Pareto optimization is employed to generate a set of non‑dominated solutions that balance explanation fidelity, algorithmic stability and proxy‑based deployment cost.
- The study shows that the selected trade‑off points can be identified without physical MCU testing or human validation.

## Context
Explainable AI is essential for trustworthy edge deployments where clinicians rely on model outputs. TinyML imposes severe computational limits, making method selection a critical design decision. This work bridges these two domains by formalizing XAI choice as an optimization problem.

## Implications
Practitioners can adopt this framework to prioritize explanations that align with user needs while staying within hardware budgets. The approach could be extended to other medical and industrial TinyML applications, fostering more transparent and efficient AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07091v1)
