# Summary: 2026-08-10_11-23-30Z_FromApproachabilityResidualstoAnytime_ValidEvidenc.md
Saved: 2026-08-11 00:06
Source: 2026-08-10_11-23-30Z_FromApproachabilityResidualstoAnytime_ValidEvidenc.md
Model: None

---

## Summary  
The paper establishes an exact algebraic link between approachability residuals and betting‑based sequential tests via Blackwell support‑function residuals, showing how the OCO regret of a learner translates into finite‑time test rejection probabilities. It introduces a controlled stochastic experiment in which actions satisfy Blackwell’s supporting‑halfspace condition for every null mean payoff, treating wealth as an e‑process that yields sublinear OCO regret and exponential growth under persistent mean separation.

## Key Contributions  
- **Exact pathwise identity**: The distance of the empirical sequence to the target set equals the average of residuals plus a regularization term: \(\displaystyle \dist(\bar r_T,S)=\frac1T\sum_{t=1}^T q_t+\frac{\Reg_T}{T}\).  
- **Finite‑time transfer bound for testing**: If OCO and log‑wealth regrets are at most \(a_T\) and \(\ell_T\), a gap exceeding \(\frac{a_T}{T}+2B\sqrt{\frac{\log(1/\alpha)+\ell_T}{T}}\) forces rejection by time \(T\); conversely, non‑rejection certifies the converse radius.  
- **General framework**: The reduction connects OCO learning, Blackwell games, and active heterogeneous data sources through the convex geometry of betting, yielding exact algebra, quantitative finite‑time guarantees, and operational results.

## Methodology  
The authors derive the identity from support‑function residuals for a compact convex target \(S\) under vector observations \(r_t\). They compose this pathwise equality with one‑sided betting to obtain transfer theorems. The experimental protocol selects actions after each normal \(w_t\), ensuring Blackwell’s supporting‑halfspace condition holds for every null mean payoff, and treats the resulting wealth as an e‑process.

## Results  
The exact identity holds pathwise for any sequence of observations. The finite‑time test bound is tight up to constant factors: a gap larger than \(\frac{a_T}{T}+2B\sqrt{\frac{\log(1/\alpha)+\ell_T}{T}}\) guarantees rejection by time \(T\), while a smaller gap yields non‑rejection with confidence at least \(\alpha\). Sublinear OCO regret implies stochastic approachability, whereas persistent mean separation under the alternative hypothesis drives exponential wealth growth at rate \(\delta^2/(4B^2)\). Deterministic Blackwell games correspond to the noise‑free case; passive tests reduce to the singleton‑action scenario.

## Significance  
This work bridges learning and testing theory with exact algebra, providing quantitative finite‑time guarantees for hypothesis testing in controlled experiments. It enables practical applications in active learning, kernel MMD, two‑sample means, and heterogeneous data sources by turning OCO regret into actionable test outcomes.

## Related Concepts  
- Approachability (Blackwell)  
- Online Convex Optimization (OCO) regret  
- Support‑function residuals  
- Betting‑based sequential tests  
- Convex geometry of betting  
- e‑processes under adaptive nulls  
- Mean separation  
- Blackwell games  
- Kernel MMD  
- Two‑sample means
