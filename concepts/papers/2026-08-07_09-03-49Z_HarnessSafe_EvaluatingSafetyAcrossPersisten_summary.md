# Summary: 2026-08-07_09-03-49Z_HarnessSafe_EvaluatingSafetyAcrossPersistentCarrie.md
Saved: 2026-08-09 20:15
Source: 2026-08-07_09-03-49Z_HarnessSafe_EvaluatingSafetyAcrossPersistentCarrie.md
Model: None

---

## Summary  
HarnessSafe is a benchmark designed to evaluate safety across persistent carriers in agent harnesses by tracing attacker influence through the Persistent‑Risk Lifecycle. It provides end‑to‑end attack‑success rates that reveal how risks propagate beyond individual carrier boundaries. The work introduces a multi‑stage trace‑based evaluation framework for seven carrier families.

## Key Contributions  
- HarnessSafe defines a comprehensive benchmark of 328 executable cases across seven persistent‑carrier families, enabling systematic study of safety propagation.  
- It introduces a multi‑stage, trace‑based evaluation that measures how far attack chains progress and where containment occurs within the lifecycle.  
- Findings reveal that containment is carrier‑specific and heavily influenced by harness‑model configuration, showing that attack success rates cannot capture distinct lifecycle progression patterns.

## Methodology  
The authors constructed executable cases representing Persistent‑Risk Lifecycle: attacker entry → persistence across carriers → system boundary crossing → benign trigger → violation. They evaluate these cases on mainstream agent harnesses using trace‑based metrics to quantify containment depth and failure points, distinguishing between carrier‑specific behaviors and overall success rates.

## Results  
Experiments show that while some carriers (e.g., memory) provide strong containment, others allow attacker influence to persist across system boundaries. The harness model backend significantly shapes outcomes: different configurations lead to varying degrees of risk propagation. Attack success rates remain high despite partial containment, indicating that traditional metrics are insufficient for lifecycle analysis.

## Significance  
This work highlights the need for granular safety evaluation beyond aggregate attack success rates, especially in complex agent ecosystems where persistent carriers enable delayed attacks. HarnessSafe provides a reusable framework for assessing how different harnesses and models handle risk propagation across carriers.

## Related Concepts  
Persistent carriers (memory, skills, tools, shared artifacts), agent harnesses, Persistent‑Risk Lifecycle, trace‑based evaluation, containment, attack success rates, system boundaries.
