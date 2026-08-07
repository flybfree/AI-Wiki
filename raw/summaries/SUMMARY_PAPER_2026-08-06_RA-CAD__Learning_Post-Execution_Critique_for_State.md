---
title: RA-CAD: Learning Post-Execution Critique for State-Aware Text-to-CAD Generation
url: http://arxiv.org/abs/2608.05714v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_07-52-45Z_RA_CAD_LearningPost_ExecutionCritiqueforState_Awar.md
generated_at: 2026-08-06 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
RA-CAD introduces a state‑aware agent that learns to generate post‑execution critiques as part of a Generate‑Execute‑Critique‑Rewrite loop for text‑to‑CAD systems. Experiments on CADFusion and Text2CAD show the agent reaches state‑of‑the‑art execution validity and geometric quality, outperforming existing methods and strong proprietary language models.

## Key Takeaways
- The agent produces explicit post‑execution critiques that are learned as policy actions rather than auxiliary outputs, aligning critique with observed design outcomes.  
- Feedback‑driven trajectory optimization using Group Relative Policy Optimization rewards both generated code and critique sequences, improving the overall interaction quality.  
- State awareness enables the agent to condition its critique on the original instruction, current code, and execution feedback, leading to more accurate and effective revisions.

## Context
This work addresses a gap in text‑to‑CAD generation where feedback mechanisms are not optimized for interpretation or translation into corrective actions. By treating critique as a learned policy decision within a trajectory‑level optimization framework, RA-CAD advances the integration of interactive learning with CAD code production.

## Implications
For industry practitioners, RA-CAD offers a scalable approach to reducing manual modeling effort and improving design fidelity through automated feedback loops. The methodology can be adapted to other domain‑specific generation tasks that benefit from state‑aware iterative refinement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05714v1)
