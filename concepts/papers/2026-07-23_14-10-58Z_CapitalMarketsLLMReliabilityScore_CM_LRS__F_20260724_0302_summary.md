# Summary: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
Saved: 2026-07-24 03:02
Source: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
Model: None

---

## Summary  
The paper introduces the Capital Markets LLM Reliability Score (CM‑LRS), a novel metric that evaluates large language model outputs at the workflow level rather than merely on question‑answer accuracy. By scoring seven dimensions—factual accuracy, evidence traceability, numerical consistency, workflow completeness, source discipline, decision usefulness, and reviewability/auditability—the authors aim to move from “plausible” drafts to truly “bankable” documents that regulators or counterparties can defend. The study compares four frontier closed‑source models with an open‑weights baseline across five capital‑markets workflows using independent judges, revealing systematic performance gaps.  

## Key Contributions  
- Finding 1: Closed‑source frontier models (Sonnet 4.6, Opus 4.7, GPT‑5.5) achieve a clustered average CM‑LRS of ~4.30, while the open‑weights Llama 3.3 70B scores lower at 3.15, indicating that model size alone does not guarantee reliability in regulated workflows.  
- Finding 2: The largest performance disparity occurs in retrieval (2.23 points) and synthesis (2.15 points), whereas extraction tasks show a smaller gap (0.84 points), suggesting that document‑grounded reasoning is more vulnerable than simple term extraction.  
- Finding 3: Decision usefulness exhibits the widest cross‑model dispersion (up to 4.0 points on issuer profiling) yet enjoys high inter‑judge agreement (mean r = 0.52), highlighting a trade‑off between consistency and domain relevance.  

## Methodology  
The authors designed CM‑LRS as a rubric anchored on signals used by reviewers in regulated settings, assigning each of the seven dimensions a 0–5 score. They evaluated five workflows—DCM transaction‑terms extraction, precedent retrieval, issuer profile synthesis, M&A comparable reasoning, and ECM term extraction—using public SEC EDGAR filings, a UK takeover release, and synthetic supplements. Four independent LLM judges (spanning GPT‑4‑style, Claude‑like, and proprietary models) scored each model’s output on all dimensions, producing an aggregate CM‑LRS that can be tuned per workflow.  

## Results  
The experimental results show that frontier closed‑source LLMs consistently outperform the open‑weights baseline across most dimensions, with the exception of extraction where the gap narrows. The retrieval and synthesis scores are the weakest links for both model families, underscoring a need for stronger document grounding. Decision usefulness shows high variance but also strong agreement among judges, indicating that subjective judgments can be reliably captured when aligned to regulatory expectations.  

## Significance  
CM‑LRS provides a concrete, rubric‑based metric that moves beyond surface fluency to assess whether LLM outputs are defensible in real capital‑markets workflows. By quantifying reliability across multiple dimensions, the framework helps firms and regulators evaluate model suitability before deployment, reducing risk of regulatory or contractual breaches.  

## Related Concepts  
- Large Language Models (LLMs)  
- Document‑grounded reasoning  
- Retrieval‑augmented generation (RAG)  
- Evaluation rubrics for regulated AI  
- Cross‑model performance clustering
