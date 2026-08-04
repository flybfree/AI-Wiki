---
title: Rapid Embodiment Adaptation for Quadrupedal Locomotion
published: 2026-08-02T21:31:49Z
authors: Dichen Li, Bo Ai, Nico Bohlinger, Jan Peters, Hao Su, Henrik I. Christensen
url: http://arxiv.org/abs/2608.01506v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rapid Embodiment Adaptation for Quadrupedal Locomotion

## Abstract
Humans readily adapt their movements as their bodies change through aging, injury, or load carrying, but learning-based robot policies often break when hardware properties shift. We introduce an online embodiment adaptation framework for quadrupedal locomotion that infers embodiment parameters from short interaction histories and conditions control on the inferred hardware state. Our method pairs a generalist policy trained under embodiment randomization with a lightweight adaptation module that identifies physical changes within half a second. We evaluate two representative forms of embodiment variation: joint-range constraints and trunk-mass changes, corresponding to joint-level kinematic degradation and body-level dynamic variation. In simulation, the module accurately estimates these changes and enables closed-loop control that substantially outperforms policies conditioned directly on interaction history. On a real Unitree Go2 robot, our system maintains stable locomotion under severe instances of the evaluated changes, including a fully locked leg and a 5 kg payload, where non-adaptive methods fail. These results demonstrate the practicality of explicit online embodiment identification for rapid adaptation to joint-limit and payload-mass changes, and provide a step toward handling broader forms of uncertain, degraded, or changing robot hardware.

## Metadata
- **Published**: 2026-08-02T21:31:49Z
- **Authors**: Dichen Li, Bo Ai, Nico Bohlinger, Jan Peters, Hao Su, Henrik I. Christensen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01506v1)