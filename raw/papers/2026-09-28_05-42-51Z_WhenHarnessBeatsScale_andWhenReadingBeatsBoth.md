---
title: When Harness Beats Scale, and When Reading Beats Both
published: 2026-09-28T05:42:51Z
authors: Ivan Bondarenko, Nikolay O. Nikitin
url: http://arxiv.org/abs/2609.34366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Harness Beats Scale, and When Reading Beats Both

## Abstract
We describe our system for DocSem, the document-grounded quantitative reasoning shared task at DocInsights 2026, and analyze why it succeeded on labeled data and failed on the test set. The pipeline pairs hybrid block retrieval with Program-of-Thoughts (PoT) generation executed in a sandboxed interpreter, self-consistency sampling, and entity enrichment from chunk-level knowledge graphs. On our held-out split, application architecture moved the metrics far more than model scale did: PoT added 0.282 joint accuracy to a compact 7B model but at most 0.005 to a 72B model, and a 27B model with the full harness matched the 72B (0.884 vs.\ 0.873) at roughly 2.7$\times$ fewer parameters and a quarter of the CO$_2$. We read this through a distinction between world knowledge, which scales steeply with parameters, and language knowledge, which scales gently, and show that structured-output training makes a compact model harness-ready rather than merely small. On the raster, watermarked test PDFs the same system collapsed to 13.58\% joint (rank 149 of 163); a controlled re-rendering of the validation set reproduces the OCR half of the collapse while bounding what the simulation misses. Auditing the physical nature of evaluation inputs precedes architecture, and the leaderboard's bimodality is consistent with reading quality, not reasoning, having separated the field.

## Metadata
- **Published**: 2026-09-28T05:42:51Z
- **Authors**: Ivan Bondarenko, Nikolay O. Nikitin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34366v1)