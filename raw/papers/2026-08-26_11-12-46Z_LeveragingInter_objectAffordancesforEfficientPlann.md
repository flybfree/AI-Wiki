---
title: Leveraging Inter-object Affordances for Efficient Planning in Contact-rich Tasks
published: 2026-08-26T11:12:46Z
authors: Pouya P. Niaz, Justus Piater, Alejandro Agostini
url: http://arxiv.org/abs/2608.25641v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Leveraging Inter-object Affordances for Efficient Planning in Contact-rich Tasks

## Abstract
Traditional task-and-motion planning (TAMP) approaches primarily focus on defining sequences of actions along with the necessary geometric and kinematic constraints to execute long-horizon tasks. However, their applicability in real-world settings is limited, as they typically assume simplified object models that overlook key physical properties critical for the successful execution of contact-rich tasks. Moreover, they often use sub-symbolic reasoning during motion planning, which drastically increases planning time and decreases overall success rates. We propose a method that leverages a TAMP approach, defining object-centric abstractions of execution constraints, called Unified TAMP (U-TAMP), to execute robotic tasks involving interactions among objects with heterogeneous shapes, sizes, and materials. Using a Vision-Language Model (VLM), we generate abstractions of inter-object affordances for characterizing physical interaction constraints between objects in contact-rich tasks, such as grasp and support constraints. These constraints are used to enrich the U-TAMP planning domain to deal with objects with variable physical properties. We perform experiments in simulated kitchen table organization scenarios and compare our results with those of the original U-TAMP, as well as a state-of-the-art VLM-based planner that leverages common sense knowledge of objects' affordances for plan generation. Our approach achieves significantly higher planning success rates and improves planning times by one to two orders of magnitude compared to other methods.

## Metadata
- **Published**: 2026-08-26T11:12:46Z
- **Authors**: Pouya P. Niaz, Justus Piater, Alejandro Agostini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25641v1)