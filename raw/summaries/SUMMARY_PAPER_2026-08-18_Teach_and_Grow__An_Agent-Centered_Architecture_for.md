---
title: Teach and Grow: An Agent-Centered Architecture for General Robot Learning
url: http://arxiv.org/abs/2608.17209v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_23-45-21Z_TeachandGrow_AnAgent_CenteredArchitectureforGenera.md
generated_at: 2026-08-18 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Teach-and-Grow Learning (TGL), an agent‑centered framework that converts a few successful demonstrations into reusable Skill Blocks for general robot tasks. The architecture enables robots to compose learned behaviors, adapt when execution fails, and store both skill libraries and experience memories without retraining policies. Experiments show state‑of‑the‑art performance on LIBERO and demonstrate persistent reuse of skills across new scenes.

## Key Takeaways
- TGL creates closed‑loop Skill Blocks from demonstrations that can be composed in novel environments, reducing the need for task‑specific policy updates.
- The system maintains a structured Experience Memory that records successes, failures, and repairs, allowing continuous learning after deployment.
- Performance follows a power‑law scaling law where future‑task error and teaching demand depend on the amount of effective reusable experience.

## Context
General robotics aims to build systems that generalize across diverse tasks and environments without extensive retraining. Current approaches often require large amounts of labeled data or manual intervention, which is costly for embodied agents. TGL’s agent‑driven pipeline addresses this bottleneck by leveraging in‑situ demonstrations and adaptive composition.

## Implications
For industry, TGL reduces the “retraining tax” that plagues vision‑language‑action systems, enabling faster deployment of new capabilities. Practitioners can rely on a skill library that evolves with experience, leading to more robust and cost‑effective robotic solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17209v1)
