---
title: Scope3Trace: Evidence-Based Identification and Extraction of Scope 3 GHG Emissions from Sustainability Reports
url: http://arxiv.org/abs/2607.17122v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_08-13-54Z_Scope3Trace_Evidence_BasedIdentificationandExtract.md
generated_at: 2026-07-23 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Scope3Trace, an evidence‑grounded framework for extracting Scope 3 greenhouse gas emissions from sustainability reports. The authors demonstrate that the system can reliably retrieve organization‑ and building‑level disclosures while providing traceable evidence, achieving high accuracy in total and category‑level extraction.

## Key Takeaways
- Scope3Trace combines OCR parsing of PDFs with LLM‑assisted page localization to reconstruct tables from heterogeneous report formats, enabling systematic collection of emissions data across different document types.  
- The framework employs hybrid rule‑LLM extraction that is verified against explicit evidence sources, reducing reliance on costly manual annotation and improving extraction reliability.  
- A dual‑level multimodal dataset created from the extracted disclosures showcases how organization‑ and building‑level Scope 3 information can be integrated transparently into downstream analyses.

## Context
The growing need for accurate carbon accounting drives research into automated ESG data mining, where large language models are commonly employed. However, most existing methods lack explicit evidence grounding, leading to opaque or inaccurate results. This work addresses those gaps by embedding verification steps within the extraction pipeline, aligning AI capabilities with rigorous scientific standards.

## Implications
For sustainability practitioners, Scope3Trace offers a scalable tool that can automate the capture of Scope 3 emissions without sacrificing traceability, supporting more trustworthy reporting and compliance. In industry practice, the framework can streamline carbon accounting workflows, reduce manual effort, and enhance data interoperability across diverse ESG disclosures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17122v1)
