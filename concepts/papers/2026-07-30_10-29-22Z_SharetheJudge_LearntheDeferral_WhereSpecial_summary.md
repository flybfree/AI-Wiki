# Summary: 2026-07-30_10-29-22Z_SharetheJudge_LearntheDeferral_WhereSpecialization.md
Saved: 2026-07-30 20:33
Source: 2026-07-30_10-29-22Z_SharetheJudge_LearntheDeferral_WhereSpecialization.md
Model: None

---

## Summary  
The paper investigates whether domain specialization should be embedded directly into an evaluator’s weights or confined to the rule that governs when a judgment can be trusted, using large‑language‑model evaluation on rubric‑conditioned examples. By training eight LoRA judges on shared data and comparing it with specialized per‑criterion adapters, the authors show that sharing learned judgments yields higher accuracy and better coverage while keeping risk low. The study also demonstrates that a cascade of correctness heads can route examples through multiple models without altering reward scores, improving performance at very low compute cost. These findings suggest a practical design rule: share learning until sufficient data justifies splitting, then place domain‑specific adaptation at the audit boundary.

## Key Contributions  
- [Finding 1] Providing the correct rubric improves locked‑test accuracy by 2.11 points over a response‑only control; replacing it with an unrelated rubric costs 2.66 points.  
- [Finding 2] Splitting the same training corpus among eight criterion‑family LoRA judges loses 10.05 points and cuts audited coverage at a 5% risk target from 24.44% to 5.43%; matching the bank’s stored capacity with one rank‑64 adapter avoids this loss.  
- [Finding 3] Initializing family adapters from a shared, trained judge recovers test accuracy to 76.85%, 19.94 points above scratch training at the same learning rate (95% interval 18.88‑21.02). The result disappears when specialization governs deferral rather than judgment.

## Methodology  
The authors study 99,952 public rubric‑conditioned examples using LoRA adapters for each criterion family. They compare three configurations: (i) a response‑only control, (ii) eight specialized LoRA judges trained separately, and (iii) a shared judge whose outputs are routed through an audited release boundary. Risk is evaluated with exact one‑sided 95% audits, and the cascade of correctness heads on RewardBench 2 is measured to assess routing efficiency.

## Results  
A shared judge baseline achieves 76.85% accuracy, which is 19.94 points above a scratch training set. Splitting among eight LoRA judges reduces accuracy by roughly 10.05 points and drops coverage to 5.43%. Using a rank‑64 adapter that matches the bank’s capacity yields no loss in performance. On RewardBench 2, a cascade of 0.6B‑4B‑8B models improves accuracy from 84.75% (8B alone) to 89.40% while consuming only 0.415 normalized parameter compute per run; margin‑based rules remain near 84.8% accuracy at ≥ 0.94 compute.

## Significance  
These results highlight that premature specialization can degrade evaluation quality and inflate risk, whereas sharing learned judgments maximizes coverage and safety. The cascade approach shows that correctness routing can boost performance without sacrificing auditability or computational budget, offering a scalable strategy for large‑scale LLM evaluation systems.

## Related Concepts  
- LoRA adapters (low‑rank adaptation)  
- Criterion families in rubric‑conditioned data  
- Risk auditing with exact one‑sided 95% thresholds  
- Deferral vs. judgment decision logic  
- Cascade models for correctness routing  
- RewardBench benchmarking of reward‑independent accuracy
