---
title: Leveraging Inter-object Affordances for Efficient Planning in Contact-rich Tasks
url: http://arxiv.org/abs/2608.25641v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_11-12-46Z_LeveragingInter_objectAffordancesforEfficientPlann.md
generated_at: 2026-08-26 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Unified TAMP (U‑TAMP) which adds object‑centric affordance abstractions to traditional task‑and‑motion planning for contact‑rich tasks. By using a Vision‑Language Model they generate constraints such as grasp and support that account for heterogeneous shapes, sizes and materials. Experiments on simulated kitchen table organization show U‑TAMP reaches higher success rates and dramatically reduces planning time compared with prior methods.

## Key Takeaways
- Unified TAMP defines object‑centric abstractions of execution constraints to capture physical interaction limits between objects.
- The Vision‑Language Model generates these affordance constraints automatically, enabling the planner to handle variable material properties without hard‑coding them.
- Experiments demonstrate a one to two orders of magnitude improvement in planning success and a reduction in planning time.

## Context
Contact‑rich tasks are central to domestic robotics where robots must organize objects on tables. Existing TAMP frameworks ignore physical affordances, leading to brittle plans that fail when object properties change. This work bridges the gap by integrating semantic knowledge with geometric constraints for more robust planning.

## Implications
Practitioners can adopt U‑TAMP to build planners that adapt to real‑world variability without extensive re‑programming. The approach offers a scalable framework for deploying robots in kitchens, warehouses and other environments where object interactions are frequent.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25641v1)
