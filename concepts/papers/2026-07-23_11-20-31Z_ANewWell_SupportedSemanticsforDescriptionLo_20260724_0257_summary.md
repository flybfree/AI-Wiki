# Summary: 2026-07-23_11-20-31Z_ANewWell_SupportedSemanticsforDescriptionLogicProg.md
Saved: 2026-07-24 02:57
Source: 2026-07-23_11-20-31Z_ANewWell_SupportedSemanticsforDescriptionLogicProg.md
Model: None

---

## Summary  
The paper proposes a new semantics for description logic programs that improves on the existing well‑supported semantics by evaluating ontological atoms more strictly, preserving NP‑complete consistency while eliminating higher‑level complexity and offering a reduct transformation characterization. It also identifies a syntactic class where this new semantics is equivalent to the old one, providing equivalence guarantees. The goal is to maintain well‑supportedness with a stricter notion that aligns better with logic programming.

## Key Contributions  
- [Finding 1] A new strict semantics that evaluates ontological atoms more strictly than the current semantics.  
- [Finding 2] Complexity of consistency remains NP‑complete rather than moving to the second level of the polynomial hierarchy.  
- [Finding 3] Identification of a syntactic class where the new semantics is equivalent to the old one, with reduct‑based transformation characterization.

## Methodology  
The authors analyze the limitations of existing well‑supported semantics—its high computational complexity and lack of reduction characterisation—and design a semantics using a fixpoint operator that processes ontological atoms in a deterministic order. They develop a reduct transformation that maps programs from the old semantics to the new one, ensuring equivalence on the identified syntactic class.

## Results  
The new semantics is proven to be strictly weaker than the prior well‑supported semantics, thus preserving well‑supportedness while being more computationally tractable. Consistency remains NP‑complete; no known algorithm improves it beyond this bound. The reduct transformation yields a decidable mapping for programs in the identified syntactic class.

## Significance  
By tightening the notion of well‑supportedness and aligning it with logic programming semantics, the paper offers a cleaner theoretical foundation and practical computational benefits for DL program solvers.

## Related Concepts  
Description Logic Programs, Well‑Supported Semantics, NP‑complete Consistency, Reduct Transformations, Fixpoint Operators, Ontological Atoms, Logical Programming.
