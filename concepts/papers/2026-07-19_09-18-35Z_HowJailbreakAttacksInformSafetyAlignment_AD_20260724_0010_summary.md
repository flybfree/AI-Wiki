# Summary: 2026-07-19_09-18-35Z_HowJailbreakAttacksInformSafetyAlignment_ADefender.md
Saved: 2026-07-24 00:10
Source: 2026-07-19_09-18-35Z_HowJailbreakAttacksInformSafetyAlignment_ADefender.md
Model: None

---

## Summary  
The paper proposes a defender‑centric evaluation framework for jailbreak attacks on large language models, arguing that an attack’s utility should be measured by the safety improvements it enables when used as red‑team data rather than solely by its success rate. It introduces A‑MESS, a set‑agnostic method to attribute and select attacks using black‑box subset observations. The framework leverages Shapley values to estimate marginal utility of each attack and selects compact subsets under user budgets via greedy or surrogate optimization. By comparing attacker‑centric metrics with defender‑centric outcomes, the authors demonstrate that safety alignment is better captured by the latter perspective.  

## Key Contributions  
- ASR rankings weakly align with defender‑centric utility, indicating that high success rates do not guarantee meaningful safety gains.  
- AttackSHAP can be estimated accurately with limited utility queries, making it feasible for practical deployment.  
- Directly optimizing subsets of attacks yields stronger safety utility than attacker‑centric or attribution‑only selection.  

## Methodology  
The authors approached the problem by treating each jailbreak attack as a resource whose marginal contribution to downstream safety is unknown. A‑MESS collects binary observations indicating whether a subset of attacks improves safety, then applies Shapley analysis to compute AttackSHAP scores that quantify each attack’s impact. The framework supports greedy or surrogate‑based optimization to pick the most effective subset within a budget, operating without explicit model access.  

## Results  
Across controlled utility landscapes and real LLM safety settings, the study found that ASR rankings correlate poorly with defender‑centric metrics, confirming misalignment between attacker and defender perspectives. AttackSHAP estimates remained stable even when only a few utility queries were provided, demonstrating robustness to sparse data. Subset selection performed via greedy optimization consistently improved safety improvement scores compared to selecting attacks based solely on ASR or attribution alone.  

## Significance  
This work shifts the focus of jailbreak evaluation from merely measuring model vulnerability to assessing how attacks can be leveraged for safety enhancement. By providing an efficient, attribute‑based method (AttackSHAP) and a selection strategy that maximizes real safety gains, A‑MESS offers a practical tool for red‑teamers and developers aiming to improve LLM robustness.  

## Related Concepts  
Jailbreak attacks, defender‑centric evaluation, Shapley values, marginal utility, black‑box subset observations, AttackSHAP, A‑MESS framework, greedy optimization, red‑teaming data, safety alignment.
