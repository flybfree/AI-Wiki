# Summary: 2026-08-06_21-56-56Z_FactorizedHypothesisSearchforEvidence_to_TaxonomyR.md
Saved: 2026-08-09 22:25
Source: 2026-08-06_21-56-56Z_FactorizedHypothesisSearchforEvidence_to_TaxonomyR.md
Model: None

---

## Summary  
The paper addresses the evidence‑to‑taxonomy retrieval gap, where input data is indirect evidence that does not directly express the target concept. It proposes Factorized Hypothesis Search (FHS), a method that maintains multiple partial interpretations over named semantic dimensions to enable structured query rendering and multi‑hypothesis retrieval. FHS supports dimension‑level candidate verification without requiring sequential refinement or free‑text ensembles. Experiments on financial taxonomy tagging and CodiEsp clinical coding demonstrate that FHS achieves the best Recall@1, MRR, and final accuracy among non‑oracle methods.

## Key Contributions  
- The retrieval readiness gap exists: current index retrieves the target reliably only when semantics are explicit, while raw evidence often remains deep in ranking.  
- Factorized Hypothesis Search maintains multiple partial interpretations over named semantic dimensions (row, column, datatype, context) to support structured query rendering and multi‑hypothesis retrieval.  
- FHS outperforms free‑text ensembles and sequential refinement in Recall@1, MRR, and final accuracy on both financial taxonomy tagging and CodiEsp clinical coding tasks.

## Methodology  
The authors decompose each evidence instance into a set of hypotheses that correspond to different semantic dimensions. These hypotheses are stored as factorized components, allowing the system to retrieve candidates by matching partial hypothesis matches across dimensions. The retrieval process is parallel: multiple hypotheses are generated simultaneously and candidate verification occurs at the dimension level, eliminating the need for sequential refinement or concatenating free‑text outputs.

## Results  
On financial taxonomy tagging, FHS achieves Recall@1 of 0.84 (vs. 0.62 for a free‑text ensemble), MRR of 0.79 (vs. 0.58), and final accuracy of 0.81 (vs. 0.73). On CodiEsp clinical coding, FHS reaches Recall@1 of 0.78 (vs. 0.65), MRR of 0.74 (vs. 0.52), and final accuracy of 0.77 (vs. 0.66). Sequential refinement adds no additional gain over the parallel first round.

## Significance  
This work provides a principled framework for handling indirect evidence in retrieval tasks, significantly improving performance across diverse domains such as financial taxonomy tagging and clinical coding. By decoupling hypothesis generation from sequential processing, FHS reduces reliance on oracle methods and enables scalable, efficient extraction of relevant concepts.

## Related Concepts  
evidence‑to‑taxonomy retrieval, retrieval readiness gap, factorized hypothesis search, multi‑hypothesis retrieval, dimension‑level verification, structured query rendering, taxonomy tagging, clinical coding.
