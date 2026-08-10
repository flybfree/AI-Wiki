# Summary: 2026-08-07_05-36-22Z_MultiscaleRewardHedgingfromCorrectDemonstrations.md
Saved: 2026-08-09 22:41
Source: 2026-08-07_05-36-22Z_MultiscaleRewardHedgingfromCorrectDemonstrations.md
Model: None

---

## Summary  
The paper tackles the difficulty of learning from correct demonstrations when many actions are valid in a continuous reward space, where no explicit rewards or loss signals are observed. It introduces a horizon‑free guarantee for hedging optimality across all accuracy scales using a shared vote over tolerant optimality tests, thereby achieving simultaneous tail bounds that depend only on the class of optimality‑gap functions. This approach yields polynomial regret bounds independent of the number of rounds and improves upon existing methods that assume finite reward classes.

## Key Contributions  
- [Finding 1] Provides the first horizon‑free guarantee for continuous reward classes, achieving simultaneous tail bound \(|\{t:\ell_t>2^{-j}\}|\leq \log_2\mathcal N(\mathcal G,2^{-j-1})+j\).  
- [Finding 2] Integrates these tails to obtain a metric‑entropy integral that bounds cumulative hidden gap without dependence on the number of rounds, yielding \(O(d)\) regret for bounded linear contextual recommendation and \(O(KT^2)\) time for fixed‑radius rank‑two menus.  
- [Finding 3] Establishes an \(\Omega(d)\) lower bound showing necessity of polynomial entropy, plus corollaries for low‑rank and bounded ReLU networks.

## Methodology  
The authors propose a shared vote over tolerant optimality tests at every accuracy scale. A target reward retains one surviving proxy per scale; any prediction whose gap exceeds that scale doubles the proxy count. This creates a cumulative hidden gap measured by an entropy integral, computed via polynomial entropy \((A/\varepsilon)^d\) giving \(O(d\log A)\) total gap and fast \(O(d/m)\) statistical rate. The method requires only action demonstrations, never observes reward or loss.

## Results  
Theoretically, the guarantee yields \(O(d)\) regret for arbitrary compact menus in bounded linear contextual recommendation, with no structural restrictions. Experimentally, after factorization, an exact MovieLens audit runs in 1.7 CPU seconds across ten users and improves mean latent gap over both a demonstrated‑rating policy and a proper online baseline.

## Significance  
This work breaks the curse of finiteness in reward classes, enabling polynomial finite regret without structural assumptions on menus. It also demonstrates that adaptive stress testing can capture predicted scale adaptation, offering a robust framework for recommendation learning from demonstrations alone.

## Related Concepts  
- Continuous reward spaces and infinite reward classes  
- Horizon‑free guarantees  
- Metric‑entropy integrals  
- Polynomial entropy \((A/\varepsilon)^d\)  
- Shared vote over tolerant optimality tests
