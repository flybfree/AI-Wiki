---
title: KIRA: A Full-Stack Reading Screening System with Dual-Pathway Analysis for Children
url: http://arxiv.org/abs/2610.28840v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_19-10-45Z_KIRA_AFull_StackReadingScreeningSystemwithDual_Pat.md
generated_at: 2026-10-21 22:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
KIRA is a full-stack, classroom-ready reading screening system designed to identify children at risk of reading difficulty in early grades (K-2). It pairs word-level fluency scoring with detailed phoneme-level error detection by adapting pretrained speech recognizers to children's speech, achieving significant reductions in both word error rate (from 13.88% to 8.84%) and phoneme error rate (from 41.66% to 23.00%). The system integrates these child-adapted models into a web-based teacher-facing interface that presents fluency scores alongside phoneme-level feedback to support targeted intervention.

## Key Takeaways
- KIRA implements a dual-pathway analysis architecture that simultaneously performs Word Reading Error (WRE) scoring and Oral Reading Fluency (ORF) assessment, two foundational tasks in K-2 reading screening, enabling a more comprehensive evaluation than prior single-metric AI screeners.
- The authors adapt pretrained word and phoneme recognizers specifically to children's speech patterns, yielding a 36% relative reduction in word error rate and a 45% relative reduction in phoneme error rate, demonstrating that domain-specific fine-tuning for child speech is critical for accurate screening.
- Unlike proprietary systems that lack transparent model specifications and evaluation metrics, KIRA is presented as a deployable, full-stack system with a web-based teacher-facing interface that provides actionable phoneme-level feedback, making it suitable for real classroom intervention rather than research-only evaluation.

## Context
Early-grade reading screening is a well-established educational practice, but existing AI-based tools have been limited in scope, evaluation transparency, or accessibility. KIRA addresses a gap in the speech recognition and educational technology literature by bridging child-adapted automatic speech recognition with practical classroom deployment, contributing to the growing body of work on child speech processing and its application to literacy assessment.

## Implications
For educators and school districts, KIRA offers a transparent, deployable alternative to proprietary reading screeners, potentially lowering barriers to early literacy intervention through actionable phoneme-level feedback rather than aggregate scores alone. For the AI research community, the paper demonstrates that significant performance gains in child speech recognition are achievable through targeted adaptation of pretrained models, which could inform future work in child-directed speech processing, dyslexia detection, and educational assistive technologies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28840v1)
