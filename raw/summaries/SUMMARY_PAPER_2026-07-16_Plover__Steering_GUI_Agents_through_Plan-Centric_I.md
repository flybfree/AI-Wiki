---
title: Plover: Steering GUI Agents through Plan-Centric Interaction
url: http://arxiv.org/abs/2607.15193v1
type: paper-summary
date: 2026-07-16
source_paper: 2026-07-16_16-48-39Z_Plover_SteeringGUIAgentsthroughPlan_CentricInterac.md
generated_at: 2026-07-16 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Plover, a plan‑centric vision‑based GUI automation system that externalizes task plans and replanning as persistent artifacts. By using a planner–executor architecture it enables inspectable supervision, localized corrections, natural‑language guidance, and screenshot‑grounded interventions while preserving prior progress during repair.

## Key Takeaways
- Plover treats plans as visible, editable objects that can be inspected and revised by users to correct autonomous GUI actions.  
- The system supports explicit replanning which makes failures structurally repairable without restarting the whole task.  
- Human participants found the plan‑centric interface improves transparency, controllability, and adaptability of GUI automation.

## Context
Autonomous agents that interact with graphical interfaces often fail because their internal planning is hidden from users. Traditional approaches rely on deep perception but lack a mechanism for transparent correction or supervision. This paper addresses those gaps by making the planning process an external, user‑controllable artifact.

## Implications
For researchers, Plover offers a framework to study how visible plans affect system performance and user trust. For industry practitioners, it suggests that integrating explicit plan management could lead to more reliable assistive tools in complex UI environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15193v1)
