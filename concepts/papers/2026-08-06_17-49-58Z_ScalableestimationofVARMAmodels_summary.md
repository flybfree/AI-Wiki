# Summary: 2026-08-06_17-49-58Z_ScalableestimationofVARMAmodels.md
Saved: 2026-08-06 23:08
Source: 2026-08-06_17-49-58Z_ScalableestimationofVARMAmodels.md
Model: None

---

## Summary  
The paper tackles the long‑standing computational bottleneck of estimating vector autoregressive moving‑average (VARMA) models, which become prohibitive as series length \(T\) grows because likelihood evaluation requires a full pass over the data. The authors introduce an estimation framework that makes each optimization iteration independent of \(T\), leveraging a partial‑autocorrelation reparametrization and Parseval identities to compute sufficient statistics in near‑linear time. This yields two point estimators—a regularized least‑squares fit and a covariance‑marginalized maximum‑a‑posteriori estimator—that recover the infinite‑autoregressive representation of the true process without asymptotic bias. The method also extends to seasonal, exogenous (VARMAX), and rolling‑window scenarios, delivering practical likelihood‑based VARMA inference where classical MLE fails.

## Key Contributions  
- [Finding 1] A reparametrization based on partial autocorrelation that simultaneously enforces stationarity and invertibility of the moving‑average component.  
- [Finding 2] Gaussian priors with separate scales for diagonal and off‑diagonal entries, enabling efficient computation via Parseval’s Fourier identity.  
- [Finding 3] Two point estimators—regularized least squares and covariance‑marginalized MAP—that achieve near‑parametric convergence to the infinite VARMA representation.

## Methodology  
The authors start from a VARMA model expressed as \(y_t = \Phi y_{t-1} + \theta_t\), where \(\theta_t\) follows an MA process. By reparameterizing the moving‑average coefficients through partial autocorrelation, the likelihood becomes separable into diagonal and off‑diagonal components. Gaussian priors are assigned to these components with distinct variance scales, allowing the joint posterior to be expressed as a product of independent terms. The sufficient statistics for each term are obtained via Parseval’s identity, which reduces evaluation to a fixed‑size Fourier transform that costs \(O(d)\) where \(d\) is the truncation length. This yields a regularized least‑squares estimator and a marginal MAP estimator that can be computed iteratively without re‑scanning the entire series.

## Results  
Both estimators recover the infinite VARMA representation at a near‑parametric rate in fixed dimension, meaning truncation introduces no asymptotic bias. The framework extends to seasonal dynamics, exogenous regressors (VARMAX), and rolling‑window refits with the same linear cost per iteration. Empirically, on retail‑demand, meteorological, and air‑quality datasets, the estimators remain close to the oracle forecast error from \(d=10\) up to \(d=40\), whereas classical conditional MLE yields non‑invertible fits whose forecasts diverge. They match or beat VAR, Bayesian‑VAR, component‑wise ARMA, and sparse‑VARMA baselines across all three domains.

## Significance  
This work removes the series‑length dependency that has limited likelihood‑based VARMA estimation to modest dimensions, opening the door for practitioners who rely on VAR models. By providing efficient point estimates that are statistically sound up to large truncation lengths, the method enables more accurate forecasts and inference in high‑dimensional economic, environmental, and industrial data.

## Related Concepts  
VARMA, partial autocorrelation, Gaussian priors, Parseval identity, regularized least squares, covariance‑marginalized MAP, seasonal dynamics, exogenous regressors (VARMAX), rolling‑window refits, sparsity, likelihood‑based inference.
