---
title: Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills
url: http://arxiv.org/abs/2608.01851v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-58-35Z_WeightsorSkills_ASurveyofRobot_LearningTechniques_.md
generated_at: 2026-08-03 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper surveys robot‑learning techniques by organizing them around the axis of “weights versus skills,” arranging 77 representative systems across six technique families into a taxonomy and providing contrast tables that define self‑improvement mechanisms for each family. The analysis reveals how code‑as‑policy methods evolve from zero‑shot synthesis to persistent skill memory, while skill discovery spans unsupervised reinforcement learning and large‑language‑model libraries.

## Key Takeaways
- Code‑as‑policy methods are grouped by their degree of self‑improvement, ranging from static zero‑shot program synthesis through closed‑loop repair and persistent skill memory to an open‑ended loop where feedback, memory, and evolutionary search converge; only a few systems such as ASPIRE, ENPIRE, and RoboClaw occupy this last cell.  
- The term “skill” is employed in at least five distinct senses across the literature, with only the code sense enabling self‑improvement without gradient updates.  
- Recent skill‑economy marketplaces distribute one‑tap static playback skills to robots, highlighting open problems of adaptation, cross‑embodiment portability, provenance, safety verification, composition, and standardisation.

## Context
Robot learning is bifurcating into two camps: policies that embed competence in frozen weights (vision‑language‑action models) and agents that generate executable skills as code. This survey situates these approaches within a broader AI landscape where dynamic skill generation competes with static policy deployment, influencing how robots interact with human operators and other robotic systems.

## Implications
The findings stress the need for standards and tooling to address adaptation, portability, safety verification, composition, and provenance of dynamically generated skills. Practitioners should anticipate that future robot ecosystems will require mechanisms to compose, verify, and evolve skills beyond simple playback, driving both research and industry investment in robust skill management frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01851v1)
