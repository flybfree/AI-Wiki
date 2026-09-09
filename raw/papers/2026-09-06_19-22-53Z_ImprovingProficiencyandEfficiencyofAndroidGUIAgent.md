---
title: Improving Proficiency and Efficiency of Android GUI Agents via Self-Generating Tool Actions
published: 2026-09-06T19:22:53Z
authors: Juyong Lee, Woogyeol Jin, Kimin Lee
url: http://arxiv.org/abs/2609.06792v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Proficiency and Efficiency of Android GUI Agents via Self-Generating Tool Actions

## Abstract
Android agents using a hybrid action space that combines GUI actions and tool actions (e.g., accessing application data via APIs) remain largely underexplored, mainly due to the excessive effort required to create tools. To address this gap, we introduce DroidTool, a framework for augmenting the agents with self-generated tools, which are realized as Python functions operating on application states (e.g., a database). To create tools with minimal human labor, DroidTool employs an agentic workflow featuring stages: proposal, implementation, test generation and execution, and repair. Notably, when testing the created tools for verification, it constructs relational tests across relevant tools for natural preparation of appropriate test preconditions and improved test coverage, rather than testing each tool separately. The GUI agents augmented with the generated tools achieved approximately 4.47%p higher performance with approximately 20.05% fewer interactions than the GUI-only agents, averaged across representative benchmarks: AndroidWorld, B-MoCA, and MobileSafetyBench.

## Metadata
- **Published**: 2026-09-06T19:22:53Z
- **Authors**: Juyong Lee, Woogyeol Jin, Kimin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06792v1)