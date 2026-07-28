# Summary: 2026-07-27_12-18-59Z_SimulatingTenantResponsestoEnergyPolicyInterventio.md
Saved: 2026-07-27 22:56
Source: 2026-07-27_12-18-59Z_SimulatingTenantResponsestoEnergyPolicyInterventio.md
Model: None

---

## Summary  
The paper proposes a friction‑aware persona modeling approach for LLMs to simulate tenant responses to energy policy interventions, focusing on perceived transaction costs. By integrating PTC into persona design, the authors aim to bridge institutional theory with interpretable LLM simulations. Using survey data from the Netherlands and multiple LLMs, they compare prompt‑only versus fine‑tuned settings across GPT‑3.5‑turbo, Ministral‑8B‑Instruct, and Llama‑3.1‑8B‑Instruct. The study demonstrates that PTC‑based personas improve simulation accuracy.

## Key Contributions  
- Finding 1: Incorporating perceived transaction cost (PTC) into persona design yields consistent improvements in LLM performance for policy simulations.  
- Finding 2: Fine‑tuning LLMs with PTC‑aware prompts outperforms prompt‑only prompting across GPT‑3.5‑turbo, Ministral‑8B‑Instruct, and Llama‑3.1‑8B‑Instruct.  
- Finding 3: Supervised fine‑tuning (SFT) and Group Relative Policy Optimization (GRPO) on open‑weight models achieve higher fidelity than prompt‑only approaches.

## Methodology  
The authors collected 40,548 QA pairs from a Dutch survey of 1,068 citizens about energy‑efficient renovation. They defined PTC dimensions: information burden, administrative effort, coordination demands, and uncertainty. Personas were constructed by combining demographic attributes with these cost perceptions. The experimental setup used three LLMs in two configurations: (i) prompt‑only prompting with persona text, and (ii) supervised fine‑tuning or GRPO on open‑weight models using the same personas as training data.

## Results  
Across all models, PTC‑enhanced prompts increased accuracy by an average of 12.4 % relative to baseline prompts. Fine‑tuned models showed up to 23 % higher alignment with survey responses compared to prompt‑only setups. SFT and GRPO both outperformed prompt‑only, with GRPO achieving the best trade‑off between performance and interpretability.

## Significance  
By linking institutional transaction‑cost theory to LLM behavior, this work provides a scalable framework for transparent policy simulation. It offers practitioners a method to embed real‑world frictions into AI models, improving decision‑making support without sacrificing model efficiency.

## Related Concepts  
- Perceived Transaction Cost (PTC)  
- Large language model (LLM) prompting vs fine‑tuning  
- Supervised Fine‑Tuning (SFT)  
- Group Relative Policy Optimization (GRPO)  
- Energy‑efficient renovation (EER)  
- Persona modeling in AI
