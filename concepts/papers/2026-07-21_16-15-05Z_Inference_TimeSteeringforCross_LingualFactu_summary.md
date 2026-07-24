# Summary: 2026-07-21_16-15-05Z_Inference_TimeSteeringforCross_LingualFactualConsi.md
Saved: 2026-07-24 01:00
Source: 2026-07-21_16-15-05Z_Inference_TimeSteeringforCross_LingualFactualConsi.md
Model: None

---

## Summary  
The paper investigates why Large Language Models (LLMs) exhibit cross‑lingual factual inconsistency, where answers shift depending on the prompt language despite identical underlying knowledge. It proposes to address this bias at inference time by forcing an English‑prompted model to answer as if it were queried in target languages such as German, Spanish and Bulgarian. The authors evaluate four intervention strategies—zero‑shot contextual steering (persona prompting), internal representation manipulation via Contrastive Activation Addition (CAA), lightweight weight modification through Direct Preference Optimization (DPO) trained on factual data, and a conceptual generalization benchmark—to determine which can reliably enforce consistent answers across languages.

## Key Contributions  
- [Finding 1] Cross‑lingual factual inconsistency is at least partly a selection problem that can be mitigated by inference‑time steering rather than retraining the model.  
- [Finding 2] Persona prompting (zero‑shot contextual steering) provides the strongest overall balance of efficacy, safety and out‑of‑domain generalization among the evaluated interventions.  
- [Finding 3] While Contrastive Activation Addition yields sharp improvements on factual consistency benchmarks, it is configuration‑sensitive and can cause knowledge degradation; DPO adapters deliver permanent but narrower gains that are less transferable.

## Methodology  
The authors investigate whether biases in LLMs’ internal representations can be corrected during inference. They force an English‑prompted model to produce answers as if the query were originally in target languages, thereby testing how different steering techniques influence answer distributions. Four interventions are compared: (1) persona prompting, which injects a contextual persona into the prompt; (2) Contrastive Activation Addition (CAA), which adds contrastive activations to reshape internal representations; (3) Direct Preference Optimization (DPO) adapters trained on benchmark‑derived factual data and conceptual generalization data; and (4) a novel generalization benchmark that includes culturally rooted queries to evaluate transferability. Experiments are conducted on the Gemma 3 12B Instruct model.

## Results  
Across all four interventions, persona prompting achieved the highest F1 score for factual consistency across German, Spanish and Bulgarian prompts while maintaining safety and generalizing well to unseen cultural contexts. CAA produced the largest drop in inconsistency metrics but required careful hyper‑parameter tuning; poor configuration led to a measurable knowledge loss. DPO adapters offered stable improvements that persisted after prompt changes but were limited to the specific factual data used for training, showing weaker cross‑lingual transfer. The generalization benchmark confirmed that persona prompting’s gains extended beyond the original dataset, indicating robust alignment.

## Significance  
These findings demonstrate that cross‑lingual inconsistency is not solely a model‑training issue but can be partially resolved by simple inference‑time steering. Persona prompting proves effective for achieving consistent, safe answers across languages without invasive architectural changes, suggesting it as a practical solution for deploying multilingual LLMs in real‑world settings.

## Related Concepts  
inference‑time steering, persona prompting, Contrastive Activation Addition (CAA), Direct Preference Optimization (DPO), factual consistency, multilingual bias, knowledge degradation, generalization benchmark.
