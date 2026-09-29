---
title: Measurement Boundaries in LLM Financial Agent Evaluation: Fixed-Tape Execution and Multi-Defect Auditing
published: 2026-09-26T08:54:21Z
authors: Weicheng Xue
url: http://arxiv.org/abs/2609.32379v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measurement Boundaries in LLM Financial Agent Evaluation: Fixed-Tape Execution and Multi-Defect Auditing

## Abstract
What controls are needed to interpret execution performance and audit scores in LLM agent evaluations? We study two limits on these interpretations in a financial agent harness. In Study~A, comparing independent runs under idealized and stressed execution on three synthetic settings that share one 24-day upward phase mixes the execution rule with fresh model responses and portfolio feedback: the parsed decision paths agree in only $19.8\%$ of $450$ pairs. Replaying each stored response tape through both execution destinations gives a narrower result. Conditional on those responses, stressed execution changes total return by $-0.0170$ (95\% interval $[-0.0230,-0.0117]$), or $10.4\%$ of the idealized baseline, and ten seed clusters do not resolve the model ranking. Study~B corrects an incomplete answer key and replaces legacy tasks with matched zero-, one-, and two-defect tasks under an explicit multi-label prompt. The drop in target violation recall from one to two defects is positive in five of six combinations of auditor and source (median $0.267$), with three surviving Holm correction. Yet the auditor that includes both target labels most often has micro-precision $0.149$, emits findings on $98/100$ zero-defect tasks, and returns the exact dual-defect set in only $21/100$ cases. Target recall by itself therefore gives a poor account of audit quality on this construction. The studies address different limits: what an execution comparison estimates, and what target recall captures. Together, they show how fixed conditions and diagnostic controls bound the claims a score can support.

## Metadata
- **Published**: 2026-09-26T08:54:21Z
- **Authors**: Weicheng Xue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32379v1)