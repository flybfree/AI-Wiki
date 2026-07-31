---
title: Evaluation Protocols and Cross-Subject Generalization in EEG Emotion Recognition
url: http://arxiv.org/abs/2607.27655v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_04-13-43Z_EvaluationProtocolsandCross_SubjectGeneralizationi.md
generated_at: 2026-07-30 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how evaluation protocols affect EEG emotion recognition accuracy, using a single archived DGCNN model on SEED and SEED‑IV. It demonstrates that protocol‑matched subject checks can align results closely with public standards, while cross‑subject assessments reveal substantial gaps in reported accuracies.

## Key Takeaways
- Protocol‑matched subject‑dependent checks yielded an accuracy within 1.47 percentage points of the reference value on SEED, highlighting the importance of consistent evaluation procedures.  
- Five‑fold subject‑disjoint validation selected checkpoints that achieved near‑perfect trial accuracies (0.9990 on SEED and 0.9920 on SEED‑IV), showing that checkpoint selection can dramatically improve performance.  
- Held‑out participants produced lower overall accuracies (0.5348 on SEED, 0.3954 on SEED‑IV) indicating substantial subject‑specific variance not captured by standard training.

## Context
EEG emotion recognition relies heavily on the interaction between model architecture and evaluation design; discrepancies often stem from differing preprocessing pipelines or representation choices across subjects. This study underscores that reported accuracies are sensitive to how data is split and evaluated, a concern relevant for reproducible AI research.

## Implications
Researchers must adopt protocol‑aligned subject checks before publishing results to avoid misleading claims of model capability. Practitioners should also consider cross‑subject validation when deploying models in real‑world settings where individual variability can impact performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27655v1)
