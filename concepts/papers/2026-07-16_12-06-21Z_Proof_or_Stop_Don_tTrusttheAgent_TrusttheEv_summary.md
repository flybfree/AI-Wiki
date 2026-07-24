# Summary: 2026-07-16_12-06-21Z_Proof_or_Stop_Don_tTrusttheAgent_TrusttheEvidence_.md
Saved: 2026-07-23 23:46
Source: 2026-07-16_12-06-21Z_Proof_or_Stop_Don_tTrusttheAgent_TrusttheEvidence_.md
Model: None

---

## Summary  
The paper introduces Proof‑or‑Stop, a loop engineering approach that gates autonomous agent lifecycle transitions only when fresh, verifiable evidence is produced. It treats agent outputs as claims rather than states and uses proof operations to enforce trust‑based gate acceptance. The method prevents false DONE or ready‑to‑merge events by requiring mechanically verifiable source‑state‑bound evidence. Evaluation shows zero false completions in 10 scenarios and a significant reduction in amplified failures.

## Key Contributions  
- Proof‑or‑Stop enables lifecycle transitions only when fresh, tracked‑source‑state‑bound, mechanically verifiable evidence satisfies the gate.  
- The unattended‑loop engine passed all 10 scenario tests with zero false DONE outcomes while rejecting 18 tamper classes without any false accepts.  
- Ablation experiments demonstrate a 1.6 percentage‑point improvement in not‑amplified rate and near‑compute A3 versus A4 comparison, indicating that enforcing review as a gate matters more than merely adding a reviewer.

## Methodology  
The authors designed Proof‑or‑Stop as a model‑agnostic control layer that monitors agent claims against evidence bundles; they implemented an unattended‑loop engine that validates source state via proof operations before allowing any transition. Experiments include mechanism tests, powered control‑policy ablation, and self‑application evidence generation across 24 tasks.

## Results  
In the 10 scenario test suite, the system achieved zero false DONE events. Tamper rejection succeeded for all 18 classes. The 9,240‑cell ablation reduced visible‑pass/hidden‑fail amplification from 31 to 2 cells (a 1.6 pp improvement, CI [0.8, 2.5]), and the A3 versus A4 comparison showed 14 vs 2 failures respectively.

## Significance  
By decoupling trust from semantic correctness and embedding evidence‑gated gates into lifecycle control, Proof‑or‑Stop offers a robust, model‑agnostic safeguard for autonomous coding agents, reducing false completions and amplifications in large codebases.

## Related Concepts  
- Lifecycle control  
- Proof operations  
- Loop engineering  
- Tamper detection  
- Evidence bundles  
- Self‑application  
- Verification  
- Automated coding agents
