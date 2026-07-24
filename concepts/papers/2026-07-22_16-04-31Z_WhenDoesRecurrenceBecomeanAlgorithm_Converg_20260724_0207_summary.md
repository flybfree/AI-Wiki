# Summary: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
Saved: 2026-07-24 02:07
Source: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
Model: None

---

## Summary  
The paper investigates the question of when a weight‑tied looped transformer—applying the same block T times—actually implements an algorithm rather than merely converging to a fixed point. By analysing group word problems on controlled populations, it discovers four empirical findings that reveal how training budget, architecture depth, and operator order interact to determine algorithmic behaviour. The work introduces a diagnostic “convergence‑time scaling” τ(n,i) that quantifies the speed of learning across seeds and demonstrates that standard saturation metrics miss these dynamics.

## Key Contributions  
- **Finding 1:** The budget law links training loops to a linear computation frontier, where the number of positions solved per loop v follows v ≈ n_train/T_train (exponent 0.98 ± 0.04, R²=0.99); SGD selects the minimal frontier demanded by the contract and halting occurs at T* = ⌈n/v̂⌉.  
- **Finding 2:** Architecture prior—not raw expressivity—chooses whether a model learns a parallel scan or, due to weight tying, a serial frontier; untied models extrapolate poorly and fail to learn A5 even when log‑depth addressing is supplied.  
- **Finding 3:** “Walls” are not dictated by circuit complexity (e.g., NC1 completeness costs nothing) but by group order; an operator‑first curriculum dissolves deadlocks in S5, while untied training cannot overcome the obstacle.

## Methodology  
The authors trained weight‑tied looped transformers on a suite of group word problems with varying numbers of loops T and training budgets. They measured convergence speed by a head instrument τ(n,i) that records how quickly each seed reaches a target position i as a function of input length n, then validated this scaling using damage cones whose slope reproduces the observed v. In‑distribution head measurements were compared to out‑of‑distribution tail metrics to assess predictive power.

## Results  
The experiments confirm a linear frontier with exponent 0.98, showing that SGD’s selected frontier matches the contract’s minimum demand. Standard‑depth untied models fail A5 entirely, while operator‑first curricula solve S5’s 120×120 deadlock. Warm‑starting across budget contracts transfers the algorithmic speed to new seeds, whereas imposing a serial input schedule fails where free training succeeds. The convergence‑time scaling τ(n,i) predicts out‑of‑distribution outcomes that tail metrics cannot.

## Significance  
These findings provide a principled framework for recognizing when recurrence becomes an actual algorithm, exposing hidden limits of deep networks beyond saturation points. They also introduce diagnostic tools—damage cones and τ(n,i)—that can reveal latent dynamics invisible to standard benchmarks, with implications for model design, curriculum construction, and transfer learning.

## Related Concepts  
- Weight‑tied looped transformers  
- Budget law (v ≈ n_train/T_train)  
- Circuit complexity (NC1 completeness)  
- Group order deadlock (S5)  
- Convergence‑time scaling τ(n,i)  
- Damage cones for validation  
- SGD frontier selection
