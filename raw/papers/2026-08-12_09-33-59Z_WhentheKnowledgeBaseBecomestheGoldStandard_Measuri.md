---
title: When the Knowledge Base Becomes the Gold Standard: Measuring Resource-Shared Evaluation Loops in Entity-Level Machine Translation
published: 2026-08-12T09:33:59Z
authors: Jinhyung Bae, Dain Kil, Seongmin Oh, Seungmin Lee
url: http://arxiv.org/abs/2608.11843v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When the Knowledge Base Becomes the Gold Standard: Measuring Resource-Shared Evaluation Loops in Entity-Level Machine Translation

## Abstract
The Seungjeongwon Ilgi, a UNESCO Memory of the World record, is only 37.4% translated, and the most conspicuous failure mode in automatic translation is the person name -- a misread name corrupts the historical fact rather than merely the surface. Low-resource historical domains have no expert gold standard for entity translation, so practitioners substitute a knowledge base (KB) for the gold. That KB is the same resource injected into the system: scoring becomes self-referential and the metric measures instruction compliance rather than translation quality.   We measure this loop. Using expert person-name annotations from the National Institute of Korean History as a gold independent of the injection pipeline, we hold the entity set fixed and vary only the provenance of the correct reading. Of 527 expert-annotated mentions, only 31.1% lie outside the injection pipeline, and the residual loop is not uniform -- in the overlapping segment the injected reading agrees with the human translation 97.8% of the time against 70.1% in the independent one, so the segment that looks healthiest is the one the loop is holding up.   Across four models, a difference-in-differences analysis shows the gain from KB injection is confined to the segment whose gold shares the injected resource; in the independent segment it is at or below zero. Post-injection preservation clusters in a narrow 0.910-0.996 band even though baseline capability differs fivefold, so the reported gain is the complement of prior performance and weaker models appear to improve more dramatically. On an independent sample built by removing the construction filter, the measure replicates within model (overlapping intervals) while discriminating between models (non-overlapping intervals) -- it reflects a property of the model, not of the sample.

## Metadata
- **Published**: 2026-08-12T09:33:59Z
- **Authors**: Jinhyung Bae, Dain Kil, Seongmin Oh, Seungmin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11843v1)