# Summary: 2026-08-05_14-56-53Z_MarginalMatchingDoesNotLicenseFactorizedSampling_A.md
Saved: 2026-08-06 21:44
Source: 2026-08-05_14-56-53Z_MarginalMatchingDoesNotLicenseFactorizedSampling_A.md
Model: None

---

## Summary  
The paper argues that matching only the marginal distribution of a latent style variable in factorized generative models does not guarantee independence from class labels; it shows this mismatch is one of four conditions needed for proper factorization and can lead to severe conditional leakage. By analyzing an exact decomposition, they demonstrate that eliminating this condition is necessary but insufficient, and empirical tests reveal persistent class‑conditional style leakage despite zero global MMD.

## Key Contributions  
- Finding 1: Matching only the marginal distribution of a latent style variable does not enforce independence from class labels; it leaves conditional distributions unconstrained.  
- Finding 2: The mismatch between marginal matching and conditional structure is one of four necessary conditions for factorized sampling, identified via an exact decomposition.  
- Finding 3: Empirical experiments show that models with zero global MMD still allow linear probes to recover classes with up to 100% accuracy, indicating severe leakage.

## Methodology  
The authors derived an analytical decomposition of the joint distribution into marginal and conditional components, showing how factorized sampling requires matching both marginals and conditionals. They constructed a case‑study model and compared it against four latent baselines using global MMD, probing with linear classifiers, clustering analysis, and external generation evaluation across two datasets (MNIST, CIFAR‑10). Perturbations varied model capacity, curriculum, prior geometry, and supervision.

## Results  
The case‑study model achieved 99.15% clustering accuracy but only 16% successful class generation; baselines had similar global MMD (<0.01) yet linear probes succeeded 74‑100%. Mitigation strategies reduced probe accuracy to 21–46%, while a post‑hoc conditional prior improved MNIST classification to 97% but not CIFAR‑10 (0.41). An empirical style bank reached 0.88 on CIFAR‑10.

## Significance  
The findings challenge the common assumption that marginal matching certifies factorized independence, highlighting risks of latent style leakage in generative models and urging more rigorous evaluation beyond global MMD.

## Related Concepts  
Factorized generative models, latent style variables, marginal vs. conditional distributions, mutual information, linear probing, clustering accuracy, global MMD, conditional prior, empirical style bank.
