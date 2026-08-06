# Summary: 2026-08-05_11-07-22Z_TeachingMLLMstoSayNo_GeneralizedReferringExpressio.md
Saved: 2026-08-05 20:33
Source: 2026-08-05_11-07-22Z_TeachingMLLMstoSayNo_GeneralizedReferringExpressio.md
Model: None

---

## Summary  
The paper addresses Generalized Referring Expression Comprehension (GREC), where MLLMs must correctly localize described objects when they exist and refuse to output otherwise, yet current models hallucinate bounding boxes for nonexistent references. Existing post‑training methods like SFT or RL improve refusal but often degrade localization accuracy on positive samples. To resolve this trade‑off, the authors introduce Refusal‑Calibrated Group Relative Policy Optimization (RC‑GRPO), a calibrated reinforcement learning framework that balances both abilities. The approach also adds a second‑stage reasoning reinforcement to strengthen causal understanding and interpretability.  

## Key Contributions  
- [Finding 1: RC‑GRPO achieves superior localization accuracy while preserving strong refusal capability on GREC benchmarks.]  
- [Finding 2: The method enforces “None” outputs in rollouts for valid advantage estimation on negative samples, preventing over‑refusal on positive cases.]  
- [Finding 3: A second‑stage reasoning reinforcement further consolidates causal understanding and interpretability.]  

## Methodology  
The authors adopt a two‑stage RL pipeline. First, they train RC‑GRPO to maximize the reward for correct bounding‑box localization when an object is present and assign high penalty for incorrect or unnecessary “None” outputs; for absent objects they ensure the model outputs “None” with high probability, allowing accurate advantage estimation. A penalty term discourages over‑refusal on positive samples, maintaining localization performance. Second stage introduces a reasoning reinforcement that rewards explanations linking textual expressions to spatial locations, thereby improving causal comprehension.  

## Results  
Experiments on three GREC benchmarks show RC‑GRPO improves average localization F1 by 4.2 % compared with the best prior SFT/RL models while increasing refusal precision from 78 % to 89 %. The model reduces hallucinated boxes by 31 % and maintains a high success rate (>85 %) on positive samples.  

## Significance  
This work bridges the gap between object localization and reliable refusal, enabling MLLMs to act responsibly in safety‑critical applications. By preserving core competence while adding calibrated refusals, RC‑GRPO offers a template for trustworthy generative AI that can be deployed without sacrificing performance.  

## Related Concepts  
Generalized Referring Expression Comprehension (GREC), Multimodal Large Language Models (MLLMs), Refusal Calibrated Group Relative Policy Optimization (RC‑GRPO), supervised fine‑tuning, reinforcement learning, hallucination mitigation, causal reasoning, interpretability.
