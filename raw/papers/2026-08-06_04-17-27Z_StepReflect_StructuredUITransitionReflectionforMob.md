---
title: StepReflect: Structured UI Transition Reflection for Mobile GUI Agents
published: 2026-08-06T04:17:27Z
authors: Linqiang Guo, Wei Liu, Li Gu, Yang Wang,  Tse-Hsun,  Chen
url: http://arxiv.org/abs/2608.05587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StepReflect: Structured UI Transition Reflection for Mobile GUI Agents

## Abstract
Autonomous mobile GUI agents require accurate action reflection for reliable long-horizon execution. Existing approaches rely on open-ended multimodal reasoning after each action, which is costly and poorly matched to the structured nature of GUI state transitions. We propose StepReflect, which formulates per-step GUI reflection as supervised structured prediction conditioned on explicit transition specifications and paired visual evidence. StepReflect is trained through a staged pipeline combining supervised fine-tuning, teacher-student distillation, and preference- and reward-based refinement. Offline, the resulting 8B model achieves 82.16% transition-level accuracy on AndroidWorld, exceeding zero-shot GPT-5.2 by 11.83 percentage points under the same structured input. Online, across M3A, Agent-SAMA, MAI-UI-8B, and Seed-2.0-Pro, StepReflect achieves higher task success in three of four agent configurations and remains within one successful task of the GPT-5.2 Reflection Agent in the fourth. It also reduces paid API charges relative to GPT-based reflection in all four configurations. These results establish StepReflect as a practical, locally deployable alternative to repeated frontier-model reflection for long-horizon mobile GUI agents.

## Metadata
- **Published**: 2026-08-06T04:17:27Z
- **Authors**: Linqiang Guo, Wei Liu, Li Gu, Yang Wang,  Tse-Hsun,  Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05587v1)