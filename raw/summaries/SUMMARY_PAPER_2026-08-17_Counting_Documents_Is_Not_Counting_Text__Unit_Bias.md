---
title: Counting Documents Is Not Counting Text: Unit Bias in Web-PDF Corpus Statistics
url: http://arxiv.org/abs/2608.16390v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_10-41-07Z_CountingDocumentsIsNotCountingText_UnitBiasinWeb_P.md
generated_at: 2026-08-17 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reveals that PDF corpora often report token counts while ignoring the number of documents, creating a unit bias that misrepresents data quality and recovery rates. The authors analyze CC‑MAIN‑2021‑31‑PDF‑UNTRUNCATED, showing severe discrepancies between document count and text coverage.

## Key Takeaways
- 3.02% of the 7.9 million web PDFs contain half the tokens, yielding a Gini coefficient of 0.807, indicating extreme token concentration among documents.
- Documents exceeding 50 pages account for only 5.00% of the corpus but 53.53% of all text, highlighting how large files dominate textual content.
- Common Crawl’s truncation cap affects 23.06% of documents yet 63.08% of the text, and recovery on those documents rises only from 3.3% to 13.2% under a 5 MiB limit.

## Context
In AI research, accurate corpus statistics are essential for training models that rely on textual data. Misleading unit bias can lead to over‑ or under‑estimation of available text, affecting model performance and resource planning.

## Implications
Researchers and industry practitioners must report both document count and token totals to avoid skewed analyses. This recommendation improves transparency, ensures fair evaluation, and guides decisions about data preprocessing and model capacity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16390v1)
