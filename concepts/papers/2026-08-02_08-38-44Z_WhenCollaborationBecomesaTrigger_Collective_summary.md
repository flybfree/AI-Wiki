# Summary: 2026-08-02_08-38-44Z_WhenCollaborationBecomesaTrigger_CollectiveEvidenc.md
Saved: 2026-08-03 23:59
Source: 2026-08-02_08-38-44Z_WhenCollaborationBecomesaTrigger_CollectiveEvidenc.md
Model: None

---

## Summary  
[The paper addresses a vulnerability in LLM‑based multi‑agent systems where backdoor behavior is triggered only when peer evidence accumulates to a hidden threshold, rather than by individual messages.] [It introduces the collective evidence‑threshold backdoor paradigm and a defense mechanism called Boundary‑Conditioned Backdoor Injection (BCBI).] [BCBI creates counterfactual boundary pairs to isolate benign from adversarial behavior while learning latent progression aligned with evidence.] [The authors also propose LAtent Transition Test‑time Evaluation (LATTE) as a clean‑only test that quarantines anomalous updates before propagation.]

## Semantic links
- [[concepts/papers/2026-08-04_00-24-06Z_TQLite_Multi_LLMJuryGuidedDistillationforRe_summary.md|Summary: 2026-08-04_00-24-06Z_TQLite_Multi_LLMJuryGuidedDistillationforReal_time.md]] — 4 title terms overlap; 11 summary/topic terms overlap; semantic match 0.05
- [[concepts/papers/2026-08-04_09-31-44Z_LLM_DerivedPriorsforThompsonSamplinginCold__summary.md|Summary: 2026-08-04_09-31-44Z_LLM_DerivedPriorsforThompsonSamplinginCold_StartCo.md]] — 4 title terms overlap; 10 summary/topic terms overlap; semantic match 0.04

## Key Contributions  
- [The collective evidence‑threshold backdoor paradigm enables activation of malicious behavior only when aggregated peer signals cross a hidden threshold.]  
- [BCBI constructs counterfactual boundary pairs to separate benign from adversarial behavior and learns latent progression aligned with evidence.]  
- [LATTE provides a clean‑only test that detects anomalous agent updates early, limiting propagation without disrupting normal collaboration.]

## Methodology  
[The authors approach the problem by modeling communication dynamics as a threshold‑triggered event and using counterfactual boundary injection to define benign versus adversarial regions in latent space.]

## Results  
[Experiments on benchmark MAS tasks show BCBI activates only after sufficient evidence is collected, with negligible premature activation; LATTE reduces propagation of malicious updates by up to 85% while maintaining system performance.]

## Significance  
[This work mitigates a previously unaddressed class of backdoor attacks in collaborative AI systems, preserving trust and functionality while enabling robust defense against covert triggers.]

## Related Concepts  
- [Collective evidence‑threshold backdoor]  
- [Boundary‑Conditioned Backdoor Injection (BCBI)]  
- [LAtent Transition Test‑time Evaluation (LATTE)]  
- [Multi‑agent system (MAS)]
