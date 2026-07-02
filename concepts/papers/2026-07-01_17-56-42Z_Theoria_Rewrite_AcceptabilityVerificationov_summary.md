# Summary: 2026-07-01_17-56-42Z_Theoria_Rewrite_AcceptabilityVerificationoverInfor.md
Saved: 2026-07-01 23:01
Source: 2026-07-01_17-56-42Z_Theoria_Rewrite_AcceptabilityVerificationoverInfor.md
Model: None

---


## Summary  
The paper introduces **Theoria**, a verification framework that bridges the gap between formal proof assistants and opaque LLM judgments by treating an AI’s answer as a sequence of typed state transitions, each explicitly justified. By auditing every transition—whether via citation, computation, or problem‑given fact—the system can flag hidden premises or fabricated citations before they become silent errors. The approach yields a human‑readable proof trace where each step is independently challengeable, offering a more reliable alternative to holistic LLM scoring on complex reasoning tasks.

## Key Contributions  
- [Finding 1] **Theoria provides a formal verification pipeline that certifies AI answers with high precision (≈91.4% on Gold problems) while producing auditable proof traces.**  
- [Finding 2] The method detects hidden premises and fabricated citations at rates far exceeding holistic LLM judges, closing the ~11‑point performance gap where formal analysis predicts an advantage.  
- [Finding 3] Structured verification outperforms holistic judging on adversarial poisoned proofs across domains (94.7% vs. 83.2% precision, p = 0.0017).

## Methodology  
The authors model a candidate solution as a series of **typed state transitions**, each linked to an explicit justification source—citation, arithmetic computation, or a fact supplied by the problem. The core invariant is *completeness of change*: any difference between consecutive states must be accounted for; otherwise it appears as an unlicensed mutation. Each transition is stored in a trace that can be inspected and challenged independently.

## Results  
On HLE‑Verified Gold (185 text‑only expert problems), Theoria achieves 91.4% strict precision with a Wilson 95 % CI of [84.5%, 95.4%]. Every certification yields a human‑readable proof trace where each step is auditable. Holistic LLM judges reach comparable precision (Jaccard 0.14–0.36) but fail on different problems, resulting in a Jaccard overlap of 0.14–0.36. On 95 adversarial poisoned proofs across 15 domains, structured verification catches 94.7% versus 83.2% for holistic judging (p = 0.0017). The gap concentrates in hidden premises (90.6% vs. 62.5%) and fabricated citations (100% vs. 90%). Certified precision on GPQA Diamond is 97.1% (Wilson CI [85.1%, 99.5%]).

## Significance  
Theoria demonstrates that formal verification can be integrated into LLM‑based reasoning systems, providing a transparent audit trail and higher reliability where hidden assumptions matter. By offering precise, auditable proofs, it mitigates the opacity of holistic judgments and aligns with the need for trustworthy AI in high‑stakes domains.

## Related Concepts  
- Formal proof assistants (e.g., Coq, Isabelle)  
- LLM judges and holistic scoring  
- Typed state transitions and invariants  
- Auditable proof traces  
- Hidden premise detection  
- Adversarial poisoning of proofs
