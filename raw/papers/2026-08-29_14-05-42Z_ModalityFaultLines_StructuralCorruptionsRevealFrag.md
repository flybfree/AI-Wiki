---
title: Modality Fault Lines: Structural Corruptions Reveal Fragile Omni-Modal Reasoning
published: 2026-08-29T14:05:42Z
authors: Zhaolu Kang, Meixin Wu, Yu Xue, Yingjie He, Qiming Shi, Lei Wei, Yidi Wang, Richeng Xuan, Zhichao Hu
url: http://arxiv.org/abs/2608.29278v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modality Fault Lines: Structural Corruptions Reveal Fragile Omni-Modal Reasoning

## Abstract
Omni-modal large language models are increasingly evaluated on clean text--vision--audio inputs, where every channel is present, synchronized, and readily interpretable. Such scores are often taken as evidence of robust cross-modal fusion, but clean evaluation cannot tell whether success depends on stable cross-modal structure or on cues sufficient only in intact inputs. To address this gap, we define a modality fault line: a boundary at which model behavior becomes unstable when a modality remains present and human-interpretable, but its internal evidence structure is perturbed. We introduce SCEval (Structure-Corruption Evaluation) a diagnostic evaluation protocol that keeps the question, answer space, and modality channels fixed while applying controlled structural corruptions to text, vision, and audio individually and jointly. Built from $273$ human-verified tri-modal examples from Social-IQ, OmniBench, and VALOR, SCEval evaluates $15$ proprietary and open-source omni-modal systems. The results show that structural corruption lowers clean accuracy, text--vision damage forms the most stable shared fault line, and multi-modal degradation is non-additive rather than a simple function of the number of corrupted modalities. Clean omni-modal accuracy therefore does not establish that a model will remain reliable when cross-modal evidence becomes structurally unreliable.

## Metadata
- **Published**: 2026-08-29T14:05:42Z
- **Authors**: Zhaolu Kang, Meixin Wu, Yu Xue, Yingjie He, Qiming Shi, Lei Wei, Yidi Wang, Richeng Xuan, Zhichao Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29278v1)