---
title: Sleight of Word Benchmark: Can Language Models Notice If Their Own Output Was Tampered With?
url: http://arxiv.org/abs/2608.29921v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_17-31-31Z_SleightofWordBenchmark_CanLanguageModelsNoticeIfTh.md
generated_at: 2026-08-31 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces “Sleight of Word,” a benchmark that tests whether language models can detect when a single word in their own generation is replaced by another during the writing process. The study measures both the model’s surprise at the perturbation and its textual reaction across 19 open‑weight models, revealing that many systems remain unaware of such subtle edits.

## Key Takeaways
- The benchmark demonstrates that language models can be fooled when a word in their output is swapped while they are generating it.  
- Surprise metrics show a wide spread, indicating that some models detect the change while others do not.  
- Textual reaction varies widely among models, suggesting differing levels of self‑awareness or sensitivity to external perturbations.

## Context
The work addresses a growing concern about model integrity in dynamic generation tasks where outputs are subject to real‑time modifications. It highlights a gap between theoretical robustness and practical behavior, prompting researchers to consider how models perceive their own content during creation.

## Implications
For developers, the findings suggest that relying solely on output quality may mask vulnerabilities to subtle tampering. Practitioners should incorporate detection mechanisms into model pipelines to safeguard against hidden edits and maintain trust in generated text.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29921v1)
