# Summary: 2026-07-29_15-20-39Z_BayesAME_BayesianActiveModelEvaluation.md
Saved: 2026-07-29 21:39
Source: 2026-07-29_15-20-39Z_BayesAME_BayesianActiveModelEvaluation.md
Model: None

---

## Summary  
The paper proposes BayesAME, a sequential Bayesian framework that automatically determines the optimal size of a coreset for evaluating large generative models. By modeling performance as a random variable across groups of items with shared historical scores, it derives posterior distributions to estimate performance and uncertainty while selecting new items via an information‑gain criterion. The method iteratively builds a coreset until both estimation fluctuation and uncertainty fall below user‑defined thresholds. A multi‑target extension captures correlations among multiple target models, further shrinking the required coreset.  

## Key Contributions  
- [Finding 1] BayesAME automatically selects a coreset size that prioritizes reliable performance estimates over computational efficiency.  
- [Finding 2] The Bayesian posterior provides both point‑estimate performance and quantified uncertainty for each added item.  
- [Finding 3] A multi‑target extension reduces coreset size by modeling performance correlations across several models simultaneously.  

## Methodology  
BayesAME treats each group of items that have exhibited similar historical model performances as a latent ability variable. The joint prior encodes the belief that these abilities are comparable, while the posterior over abilities is updated as new log‑likelihoods are observed. Performance estimators are obtained by integrating this posterior, and an information‑gain metric selects the next most informative item to add. The process repeats until convergence criteria are met.  

## Results  
Experiments across diverse benchmarks show that BayesAME consistently yields smaller coresets than sequential adaptations of existing methods while achieving comparable or better performance estimates. Theoretical analysis confirms that non‑random coreset selection outperforms random sampling, and using continuous log‑likelihoods rather than binary scores improves estimation accuracy.  

## Significance  
By decoupling coreset size from arbitrary user input, BayesAME enables more efficient model evaluation without sacrificing reliability—a critical advantage for large‑scale generative models where exhaustive testing is infeasible. The automatic selection mechanism reduces computational overhead and resource consumption, making high‑quality performance assessments accessible to practitioners.  

## Related Concepts  
- Latent ability modeling of item groups  
- Sequential Bayesian inference with posterior integration  
- Information‑gain based coreset expansion
