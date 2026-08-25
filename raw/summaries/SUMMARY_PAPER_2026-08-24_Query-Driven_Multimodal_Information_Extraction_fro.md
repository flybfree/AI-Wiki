---
title: Query-Driven Multimodal Information Extraction from Long Documents
url: http://arxiv.org/abs/2608.22214v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_04-37-34Z_Query_DrivenMultimodalInformationExtractionfromLon.md
generated_at: 2026-08-24 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces a query‑driven approach for extracting both textual attribute values and the corresponding image bounding boxes from long, multimodal documents. The authors present ITJoint, a manually annotated benchmark, and Q2IT, a multi‑agent framework that collaboratively improves extraction performance. Experiments show that standalone vision‑language models underperform while Q2IT yields significant gains.

## Key Takeaways  
- The work focuses on outputting query‑requested textual attributes together with image bounding boxes rather than only textual answers or evidence regions.  
- A two‑level taxonomy is designed to handle both user intent at the query level and document content at the instance level.  
- Q2IT’s multi‑agent collaboration across evidence collection, page selection, and target‑image localization markedly boosts performance on the ITJoint benchmark.

## Context  
The field of multimodal information extraction struggles with long documents where images carry essential knowledge that plain text alone cannot convey. Existing methods often limit themselves to generating answers or locating evidence without integrating both modalities in a query‑driven manner, highlighting a gap in current research and applications.

## Implications  
For industry practitioners, this approach enables more accurate retrieval of visual information alongside textual details from lengthy reports, enabling smarter document analysis tools. Practitioners can leverage Q2IT’s framework to build robust systems that understand both text and images, improving decision‑making across domains such as healthcare, legal, and e‑commerce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22214v1)
