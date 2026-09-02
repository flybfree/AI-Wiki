---
title: SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems
published: 2026-09-01T02:34:44Z
authors: Rui Yang, Junjie Xu, Zhengyu Liu, Neil Fendley, Yang Hong, Ziyang Li, Yinzhi Cao
url: http://arxiv.org/abs/2609.00595v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems

## Abstract
Safe agents can fail together. Multi-agent LLM systems (MAS) move information, state, decisions, and authority across principal boundaries, creating failures that local checks may miss. Without an execution-level view, a multi-agent setting can easily be mistaken for evidence of a genuinely multi-agent security effect. We thus systematize MAS security through an execution-centered analysis of 197 works, covering six interaction interfaces, four adversary positions, seven system-level risks, and eight recurring attack paths. We introduce an A-I-R framework that organizes attacks by adversary position, interaction interface, and resulting system-level risk, unifying otherwise fragmented attack mechanisms across MAS. We organize defenses through a five-part contract covering path target, observation, intervention, trust boundary, and recovery, and identify path closure and recovery as key challenges. We audit 44 evaluation and benchmark works and identify open challenges in isolating interaction effects, designing comparable and diagnostic metrics, supporting reuse across MAS designs, and evaluating open-system operation. Together, these findings motivate an interaction-aware view of MAS security: trace attacks end to end, test whether defenses close those paths, and evaluate system-level effects with appropriate counterfactuals.

## Metadata
- **Published**: 2026-09-01T02:34:44Z
- **Authors**: Rui Yang, Junjie Xu, Zhengyu Liu, Neil Fendley, Yang Hong, Ziyang Li, Yinzhi Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00595v1)