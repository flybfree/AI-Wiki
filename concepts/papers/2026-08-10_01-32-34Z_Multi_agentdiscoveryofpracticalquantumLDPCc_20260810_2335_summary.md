# Summary: 2026-08-10_01-32-34Z_Multi_agentdiscoveryofpracticalquantumLDPCcodes.md
Saved: 2026-08-10 23:35
Source: 2026-08-10_01-32-34Z_Multi_agentdiscoveryofpracticalquantumLDPCcodes.md
Model: None

---

## Summary  
The paper aims to discover practical quantum low‑density parity‑check (qLDPC) codes that satisfy hardware constraints such as binary CSS construction, block length ≤ 400, and overall weight ≤ 10. It introduces a multi‑agent discovery framework that combines specialist proposal and review, persistent scientific memory, long‑horizon evolution of executable programs, and deterministic construction/evaluation within a closed loop. The search space is populated by coset‑orbit balanced‑product codes, which include bicycle and lifted‑product constructions as well as non‑normal subgroup actions. The framework yields concrete code instances with competitive rate–distance performance for every weight class considered.

## Key Contributions  
- [Finding 1] Discovery of high‑rate‑distance code instances such as [[288, 16, 18]] at weight 7 and [[288, 18, 18]] at weight 9 within the imposed constraints.  
- [Finding 2] Identification of structurally distinct constructions, including a candidate [[336, 12, ≤24]] and a genuine [[368, 18, 16]], both realized as balanced‑product codes with non‑normal subgroup actions.  
- [Finding 3] Demonstration that these codes achieve low logical failure rates under depolarizing noise when decoded via the BP‑OSD protocol.

## Methodology  
The authors adopt a multi‑agent scientific discovery framework: specialist agents propose candidate qLDPC code parameters, while review agents evaluate their viability. A persistent memory stores past proposals and evaluations to guide long‑horizon evolution of executable programs that implement coset‑orbit balanced‑product constructions. The search is deterministic, constructing and evaluating each candidate within a closed loop, thereby guaranteeing reproducibility and scalability.

## Results  
The framework discovers codes with leading or competitive rate–distance performance across all weight classes up to 10. Representative instances include [[288, 16, 18]] (w=7), [[288, 18, 18]] (w=9) and [[234, 28, 18]] (w=10). Additional candidates are a [[336, 12, ≤24]] code and a [[368, 18, 16]] code. All codes exhibit low logical error rates under depolarizing noise when processed by the BP‑OSD decoding protocol.

## Significance  
These results provide hardware‑relevant finite‑length qLDPC candidates that can be directly evaluated in experimental settings. The structured agentic search demonstrates how combining AI‑driven proposal/review and deterministic construction/evaluation can accelerate scientific discovery, offering a template for future practical quantum code design.

## Related Concepts  
qLDPC codes, CSS (concatenated) codes, balanced‑product constructions, coset‑orbit codes, non‑normal subgroup actions, BP‑OSD decoding protocol, multi‑agent scientific discovery framework.
