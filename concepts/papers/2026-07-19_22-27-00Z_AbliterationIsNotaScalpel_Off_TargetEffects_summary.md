# Summary: 2026-07-19_22-27-00Z_AbliterationIsNotaScalpel_Off_TargetEffectsofRefus.md
Saved: 2026-07-24 00:12
Source: 2026-07-19_22-27-00Z_AbliterationIsNotaScalpel_Off_TargetEffectsofRefus.md
Model: None

---

## Summary  
The paper investigates the off‑target consequences of abliterating model refusals in open‑weight AI systems. By removing a model’s refusal direction from its weights while keeping all other provenance constant, the authors compare decision outcomes across two Mixture‑of‑Experts families. The study finds systematic shifts in optimism, confidence, and language use that are unrelated to capability degradation. This work demonstrates that “uncensored” models behave differently than the base model minus refusals.  

## Key Contributions  
- [Finding 1] Abliterated models across both Gemma‑4‑26B‑A4B‑it and Qwen3‑30B‑A3B‑Instruct‑2507 are systematically more optimistic, justifying their decisions at greater length.  
- [Finding 2] The same surgery makes Gemma‑abliterated models less confident while Qwen‑abliterated models become more confident, with non‑overlapping confidence intervals.  
- [Finding 3] No economic skill improvement is observed; the apparent edge resides in regime β rather than α.  

## Methodology  
The authors construct a controlled experiment using 21,600 weekly up/down calls on 60 Warsaw Stock Exchange equities recorded over 18 weeks. The decision‑layer model is frozen while only the abliterated vs. base arm varies. All components—official BF16 checkpoints, single author, identical serving stack, and one‑byte‑identical prompts—are held constant to isolate surgical effects.  

## Results  
Weekly clustered bootstrap confidence intervals exclude zero for all comparisons. Gemma‑abliterated arms show a +12.2 percentage point increase in optimism (p < 0.05), Qwen‑abliterated arms +7.4 pp (p < 0.05). Exploratory analyses reveal longer justification texts and fewer explicit uncertainty words. Confidence scores reverse: Gemma drops, Qwen rises. Skill metrics (alpha/beta) remain unchanged, confirming the effect is not due to performance drift.  

## Significance  
This research reveals that removing refusals introduces measurable behavioral artifacts that can mislead deployment decisions. Stakeholders treating “uncensored” models as mere base models minus refusals risk overlooking systematic confidence and language biases that affect real‑world outcomes. The findings also highlight the fragility of community‑modified checkpoints to toolchain contamination.  

## Related Concepts  
- Abliteration (weight‑level refusal removal)  
- Mixture‑of‑Experts model families  
- Decision disposition under uncertainty  
- Off‑target effects in AI system modifications  
- Regime α vs. β performance drift
