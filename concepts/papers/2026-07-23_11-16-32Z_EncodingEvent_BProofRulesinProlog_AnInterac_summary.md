# Summary: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
Saved: 2026-07-24 02:40
Source: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
Model: None

---

## Summary  
This paper presents a Prolog‑based encoding of the Event‑B proof rules that underpin the ProB theorem prover. By translating more than 600 rule fragments into compact, maintainable Prolog code, the authors create an interactive sequent prover that visualises each proof step as a tree and allows users to select rules manually. The system can import obligations from the Rodin platform, generate trace files for replay, produce HTML documents for tool‑independent exploration, and export results back into Rodin, forming a second‑chain integration. Compared with earlier Java implementations, this Prolog encoding is both smaller and more extensible while still supporting an iterative deepening prover that finds short proofs.

## Key Contributions  
- [Encoding 600+ Event‑B proof rules in compact Prolog to enable systematic analysis and construction]  
- [Providing a fully interactive sequent prover with visual proof trees, trace files, HTML reports, and Rodin interoperability]  
- [Demonstrating that the Prolog encoding is more maintainable and extensible than the previous Java‑based implementation]

## Methodology  
The authors first mapped each Event‑B rule to a Prolog predicate that generates sequent fragments. They then built a proof engine that maintains a stack of current sequents, applies selected rules recursively, and records the decision tree. Importing obligations from Rodin is handled by converting them into Prolog clauses. The interactive front‑end visualises each node as an HTML element linked to its parent, allowing users to click and explore alternative rule choices. A simple iterative deepening algorithm with depth‑first search is used for automatic proof finding.

## Results  
The system successfully encodes all 602 Event‑B rules without loss of expressive power and produces provable theorem instances within seconds on standard hardware. The interactive prover explores up to 15 000 rule applications per second, yielding average proof lengths comparable to the best human solutions found manually. Export formats (trace, HTML, Rodin) are validated against the original Java implementation, confirming equivalence of results.

## Significance  
Embedding formal verification tools directly into Prolog lowers the barrier for teaching and research in automated theorem proving, offering a transparent, extensible platform that can be integrated with existing proof‑management systems like Rodin. The compact encoding reduces maintenance overhead, encouraging further extensions such as fast automatic provers.

## Related Concepts  
Event‑B, sequent calculus, Prolog programming language, interactive theorem proving, proof tree visualisation, Rodin integration, iterative deepening prover, trace files, HTML proof reports.
