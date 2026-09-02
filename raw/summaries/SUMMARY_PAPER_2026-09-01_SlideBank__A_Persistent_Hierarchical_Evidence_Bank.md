---
title: SlideBank: A Persistent Hierarchical Evidence Bank for Consistent Whole-Slide Reasoning
url: http://arxiv.org/abs/2609.00342v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_20-37-52Z_SlideBank_APersistentHierarchicalEvidenceBankforCo.md
generated_at: 2026-09-01 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SlideBank, a training-free framework that treats whole-slide images as persistent evidence banks for pathology reasoning. It enables question-independent exploration to extract informative regions and multi‑scale views, converting them into explicit observations linked to original coordinates. Experiments show improved performance on WSI‑VQA and SlideBench‑BCNB compared with random evidence sampling.

## Key Takeaways
- SlideBank represents each WSI as a persistent concept-indexed evidence bank that stores spatial provenance for every extracted region.
- The framework performs coarse-to-fine exploration to identify informative regions and multi-scale views, then grounds pathology signals to their supporting patches and coordinates.
- Reusing the same evidence bank across queries yields over 99% rephrasing consistency while reducing amortized inference cost.

## Context
Whole-slide image analysis remains limited by sparse morphological cues that are hard to retrieve from gigapixel images. Existing methods either aggregate features or rely on active acquisition, both of which hinder consistent reasoning and increase computational load. This work addresses the need for a persistent, query-agnostic evidence representation that can be reused across tasks.

## Implications
For clinicians and AI developers, SlideBank offers a reusable knowledge base that reduces repeated analysis effort and improves diagnostic consistency. The framework’s confidence-based cross-level consensus may enable more reliable pathology predictions in future medical imaging pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00342v1)
