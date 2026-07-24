# Summary: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
Saved: 2026-07-24 02:08
Source: 2026-07-22_16-04-31Z_WhenDoesRecurrenceBecomeanAlgorithm_ConvergenceSel.md
Model: None

---

## Summary  
The paper investigates the question of when a weight‑tied looped transformer—i.e., applying one block repeatedly T times—actually implements an algorithm rather than merely approximating it. By analysing controlled populations on group word problems, the authors uncover four empirical findings that reveal how training dynamics, architectural priors, and computational limits interact to produce or prevent true algorithmic behaviour. Their work shows that a linear computation frontier is established by free training (budget law), that architecture prior selects either parallel scans or serial execution depending on weight tying, that certain “walls” arise from group order rather than intrinsic complexity, and that mechanisms are portable but mandatable only under specific input schedules. These insights expose the hidden conditions under which a transformer loop behaves algorithmically.

## Key Contributions  
- [Finding 1] The budget law: free training creates a linear computation frontier where the speed v is proportional to n_train/T_train (exponent 0.98 ± 0.04, R²=0.99), and SGD selects a frontier that matches the minimum contract demand; halting occurs at T* = ceil(n / v̂).  
- [Finding 2] Architecture prior, not expressivity, decides algorithmic behaviour: untied models learn parallel scans while weight‑tying forces serial execution even when log‑depth positional addressing is available.  
- [Finding 3] Walls are order‑driven, not complexity‑driven; NC1‑completeness incurs no cost (A5 generalises fully), whereas group order creates deadlocks (e.g., S5’s 120×120 operator) that an operator‑first curriculum can dissolve.

## Methodology  
The authors performed controlled experiments on a set of group word problems, varying training length T_train and testing loop count T. They measured the effective computation frontier v via head measurements (convergence‑time scaling τ(n,i)), validated it with damage cones whose slopes reproduce v, and compared untied versus weight‑tied models under matched depth and parameters. An operator‑first curriculum was applied to dissolve order‑induced walls, and warm‑starting across budget contracts was examined for portability of the algorithm.

## Results  
The linear frontier obeys v ≈ n_train/T_train (exponent 0.98 ± 0.04, R²=0.99) and converges exactly to unity when T = n training. SGD selects a frontier that meets the contract’s minimum demand; granting more test loops than trained rescues late positions at fixed input length via T* = ceil(n / v̂). Untied models extrapolate worst and fail to learn A5 entirely, while weight‑tied ones succeed. NC1 completeness is costless (A5 generalises fully), whereas S5’s group order deadlocks joint learning; an operator‑first curriculum eliminates the wall in every seed. Warm‑starting transfers the algorithm across contracts, but imposing seriality via input schedule fails where free training succeeds. The head instrument τ(n,i) predicts out‑of‑distribution fate where tail metrics do not.

## Significance  
These findings clarify when a transformer loop truly implements an algorithm, informing training design, hardware efficiency, and generalisation strategies. By separating architecture prior from intrinsic expressivity and exposing order‑driven walls, the work offers practical guidance for mitigating deadlocks and improving convergence without sacrificing speed.

## Related Concepts  
weight‑tied looped transformer; budget law; computation frontier v; parallel vs serial scans; NC1 completeness; group order deadlock; operator‑first curriculum; convergence‑time scaling τ(n,i); damage cones; head measurements; extrapolation failure.
