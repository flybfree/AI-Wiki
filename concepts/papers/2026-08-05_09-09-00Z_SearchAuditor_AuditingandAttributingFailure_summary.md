# Summary: 2026-08-05_09-09-00Z_SearchAuditor_AuditingandAttributingFailuresinLong.md
Saved: 2026-08-06 21:40
Source: 2026-08-05_09-09-00Z_SearchAuditor_AuditingandAttributingFailuresinLong.md
Model: None

---

## Summary  
Deep search agents generate long‑horizon web interactions that can propagate small reasoning errors into fluent but incorrect answers, making failure diagnosis a bottleneck for humans. This paper introduces SearchAuditBench, a benchmark of expertly annotated failed trajectories, and builds SearchAuditor, a multi‑perspective auditing framework that localizes, attributes, and repairs these failures automatically. By grounding adjudication in evidence from the trace, SearchAuditor reduces reliance on manual inspection and enables agents to recover more effectively. The work demonstrates that even frontier models struggle with error attribution without such tools.

## Key Contributions  
- Finding 1: Creation of SearchAuditBench, a benchmark containing 1,243 expertly annotated failed trajectories from eight open‑weight models across five deep‑search benchmarks.  
- Finding 2: Design of SearchAuditor, a multi‑perspective framework that localizes the critical error step, attributes it to a specific search‑specific root cause, and proposes a repair using evidence‑grounded adjudication.  
- Finding 3: Demonstration that SearchAuditor consistently outperforms all baselines, achieving an end‑to‑end pass rate of 32.3% versus 26.6% for the strongest baseline (GPT‑5.5), and that its repairs improve agent recovery.

## Methodology  
The authors assembled a dataset by extracting failed execution traces from eight open‑weight models on five deep‑search benchmarks, annotating each trace with the critical error step, a search‑specific root cause, and a reference repair with grading rubrics. SearchAuditor comprises three modules: a localizer that extracts the failure point, an attributor that links it to the identified root cause, and a repairer that generates a corrected continuation based on the evidence. These modules operate in parallel, producing a unified audit output that can be fed back into the search agent.

## Results  
Experiments show that the strongest baseline (GPT‑5.5) reaches only 26.6% end‑to‑end pass rate when auditing failures. In contrast, SearchAuditor achieves a higher 32.3% pass rate across all frontier models and its repair actions enable agents to resume execution more reliably, reducing the number of dead‑ended trajectories.

## Significance  
This work alleviates the manual inspection burden for long‑horizon search agents, providing an automated pipeline that can diagnose and fix errors at scale. By improving attribution accuracy and recovery rates, SearchAuditor enhances the robustness and reliability of complex reasoning systems, which is crucial as these agents become more widely deployed.

## Related Concepts  
Long‑horizon search agents, failure propagation, trace auditing, error attribution, repair generation, evidence‑grounded adjudication, benchmark evaluation, multi‑perspective frameworks.
