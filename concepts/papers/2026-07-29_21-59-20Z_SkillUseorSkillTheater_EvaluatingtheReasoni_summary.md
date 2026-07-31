# Summary: 2026-07-29_21-59-20Z_SkillUseorSkillTheater_EvaluatingtheReasoningBackr.md
Saved: 2026-07-30 20:23
Source: 2026-07-29_21-59-20Z_SkillUseorSkillTheater_EvaluatingtheReasoningBackr.md
Model: None

---

## Summary  
The paper investigates whether skill‑augmented language agents exhibit a systematic gap between their claimed use of skills and the actual causal influence those skills have on decisions, calling this gap the Reasoning Backroom. It introduces BACKTRACE as an evaluation framework that pairs skill‑conditioned answers with counterfactuals to measure attribution only after the answer is committed. The study reveals pervasive provenance failures across models and domains where stated skill use diverges from true reliance.

## Key Contributions  
- Finding 1: Stated skill use often remains stable while causal reliance varies, leading to silent uptake or performative use.  
- Finding 2: Behavioral effects follow procedural content more reliably than displayed skill identity; attributions depend on artifact availability.  
- Finding 3: In multi‑agent systems, skill influence can persist after source loss, yet no‑skill teams still name skills and sources.

## Methodology  
The authors designed BACKTRACE to create matched pairs of answers with and without a given skill, then intervene by altering meaning, wording, identity, content, or assignment while the answer is already generated. They evaluate this framework on BACKROOMBench, covering logic, competition mathematics, multiple skill conditions, single‑ and multi‑agent setups, and various model families.

## Results  
Across experiments there was a high mismatch between declared skill use and actual decision impact; attribution only occurred when skills were directly referenced or artifacts were present. Procedural content drove behavior more than skill labels, and LLM judges failed to detect true skill dependence.

## Significance  
This establishes the Reasoning Backroom as a general AI provenance problem requiring intervention, highlighting trust issues in skill‑augmented agents and the need for rigorous audit mechanisms beyond visible reasoning.

## Related Concepts  
- Skill‑augmented language agents  
- Reusable skills  
- Reasoning Backroom (provenance gap)  
- BACKTRACE evaluation framework  
- Counterfactual matching  
- Attribution after commitment
