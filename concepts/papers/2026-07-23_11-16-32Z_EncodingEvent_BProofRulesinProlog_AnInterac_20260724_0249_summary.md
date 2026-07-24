# Summary: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
Saved: 2026-07-24 02:49
Source: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
Model: None

---

## Summary  
The paper presents an encoding of Event‑B proof rules in Prolog to enable interactive proof construction and analysis within the ProB theorem prover for probabilistic programs. By translating over 600 event‑b proof rules into Prolog predicates, it creates a proof tree visualisation that students can manipulate directly, offering a more compact and extensible alternative to the earlier Java implementation.

## Key Contributions  
- Encoding of >600 Event‑B proof rules in Prolog for systematic analysis.  
- Development of an interactive sequent prover integrated with ProB, supporting trace export, HTML exploration, and back‑import to Rodin.  
- Demonstration that the Prolog encoding is more compact, maintainable, and extensible than the earlier Java version.

## Methodology  
The authors mapped each Event‑B rule into a Prolog predicate representing its logical form (e.g., event rules as Horn clauses). They built a sequent prover that maintains proof trees using Prolog’s backtracking search, allowing users to select rules interactively. The tool imports obligations from the Rodin platform, generates trace files, interactive HTML documents, and can export proofs back into Rodin, enabling the ProB prover to be used as a second chain.

## Results  
Compared with the Java prototype, the Prolog version reduces code size by roughly 40 % and improves extensibility; the interactive prover finds short proofs quickly using iterative deepening heuristics. Export formats are functional for both teaching (HTML) and validation pipelines (trace). The system demonstrates practical utility in educational settings.

## Significance  
Providing a lightweight, rule‑centric proof environment lowers barriers to learning event‑b reasoning and makes existing probabilistic verification tools more accessible; it also paves the way for automated provers that can be extended without rewriting core logic.

## Related Concepts  
Event‑B (event calculus), sequent calculus, Prolog, ProB (probabilistic program verifier), Rodin platform, interactive proof trees, Horn clauses, backtracking search.
