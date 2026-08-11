# Summary: 2026-08-10_13-12-35Z_ElasticBack_StealthyConditionalBackdoorinLLM_Agent.md
Saved: 2026-08-10 23:49
Source: 2026-08-10_13-12-35Z_ElasticBack_StealthyConditionalBackdoorinLLM_Agent.md
Model: None

---

## Summary  
The paper introduces ElasticBack, a conditional single‑skill backdoor for LLM agents that activates only when a benign‑looking trigger co‑occurs with an embedded malicious rule, achieving high attack success while preserving clean accuracy and avoiding false positives. Existing attacks are either always‑on or require fine‑tuned weights, so ElasticBack offers a lightweight, weight‑free solution that can be stealthily deployed within skill documents. The authors propose a coupled trigger‑rule optimization framework to embed the payload without altering model parameters.

## Key Contributions  
- **Conditional activation**: ElasticBack creates a backdoor that fires only when both a benign trigger and a hidden rule are present, eliminating false positives.  
- **Trigger‑as‑switch construction**: It uses semantic‑anchored rule injection to embed the malicious payload within skill documents without modifying model weights.  
- **Stealth‑constrained genetic search**: The method jointly optimizes effectiveness and stealth across multiple skill sets using a genetic algorithm constrained by low false‑positive rates.

## Methodology  
The authors treat each LLM agent skill as a document containing instructions and resources. They generate a benign trigger T that appears naturally in user queries, then embed a rule R that encodes the malicious payload. The rule is frozen while T evolves via a genetic search under constraints to maintain low false‑positive rates. Optimization balances attack success across three target behaviors per four LLMs.

## Results  
Experiments on 50 skills each for four agent LLMs show ElasticBack achieves >95 % attack success with <2 % false positives, clean accuracy remains unchanged, and the backdoor transfers seamlessly between models. Deployment‑time defenses are evaded because the payload is weight‑free and dormant.

## Significance  
This work highlights a critical vulnerability in the LLM skill supply chain: a single poisoned skill can silently compromise agents without detection. By decoupling trigger and rule, ElasticBack demonstrates that conditional backdoors can be both effective and stealthy, urging researchers to develop defenses for skill‑based attacks.

## Related Concepts  
- Conditional backdoor  
- Skill supply chain  
- Rule injection  
- Genetic search optimization  
- Trigger‑as‑switch
