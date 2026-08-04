# Summary: 2026-08-03_10-44-04Z_CompanionBench_ATheory_Anchored_Real_World_Grounde.md
Saved: 2026-08-03 23:52
Source: 2026-08-03_10-44-04Z_CompanionBench_ATheory_Anchored_Real_World_Grounde.md
Model: None

---

## Summary  
CompanionBench is a theory‑anchored, real‑world grounded benchmark for evaluating AI emotional companionship that addresses the shortcomings of existing benchmarks by using de‑identified human interaction data and an interactive bilingual interface. It introduces ten capabilities derived from 25 psychological and counseling theories, four of which are novel to prior work, and evaluates agents on both a subjective rubric and a deterministic measure of disclosure depth. The benchmark mitigates common biases such as same‑family favoritism through a cross‑family panel and employs an Item Response Theory model to separate agent quality from judge severity. Rankings across Chinese and English versions show high reproducibility (ρ = 0.996, 0.953).  

## Key Contributions  
- [Finding 1] CompanionBench is the first companion benchmark that grounds both its scenarios and a trained user simulator in de‑identified real‑world data, providing authenticity beyond hand‑crafted prompts.  
- [Finding 2] It operationalizes ten capabilities from 25 theories, adding four new ones (holding ambiguity, selfobject responsiveness, positive resonance, calibrated challenge) that were not explicitly graded before.  
- [Finding 3] The benchmark reveals capability‑level differences obscured by aggregate scores and identifies emotion regulation and calibrated challenge as common weaknesses, while role‑play agents rank near the bottom due to superficial immersion.  

## Methodology  
The authors built an interactive bilingual companion system where each persona’s trajectory is controlled by a hidden disclosure gate that branches based on the agent’s behavior, creating an unscripted interaction state space. Ten capabilities derived from theory are measured using a subjective ten‑capability rubric and a deterministic metric of whether deeper disclosure was earned. A cross‑family panel of judges reduces same‑family favoritism bias, while an Item Response Theory model separates agent quality from judge severity. The evaluation code and 500 Chinese‑English parallel pairs will be released publicly.  

## Results  
Rankings are highly reproducible across languages (ρ = 0.996 for ZH, 0.953 for EN). Evaluation of 28 agents shows that emotion regulation and calibrated challenge consistently underperform; holding ambiguity is the strongest discriminating capability. Role‑play agents rank near the bottom, indicating that immersion does not guarantee relational competence. The dominant failure mode across agents is substituting surface warmth with substantive relational support.  

## Significance  
CompanionBench provides a rigorous, bias‑aware evaluation framework for AI emotional companionship, enabling developers to design agents that meet psychological theory and real‑world user needs rather than relying on superficial aggregate scores. By grounding scenarios in authentic data and separating capability measurement from judge variability, it advances both research methodology and practical deployment of companion systems.  

## Related Concepts  
Theory‑anchored benchmarking, real‑world grounded data, hidden disclosure gate, capability rubric, Item Response Theory, same‑family favoritism bias, emotion regulation, calibrated challenge, holding ambiguity, role‑play immersion.
