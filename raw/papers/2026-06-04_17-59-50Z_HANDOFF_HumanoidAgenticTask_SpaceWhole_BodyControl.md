---
title: HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers
published: 2026-06-04T17:59:50Z
authors: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames
url: http://arxiv.org/abs/2606.06493v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

## Abstract
For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface that is intuitive, general, modular, and expressive enough for diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid whole-body controller that follows this interface and is distilled via multi-teacher KL distillation under a context-conditioned gating scheme into a mixture-of-experts student from three complementary specialists: whole-body motion tracking with safety-filtered data, locomotion, and fall-recovery. On the Unitree G1, HANDOFF matches state-of-the-art velocity tracking and offers one of the largest robust manipulation workspaces. We further demonstrate hardware feasibility through multiple natural-language-driven task roll-outs, powered by a VLM-driven agentic planner with no task-specific data or controller fine-tuning.

## Metadata
- **Published**: 2026-06-04T17:59:50Z
- **Authors**: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.06493v1)