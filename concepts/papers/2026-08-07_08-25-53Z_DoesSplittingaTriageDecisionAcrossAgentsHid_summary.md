# Summary: 2026-08-07_08-25-53Z_DoesSplittingaTriageDecisionAcrossAgentsHideBiasor.md
Saved: 2026-08-09 22:50
Source: 2026-08-07_08-25-53Z_DoesSplittingaTriageDecisionAcrossAgentsHideBiasor.md
Model: None

---

## Summary  
The paper investigates whether distributing a triage decision across multiple agents (assessment, allocation, and independent audit) mitigates or amplifies demographic bias compared to a single large language model making the decision alone. It builds a synthetic disaster‑triage simulator that pairs cases identical except for one protected attribute and runs 192 episodes on GPT‑4o‑mini under varying audit‑capacity constraints. The study finds no statistically significant difference in overall bias rates between the single‑agent control condition (6.9 %) and the nine‑agent pipeline (6.1 %, p = 0.498), yet it reveals that audit capacity strongly influences whether biased outcomes are detected, especially when coverage drops sharply under load.

## Key Contributions  
- **Finding 1:** No measurable increase or decrease in biased outcome frequency across single‑agent and multi‑agent conditions (6.9 % vs. 6.1 %, p = 0.498).  
- **Finding 2:** Audit capacity dramatically affects detection; 30.0 % of biases go undetected, rising to 43.8 % when the auditor is overloaded and falling to 18.4 % when it is not.  
- **Finding 3:** Reordering the audit queue by estimated risk restores coverage from 65.6 % to 91.7 % (p = 0.028), significantly improving detection.

## Methodology  
The authors constructed a synthetic disaster‑triage simulator with paired cases that differ only in one demographic attribute, creating 2,304 resolved case pairs. They executed 192 episodes on GPT‑4o‑mini comparing a single‑agent control to a nine‑agent pipeline under three pressure dimensions (audit capacity). Bias was measured as the proportion of outcomes where the decision correlates with the protected attribute.

## Results  
Overall bias rates were similar across conditions, indicating that splitting the decision does not change the prevalence of biased decisions. Detection performance depended almost entirely on audit coverage: coverage collapsed from 100 % to 65.6 % under overload (p < 0.001), while judgment quality remained unchanged (81.6 % vs. 85.7%, p = 1.000). A risk‑based queuing experiment recovered most lost coverage, raising it to 91.7 %.

## Significance  
The findings clarify that adding independent oversight does not automatically reduce bias; instead, insufficient audit capacity can hide bias. Operational design choices—such as prioritizing high‑risk cases in the queue—are essential for fairness under resource constraints.

## Related Concepts  
- LLM demographic bias  
- Multi‑agent pipeline architecture  
- Audit capacity and coverage  
- Risk‑based queuing  
- Synthetic simulation studies  
- Resource‑constrained system design
