---
title: SynAct: A Reasoning-Acting Large Language Model Agent for Adaptive Synthesis Optimization
published: 2026-08-13T03:02:25Z
authors: Fangzhou Liu, Peiyi Han, Jiawei Liu, Yuan Pu, Zhuolun He, Rongliang Fu, Tsung-Yi Ho, Bei Yu
url: http://arxiv.org/abs/2608.12751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SynAct: A Reasoning-Acting Large Language Model Agent for Adaptive Synthesis Optimization

## Abstract
Logic synthesis transforms RTL designs into gate-level netlists, where PPA results are highly sensitive to the choice of optimization commands, making synthesis tuning both high-dimensional and expensive. Previous approaches fall into two categories: automated methods, which perform black-box search over fixed action spaces with limited decision-level interpretability, and LLM-based methods, which typically generate static scripts upfront and cannot adapt to evolving circuit states. We present SynAct, an adaptive closed-loop LLM reasoning--acting agent that iteratively diagnoses live synthesis reports and reasons over the current circuit state, retrieved tool knowledge, and historical optimization experience to issue targeted commands. SynAct focuses on improving timing, particularly worst negative slack (WNS), while maintaining balanced area and power trade-offs. Experiments on a commercial synthesis tool across 14 designs show that SynAct reduces average WNS to 27% of that from bootstrap synthesis.

## Metadata
- **Published**: 2026-08-13T03:02:25Z
- **Authors**: Fangzhou Liu, Peiyi Han, Jiawei Liu, Yuan Pu, Zhuolun He, Rongliang Fu, Tsung-Yi Ho, Bei Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12751v1)