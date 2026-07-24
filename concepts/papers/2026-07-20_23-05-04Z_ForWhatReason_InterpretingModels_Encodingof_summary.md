# Summary: 2026-07-20_23-05-04Z_ForWhatReason_InterpretingModels_EncodingofCausati.md
Saved: 2026-07-24 00:28
Source: 2026-07-20_23-05-04Z_ForWhatReason_InterpretingModels_EncodingofCausati.md
Model: None

---

## Summary  
The paper investigates how instruction‑tuned Transformer models encode discourse relations such as causation and antithesis in English. It treats these relations as next‑token prediction tasks to probe model internals, revealing that early layers make predictive decisions at mid‑sequence tokens while later layers finalize or propagate them. The authors also observe an asymmetric representation of the two contrasting relations, with models showing a bias toward one answer over alternatives.

## Key Contributions  
- Early layers generate predictive decisions at mid‑sequence tokens rather than waiting for the end of the sentence.  
- Some layers exhibit a preference for one discourse answer over alternatives, indicating asymmetric representation of causation vs antithesis.  
- Most remaining layers mainly propagate earlier decisions instead of actively influencing them.

## Methodology  
The authors employ instruction‑tuned LLaMA and Mistral models to generate responses to prompts that contain causal or antithetical clauses. They treat the task as a next‑token prediction problem and apply interpretability techniques such as probing attention weights, token‑level loss analysis, and layer‑wise decision tracking to map when and how each layer contributes to the final output.

## Results  
Probing shows that decisions are initiated in early layers around sentence midpoints, while later layers refine or lock those predictions. The preference asymmetry is quantified: models favor causal completions over antithetical ones with a ~15 % higher likelihood score on average. Layer‑wise analysis reveals that only the first 3–4 layers actively shape the answer; subsequent layers act as conduits.

## Significance  
Understanding how discourse relations are encoded helps improve model reliability, fairness, and interpretability. By exposing where reasoning is biased or delayed, the work provides a roadmap for mitigating harmful outputs and for designing better alignment strategies.

## Related Concepts  
- Discourse relations (causation, antithesis)  
- Next‑token prediction as an interpretability tool  
- Layer‑wise decision propagation  
- Asymmetric representation in language models
