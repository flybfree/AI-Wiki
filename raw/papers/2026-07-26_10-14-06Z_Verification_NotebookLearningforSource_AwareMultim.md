---
title: Verification-Notebook Learning for Source-Aware Multimodal Misinformation Detection
published: 2026-07-26T10:14:06Z
authors: Junyuan Tan
url: http://arxiv.org/abs/2607.23581v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verification-Notebook Learning for Source-Aware Multimodal Misinformation Detection

## Abstract
Multimodal misinformation verification is challenging because misleading signals may come from different parts of a post and require different forms of evidence. LVLMs are well suited to this task, but their verification performance often depends on the inference procedure applied to each instance. Existing methods improve this procedure through stronger prompting, retrieval, or deliberation, but rarely retain the verification patterns learned from previous examples. We propose Verification-Notebook Learning (VNL), a non-parametric framework that learns an external verification procedure for a frozen LVLM before inference. VNL builds a compact notebook of decision principles, evidence cues, and recurring pitfalls from prior verification experience. The notebook remains fixed during inference and guides the verification of new examples. Rather than updating model parameters or storing demonstrations, VNL records learned knowledge in an artifact that can be inspected directly. Experiments show that VNL consistently outperforms a range of competitive baselines. Further analyses show that the Verification Notebook improves fine-grained source attribution while remaining compact and interpretable, providing an effective way to accumulate verification knowledge without model training.

## Metadata
- **Published**: 2026-07-26T10:14:06Z
- **Authors**: Junyuan Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23581v1)