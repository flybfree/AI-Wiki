# Summary: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
Saved: 2026-07-24 02:56
Source: 2026-07-23_11-16-32Z_EncodingEvent_BProofRulesinProlog_AnInteractiveSeq.md
Model: None

---

## Summary  
The paper presents an encoding of Event‑B proof rules in Prolog, enabling a Prolog‑based interactive sequent prover for ProB that visualizes proof trees and supports teaching and validation. It integrates hundreds of rule encodings into the ProB framework, allowing users to select rules interactively and export proofs to multiple formats. Compared with previous Java implementations, the Prolog encoding is more compact and extensible. The authors aim to develop fast automatic provers for larger domains.

## Key Contributions  
- [Finding 1] Encoding over 600 Event‑B proof rules in Prolog for systematic analysis.  
- [Finding 2] Integration into ProB creates an interactive proof system with tree visualization.  
- [Finding 3] Export capabilities: trace files, HTML docs, and back‑compatibility to Rodin.

## Methodology  
The authors approached the problem by translating each Event‑B rule into a Prolog predicate that captures its logical structure. They used the existing ProB framework as a host, allowing rules to be loaded dynamically. The interactive prover is built on iterative deepening with simple heuristics; later they plan to replace it with faster automatic provers. Proof trees are generated and rendered in HTML for tool‑independent exploration.

## Results  
The system successfully encodes 600+ rules, producing compact Prolog code compared to Java. Interactive proof construction was demonstrated by students selecting rules to build proofs of sample propositions. Exports include trace files compatible with ProB, interactive HTML documents that display the full tree, and back‑compatible outputs for Rodin. The iterative deepening prover finds short proofs quickly.

## Significance  
This work bridges formal verification and education, offering a maintainable, extensible proof engine that can be reused across tools. By using Prolog’s expressive power, the authors reduce overhead and enable easy addition of new rules. It also supports automated provers for larger domains, advancing both research and teaching in event‑based reasoning.

## Related Concepts  
Event‑B, predicate logic, set theory, Prolog, ProB, Rodin, interactive proof tree visualization, iterative deepening, automatic prover.
