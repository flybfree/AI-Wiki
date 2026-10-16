---
title: Does Personalization Break Trust? Open-Set Rejection Calibration Under Few-Shot On-Device Intent Adaptation
published: 2026-10-12T18:54:51Z
authors: Vaibhav Prajapati, Pushp Garg
url: http://arxiv.org/abs/2610.20652v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Personalization Break Trust? Open-Set Rejection Calibration Under Few-Shot On-Device Intent Adaptation

## Abstract
Always-on virtual assistants increasingly personalize on-device to new user-specific commands via few-shot fine-tuning (e.g., LoRA), but this adaptation is evaluated almost exclusively on whether it learns the new commands, not on whether the assistant can still recognize an input that matches none of its intents - the out-of-scope (OOS) rejection problem. We show that naive few-shot LoRA personalization degrades OOS-rejection AUROC (area under the ROC curve) on every one of five public intent-classification benchmarks (mean drop $0.055$--$0.258$, five seeds each), while in-scope accuracy is preserved. A scorer-invariant check shows part of this drop is an artifact of the standard confidence scorer's own miscalibration under adaptation, though a smaller, genuine effect remains under any scorer; we trace it to a measurable shrinkage of the embedding margin around known-intent regions (pooled Spearman rho=0.61$). A deployment-cheap fix is scoring rejection by Mahalanobis distance instead of softmax confidence without extra training/retraining recovers most of the lost quality on 3 of 5 datasets at no accuracy cost, beats two further OOD scoring baselines, and generalizes across shot count, LoRA rank, and a second base encoder. We report honestly where the fix falls short and release all code for reproducibility.

## Metadata
- **Published**: 2026-10-12T18:54:51Z
- **Authors**: Vaibhav Prajapati, Pushp Garg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20652v1)