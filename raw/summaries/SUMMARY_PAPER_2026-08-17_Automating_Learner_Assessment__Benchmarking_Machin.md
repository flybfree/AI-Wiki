---
title: Automating Learner Assessment: Benchmarking Machine Learning and Deep Learning Models for EEG-Based Familiarity Prediction
url: http://arxiv.org/abs/2608.16541v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_13-15-45Z_AutomatingLearnerAssessment_BenchmarkingMachineLea.md
generated_at: 2026-08-17 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper aims to benchmark fifteen machine learning and deep learning models that predict cognitive familiarity from continuous EEG data, using two educational tasks: recognizing faces and solving mathematical equations. The authors demonstrate that while conventional cross‑validation inflates performance, a trial‑independent Group K‑Fold evaluation yields realistic F1 scores around 0.60 for the best CNN model.

## Key Takeaways
- Standard stratified cross‑validation can produce artificially high classification metrics such as an F1-score of up to 0.9853 using a CNN, but this performance is misleading because it suffers from temporal leakage across neighboring epochs.
- When evaluated with trial‑independent Group K‑Fold, the peak model performance drops to an F1-score of 0.6038, which remains statistically significant above the 25% chance level for EEG familiarity prediction.
- Feature importance and SHAP analysis identify temporal and frontal Gamma and Beta oscillations as the most critical biomarkers influencing familiarity detection.

## Context
The study contributes to the growing interest in using brain‑derived signals for educational assessment, positioning EEG as a non‑invasive tool that can capture real‑time cognitive states. By benchmarking multiple models under rigorous validation protocols, it provides a baseline for future research aiming at reliable affective and learning monitoring systems.

## Implications
For educators and developers of intelligent tutoring platforms, this work underscores the importance of trial‑independent evaluation to avoid overestimating model utility in real classrooms. Practitioners can rely on these realistic scores when integrating EEG feedback into adaptive learning environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16541v1)
