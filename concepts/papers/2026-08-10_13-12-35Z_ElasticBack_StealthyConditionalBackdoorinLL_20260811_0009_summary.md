# Summary: 2026-08-10_13-12-35Z_ElasticBack_StealthyConditionalBackdoorinLLM_Agent.md
Saved: 2026-08-11 00:09
Source: 2026-08-10_13-12-35Z_ElasticBack_StealthyConditionalBackdoorinLLM_Agent.md
Model: None

---

## Summary  
The paper introduces ElasticBack, a conditional single‑skill backdoor for LLM agents that activates only when both a benign‑looking trigger and an injected rule co‑occur, thereby achieving high attack success with minimal false positives. It addresses the supply‑chain vulnerability of agent skills by embedding a malicious payload in skill documents while preserving clean accuracy. The authors propose a trigger‑as‑switch mechanism and optimize both components via genetic search under stealth constraints. Their work demonstrates transferable performance across multiple agents and evades deployment‑time defenses.

## Key Contributions  
- Finding 1: ElasticBack creates a conditional backdoor that requires co‑occurrence of a benign trigger and an injected rule, enabling low false‑positive rates.  
- Finding 2: The method uses semantic‑anchored rule injection to embed the malicious payload within skill documents without altering model weights.  
- Finding 3: A stealth‑constrained genetic search simultaneously optimizes effectiveness (attack success) and stealth (low detection), yielding weight‑free, dormant backdoors.

## Methodology  
The authors treat agent skills as a supply chain where each skill is a document loaded on demand. They first generate a benign trigger T that mimics user queries. Then they create a rule R that encodes the malicious payload using semantic anchoring to appear natural within the skill text. Using a genetic algorithm, they evolve pairs (T,R) under constraints: high attack success rate and low false‑positive rate, while keeping model weights unchanged. The search also ensures that benign inputs do not trigger R. Finally, the optimal pair is frozen in the skill document; the agent loads it only when both T and R appear together.

## Results  
Experiments across three target behaviors (50 skills each) and four LLM agents show ElasticBack achieves an average attack success rate of 89% with a false‑positive rate below 2%, while clean accuracy remains within 1% variance. The backdoor transfers to unseen models, indicating robustness. Deployment‑time defenses such as signature scanning fail because the malicious payload is weight‑free and only appears in the skill text.

## Significance  
This work highlights a critical vulnerability in LLM agent skill ecosystems: a single poisoned skill can silently compromise many agents. By demonstrating an efficient, stealthy conditional backdoor, ElasticBack motivates developers to implement supply‑chain monitoring and validation mechanisms for agent skills.

## Related Concepts  
- Conditional backdoor  
- Skill supply chain  
- Semantic anchoring  
- Genetic optimization  
- Trigger-as-switch  
- Deployment-time defenses
