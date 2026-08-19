# Summary: 2026-08-18_14-06-26Z_WhetherLLMsCanNavigateBeliefsandFactsDependsonHowY.md
Saved: 2026-08-18 21:39
Source: 2026-08-18_14-06-26Z_WhetherLLMsCanNavigateBeliefsandFactsDependsonHowY.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) handle mixed beliefs and facts when users express uncertainty or doubt, showing that performance varies dramatically with the epistemic verb used. By testing ten LLMs on eighteen belief‑facts pairs, the authors find an accuracy gap ranging from +50 % for “I vaguely remember” to –14 % for “I seriously doubt,” indicating that some phrasings improve factual alignment while others worsen it. The study also reveals a systematic task confusion: models default to fact‑checking the underlying claim and override the user’s stated belief, which can be reversed with a single instruction.

## Key Contributions  
- Finding 1 – Accuracy gap depends on the epistemic verb; ranges from +50 % (vague) to –14 % (doubt).  
- Finding 2 – Task confusion causes models to default to fact‑checking, overriding user‑stated beliefs.  
- Finding 3 – A single instruction can reverse failure across verb families.

## Methodology  
The authors evaluated ten LLMs on eighteen epistemic expressions that combine a false belief with a factual claim. They measured response accuracy for each expression and compared two chains of thought: one that explicitly fact‑checks the claim, the other that does not. Additionally, they attempted to suppress attention to false beliefs during decoding time as an intervention.

## Results  
“ I vaguely remember” yielded +50 % correct responses, while “I seriously doubt” produced –14 % accuracy. Fact‑checking chains performed worse on false information than non‑fact‑checking chains. Attention suppression partially recovered accuracy only in some models and only for certain verb families.

## Significance  
These findings clarify earlier observations that LLMs sometimes ignore user beliefs, exposing a conflict between the generally desirable fact‑checking behavior and effective belief tracking. The results provide concrete guidance for instruction tuning to align model responses with users’ epistemic stance, which is crucial for user‑facing applications where mixed belief‑fact communication matters.

## Related Concepts  
- Large language model (LLM)  
- Belief‑fact integration  
- Epistemic expressions  
- Fact‑checking  
- Attention mechanisms  
- Instruction tuning
