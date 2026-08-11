# Summary: 2026-08-10_08-18-48Z_PrivilegedLikelihoodIsNotAutomaticallyValue_ThreeC.md
Saved: 2026-08-10 23:41
Source: 2026-08-10_08-18-48Z_PrivilegedLikelihoodIsNotAutomaticallyValue_ThreeC.md
Model: None

---

## Summary  
The paper argues that token likelihood changes produced by privileged self‑distillation are not automatically valuable for improving model reasoning; they must pass three separate checks concerning whether the score tracks better actions, how feedback is constructed, and what behavior the training loss reinforces. It formalizes these distinctions and demonstrates that using hindsight feedback from the same rollout creates direct self‑dependence, leading to near‑chance performance on benchmark tasks.

## Key Contributions  
- **Finding 1:** Token likelihood changes do not necessarily reflect better actions or improved reasoning; they can be misleading signals.  
- **Finding 2:** Using hindsight feedback written about the same rollout introduces self‑dependency, making the score less reliable and often near chance.  
- **Finding 3:** Removing self‑dependency by feeding cross‑rollout feedback still yields performance close to random, indicating that token credit is not guaranteed even without direct dependence.

## Methodology  
The authors adopt a three‑check framework to validate token credit: (1) does the score track better actions? (2) does feedback construction alter what is being compared? (3) what behavior does the training loss reinforce? They implement an additive token‑score on AIME 2025 using a 20B model. Experiments compare five variants of the additive score against an outcome‑only control, with and without hindsight feedback (same rollout vs. another rollout), and after length adjustment to isolate effects.

## Results  
The outcome‑only control achieved an AUC of 64.2 %. The five token‑score variants performed between 24.2 % and 33.9 %, indicating that adding token credit does not improve performance. When the additive score is near chance (AUC ≈ 0.505) after length adjustment, it even slightly favors incorrect traces, suggesting that the signal may reinforce noise rather than correct errors.

## Significance  
Validating the meaning of feedback construction and training behavior separately is crucial before treating likelihood changes as credit signals; otherwise privileged self‑distillation may amplify irrelevant or harmful patterns. The study highlights the need for rigorous checks to ensure that token scores truly reflect useful learning gains.

## Related Concepts  
- Privileged self‑distillation  
- Token credit / additive scoring  
- Hindsight feedback (same rollout vs. cross‑rollout)  
- On‑policy self‑distillation  
- Outcome verification  
- AIME 2025 benchmark
