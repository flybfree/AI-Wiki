# Summary: 2026-07-28_15-42-53Z_Stemma_InducedDecisionRegionsRevealLLMProvenance.md
Saved: 2026-07-28 22:54
Source: 2026-07-28_15-42-53Z_Stemma_InducedDecisionRegionsRevealLLMProvenance.md
Model: None

---

## Summary  
The paper tackles the challenge of verifying whether a suspect large language model (LLM) originates from the same lineage as a source model, despite surface‑form changes that can alter response characteristics. By abstracting open‑ended LLM outputs into a finite decision space through induced decision regions, the authors reframe provenance testing as measuring inheritance of these stable regions rather than raw textual responses. They introduce Stemma, a black‑box fingerprinting method that leverages three probe‑selection principles—stability, robustness, and specificity—to estimate this inheritance reliably. The approach achieves state‑of‑the‑art performance on both benchmark and deployment‑wide datasets.

## Key Contributions  
- **Induced decision regions** map open‑ended LLM outputs into a finite space, abstracting surface variation and isolating the underlying decision logic that persists across adaptations.  
- **Stemma**, a practical black‑box fingerprinting tool, operationalises stability, robustness, and specificity as complementary probe‑selection principles to measure region inheritance with high precision and recall.  
- The method outperforms four baselines: 0.967 AUC / 87.8 % TPR at 1 % FPR on 770 source‑suspect pairs; 0.995 AUC / 93.5 % TPR at 1 % FPR across 1,260 pairs from 91 diverse deployment instances.

## Methodology  
The authors first define an induced decision region as the set of input‑output pairs that trigger a specific output class in a classifier trained on the source model’s outputs. This mapping collapses continuous textual variation into discrete regions, preserving the logical structure of the model’s behavior. Stemma then evaluates whether suspect models produce responses that fall within the same region by measuring three probe metrics: stability (region preservation under adaptation), robustness (consistency across different deployment settings), and specificity (ability to distinguish source from unrelated lineages). The probe‑selection principle guides which regions are probed, ensuring the test is both sensitive and specific.

## Results  
Across 770 pairs drawn from 56 public checkpoints spanning model‑weight transformations, Stemma achieves an AUC of 0.967 with a true‑positive rate (TPR) of 87.8 % at a false‑positive rate (FPR) of 1 %. On a broader set of 1,260 pairs covering 91 deployment instances, performance improves to AUC = 0.995 and TPR = 93.5 % at the same FPR. These results surpass four representative baselines in both precision and recall.

## Significance  
Accurate LLM provenance testing is critical for security, licensing compliance, and model‑governance, yet existing black‑box methods are vulnerable to surface changes that obscure lineage signals. Stemma’s induced decision regions provide a principled abstraction that isolates the underlying decision logic, delivering high‑confidence provenance estimates even when models are adapted or deployed in varied environments.

## Related Concepts  
- LLM provenance testing  
- Induced decision regions  
- Black‑box fingerprinting  
- Stability, robustness, specificity (probe‑selection principles)  
- AUC, TPR, FPR metrics  
- Model lineage / checkpoint verification  
- Deployment‑time inference settings
