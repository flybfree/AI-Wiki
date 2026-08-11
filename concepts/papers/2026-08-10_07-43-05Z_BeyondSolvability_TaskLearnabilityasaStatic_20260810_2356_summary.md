# Summary: 2026-08-10_07-43-05Z_BeyondSolvability_TaskLearnabilityasaStaticPriorfo.md
Saved: 2026-08-10 23:56
Source: 2026-08-10_07-43-05Z_BeyondSolvability_TaskLearnabilityasaStaticPriorfo.md
Model: None

---

## Summary  
The paper investigates why reinforcement‑learning (RL) post‑training can elicit diverse reasoning abilities across large language models, arguing that uniform task sampling ignores a hidden factor: how well a task will improve with further training. By defining **task learnability** as the expected positive response to continued RL under a fixed schedule, the authors show this metric is stable across tasks and predicts downstream performance. They introduce **TrajVal**, a lightweight probe‑based estimator that captures learnability from only two endpoint evaluations and a short probe run, enabling its use as a static prior or multiplicative factor in online schedulers.

## Key Contributions  
- [Finding 1] Task learnability is a reproducible, task‑specific signal that predicts how much a model will benefit from additional RL training.  
- [Finding 2] The metric can be estimated cheaply with TrajVal using only two endpoint rewards and a brief probe, making it practical for pre‑training selection.  
- [Finding 3] Incorporating learnability as a static prior or multiplicative factor improves data efficiency compared to uniform sampling and yields complementary gains when combined with online schedulers.

## Methodology  
The authors collect per‑task reward trajectories across multiple model scales, then fit a simple linear regression to each trajectory’s slope to approximate the expected improvement (learnability). TrajVal replaces this regression with an estimator that uses only two endpoint rewards—representing the best and worst performance observed—and a short probe run that captures intermediate behavior. The resulting estimate is used either as a fixed weight for task selection or multiplied into existing online learning schedules.

## Results  
Experiments on mathematical reasoning (e.g., MATH) and logical puzzles (e.g., LogicalQA) across GPT‑2, LLaMA‑2, and larger models demonstrate that tasks with higher TrajVal scores are learned more efficiently. Uniform sampling yields a 15–20 % reduction in sample efficiency, whereas using TrajVal as a static prior improves it by up to 30 %. When combined multiplicatively with an online scheduler, the total improvement reaches ~40 %, confirming that learnability provides both a pre‑training filter and a fine‑tuning accelerator.

## Significance  
By treating task learnability as a static prior, the work offers a principled way to allocate RL compute where it matters most, reducing wasted effort on tasks unlikely to improve. This approach is especially valuable for large‑scale models with limited training budgets, aligning resource allocation with actual learning potential.

## Related Concepts  
- Reinforcement Learning (RL) post‑training  
- Task learnability / residual axis of solvability  
- Probe‑based estimation  
- Uniform vs. informed task sampling  
- Online RL schedulers
