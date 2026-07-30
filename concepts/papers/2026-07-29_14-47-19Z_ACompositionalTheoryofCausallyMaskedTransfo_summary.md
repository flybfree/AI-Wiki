# Summary: 2026-07-29_14-47-19Z_ACompositionalTheoryofCausallyMaskedTransformers.md
Saved: 2026-07-29 20:35
Source: 2026-07-29_14-47-19Z_ACompositionalTheoryofCausallyMaskedTransformers.md
Model: None

---

## Summary  
This paper asks what decision problems a causally masked transformer can solve when its internal arithmetic is limited by finite‑precision floating‑point rounding and the order of evaluation. By treating each attention head’s state as an element of a finite semigroup, the authors develop an algebraic formalism that derives expressivity directly from the model’s dynamics rather than relying on idealized arithmetic. Their analysis shows that the four possible attention types—definite, R‑trivial, locally R‑trivial, and aperiodic—correspond to distinct computational capabilities, and they prove that these bounds are tight under a free‑wiring assumption.

## Key Contributions  
- [Finding 1] The authors introduce an algebraic formalization that maps the finite internal state of each attention head to a semigroup operation, establishing a compositional view from model assumptions to expressivity limits.  
- [Finding 2] They identify four expressive cases for causal masked transformers: definite operations, R‑trivial operations, locally R‑trivial operations, and aperiodic semigroups, each realized by different attention mechanisms.  
- [Finding 3] Empirically they show that ordinary left‑to‑right floating‑point soft attention is more expressive than bounded‑suffix sliding‑window attention or checklist‑like irreversible memory.

## Methodology  
The researchers analyze a finite‑precision transformer layer as a composition of independent head updates. Each head’s state evolves according to a deterministic semigroup operation that depends only on the prefix visible to future queries. By composing these operations across layers, they derive upper and lower bounds on what functions can be computed. The analysis is performed without positional embeddings, focusing solely on the attention pattern and its numerical semantics.

## Results  
Theoretical results establish a hierarchy: width‑one sliding‑window attention supports bounded suffix memory (R‑trivial), modified soft attention yields irreversible checklist‑like state (locally R‑trivial), while ordinary left‑to‑right soft attention can realize the most expressive aperiodic semigroup. All four bounds are tight under the free‑wiring assumption, confirming that no additional architectural tricks can surpass these limits.

## Significance  
This work provides a precise computational taxonomy for causal masked transformers, clarifying the trade‑offs between memory efficiency and expressive power. It guides designers toward architectures that match their intended problem class to the appropriate attention mechanism, avoiding unnecessary complexity while respecting finite‑precision constraints.

## Related Concepts  
Causal masking, finite‑precision arithmetic, semigroup theory, R‑trivial operations, sliding‑window attention, checklist mechanisms, left‑to‑right soft attention.
