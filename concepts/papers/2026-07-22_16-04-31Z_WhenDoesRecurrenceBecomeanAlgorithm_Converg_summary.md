# Summary: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
Saved: 2026-07-24 02:05
Source: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
Model: None

---

## Summary  
The paper asks when a weight‑tied looped transformer actually implements an algorithm, answering this question through four findings from controlled experiments on group word problems. It demonstrates that the training budget creates a linear computation frontier, that architecture priors—not model expressivity—determine whether parallel or serial execution is selected, and that certain operators impose practical “walls” despite theoretical completeness. The work also shows how mechanisms can be portable across seeds while standard metrics fail to reveal these dynamics.

## Key Contributions  
- [Finding 1] The budget law: free training installs a linear computation frontier, v ≈ n_train/T_train (exponent 0.98 ± 0.04, R²=0.99), with SGD selecting the minimum‑contract frontier and halting at T* = ceil(n/v̂).  
- [Finding 2] Architecture prior, not expressivity, picks the algorithm: standard‑depth transformers learn parallel scans; weight tying flips to a serial frontier even when log‑depth addressing is provided. Untied models extrapolate poorly and fail A5 entirely.  
- [Finding 3] The walls are not where circuit complexity says: NC1‑completeness costs nothing (A5 generalizes fully), while group order does (S5’s 120×120 operator deadlocks joint learning); an operator‑first curriculum dissolves the wall in every seed.

## Methodology  
The authors controlled populations on a series of group word problems, varying training loops T_train and input length n. They measured execution speed v under free training and SGD selection, compared untied versus tied models at matched depth/parameters, introduced a head instrument τ(n,i) that encodes convergence‑time scaling, validated its slope via damage cones reproducing the observed v, and used in‑distribution head measurements to predict out‑of‑distribution fate where tail metrics do not.

## Results  
Experiments confirm a linear frontier with exponent 0.98 ± 0.04 (R²=0.99). SGD selects the minimum contract frontier; granting more test loops than ever trained rescues late positions at fixed input length, yielding T* = ceil(n/v̂). Untied models exhibit worst extrapolation and cannot learn A5. The operator‑first curriculum eliminates S5 deadlocks. Warm‑starting across budget contracts transfers the algorithm in every seed, while imposing seriality through input schedule fails where free training succeeds. Convergence‑time scaling τ(n,i) predicts out‑of‑distribution behavior.

## Significance  
These findings reveal that recurrence becomes an algorithm only when the training budget aligns with a linear computation frontier, exposing a tension between architecture design and expressivity. Standard instruments saturate at fixed points, obscuring true dynamics; the work provides a principled halting rule for looped transformers and demonstrates that mechanisms are portable across seeds.

## Related Concepts  
- Weight‑tied looped transformer  
- Budget law (v ≈ n_train/T_train)  
- Computation frontier v  
- SGD selection of frontier  
- Parallel vs. serial execution  
- NC1‑completeness, group order deadlock  
- Convergence‑time scaling τ(n,i)  
- Damage cones (slope validation)
