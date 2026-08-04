---
title: Fast and Accurate Quotation Attribution in Literary Texts
url: http://arxiv.org/abs/2608.02359v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
generated_at: 2026-08-03 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an encoder‑based formulation called joint scoring to attribute quotations to their speakers in literary texts efficiently. The authors achieve state‑of‑the‑art 94.5 % overall attribution accuracy on the Project Dialogism Novel Corpus while processing novels twenty times faster than standard methods and over a thousand times faster than large language model approaches.

## Key Takeaways
- The joint scoring method reaches SOTA performance, delivering 94.5 % attribution accuracy across more than 35,000 annotated quotations from 22 English novels.
- It processes novels twenty times faster than comparable standard methods and more than a thousand times faster than LLM‑based approaches on an A100 GPU.
- The analysis shows that joint scoring preserves long‑range anaphora resolution signals already present in pretrained encoders, improving handling of challenging attribution examples.

## Context
Literary text processing requires accurate speaker attribution at scale, yet current methods face a trade‑off between accuracy and computational cost. Large language models excel at performance but are prohibitively expensive for large corpora, while traditional approaches sacrifice speed or precision. This work bridges that gap by delivering high accuracy with minimal resource usage.

## Implications
The joint scoring approach enables scalable annotation pipelines for literary analysis, reducing costs for researchers and industry users who need precise speaker attribution across massive datasets. By integrating efficiently into existing NLP workflows, it supports broader applications such as automated summarization, dialogue reconstruction, and educational tools that rely on accurate quotation attribution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02359v1)
