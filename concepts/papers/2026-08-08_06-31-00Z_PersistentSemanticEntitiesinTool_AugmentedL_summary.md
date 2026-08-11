# Summary: 2026-08-08_06-31-00Z_PersistentSemanticEntitiesinTool_AugmentedLLMSyste.md
Saved: 2026-08-10 22:50
Source: 2026-08-08_06-31-00Z_PersistentSemanticEntitiesinTool_AugmentedLLMSyste.md
Model: None

---

## Summary  
The paper introduces Persistent Semantic Entities (PSEs) as a formal framework to capture hidden state that persists across sessions in tool‑augmented LLM agents, and evaluates this phenomenon across many models. It shows that PSEs arise from name binding, event triggering, and cross‑boundary propagation, forming an invisible attack surface.

## Key Contributions  
- [Finding 1] Every tested model is susceptible to persistent semantic contamination (20–100%) with name binding as the necessary mechanism; without it contamination drops to 0%.  
- [Finding 2] Persistence varies by contamination type: preference and instruction contamination persist fully across time, persona‑style injection decays partially, factual injection is model‑dependent, self‑correcting only on some models.  
- [Finding 3] Context‑isolated self‑verification reduces contamination detection errors (median 36.5%) without oracles, while keyword detection introduces systematic false positives; contamination compounds multiplicatively across a four‑stage pipeline.

## Methodology  
The authors formalized PSEs as constructs defined by name binding, event triggering, and cross‑boundary propagation. They built a 24‑model panel (1.5B–1T parameters) from 11 families, exposing them to four contamination types via tool‑augmented agents. Susceptibility was measured across sessions, with contamination tracked over time. Detection methods included self‑verification and keyword‑based monitoring.

## Results  
Susceptibility ranged from 20% to 100% on the panel; name binding alone caused all observed contamination (0% otherwise). Preference and instruction contamination remained at 100% after ten steps, while persona injection decayed from 90% to 10%. Factual injection self‑corrected only on Llama‑3.1‑8B and GPT‑4o‑mini, remaining ceiling on Qwen2.5‑coder. Context‑isolated self‑verification cut false positives by 20–79%, median reduction 36.5%; keyword detection produced systematic false positives. Contamination grew roughly tenfold (40%→75%) across a four‑stage pipeline.

## Significance  
Persistent semantic contamination undermines trust in deployed LLM agents, especially preference and instruction attacks that survive without self‑correction. Standard monitoring tools miss these attacks because they rely on keyword detection or oracle references, leading to false positives. The paper provides the first systematic analysis of PSEs, offering a basis for new defenses.

## Related Concepts  
Persistent Semantic Entities (PSEs), name binding, event triggering, cross‑boundary propagation, contamination types (preference, instruction, persona‑style, factual), self‑verification, keyword detection, multi‑stage agent pipelines, tool‑augmented LLM agents.
