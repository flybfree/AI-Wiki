# Summary: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
Saved: 2026-07-24 02:46
Source: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
Model: None

---

## Summary  
The paper introduces CM‑LRS, a Capital Markets LLM Reliability Score that evaluates large language model outputs at the workflow‑output layer rather than merely at question‑answer level, to determine whether drafts are “bankable” in regulated capital‑markets settings. It moves beyond surface fluency by assessing seven dimensions—factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, and reviewability/auditability—each scored 0–5 against a rubric grounded in signals reviewers use. The authors demonstrate that the score can be tuned to specific workflows and provides a standardized metric for comparing model reliability across finance‑focused tasks.

## Key Contributions  
- Frontier closed‑source models cluster within 0.22 points on four‑judge averaged CM‑LRS (Sonnet 4.6 = 4.31, Opus 4.7 = 4.30, GPT‑5.5 = 4.09) while the open‑weights baseline Llama 3.3 70B scores lowest at 3.15.  
- The performance gap concentrates on retrieval (2.23) and synthesis (2.15), not extraction (0.84).  
- Decision Usefulness shows the widest cross‑model dispersion (up to 4.0 points) with high inter‑judge agreement (mean r = 0.52).

## Methodology  
CM‑LRS is built as a rubric that scores each of seven dimensions from 0 to 5, anchored on signals used by regulators and practitioners in capital‑markets workflows; the aggregate score can be tuned per workflow. The authors evaluate this rubric across five real‑world finance workflows—DCM transaction‑terms extraction, precedent retrieval, issuer profile synthesis, M&A comparable reasoning, and ECM transaction‑terms extraction—using public SEC EDGAR filings, a UK takeover release, and synthetic supplements. Four independent LLM judges rate each model’s output on the rubric.

## Results  
The comparative study shows that closed‑source frontier models achieve high reliability scores (average ≈ 4.31) whereas the open‑weights model lags significantly behind all others. The most pronounced gaps appear in retrieval and synthesis dimensions, indicating weaker grounding of answers to source material. Decision Usefulness exhibits the greatest variability across models, with a spread of up to four points, yet judges still agree strongly (r = 0.52). Extraction performance is relatively stable, reflecting its reliance on direct parsing rather than synthesis.

## Significance  
By providing a regulator‑aligned metric that captures both factual correctness and workflow completeness, CM‑LRS helps finance professionals assess whether LLM drafts are defensible in front of counter‑parties or regulators. This reduces reliance on superficial fluency checks and supports more trustworthy automation, thereby lowering risk in high‑stakes capital‑markets processes.

## Related Concepts  
Capital Markets LLM Reliability Score (CM‑LRS), factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, reviewability/auditability, rubric scoring 0–5, benchmarking closed‑source vs. open‑weights LLMs, retrieval/synthesis/extraction tasks, regulator‑driven signals, fintech workflow automation.
