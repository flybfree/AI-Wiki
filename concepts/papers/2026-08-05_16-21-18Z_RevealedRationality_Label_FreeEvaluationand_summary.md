# Summary: 2026-08-05_16-21-18Z_RevealedRationality_Label_FreeEvaluationandRegular.md
Saved: 2026-08-05 22:32
Source: 2026-08-05_16-21-18Z_RevealedRationality_Label_FreeEvaluationandRegular.md
Model: None

---

## Summary  
The paper argues that representation theorems in decision theory provide a foundation for label‑free evaluation and regularization of LLMs by checking axiom compliance from the model’s own responses to synthetic choice problems. It introduces three rationalities—probabilistic coherence via de Finetti, preference rationality via Afriat, and subjective expected utility via Echenique–Saito—and derives continuous penalties that vanish when behavior is rationalizable. The approach allows objective assessment without external labels or human feedback.

## Key Contributions  
- Finding 1: Representation theorems give necessary‑and‑sufficient conditions for rational behavior.  
- Finding 2: Axiom compliance can be evaluated label‑free using synthetic choice problems, yielding computable penalties.  
- Finding 3: Continuous rationality penalties derived from three distinct theoretical frameworks complement existing evaluation signals.

## Methodology  
The authors construct synthetic choice tasks that map model outputs to decision variables and then apply the respective representation theorems to compute whether the model’s behavior satisfies the corresponding axiom. Penalties are calculated as continuous functions of the output distribution or preference ranking, zero when the theorem is satisfied. This procedure isolates rationality violations from any external labeling.

## Results  
Theoretical analysis shows that penalties vanish exactly on rationalizable data; empirical tests on LLM responses demonstrate that models scoring zero under each rationality test exhibit behavior consistent with the respective axioms. The combined penalties provide a unified regularization signal across coherence, preference, and utility domains.

## Significance  
By grounding evaluation in necessary‑and‑sufficient theorems, the method offers a principled, label‑free way to detect rational anomalies, potentially improving model alignment without relying on costly human feedback or external benchmarks.

## Related Concepts  
- Representation theorem (decision theory)  
- De Finetti’s theorem (probabilistic coherence)  
- Afriat’s theorem (preference rationality)  
- Echenique–Saito theorem (subjective expected utility)
