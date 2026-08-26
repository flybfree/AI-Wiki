---
title: Reflection with Action-Induced Visual Differences for Desktop GUI Agents
published: 2026-08-25T03:10:01Z
authors: Yijie Ma, Chaoyue Niu, Fan Wu, Guihai Chen
url: http://arxiv.org/abs/2608.24015v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reflection with Action-Induced Visual Differences for Desktop GUI Agents

## Abstract
The Planner-Operator-Reflector (POR) framework is widely used in GUI agents to maintain objective alignment in complex tasks through modular collaboration. However, desktop GUIs introduce a key challenge: large, dense interfaces often exhibit subtle or scattered state changes, placing most of the burden on the reflector, which must compare pre- and post-action screens, while the planner and operator reason over a single state. Existing reflectors collapse change detection and outcome verification into one step, leaving evidence implicit and yielding weakly grounded decisions. To address this limitation, we propose Evidence-First Reflection (EFR), a two-stage reflector that explicitly decouples action-induced visual differences extraction from outcome verification. EFR identifies the action location and candidate changed regions with Set-of-Marks annotations, describes and filters action-relevant changes, and makes the final judgment from the cleaned evidence. This evidence-reasoning decoupled design makes reflection better grounded in screen transitions, while reducing both visual search complexity and reasoning burden. Experiments on OSWorld-Verified and WindowsAgentArena demonstrate that EFR improves reflector accuracy by 7.11%, yielding average end-to-end task success gains of 5.94% and 4.95% on the two benchmarks, respectively.

## Metadata
- **Published**: 2026-08-25T03:10:01Z
- **Authors**: Yijie Ma, Chaoyue Niu, Fan Wu, Guihai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24015v1)