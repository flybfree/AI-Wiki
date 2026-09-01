---
title: The Differential Reasoning Router: Operationalizing Cost-Aware LLM Annotation in E-commerce
published: 2026-08-31T04:11:39Z
authors: Cheng Lyu, Jingyue Zhang, Vinny DeGenova, Mengwei Li, Yuanli Pei
url: http://arxiv.org/abs/2608.30224v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Differential Reasoning Router: Operationalizing Cost-Aware LLM Annotation in E-commerce

## Abstract
Large Language Models (LLMs) are increasingly used to annotate structured product data in e-commerce, but early deployment often begins as a cold-start problem: only limited pre-launch labels are available, the value of expensive reasoning is unknown, and human review is needed before the system can be trusted at scale. This challenge is especially common in rule-based annotation workflows, where each item must satisfy multiple business rules and both model errors and ambiguous rule boundaries affect final decisions. We introduce the Differential Reasoning Router (DRR), a cost-aware framework for cold-start LLM annotation that jointly optimizes model selection and human escalation. Rather than treating a reasoning model as a default fallback, DRR estimates separate success probabilities for a direct model and a reasoning model at both the sample and business-rule levels, enabling adaptive routing: easy cases are handled directly, reasoning is reserved for cases where it is expected to improve the decision, and likely double-failure or rule-disagreement cases are escalated to human annotators. The resulting labels provide targeted ground truth for prompt engineering, supervised fine-tuning, calibration, and rule refinement, enabling a gradual shift from human-heavy cold-start annotation toward high-confidence automated routing. In a production e-commerce workflow, DRR reaches accuracy parity with the strongest confidence-based router while achieving more than 60\% reasoning-token cost savings.

## Metadata
- **Published**: 2026-08-31T04:11:39Z
- **Authors**: Cheng Lyu, Jingyue Zhang, Vinny DeGenova, Mengwei Li, Yuanli Pei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30224v1)