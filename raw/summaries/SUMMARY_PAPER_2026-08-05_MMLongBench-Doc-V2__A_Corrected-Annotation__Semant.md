---
title: MMLongBench-Doc-V2: A Corrected-Annotation, Semantics-Aware Revision of MMLongBench-Doc
url: http://arxiv.org/abs/2608.03397v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_09-51-54Z_MMLongBench_Doc_V2_ACorrected_Annotation_Semantics.md
generated_at: 2026-08-05 01:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper MMLongBench-Doc-V2 presents a corrected version of the MMLongBench-Doc benchmark, addressing two flaws: an answer-count metric that misrepresents performance and ground‑truth annotations that are often inaccurate. By fixing 106 annotations with precise page references and replacing the string metric with a semantic judge, V2 yields scores that better reflect true understanding.

## Key Takeaways
- The original benchmark’s reference metric compared raw answer counts, causing inflated numbers despite poor quality answers.
- A significant portion of ground‑truth annotations were wrong, ambiguous or incomplete, concentrated in questions systems could already solve correctly.
- V2 corrected 106 entries, removed ten mislabeled files and one duplicate, resulting in a cleaner dataset.

## Context
Long‑document QA evaluation is crucial for measuring how models handle complex, multi‑page information. Existing benchmarks often suffer from annotation errors that skew results, limiting trustworthy comparisons of model capabilities.

## Implications
For researchers, V2 provides a more reliable benchmark to guide model development and for practitioners, it reduces the risk of overestimating performance based on flawed metrics. The decision procedure for handling empty answer keys also offers a template for improving dataset integrity in future QA tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03397v1)
