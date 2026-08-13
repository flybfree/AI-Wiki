---
title: Herding End-to-End Autonomous Driving via Neuro-Symbolic Safety Guards
url: http://arxiv.org/abs/2608.11451v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_21-27-27Z_HerdingEnd_to_EndAutonomousDrivingviaNeuro_Symboli.md
generated_at: 2026-08-12 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents a neuro‑symbolic safety guard that attaches to an end‑to‑end driving agent without retraining, ensuring compliance with traffic rules. Evaluated on long‑tail benchmarks using the TransFuser v6 model, the guard raises success rates by 15% and cuts safety‑critical collisions up to 53% while keeping the original driving score unchanged.

## Key Takeaways
- The neuro‑symbolic module checks each command against explicit safety rules before execution and substitutes unsafe actions with safe alternatives when needed.  
- Interventions are directly traceable to the rule that triggered them, providing clear accountability without adding learned components.  
- The guard improves overall success rates by 15% and reduces fatal collisions by up to 53%, demonstrating measurable safety gains alongside performance preservation.

## Context
Current end‑to‑end driving agents rely solely on statistical learning, which can produce actions that violate basic traffic rules. This creates opaque decision pathways where safety constraints are not enforced, posing risks in real‑world deployment. The proposed neuro‑symbolic guard bridges the gap between learned perception and rule‑based safety enforcement.

## Implications
For industry practitioners, the solution offers a lightweight retrofit that integrates seamlessly with existing models, avoiding costly retraining pipelines. It signals a shift toward hybrid AI approaches where symbolic reasoning enforces hard constraints, fostering trustworthy autonomous systems in high‑stakes environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11451v1)
