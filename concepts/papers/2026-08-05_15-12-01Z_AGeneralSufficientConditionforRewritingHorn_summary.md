# Summary: 2026-08-05_15-12-01Z_AGeneralSufficientConditionforRewritingHorn_ALCHIA.md
Saved: 2026-08-05 23:13
Source: 2026-08-05_15-12-01Z_AGeneralSufficientConditionforRewritingHorn_ALCHIA.md
Model: None

---

## Summary  
The paper tackles the challenge of evaluating ontology‑mediated queries (OMQs) expressed in Horn‑ALCHI against the ISO standard GQL language. By introducing a novel formalism—DL automata—that captures the semantics of these OMQs as runs over fact sets, the authors demonstrate that a broad class of such queries can be rewritten into unions of conjunctive two‑way regular path queries (UC2RPQs), which constitute a core fragment of GQL. This rewrite is enabled by a state‑stratification technique that eliminates problematic cyclic dependencies, thereby providing a general sufficient condition for the conversion. The contribution therefore bridges expressive power between Horn‑ALCHI and GQL, opening new avenues for automated query translation in ontology systems.

## Key Contributions  
- [Finding 1] A general sufficient condition is established under which any Horn‑ALCHI atomic OMQ can be rewritten into a GQL expression.  
- [Finding 2] DL automata are defined to model the semantics of these queries and shown that they can be decomposed into unions of UC2RPQs.  
- [Finding 3] A stratification of automaton states is introduced, which removes cyclic dependencies and guarantees the applicability of the rewrite.

## Methodology  
The authors first translate Horn‑ALCHI atomic queries into a set of DL automata that operate on fact sets, preserving logical equivalence. They then analyze these automata by stratifying their state space into layers that respect dependency directions, thereby preventing cycles that would otherwise impede rewriting. Using this stratification, they construct UC2RPQs whose union reproduces the original query’s semantics. The methodology combines model‑theoretic reasoning with regular path‑query theory to achieve a systematic conversion process.

## Results  
Theoretical analysis proves that for any OMQ satisfying the stratified condition, the resulting GQL expression is equivalent and can be evaluated efficiently using standard UC2RPQ solvers. Experimental evaluation on synthetic Horn‑ALCHI instances confirms that the generated GQL queries produce identical results to the original ALCHI queries while leveraging existing GQL engines.

## Significance  
This work matters because it resolves a longstanding compatibility gap between descriptive logic and modern query languages, enabling seamless integration of ontology reasoning into GQL‑based systems. By providing a general sufficient condition and practical conversion tools, the paper enhances the usability of Horn‑ALCHI in large‑scale knowledge graphs and supports automated reasoning pipelines.

## Related Concepts  
Horn‑ALCHI (a Description Logic), GQL (first‑order logic with controlled recursion), UC2RPQ (conjunctive two‑way regular path queries), DL automata, stratified state spaces, cyclic dependencies in query translation.
