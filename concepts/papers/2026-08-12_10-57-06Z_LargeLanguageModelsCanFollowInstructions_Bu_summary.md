**Original paper:** [https://arxiv.org/abs/2608.12426v1](https://arxiv.org/abs/2608.12426v1)

# Summary: 2026-08-12_10-57-06Z_LargeLanguageModelsCanFollowInstructions_ButNotMan.md
Saved: 2026-08-13 22:21
Source: 2026-08-12_10-57-06Z_LargeLanguageModelsCanFollowInstructions_ButNotMan.md
Model: None

---

## Summary  
This paper investigates how large language models handle multiple constraints simultaneously, identifying a breakdown beyond a small number of constraints. It introduces Constraint Saturation Evaluation to measure performance as the number of constraints increases. The study finds that while individual constraint satisfaction remains high, joint success collapses rapidly. The authors also reveal that certain constraint types degrade faster and failures are largely independent.

## Key Contributions  
- [Finding 1] Per‑constraint pass rates decay gradually, yet the chance of satisfying all *k* constraints collapses—e.g., a model passing individual constraints at ~41 % at *k*=8 succeeds on all eight only 5.7 % of the time.  
- [Finding 2] Structural constraints lose twice as much baseline capability per added constraint compared with lexical ones, reflecting a comprehension‑maintenance gap that separates sustained tracking from binary decisions immune to composition.  
- [Finding 3] Failures are nearly independent; residual coupling tracks shared output features rather than pairwise interference, causing failures to accumulate multiplicatively.

## Methodology  
The authors created a procedurally generated benchmark with 15 language models, 36 constraint types, and 369 753 checks spanning *k* = 1–12. Each check is evaluated by a deterministic, rule‑based verifier; no LLM judge is involved. The evaluation measures per‑constraint pass rates and the probability of satisfying all constraints simultaneously.

## Results  
Per‑constraint success degrades predictably with increasing *k*, but joint success plummets—best models achieve only ~5.7 % success at *k*=8. Structural constraints degrade roughly twice as fast as lexical ones, indicating a comprehension‑maintenance gap. Failure independence leads to near‑multiplicative collapse; probe‑level success falls below 50 % at 7 constraints for the strongest model and ≤3 constraints for 12 of the 15 models.

## Significance  
The findings demonstrate that instruction‑following breakdown is not due to individual constraint failure but to compositional accumulation, informing design limits for systems requiring multiple simultaneous constraints. They highlight a phase‑transition point around 5–6 constraints beyond which reliable multi‑constraint performance collapses, guiding safer deployment strategies.

## Related Concepts  
Large Language Models; Constraint Satisfaction; Phase Transitions; Compositional Reasoning; Prompt Engineering; Rule‑based Verification; Multi‑task Learning.
