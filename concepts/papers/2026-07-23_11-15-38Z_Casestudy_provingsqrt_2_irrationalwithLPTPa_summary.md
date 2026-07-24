# Summary: 2026-07-23_11-15-38Z_Casestudy_provingsqrt_2_irrationalwithLPTPandanLLM.md
Saved: 2026-07-24 02:40
Source: 2026-07-23_11-15-38Z_Casestudy_provingsqrt_2_irrationalwithLPTPandanLLM.md
Model: None

---

## Summary
The paper presents a case study where an LLM collaborates with LPTP to prove that sqrt(2) is irrational, using logic programming predicates and natural deduction. It demonstrates how LLMs can assist in generating proof fragments while LPTP verifies them. The work showcases integration of AI‑generated reasoning with formal theorem proving. The contribution lies in a partially human‑written but LLM‑assisted proof that is fully checked by the prover. The collaboration illustrates how generative AI can be harnessed within a formal proof environment.

## Key Contributions
- Integration of an LLM into LPTP to generate proof fragments for irrationality of sqrt(2), showing that the model can produce syntactically correct natural‑deduction clauses.
- Use of natural deduction syntax within LPTP, making proofs readable and verifiable by human experts.
- Demonstration that AI‑generated content can be fully verified by a theorem prover, achieving zero verification errors in this case.

## Methodology
The authors defined pure logic programming predicates such as rational(x) and sqrt2(x) and then used LPTP's proof language to encode the classic contradiction argument that assumes sqrt(2)=p/q leads to p^2=2q^2, implying both p and q even, contradicting coprimality. The LLM was prompted to produce the sequence of deduction steps; those snippets were inserted into the LPTP script. The human reviewed and edited the AI output for correctness.

## Results
The final proof consists of 12 natural‑deduction clauses that LPTP accepted as a correct theorem. The AI contributed roughly half of the clause generation, while the human authored the rest and ensured logical consistency. Verification confirmed that all clauses were syntactically valid and logically sound, with no contradictions detected.

## Significance
This study highlights a practical pathway for augmenting formal verification with generative AI, reducing manual proof effort and enabling scalable automation in logic programming. This approach could be extended to other mathematical theorems requiring formal proof generation.

## Related Concepts
Logic Programming (LP), LPTP theorem prover, Natural Deduction, Large Language Models (LLMs), Irrationality of sqrt(2), Coprimality argument, Formal Verification
