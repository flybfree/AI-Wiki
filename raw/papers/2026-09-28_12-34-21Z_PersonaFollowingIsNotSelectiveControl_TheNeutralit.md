---
title: Persona Following Is Not Selective Control: The Neutrality Gap in LLM User Simulation
published: 2026-09-28T12:34:21Z
authors: Jiashen Ren, Wenlin Zhang, Bohan Zhang, Xiaopeng Li, Zichuan Fu, Wanyu Wang, Junyi Li, Xiangyu Zhao
url: http://arxiv.org/abs/2609.35036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Persona Following Is Not Selective Control: The Neutrality Gap in LLM User Simulation

## Abstract
Persona prompting is widely used to construct user simulations with large language models (LLMs), yet it relies on a largely untested assumption: specifying one user attribute should change that attribute alone. We test this assumption and identify a systematic failure of selective control: across all eight black-box LLMs we audit, changing a target attribute also shifts responses on unspecified, non-target attributes. For example, describing a user as more risk-seeking shifts color choices, even though the prompt never mentions color; we term this cross-attribute influence. Semantic, contextual, and internal analyses collectively suggest that models treat a persona prompt as evidence about the user and extend the inferred profile to unspecified preferences, a process we call trait-conditioned completion. We next ask whether explicitly specifying non-target attributes restores selective control. When a non-target attribute is assigned a clear direction, models generally follow the declaration and suppress the target attribute's influence. However, when the same attribute is declared neutral, the target continues to affect choices across all five open-weight checkpoints, even when the model correctly reports the declared state. This disparity, the neutrality gap, demonstrates that successful persona following does not imply selective persona control, which additionally requires keeping non-target attributes stable. We operationalize this distinction with a three-state diagnostic that leaves the non-target attribute unspecified or declares it directional or neutral; because directional tests can be passed by simply following the stated persona, the neutral state reveals failures they miss. In a post hoc analysis of independent items, neutral declarations leave 51-81% of items target-sensitive, against at most 1 of 320 item-pole comparisons under directional ones.

## Metadata
- **Published**: 2026-09-28T12:34:21Z
- **Authors**: Jiashen Ren, Wenlin Zhang, Bohan Zhang, Xiaopeng Li, Zichuan Fu, Wanyu Wang, Junyi Li, Xiangyu Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35036v1)