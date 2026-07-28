---
title: Beyond Local Inspection: Global, Guideline-Grounded Evaluation of Post-hoc XAI Methods for ECG Classification
published: 2026-07-27T06:16:28Z
authors: Nils Gumpfer, Michael Guckert, Samuel Sossalla, Birgit Aßmus, Jennifer Hannig
url: http://arxiv.org/abs/2607.24035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Local Inspection: Global, Guideline-Grounded Evaluation of Post-hoc XAI Methods for ECG Classification

## Abstract
Explainable AI (XAI) is used to assess whether artificial intelligence models rely on meaningful patterns, yet explanations that appear plausible for individual predictions may systematically misrepresent model behavior. This is particularly problematic in medicine, where models may rely on irrelevant signal characteristics rather than disease-specific patterns without being recognizable. We address this challenge using electrocardiogram (ECG) data, for which clinical guidelines provide explicit knowledge about diagnostically relevant signal regions. We introduce a global, guideline-grounded framework that aggregates explanations across heartbeats to evaluate them against clinically defined regions of interest. Using four binary classifiers trained on PTB-XL, we assess 13 gradient-based methods across two categories of patterns: low-amplitude segments and high-amplitude QRS morphology. Our results reveal a systematic failure of methods transferred from computer vision. Their explanations often follow signal amplitude rather than clinical relevance, with mean Spearman correlations up to 0.69, leading them to overlook diagnostically decisive low-amplitude regions. For ischemia, LRP-$ε$ assigns only 4.6% of relevance to the ST segment, compared with 63.8% for LRP-SIGN. Nine of 13 methods fall below chance for at least one condition, indicating inconsistent reliability across patterns. These findings show that global, domain-grounded evaluation can uncover systematic explanation failures not obvious from sample-level heatmaps.

## Metadata
- **Published**: 2026-07-27T06:16:28Z
- **Authors**: Nils Gumpfer, Michael Guckert, Samuel Sossalla, Birgit Aßmus, Jennifer Hannig
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24035v1)