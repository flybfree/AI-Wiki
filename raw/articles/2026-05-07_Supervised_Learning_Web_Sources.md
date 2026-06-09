---
title: Supervised Learning Web Sources
status: note
date: 2026-05-07
tags: [sources, supervised-learning, classification, regression, metrics]
---

# Supervised Learning Web Sources

These sources were used to strengthen the supervised learning lesson with current, authoritative web material.

## Core overview

- IBM, "What Is Supervised Learning?"  
  https://www.ibm.com/think/topics/supervised-learning  
  Useful for the basic definition of supervised learning, plus examples of classification and regression.

- scikit-learn documentation, "1. Supervised learning"  
  https://scikit-learn.org/stable/supervised_learning.html  
  Useful for a broad survey of supervised estimators, probability calibration, and problem families.

## Classification and regression

- Google for Developers, "Classification" (Machine Learning Crash Course)  
  https://developers.google.com/machine-learning/crash-course/classification  
  Useful for framing classification as predicting categories and understanding thresholds.

- Google for Developers, "Linear regression" (Machine Learning Crash Course)  
  https://developers.google.com/machine-learning/crash-course/linear-regression  
  Useful for explaining regression as predicting a label value from features.

- IBM, "Classification vs Regression"  
  https://www.ibm.com/think/topics/classification-vs-regression  
  Useful for the clean contrast between discrete labels and numeric targets.

- scikit-learn documentation, "Tuning the decision threshold for class prediction"  
  https://scikit-learn.org/stable/modules/classification_threshold.html  
  Useful for explaining how a threshold turns scores into final class predictions.

- scikit-learn documentation, "Probability calibration"  
  https://scikit-learn.org/stable/modules/calibration.html  
  Useful for explaining why predicted probabilities may need calibration before thresholding.

## Evaluation metrics

- Google for Developers, "Classification: Accuracy, recall, precision, and related metrics"  
  https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall  
  Useful for precision, recall, and F1 explanations.

- scikit-learn documentation, "f1_score"  
  https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html  
  Useful for the harmonic-mean definition of F1.

- scikit-learn documentation, "classification_report"  
  https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html  
  Useful for summarizing precision, recall, and F1 across classes.

- scikit-learn documentation, "Metrics and scoring: quantifying the quality of predictions"  
  https://scikit-learn.org/stable/modules/model_evaluation.html  
  Useful for the broader model evaluation and scoring vocabulary.

## Notes for the lesson

- Supervised learning depends on labeled examples.
- Classification predicts categories.
- Regression predicts numbers.
- Many classifiers output scores or probabilities before the final label is chosen.
- Metrics should match the task and the business goal.
- Model quality depends heavily on label quality and evaluation design.
- Threshold choice can change the balance between precision and recall.
- Probability calibration can make score-based decisions more trustworthy.
