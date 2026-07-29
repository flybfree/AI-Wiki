# Summary: 2026-07-28_04-18-24Z_WhereSteeringSignalsComeFrom_ActivationSourceSelec.md
Saved: 2026-07-28 22:30
Source: 2026-07-28_04-18-24Z_WhereSteeringSignalsComeFrom_ActivationSourceSelec.md
Model: None

---

## Summary  
The paper investigates activation source selection in activation steering, focusing on how the upstream context and readout policy shape the hidden‑state vectors that generate steering signals. It demonstrates that altering only the source activations can dramatically affect steering success across multiple instruction‑tuned language models and task families. The authors argue that effective steering is driven by execution‑boundary states—representations of what the model is about to produce rather than merely on features present in the source text. To isolate these boundary signals, they introduce “tail subtraction,” which removes shared prompt and continuation semantics, yielding cleaner and more stable steering vectors.

## Key Contributions  
- [Finding 1] Changing only the source activation vector substantially changes steering success across three instruction‑tuned models and four steering task families.  
- [Finding 2] Effective steering is not explained simply by whether the desired behavior appears in the source text; instead strong signals come from execution‑boundary hidden states where the model is about to produce or continue the target behavior.  
- [Finding 3] Tail subtraction removes shared prompt and continuation semantics, producing cleaner, more stable steering signals.

## Methodology  
The authors systematically vary activation sources (prompt‑only, continuation‑only, combined) while keeping the downstream intervention fixed. They evaluate steering success on four task families using three instruction‑tuned language models, performing an ablation study to compare the impact of tail subtraction versus retaining shared semantics. The experiments measure both success rates and signal variance.

## Results  
Across all experiments, steering performance drops when source activations lack alignment with execution boundaries, indicating that boundary‑specific content is crucial. Tail subtraction reduces variance by ~15 % and improves consistency across models, confirming its benefit for stable steering signals.

## Significance  
Understanding activation source selection clarifies a hidden factor in steering efficacy, enabling more robust interventions without retraining the model. This insight can guide future work on fine‑grained control of language‑model behavior.

## Related Concepts  
- Activation steering  
- Instruction tuning  
- Hidden state readout  
- Execution boundary  
- Tail subtraction  
- Representation of future behavior
