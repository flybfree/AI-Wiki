# Summary: 2026-08-04_19-40-30Z_Test_thenRoute_HowLanguageModelsExecuteIn_ContextC.md
Saved: 2026-08-05 22:21
Source: 2026-08-04_19-40-30Z_Test_thenRoute_HowLanguageModelsExecuteIn_ContextC.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) implement in‑context conditional rules such as “if P(x) then A else B” across different model families and languages, asking whether the rule is executed by a global routing module or by local token‑level mechanisms. Using activation patching on four‑donor designs that make the condition and answer word disagree, the authors probe which layers carry each component of the rule. Their contribution is empirical evidence that rule execution is highly localized to mid‑stack residual bands (the “test” part) while the routing of A/B occurs in a token‑bound, non‑transferable subspace (the “route” part). The findings demonstrate modularity: the condition can be flipped independently and reroutes answers with near‑perfect fidelity, whereas the response mapping is fragile across new rule pairs.  

## Key Contributions  
- [Finding 1] Activation patching reveals that the predicate’s truth value resides in a mid‑stack residual band; flipping the condition reroutes the answer with predicate‑outcome flip near 1.0 and mapping flip near 0.0, satisfying an isolation criterion in 17 of 18 cells across five predicate families.  
- [Finding 2] The router direction is token‑bound and non‑transferable: a learned subspace flips A and B almost perfectly within the trained pair but transfers to new pairs at ≈ 0, except that Gemma‑3‑4B shows transfer ≈ 0.98 to the same pair in other languages.  
- [Finding 3] The “test” (condition) is modular; under these probes the “route” (response mapping) is not, indicating that rule execution is not a single abstract module but rather separate token‑level processes.  

## Methodology  
The authors employ activation patching on four‑donor designs where two donors encode the conditional predicate and the other two encode the answer word. By swapping these donors so they disagree, each layer reveals whether it carries the condition or the answer. They probe three open models from two families (Qwen and Gemma) across six languages that share a fixed item bank, thereby testing cross‑lingual generalization of rule execution.  

## Results  
Mid‑stack residual bands carry the predicate’s truth value; patching it causes near‑perfect rerouting (predicate flip ≈ 1.0, mapping flip ≈ 0.0) and meets isolation in 17/18 cells across five predicate families. The router shows an opposite profile: a learned subspace flips A/B with high fidelity within the trained pair but transfers to new pairs at ≈ 0; Gemma‑3‑4B achieves near‑perfect transfer (≈ 0.98) to the same pair in other languages. Crucially, the router direction is token‑bound and non‑transferable—answer readout in Gemma, pair‑specific in Qwen—confirming that rule execution is modular: test is independent of route.  

## Significance  
These results show that LLMs do not rely on abstract global routing modules to implement conditional rules; instead, they decompose the task into local token‑level computations for testing and response generation. This insight advances AI interpretability, informs design of more robust in‑context learning mechanisms, and suggests pathways for cross‑model and cross‑language consistency.  

## Related Concepts  
- In‑context learning  
- Activation patching  
- Residual networks (mid‑stack bands)  
- Conditional reasoning  
- Language model routing  
- Token‑bound computation  
- Cross‑lingual transfer
