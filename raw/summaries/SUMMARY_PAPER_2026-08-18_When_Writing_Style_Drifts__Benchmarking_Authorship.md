---
title: When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era
url: http://arxiv.org/abs/2608.17979v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-29-24Z_WhenWritingStyleDrifts_BenchmarkingAuthorshipVerif.md
generated_at: 2026-08-18 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces AVShift, a German benchmark that tests authorship verification under three distribution shifts: genre changes, temporal gaps, and AI‑assisted writing. Experiments show that fine‑tuned large language models generalize best across genres and improve with diverse training data, while performance drops sharply as the time gap between documents widens. No measurable shift due to AI assistance is detected on this dataset.

## Key Takeaways
- Fine‑tuned LLMs achieve the highest cross‑genre verification accuracy when trained on stylistically varied material, indicating that genre diversity aids robustness.  
- Temporal drift is a strong factor: authorship scores degrade noticeably as the years between texts increase, highlighting time as a critical shift dimension.  
- The benchmark reveals no significant AI‑era distribution shift within AVShift, suggesting current models are not yet biased by AI assistance in this specific setting.

## Context
Authorship verification remains a key challenge for text analysis systems that must differentiate genuine authors from impersonators or automated generation. Existing benchmarks often isolate factors like genre or time, limiting insight into how combined shifts affect model performance. This work expands the scope to German texts and multiple genres, providing a more realistic evaluation framework.

## Implications
For researchers, AVShift offers a comprehensive test set that can guide the development of more resilient verification models across languages and domains. Practitioners in publishing or legal fields may use these findings to anticipate failure modes when documents span long periods or shift genres, ensuring reliable authorial attribution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17979v1)
