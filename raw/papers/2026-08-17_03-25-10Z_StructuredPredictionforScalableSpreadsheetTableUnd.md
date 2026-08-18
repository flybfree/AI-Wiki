---
title: Structured Prediction for Scalable Spreadsheet Table Understanding: From Cell Types to Table Ranges (Extended Version)
published: 2026-08-17T03:25:10Z
authors: Antoine Gauquier, Ioana Manolescu, Pierre Senellart
url: http://arxiv.org/abs/2608.16050v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structured Prediction for Scalable Spreadsheet Table Understanding: From Cell Types to Table Ranges (Extended Version)

## Abstract
Spreadsheets are a primary medium for publishing tabular data, yet automatically extracting structured content from them remains difficult due to heterogeneous layouts, diverse file formats, and inconsistent organizational conventions. We address two core tasks in spreadsheet understanding: Cell-Type Classification (CTC), which assigns roles to cells, and Table Detection (TD), which identifies table bounding boxes within sheets. We propose an efficient two-stage pipeline in which a learned CTC model feeds a deterministic TD algorithm. For CTC, we use a LightGBM classifier over 65 structured features together with a pairwise CRF enforcing spatial consistency across the cell grid. Our TD method extracts table ranges from predicted cell types by a deterministic five-stage procedure. For evaluation, we built and share StatSheets, a multilingual benchmark of 737 manually annotated sheets from 14 public data providers across multiple countries and file formats. Under 5-fold cross-validation, our CRF-LightGBM system achieves a Mean File-Macro F1 score of 0.937 on CTC, within 0.6 percentage points of the GPU-based TUTA Transformer, while requiring substantially fewer computational resources. For TD, our deterministic approach outperforms region-based baselines and remains competitive with recent LLM-based systems such as SpreadsheetLLM. These results demonstrate that combining non-linear structured prediction with deterministic range extraction provides a competitive, scalable, and computationally efficient approach to spreadsheet table understanding.

## Metadata
- **Published**: 2026-08-17T03:25:10Z
- **Authors**: Antoine Gauquier, Ioana Manolescu, Pierre Senellart
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16050v1)