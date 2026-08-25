---
title: DIAG: Diagnostic Iterative Alignment and Generation for Data-Efficient Mathematical Preference Distillation
published: 2026-08-24T05:09:12Z
authors: Guhan Chen, Songtao Tian, Bohan Li, Hejin Wang, YeXin Xie, Zixiong Yu
url: http://arxiv.org/abs/2608.22806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DIAG: Diagnostic Iterative Alignment and Generation for Data-Efficient Mathematical Preference Distillation

## Abstract
Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-informative, which leads to a scarcity of valid preference pairs. We propose DIAG, a Diagnostic Iterative Alignment and Generation framework that adaptively reshapes the practice distribution to increase informative supervision and focus training near the student's current competence boundary. DIAG consists of two phases: (1) diagnosing valid preference-pair yield to calibrate the exploration-exploitation trade-off and allocate topic quotas via an Empirical Bayes shrinkage estimator, thereby prioritizing high-yield concepts; and (2) generating targeted practice, where a teacher synthesizes variants from the student's failure traces. We further provide a theoretical view interpreting DIAG as a teacher-mediated approximation to KL-regularized reweighting of the practice distribution toward the student's competence boundary, where valid preference-pair yield is maximized. Experiments show that DIAG boosts yield across iterations and delivers stronger reasoning performance under an iso-effective training budget, demonstrating that it can distill more informative preference supervision for mathematical reasoning.

## Metadata
- **Published**: 2026-08-24T05:09:12Z
- **Authors**: Guhan Chen, Songtao Tian, Bohan Li, Hejin Wang, YeXin Xie, Zixiong Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22806v1)