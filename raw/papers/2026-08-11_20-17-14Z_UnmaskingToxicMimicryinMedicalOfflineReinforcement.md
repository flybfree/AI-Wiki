---
title: Unmasking Toxic Mimicry in Medical Offline Reinforcement Learning for ICU Sepsis Management via Counterfactual Clinical Audits
published: 2026-08-11T20:17:14Z
authors: Hangqi Ren, Junyi Liao
url: http://arxiv.org/abs/2608.11410v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unmasking Toxic Mimicry in Medical Offline Reinforcement Learning for ICU Sepsis Management via Counterfactual Clinical Audits

## Abstract
Offline reinforcement learning (RL) offers considerable promise for optimizing ICU treatment decisions, yet standard evaluation metrics Mean Squared Error (MSE) and Fitted Q-Evaluation (FQE) assess only behavioral imitation and cannot detect Toxic Mimicry, a failure mode in which agents replicate harmful patterns such as treatment withdrawal during comfort-care transitions. Using the MIMIC-III database, we propose the Counterfactual Clinical Audit (CCA) framework, which stress-tests RL agents through physiological perturbations anchored in Surviving Sepsis Campaign (SSC) guidelines. We audit a Medical Decision Transformer (MedDT) and a Historical Causal Transformer (HCT-RL), the latter employing Causal Action Shielding, propensity-based importance weighting, and Conservative Q-Learning. CCA reveals that MedDT paradoxically reduces vasopressor dosage as lactate escalates, contradicting resuscitation guidelines, while HCT-RL maintains physiologically consistent responses. These findings expose a systemic misalignment between statistical fit and clinical safety, supporting counterfactual audits as a necessary evaluation standard for medical RL.

## Metadata
- **Published**: 2026-08-11T20:17:14Z
- **Authors**: Hangqi Ren, Junyi Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11410v1)