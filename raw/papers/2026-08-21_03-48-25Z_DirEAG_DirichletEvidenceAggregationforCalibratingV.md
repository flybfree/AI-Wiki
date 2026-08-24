---
title: DirEAG: Dirichlet Evidence Aggregation for Calibrating Verbalized Confidence in Mathematical Reasoning
published: 2026-08-21T03:48:25Z
authors: Haorui Xu, Yuzhou Zhu, Liyuan Gao
url: http://arxiv.org/abs/2608.20717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DirEAG: Dirichlet Evidence Aggregation for Calibrating Verbalized Confidence in Mathematical Reasoning

## Abstract
Reliable confidence estimation is essential for using large language models in mathematical reasoning, but black-box verbalized confidence is difficult to calibrate. When the same problem is queried under multiple confidence-steering prompts, the resulting answer-confidence observations contain useful uncertainty information, yet their scales may shift across steering levels, models, and datasets. Existing black-box uncertainty methods often rely on answer agreement, sample consistency, or entropy, which describe output variation but do not model the numerical meaning of self-reported confidence. Conversely, direct averaging or heuristic aggregation of elicited confidence cannot learn prompt- and task-dependent bias. We propose DirEAG, a Dirichlet Evidence Aggregation method that converts each elicited answer-confidence observation into calibrated soft evidence over generated candidate answers and an additional null state, allowing the model to represent cases where none of the candidates is correct. Experiments on GSM8K, SVAMP, and GSM-Hard with Qwen, Mistral, and Gemma models show that, compared with direct confidence averaging and heuristic confidence-steering aggregation, DirEAG often achieves better calibration while maintaining competitive answer selection. Ablations further reveal that evidence aggregation and final binary calibration address distinct parts of the calibration problem.

## Metadata
- **Published**: 2026-08-21T03:48:25Z
- **Authors**: Haorui Xu, Yuzhou Zhu, Liyuan Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20717v1)