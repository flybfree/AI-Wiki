# Summary: 2026-08-10_11-23-30Z_FromApproachabilityResidualstoAnytime_ValidEvidenc.md
Saved: 2026-08-10 23:47
Source: 2026-08-10_11-23-30Z_FromApproachabilityResidualstoAnytime_ValidEvidenc.md
Model: None

---

## Summary  
The paper establishes a precise algebraic link between betting‑based sequential tests and Blackwell approachability via support‑function residuals, showing that the distance of empirical data to a compact convex target equals the average of the learner’s \(q_t\) terms plus a regularisation term. It then uses this identity to derive finite‑time transfer rates under bounded online‑convex‑optimization (OCO) and log‑wealth regrets, yielding an exact rejection criterion that depends on the OCO regret bound \(a_T\) and the log‑wealth regret \(\ell_T\). The framework is presented as a controlled stochastic experiment where each active action satisfies Blackwell’s supporting‑halfspace condition for every null mean payoff. This bridges deterministic Blackwell games (noise‑free) with passive tests (single‑action) through an exact algebraic reduction that is both quantitative at finite time and operational in practice.

## Key Contributions  
- [Finding 1] The exact pathwise identity \(\displaystyle \dist(\bar r_T,S)=\frac{1}{T}\sum_{t=1}^T q_t+\frac{\Reg_T}{T}\) holds for any OCO learner selecting a normal \(w_t\) and computing \(q_t=\langle w_t,r_t\rangle-h_S(w_t)\).  
- [Finding 2] When \(|q_t|\le B\), composing the identity with one‑sided betting gives a finite‑time transfer: if OCO regret \(\le a_T\) and log‑wealth regret \(\le \ell_T\), then a target gap exceeding \(\frac{a_T}{T}+2B\sqrt{\frac{\log(1/\alpha)+\ell_T}{T}}\) forces rejection by time \(T\); non‑rejection certifies the converse radius.  
- [Finding 3] Sublinear OCO regret yields stochastic approachability, whereas persistent mean separation under an alternative hypothesis produces exponential wealth growth at rate at least \(\frac{\delta^2}{4B^2}\).

## Methodology  
The authors consider a compact convex target \(S\subset\mathbb{R}^d\) and vector observations \(\{r_t\}_{t=1}^{T}\). An OCO learner chooses a predictable normal \(w_t\) and defines the residual \(q_t=\langle w_t,r_t\rangle-h_S(w_t)\). By composing this identity with one‑sided betting, they obtain finite‑time guarantees. They also formulate a controlled stochastic experiment in which every action selected after \(w_t\) satisfies Blackwell’s supporting‑halfspace condition for all null mean payoffs, treating the resulting wealth process as an e‑process under adaptive nulls.

## Results  
The reduction provides an exact algebraic connection between betting, approachability and convex geometry. It yields quantitative finite‑time performance: a target gap larger than \(\frac{a_T}{T}+2B\sqrt{\frac{\log(1/\alpha)+\ell_T}{T}}\) forces rejection by time \(T\), while non‑rejection certifies the converse radius. Sublinear OCO regret translates to stochastic approachability, and persistent mean separation under an alternative hypothesis yields exponential wealth at rate \(\ge \delta^2/(4B^2)\). Deterministic Blackwell games correspond to the noise‑free case, while passive tests are the singleton‑action limit of this protocol.

## Significance  
This unified framework links betting strategies, approachability theory and convex geometry, delivering precise finite‑time guarantees for active learning under adversarial settings. It improves theoretical foundations for online convex optimization with bounded regrets and offers practical tools for designing controlled experiments where hypothesis testing is performed via betting. The results are applicable to deterministic Blackwell games (noise‑free) and passive tests (single action), making the theory both theoretically rigorous and operationally useful.

## Related Concepts  
Blackwell approachability, support‑function residuals, OCO regret, log‑wealth regret, one‑sided betting, convex target \(S\), e‑process with adaptive nulls, Blackwell’s supporting‑halfspace condition, two‑sample means, kernel MMD, active heterogeneous data sources.
