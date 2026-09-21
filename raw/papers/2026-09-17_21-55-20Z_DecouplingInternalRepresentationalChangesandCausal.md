---
title: Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models
published: 2026-09-17T21:55:20Z
authors: Lingfang Li, Procheta Sen, Shubham Das, Danushka Bollegala
url: http://arxiv.org/abs/2609.21113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models

## Abstract
Fine-tuning has emerged as a widely adopted approach for adapting LLMs to a variety of downstream tasks. However, how it reshapes their internal mechanisms remains poorly understood. To address this, we investigate how fine-tuning alters internal representations in LLMs, including attention patterns and layer-wise activations, and examine whether these changes are linked to task-relevant components identified by EAP (e.g., attention heads and logit-level activations) that drive task performance. We find that EAP-identified components are concentrated within specific layers, indicating a degree of functional localisation in how models internalise task-specific behavior. Notably, the distribution of these components across layers is largely uncorrelated with the layers undergoing the most substantial representational changes during fine-tuning. Furthermore, we observe that overlap in EAP-identified components across tasks does not translate into cross-task performance transfer if the tasks are different in nature (e.g. classification vs. generative tasks). More specifically, fine-tuning on one task can lead to a degradation of performance on another when the two tasks exhibit a high degree of overlap in their EAP-identified components.

## Metadata
- **Published**: 2026-09-17T21:55:20Z
- **Authors**: Lingfang Li, Procheta Sen, Shubham Das, Danushka Bollegala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21113v1)