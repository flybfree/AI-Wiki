---
title: Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction
published: 2026-08-27T17:28:35Z
authors: Jin Mu, Guanhua Chen
url: http://arxiv.org/abs/2608.27397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Making Clinical Language Models Auditable: Concept-Guided Fine-Tuning for Robust Prediction

## Abstract
Clinical language models can achieve strong in-hospital accuracy yet fail under deployment shifts because they exploit note-specific artifacts (e.g., templates, separators, boilerplate) that do not reflect patient state. We propose CAST (Concept-guided Artifact Suppression Tuning), an SAE-based framework for auditable clinical text classification. CAST uses Sparse Autoencoders to expose sparse, human-auditable features from intermediate Transformer activations, labels SAE latents with an LLM-assisted interpretation pipeline and ICD-10 retrieval constraints, suppresses verified artifact latents via residual subtraction during fine-tuning, and provides post-hoc per-concept attributions for auditing model decisions. On MIMIC-IV discharge-note mortality prediction, CAST improves over its corresponding fine-tuned encoder baselines and remains competitive with strong LLM baselines, while producing a feature-level audit trail of the clinical concepts that support each prediction and the artifact concepts suppressed during training.

## Metadata
- **Published**: 2026-08-27T17:28:35Z
- **Authors**: Jin Mu, Guanhua Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27397v1)