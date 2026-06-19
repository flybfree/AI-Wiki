# Summary: 2026-06-18_15-20-10Z_OntheVarianceofTemporalDifferenceLearninganditsRed.md
Saved: 2026-06-18 21:01
Source: 2026-06-18_15-20-10Z_OntheVarianceofTemporalDifferenceLearninganditsRed.md
Model: None

---


## Summary  
This paper investigates the variance characteristics of temporal difference (TD) learning in a phased tabular setting and demonstrates that its variance reduction stems from aggregating over multiple independent trajectories. It establishes an asymptotic upper bound on TD variance comparable to Monte Carlo estimators, shows that shorter‑horizon updates incur less variance for a fixed number of samples, and identifies Direct Advantage Estimation (DAE) as a regression‑adjusted control variate achieving tighter bounds. The analysis is supported by numerical experiments in carefully designed environments.

## Key Contributions  
- [Finding 1] The variance of TD learning can be asymptotically bounded above by Monte Carlo estimators, showing it is no worse than MC in the large‑sample limit.  
- [Finding 2] Shorter horizon updates incur less variance for a given number of samples, implying that truncating the planning horizon improves stability.  
- [Finding 3] Direct Advantage Estimation (DAE) can be interpreted as a control variate regression on the advantage function, yielding tighter variance bounds than TD.

## Methodology  
The authors analyze TD variance analytically within a phased tabular representation, deriving expressions for estimator variance and comparing them to Monte Carlo. They also construct DAE as a linear regression of advantages with control‑variates derived from baseline returns, then evaluate both methods via simulation in synthetic environments.

## Results  
Theoretical analysis shows that TD variance ≤ MC variance asymptotically; empirical runs confirm lower variance with shorter horizons and that DAE reduces variance by roughly 15 % relative to TD. Numerical experiments on a custom grid‑world environment validate these trends across varying sample counts.

## Significance  
Understanding the sources of TD variance helps practitioners choose more stable learning strategies, especially in long‑horizon planning tasks where MDPs are large. The control‑variate insight provides a principled way to improve off‑policy estimators beyond simple truncation.

## Related Concepts  
Temporal Difference (TD), Monte Carlo (MC) estimation, Control Variates, Direct Advantage Estimation (DAE), Phased tabular representation, Asymptotic variance bounds, Regression‑adjusted control variates.
