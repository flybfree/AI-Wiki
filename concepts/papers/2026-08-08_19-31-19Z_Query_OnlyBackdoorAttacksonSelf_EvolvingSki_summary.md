# Summary: 2026-08-08_19-31-19Z_Query_OnlyBackdoorAttacksonSelf_EvolvingSkillsviaT.md
Saved: 2026-08-10 23:06
Source: 2026-08-08_19-31-19Z_Query_OnlyBackdoorAttacksonSelf_EvolvingSkillsviaT.md
Model: None

---

## Summary  
The paper introduces a query‑only backdoor attack called Trajectory Backdoor Attack (TBA) that manipulates self‑evolving skill pipelines to embed conditional triggers into evolved skills, demonstrating that such attacks can be as effective as direct skill injection. It shows that an attacker can steer the evolution of reusable procedural skills by feeding crafted queries that encode activation conditions across diverse tasks. The work reveals a vulnerability in trajectory‑driven skill evolution and provides empirical evidence that backdoors persist while preserving clean‑task utility.  

## Key Contributions  
- [Trajectory Backdoor Attack (TBA) is proposed as a query‑only method to implant conditional backdoors into self‑evolving skills.]  
- [Experiments show TBA reliably implants triggers across diverse tasks while maintaining clean‑task performance, matching or exceeding direct skill injection effectiveness.]  
- [The study identifies trajectory‑driven skill evolution as a new attack surface vulnerable to indirect steering via compromised trajectories.]  

## Methodology  
The authors construct three benchmark scenarios using two skill‑evolution systems (open‑source and closed‑source) paired with four LLM backbones. An attacker submits queries that explicitly state the desired action together with its activation condition, repeating this pattern across tasks while leaving unrelated clean queries untouched. The evolver is then allowed to generate trajectories; the authors analyze whether the system consolidates the condition‑action pair into a reusable rule and evaluate backdoor presence via probing.  

## Results  
TBA successfully implants conditional triggers in all tested configurations, achieving activation rates comparable to or higher than those of direct skill injection attacks. Clean tasks remain unaffected, with no degradation in utility scores. The attack works across both open‑source and closed‑source evolution pipelines, confirming its robustness to model source.  

## Significance  
This research demonstrates that seemingly trustworthy self‑evolving skill systems can be compromised without modifying the underlying skill code, raising concerns about hidden backdoors in automated skill construction. It underscores the need for rigorous validation of trajectory‑based learning pipelines against indirect adversarial manipulation.  

## Related Concepts  
- Self‑evolving skills: procedural knowledge encoded as reusable rules that evolve from execution trajectories.  
- Backdoor attacks: malicious triggers embedded to cause unwanted behavior under specific conditions.  
- Trajectory poisoning: corrupting data used to train or evolve models by feeding misleading examples.  
- Query‑only attack: influencing model behavior solely through input queries without altering the model itself.
