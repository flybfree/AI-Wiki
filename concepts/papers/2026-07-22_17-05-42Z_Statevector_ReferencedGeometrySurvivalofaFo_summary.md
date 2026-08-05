# Summary: 2026-07-22_17-05-42Z_Statevector_ReferencedGeometrySurvivalofaFour_Qubi.md
Saved: 2026-07-23 00:02
Source: 2026-07-22_17-05-42Z_Statevector_ReferencedGeometrySurvivalofaFour_Qubi.md
Model: None

---

## Summary  
The paper investigates whether the geometry encoded by a frozen four‑qubit ZZ feature map survives execution on IBM Quantum hardware, using it as a diagnostic for quantum kernel methods. It measures survival across three single‑job configurations—baseline, dynamical decoupling alone, and gate twirling alone—each with 1024 shots per circuit on the ibm_fez backend. The authors reconstruct Gram matrices from N = 24 real indoor air‑quality windows and assess preservation via full‑matrix centered kernel alignment (CKA) and other metrics. While hardware noise dominates over finite sampling, the study demonstrates that gate twirling preserves geometry best, whereas dynamical decoupling offers no clear advantage.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- Finding 1: Gate twirling yields the highest CKA values (0.933–0.989) and full‑matrix centered kernel alignment, indicating it is the most faithful configuration for preserving the ZZ geometry.  
- Finding 2: Dynamical decoupling alone does not separate from the baseline; residual hardware distortion remains the dominant source of error rather than finite shot noise.  
- Finding 3: The most faithful execution (gate twirling) exhibits the lowest centered kernel‑target alignment, which is at or below label‑permutation references for both statevector and hardware, revealing a reversal between fidelity and geometric preservation.

## Methodology  
The authors employ a frozen four‑qubit ZZ feature map on 24 real indoor air‑quality windows to generate a Gram matrix. They execute each configuration as a single non‑interleaved job with 1024 shots per circuit, measuring the survival of the intended geometry via full‑matrix centered kernel alignment (CKA), mean absolute error, and Spearman correlation. The three configurations—baseline (no mitigation), dynamical decoupling alone, and gate twirling alone—are compared to assess which mitigates hardware distortion most effectively.

## Results  
All three configurations produced a complete, finite, positive‑semidefinite Gram matrix, confirming that the kernel is not broken by error accumulation. CKA scores for gate twirling (0.933–0.989) exceed those of baseline and dynamical decoupling alone. Dynamical decoupling fails to improve upon baseline at the frozen‑window scale, indicating that hardware noise persists. Moreover, fidelity and label alignment are inversely related: the configuration with highest fidelity also shows the lowest centered kernel‑target alignment, which is below reference values for both statevector and hardware.

## Significance  
These findings highlight that quantum kernel methods assume geometry survival but often encounter non‑affine distortions from hardware noise rather than finite sampling. The study provides a fixed‑subset diagnostic across three mitigation strategies, emphasizing the need to report both implementation fidelity (CKA) and task relevance (label alignment). It underscores that quantum advantage claims should not conflate hardware performance with algorithmic success.

## Related Concepts  
Gram matrix, ZZ feature map, IBM Quantum (ibm_fez), statevector geometry preservation, CKA metric, frozen window, dynamical decoupling, gate twirling, finite sampling vs. hardware distortion, quantum kernel method, quantum advantage claim, hardware classifier superiority, implementation fidelity, task relevance.
