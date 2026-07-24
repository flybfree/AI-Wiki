# Summary: 2026-07-19_08-13-54Z_Scope3Trace_Evidence_BasedIdentificationandExtract.md
Saved: 2026-07-24 00:06
Source: 2026-07-19_08-13-54Z_Scope3Trace_Evidence_BasedIdentificationandExtract.md
Model: None

---

## Summary  
Scope3Trace is an evidence‑grounded information extraction framework for identifying Scope 3 greenhouse gas emissions from sustainability reports. The paper addresses the challenge of sparse, heterogeneous disclosures by integrating OCR parsing, LLM page localization, table reconstruction, and verification steps. It delivers a dual‑level dataset with organization‑ and building‑level emissions data extracted from real ESG documents. The framework ensures traceable, reliable extraction of Scope 1‑3 totals and category breakdowns.

## Key Contributions  
- Evidence‑grounded extraction pipeline that combines OCR parsing, LLM page localization, table reconstruction, and hybrid rule‑LLM extraction with verification.  
- Construction of a dual‑level multimodal dataset containing organization‑ and building‑level Scope 3 disclosures extracted from heterogeneous sustainability reports.  
- Demonstration that the framework achieves high accuracy in extracting both total emissions and category‑specific Scope 3 data.

## Methodology  
The authors built a pipeline where PDFs are collected via OCR, LLM localizes relevant pages and reconstructs tables, while a hybrid rule‑LLM model extracts organization‑level disclosures using evidence cues; building‑level details are captured with table reconstruction. Verification steps confirm extraction reliability by cross‑checking extracted figures against the original report text.

## Results  
Experiments on a collection of 20 sustainability reports show the framework extracts 96 % of reported Scope 3 totals and 94 % of category breakdowns, outperforming baseline LLM methods by roughly 15 % accuracy; verification reduces false positives to under 2 %.

## Significance  
By providing traceable extraction, Scope3Trace enables auditable carbon accounting at scale, supporting corporate ESG reporting compliance and enabling downstream analysis for investors and regulators.

## Related Concepts  
Scope 3 emissions, sustainability reports, ESG disclosures, large language models, OCR, hybrid rule‑LLM systems, multimodal data, evidence grounding, verification.
