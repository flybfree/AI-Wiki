# Summary: 2026-07-22_20-01-44Z_CEDAR_CausalEdgeDiscoveryforAutoregressiveProcesse.md
Saved: 2026-07-24 02:19
Source: 2026-07-22_20-01-44Z_CEDAR_CausalEdgeDiscoveryforAutoregressiveProcesse.md
Model: None

---

## Summary  
CEDAR (Causal Edge Discovery for Autoregressive Processes) introduces a constraint‑based framework designed to identify the most relevant lagged causal edges in sparse, AR(1)-structured time series. The method screens candidate cross‑variable lags using an AR(1)-residualized distance correlation and then applies targeted conditional‑independence tests to retain at most one lag per ordered pair of variables. By integrating a stable MCI pruning step that eliminates indirect edges and optional deterministic C‑nodes for trend‑like nonstationarity, CEDAR delivers interpretable edge‑level results while requiring only \(O(d^2)\) CI tests after screening—making it efficient when data are scarce.

## Key Contributions  
- [Finding 1] A novel AR(1)-residualized distance correlation that efficiently screens candidate cross‑variable lags in sparse autoregressive settings.  
- [Finding 2] A two‑stage conditional‑independence testing pipeline that selects at most one lag per ordered variable pair, preserving edge‑level interpretability.  
- [Finding 3] An MCI pruning mechanism combined with deterministic C‑nodes to remove indirect edges and adjust for trend‑like nonstationarity without sacrificing stability.

## Methodology  
The authors begin by computing residuals after fitting an AR(1) model to each series, then centering these residuals around the sample mean. Distance correlation is calculated between pairs of centered residuals across different lags, yielding a scalar measure that captures lagged cross‑variable dependence. Significant lag candidates are identified when this distance exceeds a threshold derived from a permutation test. For each surviving candidate, CEDAR conducts two conditional‑independence tests (e.g., CUSUM or CUSUM+), accepting the lag only if both tests reject independence. The MCI step iteratively removes edges that can be inferred as indirect consequences of other detected lags, ensuring a minimal set of causal edges. Deterministic C‑nodes are optionally added to model systematic trends by fixing the first lag’s coefficient.

## Results  
Experiments on synthetic and real sparse time series demonstrate that CEDAR outperforms standard permutation‑based methods in terms of false‑positive rates while maintaining comparable true‑positive detection. The computational complexity is \(O(d^2)\) CI tests after screening, which scales well for moderate numbers of variables (\(d \approx 10–30\)). Sensitivity analysis shows that CEDAR’s performance degrades when higher‑order autoregressive or simultaneous multi‑lag effects dominate, suggesting the method’s suitability for first‑order dynamics.

## Significance  
CEDAR addresses a critical gap in causal inference for time series: it provides interpretable lagged edges without requiring dense data or complex modeling assumptions. By balancing computational efficiency with statistical rigor, CEDAR enables practitioners to extract actionable insights from limited observational datasets where traditional regression lags are noisy or confounded.

## Related Concepts  
- Autoregressive (AR) processes and their residuals  
- Distance correlation as a non‑parametric dependence measure  
- Conditional independence testing in high dimensions  
- MCI pruning for sparse causal networks  
- C‑nodes for trend adjustment in time series
