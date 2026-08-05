# Summary: 2026-08-02_05-58-00Z_Caliber_Cross_ArchitectureExtraction_CostControlfo.md
Saved: 2026-08-03 21:34
Source: 2026-08-02_05-58-00Z_Caliber_Cross_ArchitectureExtraction_CostControlfo.md
Model: None

---

## Summary  
Caliber proposes a defense for score‑returning APIs that mitigates model extraction by treating noise selection as a calibration problem: it balances the degradation of supervision signals used to train a surrogate against the per‑input cost of recovering clean logits. The authors prove two key properties—monotone agreement degradation and a closed‑form minimax lower bound on query complexity—and demonstrate that calibrated Gaussian perturbations can be fitted with a logistic curve, either per model or shared across tasks. Experiments across 30+ model‑dataset pairs show mean absolute relative errors of only 0.6–1.4% for per‑model calibration and end‑to‑end surrogate performance tracks the configured degradation. This work thus offers provable cost control and high accuracy for robust score‑returning systems.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- **Finding 1:** Monotone agreement degradation: when clean logits have a unique maximizer, agreement with the true prediction decreases strictly as noise scale increases, establishing computable lower and upper envelopes for task accuracy.  
- **Finding 2:** Per‑input recovery cost bound: a closed‑form minimax lower bound is derived on the number of repeated queries needed to recover clean logits for any fixed input.  
- **Finding 3:** Calibration achieves low MARE: per‑model calibration yields mean absolute relative errors between 0.6% and 1.4%, while end‑to‑end surrogate performance follows the configured degradation.

## Methodology  
Caliber adds independent Gaussian noise to internal logits, normalizing variance by the squared median top‑two logit margin to control signal loss. The authors fit a logistic curve to the resulting noise‑utility relationship, either per model or shared within a task, enabling systematic calibration of how much degradation is acceptable for surrogate training.

## Results  
Across more than thirty model‑dataset combinations, per‑model calibration attains mean absolute relative errors of 0.6–1.4%. Theoretical analysis provides a closed‑form minimax lower bound on query complexity. End‑to‑end experiments confirm that surrogate performance tracks the configured degradation, while fixed‑input averaging exhibits expected variance reduction.

## Significance  
By formalizing noise selection as a calibration problem and providing provable bounds on accuracy loss and query cost, Caliber enables robust score‑returning APIs that resist model extraction attacks without sacrificing utility. The approach offers a principled trade‑off between defense strength and computational expense, which is crucial for privacy‑preserving AI services.

## Related Concepts  
- Output perturbation defense  
- Calibration problem (balancing signal loss vs. cost)  
- Surrogate learning with degraded supervision  
- Score‑returning APIs and model extraction attacks  
- Gaussian noise injection  
- Logistic curve fitting for utility modeling  
- Median top‑two logit margin as a scaling factor
