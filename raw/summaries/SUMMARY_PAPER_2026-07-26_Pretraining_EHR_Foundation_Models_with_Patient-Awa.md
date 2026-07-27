---
title: Pretraining EHR Foundation Models with Patient-Aware Sampling
url: http://arxiv.org/abs/2607.22114v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_09-10-43Z_PretrainingEHRFoundationModelswithPatient_AwareSam.md
generated_at: 2026-07-26 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Patient Sampling, a pretraining technique for autoregressive electronic health record (EHR) foundation models that allows explicit control over how training signals are distributed across individual patients. Compared with the standard Global Stream method, which concatenates all patient records into one long token stream, Patient Sampling enables stochastic weighting of patients to balance representation and optimization efficiency. The authors report improved macro AUROC and AUPRC on downstream clinical tasks using MIMIC-IV v2.2 and v3.1 datasets.

## Key Takeaways
- Patient Sampling lets researchers assign variable weights to patients during sequence construction, preventing longer records from dominating the training signal.
- By controlling sampling probabilities, the method reduces bias introduced by concatenated global streams that favor high-volume patients.
- The approach yields measurable gains in both macro AUROC and AUPRC across multiple clinical tasks, highlighting the importance of patient‑aware sequence design.

## Context
Autoregressive foundation models for EHRs have traditionally borrowed language modeling pretraining strategies, treating each record as part of a single continuous stream. This paradigm often overlooks the heterogeneous length and relevance of individual patient trajectories, leading to suboptimal performance on tasks that require fine-grained understanding. The paper situates Patient Sampling within this broader challenge of aligning model training with real‑world data distribution.

## Implications
For practitioners developing EHR foundation models, Patient Sampling offers a practical way to mitigate bias without discarding valuable long records. It encourages systematic evaluation of sequence construction choices and could be adopted across healthcare AI pipelines to enhance fairness and accuracy in clinical decision support systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22114v1)
