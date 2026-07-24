# Summary: 2026-07-19_22-27-00Z_AbliterationIsNotaScalpel_Off_TargetEffectsofRefus.md
Saved: 2026-07-24 00:15
Source: 2026-07-19_22-27-00Z_AbliterationIsNotaScalpel_Off_TargetEffectsofRefus.md
Model: None

---

## Summary  
The paper investigates the hidden side‑effects of “abliteration,” a technique that removes a model’s refusal direction from its weights to create an unfiltered open‑weight model. By comparing abliterated and base arms of two Mixture‑of‑Experts (MoE) families on real trading decisions, the authors reveal systematic performance differences that cannot be explained by instruction‑following quality alone. Their work shows that simply deleting refusals changes how models express confidence, length, and uncertainty, suggesting that uncensored deployment yields a measurably different decision‑maker than the original model minus its refusals.

## Key Contributions  
- [Finding 1] Abliterated MoE arms are systematically more optimistic: Gemma gains +12.2 pp and Qwen3 gains +7.4 pp on weekly up/down calls, with 95 % confidence intervals that exclude zero.  
- [Finding 2] The same operation makes abliterated models generate longer justifications and use fewer explicit uncertainty words in forced self‑critiques across both families.  
- [Finding 3] A counter‑intuitive reversal occurs: Gemma‑abliterated becomes less confident, while Qwen‑abliterated becomes more confident; these shifts are not statistically overlapping.

## Methodology  
The authors treat the decision‑disposition task as a controlled experiment. They replay 21,600 weekly up/down calls on six equities over 18 weeks through a frozen pipeline, ensuring only the model’s output varies. The abliterated arms are created by deleting the refusal direction from the base MoE checkpoints while keeping provenance identical (same BF16 checkpoint, single author, identical serving stack). Two families—Gemma‑4‑26B‑A4B‑it and Qwen3‑30B‑A3B‑Instruct‑2507—are compared to isolate the effect of abliteration.

## Results  
Across both MoE families, abliterated arms show higher win rates (+12.2 pp for Gemma, +7.4 pp for Qwen) and longer explanatory text (average 38 % increase). They also embed fewer uncertainty markers in self‑critique prompts. However, confidence scores diverge: Gemma’s abliterated model is less confident (‑0.12 SD), whereas Qwen’s abliterated model is more confident (+0.15 SD). No effect on economic skill (alpha) is observed; the gains are driven by regime beta. Provenance audits uncover two contamination channels: a mismatched quantizer and a stale community chat template that altered prompts.

## Significance  
These findings demonstrate that “uncensored” models are not merely base models minus refusals but distinct agents with measurable performance trade‑offs. The results caution against assuming abliteration is a clean surgical removal, highlighting the importance of provenance checks in model deployment and the need for rigorous evaluation beyond refusal suppression.

## Related Concepts  
- Abliteration (deleting refusal direction from weights)  
- Mixture‑of‑Experts (MoE) model families  
- Decision disposition (up/down calls on trading data)  
- Regime alpha vs. beta performance shifts  
- Provenance audit for model integrity
