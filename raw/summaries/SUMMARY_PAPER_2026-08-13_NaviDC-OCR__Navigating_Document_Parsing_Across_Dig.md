---
title: NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents
url: http://arxiv.org/abs/2608.12898v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_07-34-21Z_NaviDC_OCR_NavigatingDocumentParsingAcrossDigitala.md
generated_at: 2026-08-13 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces NaviDC-OCR, a unified framework that tackles document parsing by integrating geometric perception and structured reasoning. The authors report state‑of‑the‑art results on three benchmarks, achieving overall scores of 96.87, 88.53, and 78.41 respectively, and ranking first in the ICDAR 2026 Sci‑ImageMiner Challenge.

## Key Takeaways  
- Deformation‑aware learning is added to VLMs so that geometric distortions in camera‑captured documents are compensated during parsing.  
- An adaptive sampling mechanism captures complex layout structures without over‑generating or hallucinating content at high resolution.  
- A content‑structure decoupled strategy explicitly models formula grammars and table layouts, improving structured representation learning.

## Context  
Document parsing is a core task in AI that combines vision and language understanding to convert unstructured pages into machine‑readable data. Recent VLMs have shown promise but still struggle with layout errors and hallucinations, limiting their practical deployment across diverse document types.

## Implications  
For industry practitioners, NaviDC-OCR offers a reliable tool for extracting structured information from both scanned and digital documents, reducing manual annotation effort. The framework’s ability to generalize across formats could accelerate automation in legal, medical, and financial sectors where accurate data extraction is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12898v1)
