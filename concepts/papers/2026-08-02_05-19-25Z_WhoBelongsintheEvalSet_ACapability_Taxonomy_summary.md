# Summary: 2026-08-02_05-19-25Z_WhoBelongsintheEvalSet_ACapability_Taxonomy_Driven.md
Saved: 2026-08-03 20:37
Source: 2026-08-02_05-19-25Z_WhoBelongsintheEvalSet_ACapability_Taxonomy_Driven.md
Model: None

---

## Summary  
This paper tackles the “regression‑economics paradox” that arises when platform teams must maintain a limited regression evaluation set while onboarding customers bring in domain‑specific eval sets. The authors propose a capability‑taxonomy‑driven pipeline that automatically decides, per query, whether to admit it into the regression set, drop it, swap an existing entry, or flag it for human review. By treating each query as exercising a combination of capabilities from a typed taxonomy, the system aims to keep the minimal set that captures maximal spread of capability signatures. The approach is taxonomy‑agnostic and can adapt when the taxonomy itself evolves based on the evidence produced by the pipeline.

## Key Contributions  
- [Finding 1] A hybrid classifier that merges deterministic specification extraction with LLM semantic inference to produce per‑query, per‑capability verdicts (admit/drop/swap/review).  
- [Finding 2] An Invocation Quality (IQ) rater that scores how thoroughly a query exercises each capability, enabling the system to recognize superior queries even when they share signatures with existing entries.  
- [Finding 3] A consolidator module employing rule‑based decision cascades and a conservative curator that only suggests evictions, ensuring incremental updates to the regression set.

## Methodology  
The pipeline consists of three intertwined components: (1) **Capability Extraction & Classification** – parses an agent specification and customer eval set to map each query onto capability tokens; (2) **IQ Scoring** – runs LLM‑based reasoning on how fully a query engages those capabilities, generating a numeric quality metric per capability; (3) **Consolidation & Curation** – compares incoming queries against the current regression set using coverage and IQ metrics, then applies a rule‑driven cascade that either retains, swaps, or removes entries. The conservative curator only proposes removals after human review, preserving data integrity.

## Results  
Experiments on Microsoft 365 Copilot agents show that the pipeline reduces the average regression set size by 27 % while increasing capability coverage from 0.48 to 0.61 across a diverse test suite. IQ scores correlate strongly (r = 0.89) with downstream regression performance, indicating that higher‑quality queries improve model evaluation fidelity. Human curators approve evictions at a rate of 5 % of suggested removals, confirming the conservative nature of the process.

## Significance  
By automating the selection of regression queries based on capability spread rather than arbitrary sampling, the pipeline addresses a critical bottleneck in agent‑extensibility platforms: maintaining a high‑quality evaluation set within strict release cadence constraints. The approach is reusable across any platform that defines a typed capability taxonomy, offering a scalable solution for future‑proof benchmark management.

## Related Concepts  
- Regression economy (trade‑off between query count and coverage)  
- Capability taxonomy (structured representation of agent functions)  
- Invocation Quality (metric quantifying how comprehensively a query exercises capabilities)  
- Hybrid classification (deterministic extraction + LLM inference)  
- Conservative curator (human‑in‑the‑loop safety net)
