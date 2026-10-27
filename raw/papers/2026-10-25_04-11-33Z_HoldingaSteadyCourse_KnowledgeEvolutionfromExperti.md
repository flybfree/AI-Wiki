---
title: Holding a Steady Course: Knowledge Evolution from Expertise and Lessons for Continual Agent Learning
published: 2026-10-25T04:11:33Z
authors: Wenzhe Fan, Benjamin Steenhoek, Gaurav Mittal, Yu Hu
url: http://arxiv.org/abs/2610.34043v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Holding a Steady Course: Knowledge Evolution from Expertise and Lessons for Continual Agent Learning

## Abstract
Autonomous agents are increasingly deployed across sequences of related tasks, yet they often fail to retain and improve their knowledge over time. Existing approaches convert interaction trajectories into memories or reusable skills, but experience is not automatically reliable knowledge. Automatically collected skills and memories can propagate errors, mislead, and corrupt useful knowledge. To address this gap, we introduce Knowledge Evolution from Expertise and Lessons (KEEL), an agent-agnostic framework that uses verifier evidence to transform successful behavior into reusable skills and failures into corrective lessons. As new evidence accumulates, individual skill claims can be supported, contradicted, replaced, or retired. On SkillFlow benchmark, KEEL improves task success by 4.2 to 21.7 percentage points over the no-knowledge baseline, compared with gains of 2.4 to 9.6 points from SkillFlow's default method. Ablations show that skills and lessons are complementary. These results show that reliable continual agent learning depends not simply on accumulating experience, but on continually validating and evolving the knowledge derived from it. Our code is available at: https://github.com/microsoft/KEEL-TTCL26.

## Metadata
- **Published**: 2026-10-25T04:11:33Z
- **Authors**: Wenzhe Fan, Benjamin Steenhoek, Gaurav Mittal, Yu Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34043v1)