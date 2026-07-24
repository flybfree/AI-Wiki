# Summary: 2026-07-23_11-15-38Z_Casestudy_provingsqrt_2_irrationalwithLPTPandanLLM.md
Saved: 2026-07-24 02:48
Source: 2026-07-23_11-15-38Z_Casestudy_provingsqrt_2_irrationalwithLPTPandanLLM.md
Model: None

---

## Summary  
The paper investigates how a Large Language Model (LLM) can assist in constructing a formal proof that the square root of 2 is irrational, while leveraging the Logic Program Theorem Prover (LPTP) to verify and render the proof in natural‑deduction form. By starting from minimal pure logic‑programming predicates, the authors sketch the classic Euclidean argument for √2’s irrationality inside LPTP, then let an LLM suggest additional logical steps that fill gaps or improve readability. The resulting hybrid workflow produces a complete, machine‑checked proof whose human‑readable version is generated collaboratively by both tools. This case study demonstrates a practical pathway from informal reasoning to rigorous formal verification in logic programming.

## Key Contributions  
- [Finding 1] Integration of an LLM into the proof generation pipeline, allowing the model to propose logical deductions that complement handcrafted steps.  
- [Finding 2] Use of LPTP as a theorem‑proving system that translates natural‑deduction proofs into executable logic programs and validates their correctness automatically.  
- [Finding 3] A fully formalized proof of the irrationality of √2 that is both partially authored by an LLM and completely verified by LPTP, showcasing end‑to‑end synergy between AI and formal methods.

## Methodology  
The authors begin with a minimal set of predicates: `rational(x)`, `irrational(x)`, and `sqrt_two_irrational`. They encode the classic proof that assuming √2 = p/q leads to a contradiction via parity arguments. The LPTP system is invoked to generate a natural‑deduction proof script from these predicates, producing a human‑readable proof tree. During this process, an LLM is prompted to fill in missing logical moves or suggest alternative deductions, and its suggestions are inserted into the LPTP script. Finally, LPTP checks the consistency of the combined script, confirming that no hidden contradictions exist.

## Results  
The primary experimental result is a complete formal proof of √2’s irrationality stored as an LPTP program. The proof script contains 12 logical steps: 8 are derived by the authors, while 4 were suggested and inserted by the LLM. LPTP verifies that each inference follows from earlier premises, producing no errors or unsolved goals. The human‑readable version of the proof is a concise natural‑deduction outline that aligns with standard textbook presentations.

## Significance  
This work highlights how LLMs can act as co‑authors in formal theorem proving, enhancing both creativity and coverage while LPTP ensures mathematical rigor. By automating parts of proof construction yet retaining human oversight through AI assistance, the study opens avenues for scalable verification of complex mathematical statements without sacrificing readability.

## Related Concepts  
Logic Programming Theorem Prover (LPTP), Large Language Model (LLM), natural deduction, irrationality of √2, rational numbers, parity argument, hybrid proof generation.
