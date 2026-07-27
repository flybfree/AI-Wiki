---
title: FSE: Continual Learning for Named Entity Recognition by Fast-Slow Experts
url: http://arxiv.org/abs/2607.22075v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_08-20-01Z_FSE_ContinualLearningforNamedEntityRecognitionbyFa.md
generated_at: 2026-07-26 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FSE, a Fast‑Slow Experts enhanced span‑based NER model designed to solve Continual Learning for Named Entity Recognition. By separating a fast expert that quickly discards unlikely spans and a slow expert that classifies the remaining ones, FSE reduces catastrophic forgetting while preserving task plasticity. Experiments on OntoNotes and FewNERD show state‑of‑the‑art performance with faster convergence.

## Key Takeaways
- The shared fast expert learns token‑level links to filter out improbable spans, limiting the number of candidates for slow expert processing.
- A length‑decay negative sampling strategy is used to balance span imbalance across tasks, improving model stability.
- FSE stabilizes learning through knowledge sharing and maintains plasticity by reducing per‑task learning burden.

## Context
Continual learning in NER remains challenging because models often forget earlier entity types when learning new ones. Existing approaches either ignore shared representations or impose heavy computational costs for each task update. FSE addresses these issues with a lightweight expert architecture that leverages fast filtering to keep training efficient.

## Implications
For practitioners, FSE offers a practical way to deploy NER systems in real‑world pipelines where entities evolve over time without retraining from scratch. The method’s efficiency can lower inference latency and reduce hardware requirements, making continual learning more accessible across industries such as healthcare and finance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22075v1)
