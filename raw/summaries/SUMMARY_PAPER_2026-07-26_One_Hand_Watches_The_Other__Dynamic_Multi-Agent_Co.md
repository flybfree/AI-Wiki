---
title: One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments
url: http://arxiv.org/abs/2607.22119v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_09-14-07Z_OneHandWatchesTheOther_DynamicMulti_AgentCooperati.md
generated_at: 2026-07-26 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DynaMAC, a framework that enables multi‑stream robot manipulation policies to treat the opposite arm as a dynamic task parameter, overcoming the limitation of assuming external reference frames are static. The approach preserves the sample efficiency and flexibility of existing policies while handling bimanual coordination in moving environments. Experiments on DynaBench show DynaMAC outperforms leading baselines by over 35 percentage points with only 20 times fewer samples.

## Key Takeaways
- DynaMAC resolves the causal assumption that environment frames are exogenous, allowing each arm to influence the other’s motion as part of the dynamic task.  
- The framework maintains the lightweight, policy‑agnostic nature of multi‑stream policies while delivering state‑of‑the‑art performance on both static and dynamic manipulation tasks.  
- DynaBench provides a benchmark that quantifies gains in sample efficiency and zero‑shot generalization from static to dynamic settings.

## Context
Robot manipulation research has long relied on models where the environment is treated as fixed, limiting applicability to real‑world scenarios with moving objects or coordinated arms. Recent advances in multi‑stream policies have shown promise but often ignore internal dynamics, creating a gap between theory and deployment.

## Implications
DynaMAC opens pathways for safer human‑robot collaboration by enabling robots to adapt to the motion of their partners without explicit leader‑follower logic. The reduced sample requirement lowers training costs, making advanced bimanual capabilities more accessible across industry and research settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22119v1)
