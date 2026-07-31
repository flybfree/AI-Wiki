---
title: Contrastive Concept Importance: Explaining Pairwise Class Decisions Through Automatically Extracted Concept Representations
published: 2026-07-30T09:19:21Z
authors: Roel Visser, Isaac Roberts, Barbara Hammer
url: http://arxiv.org/abs/2607.27904v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contrastive Concept Importance: Explaining Pairwise Class Decisions Through Automatically Extracted Concept Representations

## Abstract
Concept-based explanations are a prevalent way to explain the decisions of complex black-box methods through semantically meaningful, human-interpretable concepts. To attribute the contribution of such concepts to a model's decisions, feature attribution methods are used to quantify how strongly each concept contributes to a model output. These attributions are typically computed for a single output class and therefore answer a non-contrastive "why P?" question. In many situations, however, such as cases of misclassification, class confusion, and low-margin predictions, the more natural question to ask is "why P rather than Q?".   We introduce contrastive concept importance (CCI), which attributes the logit margin between a target class and a contrast, or foil, class to concepts in an automatically extracted visual concept basis. The resulting scores are signed, indicating whether a concept supports the target over the foil or the foil over the target, and can be decomposed into target-logit and foil-logit effects. This makes it possible to distinguish globally important concepts from concepts that specifically influence a class-pair distinction, including whether their effect is shared, one-sided, or directly contrastive.   We evaluate the method on ImageNet class pairs using CRAFT-style concept bases, insertion and deletion curves, logit-wise decomposition analysis, and semantic class hierarchy. The results show that contrastive concept importance reveals class-pair-specific model behavior that is not captured by ordinary concept importance alone, and that highly contrastive concepts can be evaluated against semantic superclass structure to assess whether they affect fine-grained distinctions rather than broad category evidence.

## Metadata
- **Published**: 2026-07-30T09:19:21Z
- **Authors**: Roel Visser, Isaac Roberts, Barbara Hammer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27904v1)