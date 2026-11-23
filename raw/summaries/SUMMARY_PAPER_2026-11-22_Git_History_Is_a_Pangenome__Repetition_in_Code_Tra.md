---
title: Git History Is a Pangenome: Repetition in Code Training Corpora and What Deduplication Removes, Keeps and Misses
url: http://arxiv.org/abs/2611.27154v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-20_05-38-42Z_GitHistoryIsaPangenome_RepetitioninCodeTrainingCor.md
generated_at: 2026-11-22 21:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper empirically measures how deduplication tools—originally designed for single-snapshot training data—interact with full Git repository histories used to train code models. The author finds that repository histories are overwhelmingly repetitive, functioning as a "pangenome" where a typical repository contains the equivalent of 19 copies of its current code and mature repositories contain up to 89 copies. The study reveals that standard deduplication pipelines fail to address this repetition effectively and introduce a critical selection bias that retains outdated file versions for training.

## Key Takeaways
- Repository histories are dominated by near-identical repetition rather than novel content: nine out of ten tokens in a changed file already existed in a prior version, meaning a typical repository holds 19 copies of its current code and mature projects hold 89. Exact-match deduplication removes none of these copies because no two versions are byte-identical, while near-identical grouping reduces repetition only to about two copies per file.
- Widely used deduplication implementations select which version of a file to keep without considering timestamps, causing the training pipeline to retain an outdated version for half of all files. Sorting versions newest-first before deduplication resolves this selection bias at negligible computational cost.
- Benchmark contamination persists across versions: a merged bug fix relevant to SWE-bench survives in a median of 18 subsequent versions of the files it touched. Removing benchmark answers therefore requires a dedicated step that scans every version in the history rather than relying on snapshot-level filtering.

## Context
As large language models for code increasingly move from training on single repository snapshots to ingesting full commit histories, the assumptions embedded in existing data-preprocessing pipelines become invalid. This paper is significant because it provides the first pre-registered, instrumented measurement of how those pipelines behave on historical data, bridging a gap between the software-engineering literature on repository mining and the machine-learning literature on training-data curation. It also connects directly to benchmark integrity concerns raised by the SWE-bench community.

## Implications
For teams building code-generation or code-repair models, the findings translate into a short, actionable set of rules: sort versions chronologically before deduplicating, apply near-identical grouping across all versions rather than within a single snapshot, and run a separate benchmark-contamination check against every version in the history. Practitioners who skip these steps risk training on stale code and inadvertently memorizing benchmark solutions, which inflates evaluation scores and undermines the reliability of downstream model assessments. The released instruments and frozen outputs give the community a reproducible baseline for auditing future training corpora.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27154v1)
