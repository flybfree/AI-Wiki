---
title: RACO: Reliability-Aware Coarse-Goal Optimization for Inspection-Oriented UAV Vision-Language Navigation
published: 2026-08-24T00:32:51Z
authors: Sen Wang, Yiming Sun, Jiaxuan He, Pengfei Zhu
url: http://arxiv.org/abs/2608.22678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RACO: Reliability-Aware Coarse-Goal Optimization for Inspection-Oriented UAV Vision-Language Navigation

## Abstract
UAV vision-language navigation (UAV-VLN) is commonly evaluated as goal reaching, but inspection-oriented deployment requires the agent to stop within a valid inspection region and avoid falsely confirming visually or semantically similar distractors. This requirement exposes a key weakness in existing coarse-to-fine UAV-VLN policies: the coarse goal predicted before local refinement is often treated as reliable, although it may drift toward plausible but incorrect object regions and limit the ability of the local stage to recover. To systematically evaluate this problem, we introduce LG-UVI, an object-centric inspection evaluation setting derived from CityNav/CityRefer. LG-UVI extends standard UAV-VLN episodes with target objects, hard distractors, type-aware inspection regions, and diagnostics for inspection-region arrival and object-level confirmation. To address this inspection-oriented setting, we further propose RACO, a reliability-aware adaptive coarse-to-fine navigation framework. Instead of treating the predicted coarse goal as a fixed waypoint, RACO views it as a runtime hypothesis and uses object-level candidate anchors to check and correct coarse localization before Stage 1 and at the Stage 1-to-Stage 2 boundary. RACO also applies scale-adaptive terminal refinement to handle terminal near-miss cases using runtime-observable geometric and anchor-based evidence. Under a unified online evaluation protocol, RACO improves SR over the reproduced HETT baseline by 9.53 and 7.98 percentage points on validation-unseen and test-unseen, respectively. It also improves inspection-region arrival and reduces false verification risk, showing that coarse-goal reliability optimization is an effective complement to existing coarse-to-fine UAV-VLN policies.

## Metadata
- **Published**: 2026-08-24T00:32:51Z
- **Authors**: Sen Wang, Yiming Sun, Jiaxuan He, Pengfei Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22678v1)