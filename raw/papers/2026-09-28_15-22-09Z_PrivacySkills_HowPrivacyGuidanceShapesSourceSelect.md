---
title: PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents
published: 2026-09-28T15:22:09Z
authors: Lucas Biechy, Cédric Eichler, Héber H. Arcolezi, Nicolas Anciaux
url: http://arxiv.org/abs/2609.35937v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents

## Abstract
While prior work has documented privacy failures in LLM agents, it remains unclear how the presentation of privacy guidance influences their choice of information sources. We introduce PrivacySkills, a controlled framework for evaluating how agents choose among acquisition pathways that provide the same task-relevant value: consulting publicly available personal information, accessing confidential sources, or interacting with the user. The evaluation framework comprises 55 synthetic tasks spanning 11 categories of personal information, with 169 associated skills that describe the available acquisition pathways. We consider privacy guidance through system-level instructions, skill-level metadata labels, or both. Separately, we vary user availability and urgency framing. With users available and no privacy guidance, agents access confidential sources in 30% of valid runs on average across five open-weight models, despite sufficient alternatives. This rate increases to 45% when users are unavailable, whereas urgency framing has no detectable effect. System-level privacy instructions alone have limited effects on confidential access, while skill-level intrusiveness labels produce a modest reduction (24% on average), but combining the two roughly halves confidential access. Our findings motivate incorporating privacy annotations into skill specifications and evaluating their effectiveness alongside system-level instructions.

## Metadata
- **Published**: 2026-09-28T15:22:09Z
- **Authors**: Lucas Biechy, Cédric Eichler, Héber H. Arcolezi, Nicolas Anciaux
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35937v1)