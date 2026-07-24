---
title: Adversarial Robustness of Phishing Email Detection: A Comparative Study of TF-IDF + Logistic Regression and Fine-Tuned DistilBERT
published: 2026-07-20T18:28:07Z
authors: Tanveer Ahmed, Seyedali Pourmoafil
url: http://arxiv.org/abs/2607.18429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adversarial Robustness of Phishing Email Detection: A Comparative Study of TF-IDF + Logistic Regression and Fine-Tuned DistilBERT

## Abstract
Phishing emails remain one of the most persistent cybersecurity threats, and machine-learning classifiers are widely used to detect them. Most reported detection accuracies, however, are measured on clean, in-distribution test data rather than on emails deliberately altered to evade detection. This paper reports a controlled, pairwise comparison of two phishing-detection approaches a TF-IDF + Logistic Regression baseline and a fine-tuned DistilBERT transformer trained on a unified corpus of 82,255 emails drawn from six public datasets and evaluated under three conditions: normal in-distribution, synthetic phishing, and adversarial phishing. Both models exceeded 98% accuracy on clean data yet degraded sharply under adversarial testing: TF-IDF + LR fell to 64.00% (a 34.59-percentage-point drop) and DistilBERT fell to 63.64% (a 35.40-percentage-point drop) a gap of only 0.36 percentage points, equivalent to a single email in the 275-sample adversarial test set. LIME, SHAP, and attention-rollout analysis indicate the two models relied on different evidence yet showed similar vulnerability. Pairwise error analysis shows the models agreed on 54.9% of adversarial samples but each made a similar number of exclusive errors (24 and 25 respectively), indicating partly complementary rather than identical failure modes. The results show that clean-data accuracy does not predict adversarial robustness, and that adversarial testing should be a standard part of phishing-detection evaluation.

## Metadata
- **Published**: 2026-07-20T18:28:07Z
- **Authors**: Tanveer Ahmed, Seyedali Pourmoafil
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18429v1)