---
title: Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training
url: http://arxiv.org/abs/2607.28109v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-15-41Z_BeyondRephrasing_Book_LevelOrganizationImprovesSyn.md
generated_at: 2026-07-30 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a scalable synthetic textbook synthesis pipeline that organizes retrieved source material into coherent book‑level documents, aiming to improve language model pre‑training. It demonstrates that the Full setting—where books are assembled from clustered and planned sections—outperforms other conditions by an average gain of +1.09 on downstream tasks.

## Key Takeaways
- The pipeline clusters source material into topical units and plans hierarchical tables of contents to assemble complete books, producing 686K textbooks with 32B tokens across 15,000+ disciplines.
- Replacing natural books in a mid‑training mix with this corpus improves downstream performance by +1.09 on average, isolating document packaging as a factor via the Full condition (+1.02) while other controls show smaller gains.
- The RandomConcat control that joins sections from different books remains below Full, ruling out length alone, and the Rephrase condition without clustering yields only +1.17 gain, highlighting the value of structured synthesis.

## Context
Most synthetic data research focuses on rewriting style or local content rather than how related material is organized into coherent documents. This paper shifts attention to document‑level organization, which is essential for maintaining coherence in long texts and for generating high‑quality pre‑training corpora.

## Implications
For practitioners, the findings suggest that book‑level organization can be leveraged to generate high‑quality pre‑training data without extensive manual curation. Industry adoption could reduce costs and improve model robustness in educational domains such as science and mathematics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28109v1)
