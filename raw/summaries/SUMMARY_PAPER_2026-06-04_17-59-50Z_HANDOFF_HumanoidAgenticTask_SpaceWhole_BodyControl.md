---
title: HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers
url: http://arxiv.org/abs/2606.06493v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-04_17-59-50Z_HANDOFF_HumanoidAgenticTask_SpaceWhole_BodyControl.md
generated_at: 2026-06-11 10:53
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces HANDOFF, a compact whole‑body controller that bridges task planning and robot motion without requiring dense kinematic or spatial references. By distilling three complementary specialists—motion tracking with safety filtering, locomotion, and fall recovery—into a mixture‑of‑experts student, HANDOFF achieves state‑of‑the‑art performance on the Unitree G1 while supporting large manipulation workspaces.

## Key Takeaways
- The controller uses a context‑conditioned gating scheme to blend three expert modules, allowing it to handle diverse manipulation tasks without task‑specific fine‑tuning.  
- HANDOFF matches state‑of‑the‑art velocity tracking on the Unitree G1 and offers one of the largest robust manipulation workspaces reported.  
- The system is distilled via multi‑teacher KL distillation, making it compact and generalizable across different skill sets.

## Context
Whole‑body control remains a bottleneck for humanoid robots because planners cannot easily translate high‑level task semantics into precise kinematic commands. This work shows that an explicit, modular interface can circumvent the need for dense sensor data, aligning with trends toward end‑to‑end and agentic AI systems.

## Implications
For robotics engineers, HANDOFF provides a practical pathway to deploy humanoid robots in real‑world settings using natural‑language driven planning. Practitioners can rely on a single controller that scales across tasks, reducing development time and hardware complexity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.06493v1)
