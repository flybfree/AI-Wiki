# Summary: 2026-07-28_23-36-05Z_Automorphism_InducedNon_CanonicityinTop_kExplanati.md
Saved: 2026-07-29 21:33
Source: 2026-07-28_23-36-05Z_Automorphism_InducedNon_CanonicityinTop_kExplanati.md
Model: None

---

## Summary  
The paper investigates why gradient‑based Graph Neural Network (GNN) explainers often assign identical attribution scores to chemically equivalent atoms, such as two nitro groups in a molecule, and why the resulting top‑k edge reports are noncanonical. It shows that this behavior is not an implementation flaw but a structural consequence of permutation equivariance: any automorphism of the input graph leaves every attention score invariant, so no single‑valued rule can simultaneously be minimal, symmetry‑respecting, and optimal. The authors develop a parameter‑free, mechanised criterion in Lean 4 that decides from the graph alone whether every optimal report must split an orbit under the automorphism group, thereby quantifying the unavoidable arbitrariness. Their analysis reveals that this obstruction is pervasive—nontrivial automorphisms appear in 93.4 % of the Mutagenicity dataset and affect a substantial fraction of molecules at typical sparsity budgets.

## Key Contributions  
- [Finding 1] Gradient‑based GNN explanations cannot distinguish atoms belonging to the same orbit because message passing is exactly permutation equivariant, leaving attribution scores unchanged under any automorphism.  
- [Finding 2] When no minimal valid explanation respects the input’s automorphism group, there exists no rule that can be simultaneously single‑valued, minimal and symmetry‑preserving; optimal reports must split an orbit, introducing arbitrariness.  
- [Finding 3] A parameter‑free, mechanised criterion implemented in Lean 4 determines from the graph alone whether every score‑optimal top‑k report is forced to break an automorphism orbit, with no exception across 21 298 instance‑budget decisions.

## Methodology  
The authors start by formalising the problem of minimal valid explanations and the action of the automorphism group on attention scores. They prove that any explanation must be equivariant up to permutation, which forces orbits to split when a single edge is chosen from an orbit. To verify this claim computationally, they generate 21 298 random graphs at typical sparsity budgets, perform mechanical model‑equivalence checks, and compare the results with their Lean‑4 criterion. The verification confirms that no counterexample exists where a neutral alternative could exist without violating minimality or symmetry.

## Results  
Across all tested instances, the criterion agrees perfectly with mechanical equivalence (0 % disagreement). Crucially, the authors report that 93.4 % of molecules in Mutagenicity contain nontrivial automorphisms, and at a sparsity budget of 24.0 % of those molecules—specifically six out of twenty‑five with two interchangeable nitro groups—the top‑k explanation arbitrarily selects one atom without any underlying bias. No case was found where the model’s “blindness” to symmetry could be overridden by a different parameterisation.

## Significance  
The findings expose a fundamental limitation in current GNN explainability methods: they inherit and amplify graph symmetries, producing noncanonical reports that are not merely implementation quirks but mathematically inevitable. By providing a concrete, verifiable criterion, the work offers a path toward fairness‑aware explanations that respect chemical equivalence without sacrificing minimality or speed.

## Related Concepts  
- Permutation equivariance in GNN attention mechanisms  
- Automorphism groups of graphs and their action on subgraphs  
- Minimal valid explanation (MVE) and orbit splitting  
- Score‑optimal top‑k reports and their combinatorial properties  
- Formal verification via Lean 4 mechanisation
