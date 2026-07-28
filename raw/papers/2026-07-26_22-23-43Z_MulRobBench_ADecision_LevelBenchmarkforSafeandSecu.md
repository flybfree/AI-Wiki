---
title: MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents
published: 2026-07-26T22:23:43Z
authors: Belal S. Alsinglawi, Weizheng Wang, Junyi Wu, Yi Jiang, Lianhai Lin, Merouane Debbah, Izzat Alsmadi
url: http://arxiv.org/abs/2607.23870v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents

## Abstract
Smart-city airspace is transforming Uncrewed Aerial Vehicles (UAVs) from passive sensing platforms into cyber-physical decision makers that must follow operational rules under degraded observations and ambiguous language. Existing UAV and multimodal benchmarks evaluate perception, navigation, collaboration, and reasoning, but few assess whether physical evidence, protocol constraints, and action risk remain coupled during critical decisions. We introduce MulRobBench, an offline, protocol-conditioned benchmark for Vision-Language-Action (VLA) UAV agents in smart-city environments. MulRobBench integrates real UAV multimodal observations, protocol-level security policies, and action-level cyber-physical safety into a unified evaluation framework. The benchmark contains 3,024 samples spanning 17 task taxonomy nodes and 12 scoring dimensions across four stages: operational context understanding, multimodal evidence arbitration, degradation-aware reasoning, and risk-aware action planning. Evaluation combines semantic scoring with structural diagnostics, including policy compliance, format compliance, unsafe actions, parsing failures, and dimension-level validity. Across 17 multimodal models, the best semantic protocol-decision score reaches only 0.5141, while the best strict mean scoring-dimension accuracy is 0.1599. A controlled 20-anchor modality-ablation study changes 4-15 action selections per model, confirming that both visual and textual inputs influence decisions. Analysis identifies modality-trust selection, constraint extraction, glare, missing data, and operator shorthand as the primary causes of decision instability. MulRobBench provides a reproducible benchmark for trustworthy multimodal UAV decision making under realistic operational constraints.

## Metadata
- **Published**: 2026-07-26T22:23:43Z
- **Authors**: Belal S. Alsinglawi, Weizheng Wang, Junyi Wu, Yi Jiang, Lianhai Lin, Merouane Debbah, Izzat Alsmadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23870v1)