---
title: A Unified Model for Cross-Domain Clone Detection via Model Merging
url: http://arxiv.org/abs/2608.04215v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_20-32-28Z_AUnifiedModelforCross_DomainCloneDetectionviaModel.md
generated_at: 2026-08-05 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a unified model for cross-domain clone detection that combines multiple trained checkpoints without requiring additional training data. By merging models using parameter, architecture, and tokenizer techniques, the authors achieve high performance across diverse code clones, reaching 0.865 combined F1 on UniXcoder while outperforming zero-shot LLMs at lower inference cost.

## Key Takeaways
- TIES merging yields a combined F1 of 0.865 on UniXcoder and generalizes well to unseen AI-generated clones, making it the recommended method despite WUDI’s higher in-distribution score.  
- Cross-base merging provides only marginal gains across all methods, indicating that task vector compatibility through a shared pre-trained base is essential for effective merging.  
- The merged detectors outperform zero-shot code LLMs on GPTCloneBench and generalize up to four times better than multi-task training to unseen AI-generated clones.

## Context
The surge in diverse clone types—syntactic, cross-language semantic, and AI‑generated—has strained existing deep learning detectors that specialize per domain. Current solutions suffer severe F1 drops outside their distribution, making a single robust detector both desirable and challenging to develop.

## Implications
For software engineering teams, this work offers a practical recipe for building cross‑domain clone detectors without retraining on all data, reducing cost and complexity. Practitioners can leverage model merging to maintain high detection accuracy across varied codebases while keeping inference lightweight.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04215v1)
