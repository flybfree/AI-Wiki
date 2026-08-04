# Summary: 2026-08-03_11-07-37Z_Cross_FittedResidualUtilityforPrimary_PreservingCo.md
Saved: 2026-08-04 00:30
Source: 2026-08-03_11-07-37Z_Cross_FittedResidualUtilityforPrimary_PreservingCo.md
Model: None

---

## Summary  
The paper addresses the post‑inference problem in automatic modulation classification by introducing a cognitive decision policy that decides when to override a trusted default prediction. It proposes a cross‑fitted residual utility framework that learns candidate‑specific utilities from out‑of‑fold predictions while preserving primary evidence. The approach integrates neural and non‑neural candidates with a structured KAN‑Fourier classifier, freezing action thresholds during validation to evaluate the complete evidence‑and‑action policy. This yields consistent accuracy gains across three benchmark datasets.

## Key Contributions  
- Finding 1: Cross‑fitted residual utility learns candidate‑specific utilities from out‑of‑fold predictions.  
- Finding 2: Primary‑preserving cognitive decision policy maintains default prediction when evidence is insufficient.  
- Finding 3: Frozen‑policy stress test demonstrates robust gains under various impairments.

## Methodology  
The authors employ a structured KAN‑Fourier classifier to supply the default probability for each modulation class, while neural and non‑neural candidates provide observable evidence. Candidate‑specific residual utility is learned from train‑split out‑of‑fold predictions; a disjoint validation split freezes action thresholds, approved transitions, conditional routes, and a unified risk mask before held‑out evaluation. Paired bootstrap and Holm‑corrected McNemar analyses are used to assess gains.

## Results  
On RMLA the system improves overall accuracy from 63.632 % to 66.332 %; on RMLB it rises from 65.161 % to 66.168 %; on HISAR it increases from 77.769 % to 79.867 %. Controlled comparisons show that the isolated utility target does not uniformly dominate alternative out‑of‑fold meta‑learners; the consistent gain comes from the complete evidence‑and‑action policy. Paired bootstrap and Holm‑corrected McNemar analyses support these gains, and a frozen‑policy stress test under carrier‑frequency offset, I/Q imbalance, and synthetic Rayleigh/Rician fading yields positive improvements in all 11 conditions, with every paired 95 % confidence interval above zero.

## Significance  
The contribution improves overall accuracy significantly across three major benchmark datasets, providing a principled cognitive decision rule that respects primary evidence while allowing appropriate overrides. It demonstrates robustness to common impairments and offers a scalable framework for integrating diverse candidate signals in real‑time modulation classification.

## Related Concepts  
- Automatic modulation classification (AMC)  
- Cognitive receiver decision making  
- Residual utility learning  
- KAN‑Fourier classifier  
- Out‑of‑fold meta‑learning  
- Primary‑preserving policy
