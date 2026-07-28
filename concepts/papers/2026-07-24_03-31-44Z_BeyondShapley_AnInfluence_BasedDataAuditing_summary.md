# Summary: 2026-07-24_03-31-44Z_BeyondShapley_AnInfluence_BasedDataAuditingPipelin.md
Saved: 2026-07-27 23:22
Source: 2026-07-24_03-31-44Z_BeyondShapley_AnInfluence_BasedDataAuditingPipelin.md
Model: None

---

## Summary  
The authors propose a scalable, inference‑only data auditing pipeline called “Beyond Shapley” that quantifies the predictive influence of individual training records in Large Language Model (LLM) alignment datasets without retraining models. By approximating the Shapley value through zero‑shot and one‑shot conditional log‑likelihood shifts on a reference LLM, they map semantic k‑NN neighborhoods into a directed graph to compute localized advantage scores for each record. The pipeline then isolates gradient‑conflicting records that cause hidden contradictions in preference or instruction data. Their experiments show dramatic reductions in manual audit effort and the discovery of systematic label failures across two major datasets.

## Key Contributions  
- [Finding 1] A zero‑shot, inference‑only method approximates Shapley values to evaluate each record’s predictive impact on a reference LLM’s probability distribution.  
- [Finding 2] Mapping semantic k‑NN neighborhoods into a directed graph yields localized advantage metrics that pinpoint gradient‑conflicting records.  
- [Finding 3] The pipeline reduces manual audit search space by ~99 % and uncovers falsely‑labeled or safety‑risk records in HelpSteer2, while exposing thousands of hidden preference inversions in Anthropic’s HH‑RLHF splits.

## Methodology  
The authors treat each training record as a node whose influence on the model’s output distribution is measured via conditional log‑likelihood differences between the reference LLM and the model after inclusion or exclusion of that record. These likelihood shifts are aggregated into a Shapley‑value approximation, which is then translated into advantage scores by constructing a directed graph where edges represent semantic proximity (k‑NN). Nodes with high adverse advantage become candidates for removal or correction. The entire process relies only on inference, enabling rapid auditing at scale.

## Results  
Applying the pipeline to HelpSteer2 cut manual audit effort by 99.1 % and revealed falsely‑labeled records across multiple failure modes. On Anthropic’s HH‑RLHF training and evaluation splits, it identified thousands of hidden safety and factual preference inversions. Crucially, auditing the evaluation split exposed a severe benchmark integrity issue: models often predict safer or more helpful responses, yet are penalized by objectively flawed human labels.

## Significance  
This work provides a mathematically grounded, highly efficient diagnostic tool that uncovers human label failures, sanitizes evaluation benchmarks, and safeguards LLM alignment data quality. By decoupling the audit from retraining, it enables continuous monitoring of dataset integrity in real time.

## Related Concepts  
Shapley value approximation, k‑NN neighborhood mapping, directed graph construction, conditional log‑likelihood shifts, data valuation pipeline, LLM alignment, dataset auditing, preference and instruction‑tuning corpora, semantic deduplication, LLM‑as‑a‑judge.
