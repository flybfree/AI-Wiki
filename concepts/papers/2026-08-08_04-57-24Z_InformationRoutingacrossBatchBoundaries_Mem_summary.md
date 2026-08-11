# Summary: 2026-08-08_04-57-24Z_InformationRoutingacrossBatchBoundaries_Memory__Ba.md
Saved: 2026-08-10 22:49
Source: 2026-08-08_04-57-24Z_InformationRoutingacrossBatchBoundaries_Memory__Ba.md
Model: None

---

## Summary  
The paper investigates how to balance memory usage (W bits) and batch size (B) in learning from stochastic Lipschitz bandits, showing a tradeoff that influences pseudo‑regret. It derives minimax bounds for the regret given constraints on live state width and committed batches, introducing a new frontier term. The authors also characterize information‑routing constraints linking regional decisions to entropy limits.

## Key Contributions  
- [Finding 1] Characterize minimax expected pseudo‑regret up to logarithmic factors when \(W \gtrsim d\log(eT)\), with lower bounds holding for every \(W\).  
- [Finding 2] Introduce a new penalty term \(T^{\frac{d+2}{d+3}} (1+(B-1)W)^{-\frac{1}{d(d+3)}}\) that captures the memory‑batch tradeoff, proving state width and update depth are not interchangeable.  
- [Finding 3] Show that information‑routing constraints force low regret to encode \(\Theta_d(s^{-d})\) regional decisions while boundary states carry at most \((B-1)W\) bits of entropy.

## Methodology  
The authors model each pull as a decision that updates a live state limited to \(W\) bits, which is then partitioned into \(B\) committed batches. They analyze the worst‑case expected pseudo‑regret using information‑theoretic arguments about regional decisions and entropy budgets, deriving both upper and lower bounds and showing how static batch boundaries compare to adaptive ones.

## Results  
Theoretical: For \(W \ge d\log(eT)\), the minimax regret is \(O(\log T)\) up to poly\((d)\) factors; a matching lower bound holds for all \(W\). The frontier term \(T^{\frac{d+2}{d+3}} (1+(B-1)W)^{-\frac{1}{d(d+3)}}\) is optimal, improving over classical sequential and unrestricted‑memory batch costs. Static batches achieve the same worst‑case bound as adaptive ones.

## Significance  
This work bridges memory constraints with batch scheduling in bandit learning, offering a principled tradeoff that improves regret beyond prior assumptions. It has implications for real‑world systems where both storage (memory) and processing (batch size) are limited.

## Related Concepts  
- Lipschitz bandits  
- Pseudo‑regret  
- Memory width \(W\)  
- Batch size \(B\)  
- Information routing  
- Regional decisions  
- Entropy budget  
- Sequential vs. batch learning
