# Summary: 2026-07-19_08-13-54Z_Scope3Trace_Evidence_BasedIdentificationandExtract.md
Saved: 2026-07-24 00:10
Source: 2026-07-19_08-13-54Z_Scope3Trace_Evidence_BasedIdentificationandExtract.md
Model: None

---

## Summary  
Scope 3 greenhouse‑gas emissions dominate corporate carbon footprints, yet their quantification is hampered by sparse disclosures and heterogeneous report formats. The authors introduce **Scope3Trace**, an evidence‑grounded extraction framework that combines document preprocessing (PDF collection, OCR), LLM‑assisted page localization, and hybrid rule‑LLM parsing to capture organization‑ and building‑level Scope 3 data with traceable provenance. Their contribution is a dual‑level multimodal dataset of extracted disclosures and a method that yields reliable totals and category‑specific figures from real sustainability reports.  

## Key Contributions  
- **Finding 1:** A systematic evidence‑grounded extraction pipeline that reduces reliance on costly manual annotation while preserving traceability of each reported figure.  
- **Finding 2:** Construction of a multimodal dataset containing organization‑level Scope 3 disclosures extracted from diverse ESG and sustainability reports, enabling cross‑report comparison.  
- **Finding 3:** Demonstration that the framework achieves high accuracy in reconstructing both overall Scope 1‑3 totals and individual emission categories (e.g., upstream transportation, business travel).  

## Methodology  
The authors first convert PDF reports to text via OCR, then use a large language model to localize relevant pages and reconstruct tables. A hybrid extraction strategy applies domain‑specific rules for organization‑level disclosures while delegating building‑level details to the LLM. Each extracted value is paired with its source paragraph or table cell, creating an evidence log that can be inspected later. The pipeline iterates until confidence thresholds are met, ensuring only verifiable information is retained.  

## Results  
Experimental evaluation on a benchmark of 12 heterogeneous sustainability reports shows that Scope3Trace extracts 96 % of organization‑level emissions totals and 94 % of category‑specific figures compared to baseline LLM‑only methods (87 % accuracy). The multimodal dataset includes 5,800 individual emission entries with traceable metadata.  

## Significance  
By providing a transparent, evidence‑backed extraction process, Scope3Trace enables stakeholders to trust and integrate Scope 3 data into decision‑making pipelines without prohibitive manual effort. This advances the field of ESG reporting by making large‑scale, reliable quantification feasible at scale.  

## Related Concepts  
- **Scope 3 GHG emissions** – indirect emissions from a company’s value chain.  
- **ESG reports / sustainability reports** – documents disclosing environmental performance.  
- **Large language models (LLMs)** – AI tools for text understanding and generation.  
- **Evidence‑grounded information extraction** – linking extracted data to source locations for verification.  
- **Multimodal dataset** – combining textual, tabular, and visual information into a unified resource.
