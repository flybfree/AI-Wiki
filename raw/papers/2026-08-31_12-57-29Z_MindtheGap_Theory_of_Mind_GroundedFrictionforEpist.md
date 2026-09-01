---
title: Mind the Gap: Theory-of-Mind-Grounded Friction for Epistemic Alignment
published: 2026-08-31T12:57:29Z
authors: Yifan Zhu, Kyeongmin Rim, James Pustejovsky
url: http://arxiv.org/abs/2608.30719v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mind the Gap: Theory-of-Mind-Grounded Friction for Epistemic Alignment

## Abstract
Productive dialogue alignment requires distinguishing \emph{surface coordination} (acknowledgments and smooth task progression) from \emph{epistemic alignment} (convergence of belief states); standard preference-based methods typically optimize response-level preferences without explicitly modeling the latter. We operationalize Theory-of-Mind (ToM) inference as a control signal within Frictive Policy Optimization by extracting, at each referring expression, a four-part belief structure: the speaker's intended referent, the addressee's interpretation, and each participant's model of the other's belief. This makes friction mechanically computable from epistemic-state comparisons, capturing \emph{silent divergence}, where both participants proceed confidently while grounding to different referents. We evaluate the signal at two levels. At the representation level, ablating the second-order channel reduces misunderstanding recall from $65\%$ to $26\%$. At the policy level, reward-shaping (FAR) and trust-region (FTR) variants improve intervention F1 and warranted-context calibration over DPO, with Brier scores independently supporting the calibration gains. Across three training runs, FAR and FTR remain substantially more stable, whereas DPO varies widely and can degrade intervention competence already present in the base policy. Thus, ToM-grounded friction provides a trainable signal for context-sensitive intervention under referential belief divergence.

## Metadata
- **Published**: 2026-08-31T12:57:29Z
- **Authors**: Yifan Zhu, Kyeongmin Rim, James Pustejovsky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30719v1)