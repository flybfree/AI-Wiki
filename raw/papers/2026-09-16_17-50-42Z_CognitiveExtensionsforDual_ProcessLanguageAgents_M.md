---
title: Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments
published: 2026-09-16T17:50:42Z
authors: João Meneses dos Santos, Arlindo L. Oliveira
url: http://arxiv.org/abs/2609.19128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection in Interactive Environments

## Abstract
Language agents remain brittle in interactive environments, where success requires long-horizon state tracking, valid action execution, and recovery from failed steps. We extend SwiftSage, a dual-process agent that combines a fast action proposer with a slower planner, using two modular cognitive extensions: an Adaptive Memory Module (AMM) for salience-gated episodic storage and trigger-driven retrieval, and a Self-Reflection Module (SRM) for bounded execution-time validation and corrective intervention. Both modules are implemented as feature-flagged extensions over the same execution substrate, enabling controlled ablations on ScienceWorld. Across four configurations---baseline, baseline+AMM, baseline+SRM, and the full system---the full system achieves the best mean final score (64.62), success rate (43.17%), and successful-step efficiency (19.33 steps), while SRM is the strongest standalone contributor. The results suggest that execution-time control is the dominant bottleneck in this setting, while episodic memory becomes most useful once the runtime loop is stabilized.

## Metadata
- **Published**: 2026-09-16T17:50:42Z
- **Authors**: João Meneses dos Santos, Arlindo L. Oliveira
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19128v1)