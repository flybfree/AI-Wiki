---
title: Decodable But Not Detachable: Training Data Granularity Determines Parametric Modularity in Large Language Models
published: 2026-08-10T20:35:43Z
authors: Marcus Armstrong, Navid Ayoobi, Arjun Mukherjee
url: http://arxiv.org/abs/2608.10214v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decodable But Not Detachable: Training Data Granularity Determines Parametric Modularity in Large Language Models

## Abstract
Do large language models contain domain-specific parametric shells: concentrated, causally necessary neuron populations whose removal selectively degrades a target domain while sparing others? We apply a uniform causal methodology across two domain granularities, three model families (1.5B to 7B parameters), and eight domains. At the academic subject level, zero neurons exceed 60\% domain selectivity across 939,008 combined FFN neurons and causal damage matrices are flat, despite domain identity being linearly decodable above 85\% accuracy. At the language and modality level, 0.65--1.14\% of neurons exceed 60\% selectivity, damage matrices are near-perfectly diagonal (ratios up to 595:1), and shell neuron sets are essentially disjoint (IoU $< 0.003$). Masking code-selective neurons reduces mathematical reasoning accuracy by 16--24 percentage points across all models; masking Spanish or Chinese neurons leaves it at or below random. Shell strength increases monotonically with scale and shells are spatially interleaved in a pattern that precludes group-level selective quantization. Parametric shells form where and only where training data was modular at the token level.

## Metadata
- **Published**: 2026-08-10T20:35:43Z
- **Authors**: Marcus Armstrong, Navid Ayoobi, Arjun Mukherjee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10214v1)