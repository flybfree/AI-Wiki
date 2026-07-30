---
title: Automated Multilabel Mpox Research Classification with Explainable Transformer Models
url: http://arxiv.org/abs/2607.26700v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_09-47-52Z_AutomatedMultilabelMpoxResearchClassificationwithE.md
generated_at: 2026-07-29 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes using multilabel classification with BERT to automatically categorize 14590 Mpox research articles into topics like outbreaks, vaccination, epidemiology. It achieved high accuracy and micro/macro F1 scores, best among tested models. SHAP analysis explains key features that drive classification decisions.

## Key Takeaways  
- BERT reached 97.05% accuracy, 97.67% micro-F1, 96.46% macro-F1 on the dataset.  
- The model classifies articles into multiple topics simultaneously using multilabel approach.  
- SHAP analysis identifies important word features and patterns that drive classification decisions.

## Context  
This work addresses information overload in public health research by applying NLP to Mpox literature, demonstrating how transformer models can automate topic extraction. It aligns with broader efforts to integrate AI for biomedical text mining and outbreak monitoring, showing potential for scalable solutions across disease surveillance.

## Implications  
Researchers can quickly retrieve relevant articles, saving time and resources. Policymakers gain timely insights into Mpox developments, supporting proactive public health strategies. The explainability of BERT via SHAP adds trust in automated decisions, encouraging adoption in clinical and policy settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26700v1)
