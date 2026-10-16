---
title: Does Personalization Break Trust? Open-Set Rejection Calibration Under Few-Shot On-Device Intent Adaptation
url: http://arxiv.org/abs/2610.20652v1
type: paper-summary
date: 2026-10-16
source_paper: 2026-10-12_18-54-51Z_DoesPersonalizationBreakTrust_Open_SetRejectionCal.md
generated_at: 2026-10-16 00:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether few-shot on-device personalization of virtual assistants via LoRA fine-tuning undermines the assistant's ability to reject out-of-scope (OOS) inputs, a critical trust and safety concern for always-on assistants. The authors demonstrate that naive LoRA adaptation consistently degrades OOS-rejection AUROC across five public intent-classification benchmarks while preserving in-scope accuracy, and they propose a deployment-cheap fix using Mahalanobis distance scoring that recovers most of the lost rejection quality without any additional training.

## Key Takeaways
- Naive few-shot LoRA personalization causes a measurable degradation in OOS-rejection AUROC across all five tested benchmarks, with mean drops ranging from 0.055 to 0.258 across five random seeds, even though in-scope classification accuracy remains intact. This means an assistant can learn new user-specific commands while simultaneously becoming worse at recognizing inputs that match none of its known intents.
- A scorer-invariant analysis reveals that part of the AUROC drop is an artifact of the standard softmax confidence scorer's own miscalibration under adaptation, but a smaller genuine effect persists under any scoring method. The authors trace this residual degradation to a measurable shrinkage of the embedding margin around known-intent regions, quantified by a pooled Spearman correlation of 0.61 between margin shrinkage and rejection quality loss.
- Replacing softmax confidence scoring with Mahalanobis distance for rejection decisions recovers most of the lost OOS-rejection quality on three of five datasets at no in-scope accuracy cost, outperforms two additional OOD scoring baselines, and generalizes across varying shot counts, LoRA ranks, and a second base encoder architecture—all without requiring any additional training or retraining.

## Context
On-device personalization via parameter-efficient fine-tuning methods like LoRA is becoming a standard deployment pattern for always-on virtual assistants, enabling users to teach new commands locally without cloud round-trips. However, the research community has overwhelmingly evaluated these adaptation pipelines solely on whether the assistant successfully learns the new intents, leaving the complementary question of whether the assistant can still correctly reject inputs belonging to no known intent largely unexamined. This paper fills that gap by systematically measuring OOS-rejection calibration degradation under few-shot adaptation and identifying its mechanistic cause in embedding-space geometry.

## Implications
For practitioners deploying on-device assistants, this work signals that personalization pipelines must be audited for OOS-rejection calibration, not just in-scope accuracy, before shipping to users who rely on the assistant to gracefully decline unfamiliar requests. The proposed Mahalanobis-distance scoring fix is attractive for production because it requires no retraining, no additional data, and no changes to the fine-tuning pipeline, making it a low-cost safeguard against trust erosion. The honest reporting of where the fix falls short on two of five datasets also sets a useful benchmark for future work aiming to close the remaining calibration gap in personalized on-device systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20652v1)
