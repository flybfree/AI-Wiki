# Summary: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
Saved: 2026-07-24 02:57
Source: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
Model: None

---

## Summary  
The paper introduces the Capital Markets LLM Reliability Score (CM‑LRS), a rubric‑based metric that evaluates large language model outputs for “bankable” quality in regulated capital‑markets workflows, moving beyond surface fluency to assess defensibility before regulators or counterparties. It proposes seven dimensions—factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, and reviewability/auditability—to score each output on a 0–5 scale, with the aggregate adjustable per workflow. The authors benchmark CM‑LRS across five real‑world financial tasks using public SEC filings and synthetic supplements, measuring four leading LLMs against independent judges.

## Key Contributions  
- Finding 1: Frontier closed‑source models cluster within 0.22 points on four‑judge averaged CM‑LRS (Sonnet 4.6 = 4.31, Opus 4.7 = 4.30, GPT‑5.5 = 4.09), while the open‑weights baseline Llama 3.3 scores 3.15 and is placed last.  
- Finding 2: The performance gap concentrates on retrieval (2.23) and synthesis (2.15), not extraction (0.84).  
- Finding 3: Decision Usefulness exhibits the widest cross‑model dispersion of any dimension (4.0 points) and shows strong inter‑judge agreement (mean r = 0.52).

## Methodology  
The authors evaluate model outputs at the workflow‑output layer across seven dimensions that reflect signals used by regulators in capital markets: factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, and reviewability/auditability. Each dimension is scored 0–5 according to a rubric grounded in reviewer expectations; the total score can be tuned to specific workflows. Experiments involve five financial tasks—DCM transaction‑terms extraction, precedent retrieval, issuer profile synthesis, M&A comparable reasoning, ECM transaction‑terms extraction—using public SEC EDGAR filings and synthetic supplements. Four models (Sonnet 4.6, Opus 4.7, GPT‑5.5, Llama 3.3 70B) are scored by four independent LLM judges.

## Results  
The average CM‑LRS for Sonnet 4.6 is 4.31, for Opus 4.7 is 4.30, and for GPT‑5.5 is 4.09; Llama 3.3 scores 3.15. The gap widens in retrieval (2.23) and synthesis (2.15), indicating those steps are harder to make bankable than extraction (0.84). Decision Usefulness shows the largest spread (4.0 points) but also high inter‑judge consistency (r = 0.52).

## Significance  
The gap between a model’s plausible draft and its bankable output is critical for regulated capital markets, where reliability determines contract enforceability and regulatory compliance. CM‑LRS provides a quantitative, rubric‑driven metric that can guide model selection, workflow design, and risk mitigation in finance.

## Related Concepts  
Capital Markets LLM Reliability Score (CM‑LRS), factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, reviewability/auditability, FinanceBench, ConvFinQA, open‑domain QA benchmarks, regulatory compliance, auditability.
