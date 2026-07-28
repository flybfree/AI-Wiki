# Summary: 2026-07-26_07-07-29Z_FormalizingFlagAlgebrasinLean.md
Saved: 2026-07-27 23:53
Source: 2026-07-26_07-07-29Z_FormalizingFlagAlgebrasinLean.md
Model: None

---

## Summary  
The paper formalizes Razborov’s flag‑algebra method for proving asymptotic extremal graph inequalities as a machine‑checked proof in Lean. It introduces a compiler that converts semidefinite‑programming certificates into algebraic proofs, independently verifying all intermediate facts over the rational numbers. The work extends beyond verification to produce concrete Turán‑type upper bounds and matching constructions, while also exploring two competing ways of imposing graph constraints within the flag algebra.  

## Key Contributions  
- [Finding 1] A complete machine‑checked formalization of the flag‑algebra framework for finite simple graphs, covering partially labeled graphs, density expressions, quotient algebras, positive homomorphisms, and downward operators.  
- [Finding 2] A certificate‑to‑proof compiler that treats external SDP output as candidate data, computes required densities over ℚ, checks exact positive semidefiniteness, and performs algebraic normalization to generate Lean proofs.  
- [Finding 3] Seven Turán‑type upper bounds (Mantel’s theorem, Erdős pentagon theorem, C₄ density bound for triangle‑free graphs, edge‑density bounds for K₄‑free, K₅‑free and C₅‑free graphs), matching constructions that achieve the exact Turán densities of Mantel and Erdős pentagon, and proofs of two Goodman inequalities.  

## Methodology  
The authors approached the problem by first laying out the theoretical foundations of flag algebra: they defined partially labeled graphs, their asymptotic densities, the quotient algebra obtained from density expressions, graph‑limit semantics realized via positive homomorphisms, and downward operators that average labels. The formalization is implemented in Lean, where the compiler receives a semidefinite program output as untrusted data; instead of accepting it blindly, Lean recomputes all required quantities, verifies their rational positivity definiteness, and carries out the normalization steps that produce the final algebraic proof. A secondary part of the work investigates two constraint‑handling strategies—building hereditary constraints into the algebra from the start versus testing inequalities on constrained limits with random label choices—and derives a root‑plantability criterion to compare them.  

## Results  
The formalization yields verified proofs for seven Turán‑type upper bounds, including Mantel’s theorem and the Erdős pentagon theorem, as well as a C₄ density bound for triangle‑free graphs and edge‑density bounds for K₄‑free, K₅‑free and C₅‑free graphs. The compiler also produces matching constructions that complete the exact Turán densities of Mantel’s theorem and Erdős pentagon, and it formally proves two inequalities of Goodman. A meta‑theoretical result is obtained: a root‑plantability criterion characterizing when the two constraint‑handling approaches agree.  

## Significance  
This work bridges extremal graph theory with formal verification, providing machine‑checked certificates that can be trusted without external trust assumptions. It demonstrates how flag algebra can be used to generate and verify proofs automatically, enabling reproducible research in combinatorial optimization. The meta‑theoretic comparison of constraint strategies offers deeper insight into the structure of flag‑algebra proofs and may guide future automated theorem‑proving systems.  

## Related Concepts  
flag algebra method, semidefinite programming certificates, partially labeled graphs, density expressions, quotient algebras, positive homomorphisms, downward operators, Turán‑type inequalities, root‑plantability criterion, hereditary constraints, machine‑checked proofs in Lean.
